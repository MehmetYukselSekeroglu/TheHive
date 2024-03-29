# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raw_ui_files/videoFrameExtractorScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_video2framWidget(object):
    def setupUi(self, video2framWidget):
        video2framWidget.setObjectName("video2framWidget")
        video2framWidget.resize(987, 595)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mainLogo/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        video2framWidget.setWindowIcon(icon)
        self.gridLayout_5 = QtWidgets.QGridLayout(video2framWidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget_4 = QtWidgets.QWidget(video2framWidget)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setStyleSheet("font: 11pt \"Hack\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.widget_4, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(video2framWidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textBrowser_logAndResults = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser_logAndResults.setMinimumSize(QtCore.QSize(951, 261))
        self.textBrowser_logAndResults.setMaximumSize(QtCore.QSize(16777215, 261))
        self.textBrowser_logAndResults.setStyleSheet("font: 11pt \"Hack\";")
        self.textBrowser_logAndResults.setObjectName("textBrowser_logAndResults")
        self.gridLayout_4.addWidget(self.textBrowser_logAndResults, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.widget_2, 2, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(video2framWidget)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_selectOutputDir = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_selectOutputDir.setStyleSheet("font: 11pt \"Hack\";")
        self.pushButton_selectOutputDir.setObjectName("pushButton_selectOutputDir")
        self.gridLayout.addWidget(self.pushButton_selectOutputDir, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setMinimumSize(QtCore.QSize(231, 23))
        self.label_3.setStyleSheet("font: 11pt \"Hack\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.pushButton_selectVideoFile = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_selectVideoFile.setStyleSheet("font: 11pt \"Hack\";")
        self.pushButton_selectVideoFile.setObjectName("pushButton_selectVideoFile")
        self.gridLayout.addWidget(self.pushButton_selectVideoFile, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setMinimumSize(QtCore.QSize(231, 23))
        self.label_2.setStyleSheet("font: 11pt \"Hack\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.textBrowser_inputFilePathPrint = QtWidgets.QTextBrowser(self.widget_3)
        self.textBrowser_inputFilePathPrint.setMinimumSize(QtCore.QSize(511, 31))
        self.textBrowser_inputFilePathPrint.setMaximumSize(QtCore.QSize(511, 31))
        self.textBrowser_inputFilePathPrint.setStyleSheet("font: 11pt \"Hack\";")
        self.textBrowser_inputFilePathPrint.setObjectName("textBrowser_inputFilePathPrint")
        self.gridLayout.addWidget(self.textBrowser_inputFilePathPrint, 0, 1, 1, 1)
        self.textBrowser_outputDirPathPrint = QtWidgets.QTextBrowser(self.widget_3)
        self.textBrowser_outputDirPathPrint.setMinimumSize(QtCore.QSize(511, 31))
        self.textBrowser_outputDirPathPrint.setMaximumSize(QtCore.QSize(511, 31))
        self.textBrowser_outputDirPathPrint.setStyleSheet("font: 11pt \"Hack\";")
        self.textBrowser_outputDirPathPrint.setObjectName("textBrowser_outputDirPathPrint")
        self.gridLayout.addWidget(self.textBrowser_outputDirPathPrint, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.pushButton_startExtraction = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_startExtraction.setMinimumSize(QtCore.QSize(231, 31))
        self.pushButton_startExtraction.setMaximumSize(QtCore.QSize(231, 31))
        self.pushButton_startExtraction.setStyleSheet("font: 11pt \"Hack\";")
        self.pushButton_startExtraction.setObjectName("pushButton_startExtraction")
        self.gridLayout.addWidget(self.pushButton_startExtraction, 3, 0, 1, 1)
        self.pushButton_stopCurrentJob = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_stopCurrentJob.setMinimumSize(QtCore.QSize(191, 31))
        self.pushButton_stopCurrentJob.setMaximumSize(QtCore.QSize(191, 31))
        self.pushButton_stopCurrentJob.setStyleSheet("font: 11pt \"Hack\";")
        self.pushButton_stopCurrentJob.setObjectName("pushButton_stopCurrentJob")
        self.gridLayout.addWidget(self.pushButton_stopCurrentJob, 3, 1, 1, 1)
        self.gridLayout_5.addWidget(self.widget_3, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(video2framWidget)
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.progressBar_statusPrinterBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar_statusPrinterBar.setMinimumSize(QtCore.QSize(761, 31))
        self.progressBar_statusPrinterBar.setMaximumSize(QtCore.QSize(16777215, 31))
        self.progressBar_statusPrinterBar.setStyleSheet("font: 11pt \"Hack\";")
        self.progressBar_statusPrinterBar.setProperty("value", 0)
        self.progressBar_statusPrinterBar.setObjectName("progressBar_statusPrinterBar")
        self.gridLayout_3.addWidget(self.progressBar_statusPrinterBar, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 7, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 4, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 6, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("font: 11pt \"Hack\";")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 3, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem6, 2, 0, 1, 1)
        self.gridLayout_5.addWidget(self.widget, 3, 0, 1, 1)

        self.retranslateUi(video2framWidget)
        QtCore.QMetaObject.connectSlotsByName(video2framWidget)

    def retranslateUi(self, video2framWidget):
        _translate = QtCore.QCoreApplication.translate
        video2framWidget.setWindowTitle(_translate("video2framWidget", "Form"))
        self.label_4.setText(_translate("video2framWidget", "<html><head/><body><p align=\"center\">Video 2 Frame </p></body></html>"))
        self.textBrowser_logAndResults.setHtml(_translate("video2framWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Hack\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-weight:600;\">LOG AND RESULTS:</span></p></body></html>"))
        self.pushButton_selectOutputDir.setText(_translate("video2framWidget", "select directory"))
        self.label_3.setText(_translate("video2framWidget", "Output Directory:"))
        self.pushButton_selectVideoFile.setText(_translate("video2framWidget", "select file"))
        self.label_2.setText(_translate("video2framWidget", "Input File:"))
        self.pushButton_startExtraction.setText(_translate("video2framWidget", "Start"))
        self.pushButton_stopCurrentJob.setText(_translate("video2framWidget", "stop proccess"))
        self.label.setText(_translate("video2framWidget", "Progress Status:"))
import main_icon_files_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    video2framWidget = QtWidgets.QWidget()
    ui = Ui_video2framWidget()
    ui.setupUi(video2framWidget)
    video2framWidget.show()
    sys.exit(app.exec_())
