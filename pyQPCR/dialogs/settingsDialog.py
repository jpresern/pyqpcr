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

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from pyQPCR.utils.odict import *

__author__ = "$Author$"
__date__ = "$Date$"
__version__ = "$Revision$"

class SuffixComboBox(QComboBox):

    def __init__(self, parent=None):
        QComboBox.__init__(self, parent)

    def addItem(self, item, *args):
        suffix = QString("%")
        item += suffix
        QComboBox.addItem(self, item, *args)

    def addItems(self, items):
        for item in items:
            self.addItem(item)

    def currentText(self):
        cText = QComboBox.currentText(self)
        return cText[:-1]

class SettingsDialog(QDialog):

    def __init__(self, parent=None, ect=0.3, ctmin=35, confidence=0.9,
                 errtype="normal"):
        self.parent = parent
        QDialog.__init__(self, parent)

        labTit = QLabel("<b>Quality Control:</b>")
        lab1 = QLabel("E(ct) maximum :")
        self.ectLineEdit = QLineEdit("%.2f" % ect)
        self.ectLineEdit.setValidator(QDoubleValidator(self))
        lab1.setBuddy(self.ectLineEdit)
        lab2 = QLabel("Negative ct maximum :")
        self.ctMinLineEdit = QLineEdit("%.2f" % ctmin)
        self.ctMinLineEdit.setValidator(QDoubleValidator(self))
        lab2.setBuddy(self.ctMinLineEdit)

        labConf = QLabel("<b>Confidence interval :</b>")
        lab3 = QLabel("Distribution type :")
        self.typeCbox = QComboBox()
        self.types = {}
        self.types[QString('Gaussian')] = 'normal'
        self.types[QString('Student t-test')] = 'student'
        self.typeCbox.addItems(self.types.keys())
        if errtype == "student":
            self.typeCbox.setCurrentIndex(0)
        else:
            self.typeCbox.setCurrentIndex(1)

        lab4 = QLabel("Confidence level :")
        self.confCbox = SuffixComboBox()

        conf = '%.2f' % (100*confidence)
        liste = OrderedDict()
        liste['75.00'] = 0
        liste['80.00'] = 1
        liste['85.00'] = 2
        liste['90.00'] = 3
        liste['95.00'] = 4
        liste['97.50'] = 5
        liste['99.00'] = 6
        liste['99.50'] = 7
        liste['99.75'] = 8
        liste['99.90'] = 9
        liste['99.95'] = 10
        self.confCbox.addItems(liste.keys())
        try:
            self.confCbox.setCurrentIndex(liste[conf])
        except KeyError:
            self.confCbox.setCurrentIndex(4)
        lab3.setBuddy(self.confCbox)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|
                                     QDialogButtonBox.Cancel)

        gLayout = QGridLayout()
        gLayout.addWidget(lab1, 0, 0)
        gLayout.addWidget(self.ectLineEdit, 0, 1)
        gLayout.addWidget(lab2, 1, 0)
        gLayout.addWidget(self.ctMinLineEdit, 1, 1)

        gLayout2 = QGridLayout()
        gLayout2.addWidget(lab3, 0, 0)
        gLayout2.addWidget(self.typeCbox, 0, 1)
        gLayout2.addWidget(lab4, 1, 0)
        gLayout2.addWidget(self.confCbox, 1, 1)

        layout = QVBoxLayout()
        layout.addWidget(labTit)
        layout.addLayout(gLayout)
        layout.addWidget(labConf)
        layout.addLayout(gLayout2)
        layout.addWidget(buttonBox)
        self.setLayout(layout)

        self.setWindowTitle("%s Settings" % QApplication.applicationName())
        # Connections
        self.connect(buttonBox, SIGNAL("accepted()"), self, SLOT("accept()"))
        self.connect(buttonBox, SIGNAL("rejected()"), self, SLOT("reject()"))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = SettingsDialog()
    form.show()
    app.exec_()
