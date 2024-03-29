# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raw_ui_files/ibanParserScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_iban_parser_form(object):
    def setupUi(self, iban_parser_form):
        iban_parser_form.setObjectName("iban_parser_form")
        iban_parser_form.resize(876, 614)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mainLogo/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        iban_parser_form.setWindowIcon(icon)
        self.gridLayout_4 = QtWidgets.QGridLayout(iban_parser_form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget = QtWidgets.QWidget(iban_parser_form)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_title = QtWidgets.QLabel(self.widget)
        self.label_title.setStyleSheet("font: 11pt \"Hack\";")
        self.label_title.setObjectName("label_title")
        self.gridLayout.addWidget(self.label_title, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(iban_parser_form)
        self.widget_2.setStyleSheet("font: 11pt \"Hack\";")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setStyleSheet("font: 11pt \"Hack\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_iban_input = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_iban_input.setStyleSheet("font: 11pt \"Hack\";")
        self.lineEdit_iban_input.setObjectName("lineEdit_iban_input")
        self.gridLayout_2.addWidget(self.lineEdit_iban_input, 1, 0, 1, 3)
        self.comboBox_saveType = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_saveType.setStyleSheet("font: 11pt \"Hack\";")
        self.comboBox_saveType.setObjectName("comboBox_saveType")
        self.comboBox_saveType.addItem("")
        self.comboBox_saveType.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_saveType, 1, 3, 1, 1)
        self.pushButton_parse_iban = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_parse_iban.setStyleSheet("font: 11pt \"Hack\";")
        self.pushButton_parse_iban.setObjectName("pushButton_parse_iban")
        self.gridLayout_2.addWidget(self.pushButton_parse_iban, 2, 0, 1, 1)
        self.pushButton_clearResult = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_clearResult.setStyleSheet("font: 11pt \"Hack\";")
        self.pushButton_clearResult.setObjectName("pushButton_clearResult")
        self.gridLayout_2.addWidget(self.pushButton_clearResult, 2, 1, 1, 1)
        self.pushButton_save_result = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_save_result.setStyleSheet("font: 11pt \"Hack\";")
        self.pushButton_save_result.setObjectName("pushButton_save_result")
        self.gridLayout_2.addWidget(self.pushButton_save_result, 2, 3, 1, 1)
        self.gridLayout_4.addWidget(self.widget_2, 1, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(iban_parser_form)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textBrowser_resultConsole = QtWidgets.QTextBrowser(self.widget_3)
        self.textBrowser_resultConsole.setStyleSheet("font: 11pt \"Hack\";")
        self.textBrowser_resultConsole.setObjectName("textBrowser_resultConsole")
        self.gridLayout_3.addWidget(self.textBrowser_resultConsole, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget_3, 2, 0, 1, 1)

        self.retranslateUi(iban_parser_form)
        QtCore.QMetaObject.connectSlotsByName(iban_parser_form)

    def retranslateUi(self, iban_parser_form):
        _translate = QtCore.QCoreApplication.translate
        iban_parser_form.setWindowTitle(_translate("iban_parser_form", "Form"))
        self.label_title.setText(_translate("iban_parser_form", "<html><head/><body><p align=\"center\">iban parser </p></body></html>"))
        self.label_2.setText(_translate("iban_parser_form", "Enter iban:"))
        self.comboBox_saveType.setItemText(0, _translate("iban_parser_form", "for human *.txt"))
        self.comboBox_saveType.setItemText(1, _translate("iban_parser_form", "for machine *.json"))
        self.pushButton_parse_iban.setText(_translate("iban_parser_form", "parse"))
        self.pushButton_clearResult.setText(_translate("iban_parser_form", "clear"))
        self.pushButton_save_result.setText(_translate("iban_parser_form", "save"))
        self.textBrowser_resultConsole.setHtml(_translate("iban_parser_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Hack\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-weight:600;\">RESULT:</span></p></body></html>"))
import main_icon_files_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    iban_parser_form = QtWidgets.QWidget()
    ui = Ui_iban_parser_form()
    ui.setupUi(iban_parser_form)
    iban_parser_form.show()
    sys.exit(app.exec_())
