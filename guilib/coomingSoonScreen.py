# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raw_ui_files/coomingSoonScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CoomingSoonScreen(object):
    def setupUi(self, CoomingSoonScreen):
        CoomingSoonScreen.setObjectName("CoomingSoonScreen")
        CoomingSoonScreen.resize(883, 421)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mainLogo/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CoomingSoonScreen.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(CoomingSoonScreen)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(CoomingSoonScreen)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_title = QtWidgets.QLabel(self.widget)
        self.label_title.setStyleSheet("font: 15pt \"Hack\";")
        self.label_title.setObjectName("label_title")
        self.gridLayout_2.addWidget(self.label_title, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.textBrowser_infotmationPage = QtWidgets.QTextBrowser(CoomingSoonScreen)
        self.textBrowser_infotmationPage.setObjectName("textBrowser_infotmationPage")
        self.gridLayout.addWidget(self.textBrowser_infotmationPage, 1, 0, 1, 1)

        self.retranslateUi(CoomingSoonScreen)
        QtCore.QMetaObject.connectSlotsByName(CoomingSoonScreen)

    def retranslateUi(self, CoomingSoonScreen):
        _translate = QtCore.QCoreApplication.translate
        CoomingSoonScreen.setWindowTitle(_translate("CoomingSoonScreen", "Form"))
        self.label_title.setText(_translate("CoomingSoonScreen", "<html><head/><body><p align=\"center\">This Future Not Available This Version</p></body></html>"))
        self.textBrowser_infotmationPage.setHtml(_translate("CoomingSoonScreen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
import main_icon_files_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CoomingSoonScreen = QtWidgets.QWidget()
    ui = Ui_CoomingSoonScreen()
    ui.setupUi(CoomingSoonScreen)
    CoomingSoonScreen.show()
    sys.exit(app.exec_())
