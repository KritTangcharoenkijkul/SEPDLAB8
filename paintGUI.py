# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paintGUI.ui',
# licensing of 'paintGUI.ui' applies.
#
# Created: Thu Mar 28 14:02:14 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(723, 572)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.drawField = QtWidgets.QGraphicsView(Form)
        self.drawField.setObjectName("drawField")
        self.gridLayout.addWidget(self.drawField, 0, 0, 1, 1)
        self.clear = QtWidgets.QPushButton(Form)
        self.clear.setObjectName("clear")
        self.gridLayout.addWidget(self.clear, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.clear.setText(QtWidgets.QApplication.translate("Form", "Clear", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "                                                                  Drag The mouse to draw ", None, -1))

