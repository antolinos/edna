#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id: EDTestCasePluginExecuteInterfacev2_2_charAtNewOrientation.py 1555 2010-05-25 07:27:29Z svensson $"
#
#    Copyright (C) 2008-2010 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Karl Levik (karl.levik@diamond.ac.uk)
#
#    Contributing authors:   Marie-Francoise Incardona (incardon@esrf.fr),
#                            Olof Svensson (svensson@esrf.fr) 
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

__authors__ = [ "Karl Levik", "Marie-Francoise Incardona", "Olof Svensson" ]
__contact__ = "karl.levik@diamond.ac.uk"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os
from EDTestCasePluginExecute    import EDTestCasePluginExecute
from EDAssert                   import EDAssert
from XSDataCommon               import XSDataString
from XSDataCommon               import XSDataInteger
from XSDataCommon               import XSDataFloat
from XSDataCommon               import XSDataBoolean


class EDTestCasePluginExecuteInterfacev2_2_charAtNewOrientation(EDTestCasePluginExecute):


    def __init__(self, _strTestName=None):
        EDTestCasePluginExecute.__init__(self, "EDPluginControlInterfacev2_2")
        self.setConfigurationFile(self.getRefConfigFile())
        self.setRequiredPluginConfiguration("EDPluginMOSFLMIndexingv10")
        self.setRequiredPluginConfiguration("EDPluginMOSFLMIntegrationv10")
        self.setRequiredPluginConfiguration("EDPluginMOSFLMGeneratePredictionv10")
        self.setRequiredPluginConfiguration("EDPluginBestv1_2")
        self.setRequiredPluginConfiguration("EDPluginRaddosev10")
        self.setDataInputFile(os.path.join(self.getPluginTestsDataHome(), 
                                           "XSDataInputInterfacev2_2_charAtNewOrientation.xml"))



    def testExecute(self):
        self.run()
        edPlugin = self.getPlugin()
        EDAssert.equal(edPlugin.hasDataOutput("resultCharacterisationv2_0"), True, "Has MXv2 result characterisation")

        if (edPlugin.hasDataOutput("resultCharacterisationv2_0")):
            xsDataResultCharacterisationv2_0 = edPlugin.getDataOutput("resultCharacterisationv2_0")[0]
            xsDataResultCharacterisation = xsDataResultCharacterisationv2_0.getMxv1ResultCharacterisation()
            EDAssert.equal(xsDataResultCharacterisation.getDataCollection() != None, True, "Has data collection output")
            EDAssert.equal(xsDataResultCharacterisation.getIndexingResult() != None, True, "Has indexing result output")
            EDAssert.equal(xsDataResultCharacterisation.getIntegrationResult() != None, True, "Has integration result")
            EDAssert.equal(xsDataResultCharacterisation.getStrategyResult() != None, True, "Has strategy result")


    def process(self):
        self.addTestMethod(self.testExecute)


if __name__ == '__main__':

    edTestCasePluginExecuteInterfacev2_2_charAtNewOrientation = EDTestCasePluginExecuteInterfacev2_2_charAtNewOrientation("EDTestCasePluginExecuteInterfacev2_2_charAtNewOrientation")
    edTestCasePluginExecuteInterfacev2_2_charAtNewOrientation.execute()
