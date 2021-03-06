#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:        Olof Svensson
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

__author__ = "Olof Svensson"
__license__ = "GPLv3+"
__copyright__ = "ESRF"

import os

from EDVerbose import EDVerbose
from EDTestCasePluginUnit import EDTestCasePluginUnit

from XSDataMXv1 import XSDataInputCharacterisation

class EDTestCasePluginUnitControlCharacterisationv1_2(EDTestCasePluginUnit):


    def __init__(self, _edStringTestName=None):
        EDTestCasePluginUnit.__init__(self, "EDPluginControlCharacterisationv1_2")
        self.strPathToReferenceInput = os.path.join(self.getPluginTestsDataHome(), \
                                           "XSDataInputCharacterisation_reference.xml")


    def testCheckParameters(self):
        strXMLInput = self.readAndParseFile(self.strPathToReferenceInput)
        xsDataInput = XSDataInputCharacterisation.parseString(strXMLInput)
        edPluginExecCharacterisation = self.createPlugin()
        edPluginExecCharacterisation.setDataInput(xsDataInput)
        edPluginExecCharacterisation.checkParameters()



    def process(self):
        self.addTestMethod(self.testCheckParameters)




if __name__ == '__main__':

    EDTestCasePluginUnitControlCharacterisationv1_2 = EDTestCasePluginUnitControlCharacterisationv1_2("EDTestCasePluginUnitControlCharacterisationv1_2")
    EDTestCasePluginUnitControlCharacterisationv1_2.execute()
