#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF, Grenoble
#
#    Principal author:       Jerome Kieffer, jerome.kieffer@esrf.fr
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

__author__ = "Jerome Kieffer, jerome.kieffer@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "ESRF, Grenoble"

from EDTestSuite  import EDTestSuite

class EDTestSuitePluginsMatrix(EDTestSuite):
    """
    This is the test suite for EDNA plugin MatrixReadv1_0 
    It will run subsequently all unit tests and execution tests.     
    """

    def process(self):
        self.addTestSuiteFromName("EDTestSuitePluginsUnitMatrix")
        self.addTestSuiteFromName("EDTestSuitePluginsExecuteMatrix")

if __name__ == '__main__':

    edTestSuitePluginExecMatrixReadv1_0 = EDTestSuitePluginsMatrix("EDTestSuitePluginsMatrix")
    edTestSuitePluginExecMatrixReadv1_0.execute()

