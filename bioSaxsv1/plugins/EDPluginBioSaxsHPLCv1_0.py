# coding: utf8
#
#    Project: <projectName>
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2012 ESRF
#
#    Principal author:        Jérôme Kieffer
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import with_statement

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2012 ESRF"
__date__ = "20120920"
__status__ = "development"

import os, h5py, fabio, numpy
from EDPluginControl import EDPluginControl
from EDThreading import Semaphore
from EDVerbose import EDVerbose
from EDFactoryPlugin import edFactoryPlugin
edFactoryPlugin.loadModule("XSDataBioSaxsv1_0")
edFactoryPlugin.loadModule("XSDataEdnaSaxs")
from XSDataBioSaxsv1_0 import XSDataInputBioSaxsHPLCv1_0, XSDataResultBioSaxsHPLCv1_0, \
                            XSDataInputBioSaxsProcessOneFilev1_0
from XSDataEdnaSaxs import XSDataInputDatcmp, XSDataInputDataver, XSDataInputDatop, XSDataInputSaxsAnalysis
from XSDataCommon import XSDataFile, XSDataStatus, XSDataString, XSDataInteger, XSDataStatus

class HPLCrun(object):
    def __init__(self, runId, first_curve=None):
        self.id = runId
        self.buffer = None
        self.first_curve = first_curve
        self.frames = []
        self.curves = []
        self.for_buffer = []
        self.hdf5_filename = None
        self.hdf5 = None
        self.start_time = None
        self.chunk_size = 100
        self.lock = Semaphore()
        if first_curve:
            self.files.append(first_curve)

    def reset(self):
        self.frames = []
        self.curves = []
        self.for_buffer = []

    def init_hdf5(self, filename):
        if self.hdf5_filename is None:
            with self.lock:
                if self.hdf5_filename is None:
                    self.hdf5_filename = filename
        if self.hdf5 is None:
            with self.lock:
                if self.hdf5 is None:
                    if os.path.exists(self.hdf5_filename):
                        os.unlink(self.hdf5_filename)
                    self.hdf5 = h5py.File(self.hdf5_filename)
        else:
            try:# the HDF5 file exist but could be closed
                fn = self.hdf5.filename
            except IOError: #if closed: reopen it without erasing it
                with self.lock:
                    self.hdf5 = h5py.File(self.hdf5_filename)

    def close_hdf5(self):
        with self.lock:
            if self.hdf5:
                try:
                    self.hdf5.flush()
                except IOError:
                    EDVerbose.WARNING("HDF5 file already closed")
                    pass

    def calc_size(self, id):
        return (1 + (id // self.chunk_size)) * self.chunk_size

    def set_scal(self, frameId, data, key="time"):
        if not self.hdf5:
            EDVerbose.WARNING("HDF5 is not initialized")
            if self.hdf5_filename :
                self.init_hdf5(self.hdf5_filename)
        with self.lock:
            if key not in self.hdf5:
                ds = self.hdf5.create_dataset(key, (self.calc_size(frameId),), "float32", chunks=(self.chunk_size,))
            else:
                ds = self.hdf5[key]
            if ds.shape[0] <= frameId:
                ds.resize((self.calc_size(frameId),))
            ds[frameId] = data

    def set_time(self, frameId, rawfilename):
        if not os.path.isfile(rawfilename):
            EDVerbose.WARNING("Raw file not on disk: %s" % rawfilename)
            return
        header = fabio.open(rawfilename).header
        if "time_of_day" in header:
            try:
                tt = float(header["time_of_day"])
            except:
                EDVerbose.WARNING("time_of_day not a float in %s" % rawfilename)
                return
            if self.start_time is None:
                with self.lock:
                    if self.start_time is None:
                        self.start_time = tt
            self.set_scal(frameId, tt - self.start_time, key="time")


    def set_2D(self, frameId, datfilename, kind="scattering"):
        if not self.hdf5:
            EDVerbose.WARNING("HDF5 is not initialized")
            if self.hdf5_filename :
                self.init_hdf5(self.hdf5_filename)
        if not os.path.isfile(datfilename):
            EDVerbose.WARNING("Ascii file not on disk: %s" % datfilename)
            return
        data = numpy.loadtxt(datfilename)
        size = data.shape[0]
        q = data[:, 0]
        I = data[:, 1]
        s = data[:, 2]
        with self.lock:
            key = kind + "_q"
            if key not in self.hdf5:
                self.hdf5[key] = q.astype("float32")

            key = kind + "_I"
            if key not in self.hdf5:
                ds = self.hdf5.create_dataset(key, (self.calc_size(frameId), size), "float32", chunks=(self.chunk_size, size))
            else:
                ds = self.hdf5[key]
            if ds.shape[0] <= frameId:
                ds.resize((self.calc_size(frameId), size))
            ds[frameId, :] = I

            key = kind + "_Stdev"
            if key not in self.hdf5:
                ds = self.hdf5.create_dataset(key, (self.calc_size(frameId), size), "float32", chunks=(self.chunk_size, size))
            else:
                ds = self.hdf5[key]
            if ds.shape[0] <= frameId:
                ds.resize((self.calc_size(frameId), size))
            ds[frameId, :] = s



class EDPluginBioSaxsHPLCv1_0(EDPluginControl):
    """
    plugin for processing Saxs data coming from HPLC
    
    runs subsequently:
    *ProcessOneFile, 
    *subtraction of buffer 
    *SaxsAnalysis
    
    todo:
    only store references: Wait for flush to construct HDF5 file and (possibly) web pages with PNG graphs  
    """

    strControlledPluginProcessOneFile = "EDPluginBioSaxsProcessOneFilev1_2"
    strControlledPluginDatop = "EDPluginExecDatopv1_0"
    strControlledPluginSaxsAnalysis = "EDPluginControlSaxsAnalysisv1_0"
    strControlledPluginDatCmp = "EDPluginExecDatcmpv1_0"
    strControlledPluginDatAver = "EDPluginExecDataverv1_0"
    dictHPLC = {} #key=runId, value= HPLCrun instance
    _sem = Semaphore()

    def __init__(self):
        """
        """
        EDPluginControl.__init__(self)
        self.setXSDataInputClass(XSDataInputBioSaxsHPLCv1_0)
        self.__edPluginProcessOneFile = None
        self.__edPluginSubtract = None
        self.__edPluginSaxsAnalysis = None
        self.__edPluginDatCmp = None
        self.xsDataResult = XSDataResultBioSaxsHPLCv1_0()
        self.runId = None
        self.frameId = None
        self.hplc_run = None
        self.curve = None
        self.subtracted = None
        self.lstExecutiveSummary = []
        self.isBuffer = False

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.rawImage, "No raw image")
        self.checkMandatoryParameters(self.dataInput.sample, "no Sample parameter")
        self.checkMandatoryParameters(self.dataInput.experimentSetup, "No experimental setup parameter")


    def preProcess(self, _edObject=None):
        EDPluginControl.preProcess(self)
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.preProcess")
        sdi = self.dataInput
        if sdi.runId is not None:
            self.runId = sdi.runId.value
        else:
            path = sdi.rawImage.path.value
            if "_" in path:
                self.runId = path[::-1].split("_", 1)[1][::-1]
            else:
                self.runId = path
        with self._sem:
            if self.runId not in self.dictHPLC:
                self.dictHPLC[self.runId] = HPLCrun(self.runId)
        self.hplc_run = self.dictHPLC[self.runId]
        if sdi.frameId is not None:
            self.frameId = sdi.frameId.value
        else:
            path = sdi.rawImage.path.value
            if "_" in path:
                digits = os.path.splitext(os.path.basename(path))[0].split("_")[-1]
                try:
                    self.frameId = int(digits)
                except ValueError:
                    self.WARNING("frameId is supposed to be an integer, I got %s" % digits)
                    self.frameId = digits
            else:
                self.warning("using frameID=0 in tests, only")
                self.frameId = 0
        with self._sem:
            self.hplc_run.frames.append(self.frameId)

        if sdi.bufferCurve and os.path.exists(sdi.bufferCurve.path.value):
            with self._sem:
                self.hplc_run.buffer = sdi.bufferCurve.path.value

        if self.hplc_run.hdf5_filename:
            hplc = self.hplc_run.hdf5_filename
        elif sdi.hplcFile:
            hplc = sdi.hplcFile.path.value
        else:
            path = sdi.rawImage.path.value
            if "_" in path:
                hplc = "_".join(os.path.splitext(path)[0].split("_")[:-1]) + ".h5"
            else:
                hplc = os.path.splitext(path)[0] + ".h5"

        if not self.hplc_run.hdf5_filename:
            with self._sem:
                self.hplc_run.init_hdf5(hplc)

        self.xsDataResult.hplcFile = XSDataFile(XSDataString(hplc))

    def process(self, _edObject=None):
        EDPluginControl.process(self)
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.process")

        xsdIn = XSDataInputBioSaxsProcessOneFilev1_0(rawImage=self.dataInput.rawImage,
                                                    sample=self.dataInput.sample,
                                                    experimentSetup=self.dataInput.experimentSetup,
                                                    rawImageSize=self.dataInput.rawImageSize,
                                                    normalizedImage=self.dataInput.normalizedImage,
                                                    integratedCurve=self.dataInput.integratedCurve,
                                                    runId=self.dataInput.runId,
                                                    frameId=self.dataInput.frameId)
        self.__edPluginProcessOneFile = self.loadPlugin(self.strControlledPluginProcessOneFile)
        self.__edPluginProcessOneFile.dataInput = xsdIn
        self.__edPluginProcessOneFile.connectSUCCESS(self.doSuccessProcessOneFile)
        self.__edPluginProcessOneFile.connectFAILURE(self.doFailureProcessOneFile)
        self.__edPluginProcessOneFile.executeSynchronous()

        if self.isFailure():
            return

        self.hplc_run.set_time(self.frameId, self.dataInput.rawImage.path.value)
        self.hplc_run.set_2D(self.frameId, self.curve, kind="scattering")

        if True:#self.hplc_run.buffer is None: always compare to first
            xsdIn = XSDataInputDatcmp(inputCurve=[XSDataFile(XSDataString(self.hplc_run.first_curve)),
                                                  XSDataFile(XSDataString(self.curve))])
            self.__edPluginDatCmp = self.loadPlugin(self.strControlledPluginDatCmp)
            self.__edPluginDatCmp.dataInput = xsdIn
            self.__edPluginDatCmp.connectSUCCESS(self.doSuccessDatCmp)
            self.__edPluginDatCmp.connectFAILURE(self.doFailureDatCmp)
            self.__edPluginDatCmp.executeSynchronous()
        else: #not executed
            xsdIn = XSDataInputDatcmp(inputCurve=[XSDataFile(XSDataString(self.hplc_run.buffer)),
                                                  XSDataFile(XSDataString(self.curve))])
            self.__edPluginDatCmp = self.loadPlugin(self.strControlledPluginDatCmp)
            self.__edPluginDatCmp.dataInput = xsdIn
            self.__edPluginDatCmp.connectSUCCESS(self.doSuccessDatCmp)
            self.__edPluginDatCmp.connectFAILURE(self.doFailureDatCmp)
            self.__edPluginDatCmp.executeSynchronous()

        if self.isFailure() or self.isBuffer:
            return

        if self.dataInput.subtractedCurve is not None:
            subtracted = self.dataInput.subtractedCurve.path.value
        else:
            subtracted = os.path.splitext(self.curve)[0] + "_sub.dat"
        xsdIn = XSDataInputDatop(inputCurve=[XSDataFile(XSDataString(self.curve)),
                                              XSDataFile(XSDataString(self.hplc_run.first_curve))],
                                 outputCurve=XSDataFile(XSDataString(subtracted)),
                                 operation=XSDataString("sub"))
        self.__edPluginDatop = self.loadPlugin(self.strControlledPluginDatop)
        self.__edPluginDatop.dataInput = xsdIn
        self.__edPluginDatop.connectSUCCESS(self.doSuccessDatop)
        self.__edPluginDatop.connectFAILURE(self.doFailureDatop)
        self.__edPluginDatop.executeSynchronous()

        if self.subtracted and os.path.exists(self.subtracted):
            xsdIn = XSDataInputSaxsAnalysis(scatterCurve=XSDataFile(XSDataString(self.subtracted)),
                                            gnomFile=XSDataFile(XSDataString(os.path.splitext(self.subtracted)[0] + ".out")))
            self.__edPluginSaxsAnalysis = self.loadPlugin(self.strControlledPluginSaxsAnalysis)
            self.__edPluginSaxsAnalysis.dataInput = xsdIn
            self.__edPluginSaxsAnalysis.connectSUCCESS(self.doSuccessSaxsAnalysis)
            self.__edPluginSaxsAnalysis.connectFAILURE(self.doFailureSaxsAnalysis)
            self.__edPluginSaxsAnalysis.executeSynchronous()



    def postProcess(self, _edObject=None):
        EDPluginControl.postProcess(self)
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.postProcess")
        if self.hplc_run.buffer:
            self.xsDataResult.bufferCurve = XSDataFile(XSDataString(self.hplc_run.buffer))
        if self.curve:
            self.xsDataResult.integratedCurve = XSDataFile(XSDataString(self.curve))
        if self.subtracted:
             self.xsDataResult.subtractedCurve = XSDataFile(XSDataString(self.subtracted))

    def finallyProcess(self, _edObject=None):
        EDPluginControl.finallyProcess(self)
        executiveSummary = os.linesep.join(self.lstExecutiveSummary)
        self.xsDataResult.status = XSDataStatus(executiveSummary=XSDataString(executiveSummary))
        self.dataOutput = self.xsDataResult

    def average_buffers(self):
        """
        Average out all buffers
        """
        self.lstExecutiveSummary.append("Averaging out buffer files: " + ", ".join(self.hplc_run.for_buffer))
        xsdIn = XSDataInputDataver(inputCurve=[XSDataFile(XSDataString(i)) for i in self.hplc_run.for_buffer])
        if self.dataInput.bufferCurve:
            xsdIn.outputCurve = self.dataInput.bufferCurve
        else:
            xsdIn.outputCurve = XSDataFile(XSDataString(self.hplc_run.first_curve[::-1].split("_", 1)[1][::-1] + "_buffer_aver%02i.dat" % len(self.hplc_run.for_buffer)))
        self.__edPluginDatAver = self.loadPlugin(self.strControlledPluginDatAver)
        self.__edPluginDatAver.dataInput = xsdIn
        self.__edPluginDatAver.connectSUCCESS(self.doSuccessDatAver)
        self.__edPluginDatAver.connectFAILURE(self.doFailureDatAver)
        self.__edPluginDatAver.executeSynchronous()

    def doSuccessProcessOneFile(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.doSuccessProcessOneFile")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsHPLCv1_0.doSuccessProcessOneFile")
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.status and  _edPlugin.dataOutput.status.executiveSummary:
            self.lstExecutiveSummary.append(_edPlugin.dataOutput.status.executiveSummary.value)
        output = _edPlugin.dataOutput
        if not output.integratedCurve:
            strErr = "Edna plugin ProcessOneFile did not produce integrated curve"
            self.ERROR(strErr)
            self.lstExecutiveSummary.append(strErr)
            self.setFailure()
            return
        self.curve = output.integratedCurve.path.value
        if not os.path.exists(self.curve):
            strErr = "Edna plugin ProcessOneFile: integrated curve not on disk !!"
            self.ERROR(strErr)
            self.lstExecutiveSummary.append(strErr)
            self.setFailure()
            return
        self.xsDataResult.integratedCurve = output.integratedCurve
        self.xsDataResult.normalizedImage = output.normalizedImage
        with self._sem:
            if not self.hplc_run.first_curve:
                 self.hplc_run.first_curve = self.curve
                 self.hplc_run.for_buffer.append(self.curve)
            self.hplc_run.curves.append(self.curve)


    def doFailureProcessOneFile(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.doFailureProcessOneFile")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsHPLCv1_0.doFailureProcessOneFile")
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.status and  _edPlugin.dataOutput.status.executiveSummary:
            self.lstExecutiveSummary.append(_edPlugin.dataOutput.status.executiveSummary.value)
        else:
            self.lstExecutiveSummary.append("Edna plugin ProcessOneFile failed.")
        self.setFailure()

    def doSuccessDatop(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.doSuccessDatop")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsHPLCv1_0.doSuccessDatop")
        if _edPlugin and _edPlugin.dataOutput:
            output = _edPlugin.dataOutput
            if output.status and  output.status.executiveSummary:
                self.lstExecutiveSummary.append(output.status.executiveSummary.value)
            if output.outputCurve:
                self.subtracted = output.outputCurve.path.value
                if os.path.exists(self.subtracted):
                    self.xsDataResult.subtractedCurve = output.outputCurve
                    self.hplc_run.set_2D(self.frameId, self.curve, kind="subtracted")
                else:
                    strErr = "Edna plugin datop did not produce subtracted file %s" % subtracted
                    self.ERROR(strErr)
                    self.lstExecutiveSummary.append(strErr)
                    self.setFailure()

    def doFailureDatop(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.doFailureDatop")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsHPLCv1_0.doFailureDatop")
        strErr = "Edna plugin datop failed."
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.status and  _edPlugin.dataOutput.status.executiveSummary:
            self.lstExecutiveSummary.append(_edPlugin.dataOutput.status.executiveSummary.value)
        else:
            self.lstExecutiveSummary.append(strErr)
        self.ERROR(strErr)
        self.setFailure()

    def doSuccessSaxsAnalysis(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.doSuccessSaxsAnalysis")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsHPLCv1_0.doSuccessSaxsAnalysis")
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.status and  _edPlugin.dataOutput.status.executiveSummary:
            self.lstExecutiveSummary.append(_edPlugin.dataOutput.status.executiveSummary.value)
        gnom = _edPlugin.dataOutput.gnom
        if gnom:
            if gnom.rgGnom:
                self.hplc_run.set_scal(self.frameId, gnom.rgGnom.value, key="gnom")
            if gnom.dmax:
                self.hplc_run.set_scal(self.frameId, gnom.dmax.value, key="Dmax")
            if gnom.total:
                self.hplc_run.set_scal(self.frameId, gnom.total.value, key="total")
            self.xsDataResult.gnom = gnom

        volume = _edPlugin.dataOutput.volume
        if volume:
            self.hplc_run.set_scal(self.frameId, volume.value, key="volume")
            self.xsDataResult.volume = volume
        rg = _edPlugin.dataOutput.autoRg
        if rg:
            if rg.rg:
                self.hplc_run.set_scal(self.frameId, rg.rg.value, key="Rg")
            if rg.rgStdev:
                self.hplc_run.set_scal(self.frameId, rg.rgStdev.value, key="Rg_Stdev")
            if rg.i0:
                self.hplc_run.set_scal(self.frameId, rg.i0.value, key="I0")
            if rg.i0Stdev:
                self.hplc_run.set_scal(self.frameId, rg.i0Stdev.value, key="I0_Stdev")
            if rg.quality:
                self.hplc_run.set_scal(self.frameId, rg.quality.value, key="quality")
            self.xsDataResult.autoRg = rg

    def doFailureSaxsAnalysis(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.doFailureSaxsAnalysis")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsHPLCv1_0.doFailureSaxsAnalysis")
        strErr = "Edna plugin SaxsAnalysis failed."
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.status and  _edPlugin.dataOutput.status.executiveSummary:
            self.lstExecutiveSummary.append(_edPlugin.dataOutput.status.executiveSummary.value)
        else:
            self.lstExecutiveSummary.append("Edna plugin SaxsAnalysis failed.")
        self.setFailure()

    def doSuccessDatCmp(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.doSuccessDatCmp")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsHPLCv1_0.doSuccessDatCmp")
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.status and  _edPlugin.dataOutput.status.executiveSummary:
            self.lstExecutiveSummary.append(_edPlugin.dataOutput.status.executiveSummary.value)
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.fidelity:
            fidelity = _edPlugin.dataOutput.fidelity.value
        else:
            strErr = "No fidelity in output of datcmp"
            self.error(strErr)
            self.lstExecutiveSummary.append(strErr)
            #self.setFailure()
            fidelity = 0
        if self.hplc_run.buffer is None:
            if fidelity > 0:
                self.isBuffer = True
                #with self._sem:
                self.hplc_run.for_buffer.append(self.curve)
            else :
                self.average_buffers()
        elif fidelity > 0:
            self.isBuffer = True
            
#complex type XSDataResultDatcmp extends XSDataResult {
#    "Higher chi-values indicate dis-similarities in the input.\n
#     Fidelity gives the likelihood of the two data sets being identical.
#    "
#    chi: XSDataDouble 
#    fidelity: XSDataDouble
#}
    def doFailureDatCmp(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.doFailureDatCmp")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsHPLCv1_0.doFailureDatCmp")
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.status and  _edPlugin.dataOutput.status.executiveSummary:
            self.lstExecutiveSummary.append(_edPlugin.dataOutput.status.executiveSummary.value)
        else:
            self.lstExecutiveSummary.append("Edna plugin DatCmp failed.")
        self.setFailure()


    def doSuccessDatAver(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.doSuccessDatAver")
        self.retrieveSuccessMessages(_edPlugin, "EDPluginBioSaxsHPLCv1_0.doSuccessDatAver")
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.outputCurve:
            buffer = _edPlugin.dataOutput.outputCurve.path.value
            if os.path.exists(buffer):
                with self._sem:
                    self.hplc_run.buffer = buffer
            else:
                strErr = "DatAver claimed buffer is in %s but no such file !!!" % buffer
                self.ERROR(strError)
                self.lstExecutiveSummary.append(strError)
                self.setFailure()

    def doFailureDatAver(self, _edPlugin=None):
        self.DEBUG("EDPluginBioSaxsHPLCv1_0.doFailureDatAver")
        self.retrieveFailureMessages(_edPlugin, "EDPluginBioSaxsHPLCv1_0.doFailureDatAver")
        if _edPlugin and _edPlugin.dataOutput and _edPlugin.dataOutput.status and  _edPlugin.dataOutput.status.executiveSummary:
            self.lstExecutiveSummary.append(_edPlugin.dataOutput.status.executiveSummary.value)
        else:
            self.lstExecutiveSummary.append("Edna plugin DatAver failed.")
        self.setFailure()


