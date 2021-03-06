# -*- coding: utf-8 -*-
#
# pyQPCR, an application to analyse qPCR raw data
# Copyright (C) 2008 Thomas Gastine
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

from PyQt4.QtGui import *
from PyQt4.QtCore import *

__author__ = "$Author$"
__date__ = "$Date$"
__version__ = "$Rev$"

class PrintingDialog(QDialog):
    """
    PrintingDialog is displayed when the user want to print
    the results in a PDF file (or send to a printer). It allows
    to choose which kind of results you want to export (table
    of results or plots)

    :attribute btnRes: a check-box that allows to select (unselect)
                       the export of the result table
    :attribute btnStd: a check-box that allows to select (unselect)
                       the export of standard curves
    :attribute btnQuant: a check-box that allows to select (unselect)
                         the export of quantification histograms
    :attribute btnPlate: a check-box that allows to select (unselect)
                         the export of the plate setup
    """
    
    def __init__(self, parent=None):
        """
        Constructor of PrintingDialog

        :param parent: the QWidget parent
        :type parent: PyQt4.QtGui.QWidget
        """
        QDialog.__init__(self, parent)

        lab0 = QLabel("&Plate setup:")
        lab1 = QLabel("&Results table:")
        lab2 = QLabel("&Standard curves:")
        lab3 = QLabel("&Quantification plots:")

        self.btnPlate = QCheckBox()
        self.btnPlate.setChecked(True)
        self.btnRes = QCheckBox()
        self.btnRes.setChecked(True)
        self.btnStd = QCheckBox()
        self.btnQuant = QCheckBox()
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|
                                     QDialogButtonBox.Cancel)     

        lab0.setBuddy(self.btnPlate)
        lab1.setBuddy(self.btnRes)
        lab2.setBuddy(self.btnStd)
        lab3.setBuddy(self.btnQuant)

        layout = QGridLayout()
        layout.addWidget(lab0, 0, 0)
        layout.addWidget(self.btnPlate, 0, 1)
        layout.addWidget(lab1, 1, 0)
        layout.addWidget(self.btnRes, 1, 1)
        layout.addWidget(lab2, 2, 0)
        layout.addWidget(self.btnStd, 2, 1)
        layout.addWidget(lab3, 3, 0)
        layout.addWidget(self.btnQuant, 3, 1)
        layout.addWidget(buttonBox, 4, 0, 1, 2)

        self.setLayout(layout)
        self.setWindowTitle("Printing")

        self.connect(buttonBox, SIGNAL("accepted()"), self, SLOT("accept()"))
        self.connect(buttonBox, SIGNAL("rejected()"), self, SLOT("reject()"))


if __name__=="__main__":
    import sys
    app = QApplication(sys.argv)
    f = PrintingDialog()
    f.show()
    app.exec_()
