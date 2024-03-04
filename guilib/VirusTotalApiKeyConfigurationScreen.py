# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raw_ui_files/ApiKeyConfigurationOnlyKeyScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ApiKeyConfScreen(object):
    def setupUi(self, ApiKeyConfScreen):
        ApiKeyConfScreen.setObjectName("ApiKeyConfScreen")
        ApiKeyConfScreen.resize(534, 142)
        self.gridLayout = QtWidgets.QGridLayout(ApiKeyConfScreen)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(ApiKeyConfScreen)
        self.label_2.setStyleSheet("font: 11pt \"Hack\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.pushButton_startConfiguration = QtWidgets.QPushButton(ApiKeyConfScreen)
        self.pushButton_startConfiguration.setStyleSheet("font: 11pt \"Hack\";")
        self.pushButton_startConfiguration.setObjectName("pushButton_startConfiguration")
        self.gridLayout.addWidget(self.pushButton_startConfiguration, 4, 0, 1, 1)
        self.lineEdit_apiKeyInput = QtWidgets.QLineEdit(ApiKeyConfScreen)
        self.lineEdit_apiKeyInput.setMinimumSize(QtCore.QSize(330, 31))
        self.lineEdit_apiKeyInput.setStyleSheet("font: 11pt \"Hack\";")
        self.lineEdit_apiKeyInput.setObjectName("lineEdit_apiKeyInput")
        self.gridLayout.addWidget(self.lineEdit_apiKeyInput, 2, 1, 1, 3)
        self.pushButton_exitScreen = QtWidgets.QPushButton(ApiKeyConfScreen)
        self.pushButton_exitScreen.setStyleSheet("font: 11pt \"Hack\";")
        self.pushButton_exitScreen.setObjectName("pushButton_exitScreen")
        self.gridLayout.addWidget(self.pushButton_exitScreen, 4, 1, 1, 1)
        self.label_apiServiceInfoMessage = QtWidgets.QLabel(ApiKeyConfScreen)
        self.label_apiServiceInfoMessage.setMinimumSize(QtCore.QSize(0, 0))
        self.label_apiServiceInfoMessage.setMaximumSize(QtCore.QSize(0, 0))
        self.label_apiServiceInfoMessage.setStyleSheet("font: 12pt \"Hack\";")
        self.label_apiServiceInfoMessage.setText("")
        self.label_apiServiceInfoMessage.setObjectName("label_apiServiceInfoMessage")
        self.gridLayout.addWidget(self.label_apiServiceInfoMessage, 1, 0, 1, 4)
        self.label_3 = QtWidgets.QLabel(ApiKeyConfScreen)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setStyleSheet("font: 11pt \"Hack\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 2)
        self.label = QtWidgets.QLabel(ApiKeyConfScreen)
        self.label.setStyleSheet("font: 11pt \"Hack\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)

        self.retranslateUi(ApiKeyConfScreen)
        QtCore.QMetaObject.connectSlotsByName(ApiKeyConfScreen)

    def retranslateUi(self, ApiKeyConfScreen):
        _translate = QtCore.QCoreApplication.translate
        ApiKeyConfScreen.setWindowTitle(_translate("ApiKeyConfScreen", "Form"))
        self.label_2.setText(_translate("ApiKeyConfScreen", "Api Key:"))
        self.pushButton_startConfiguration.setText(_translate("ApiKeyConfScreen", "Start Configuration"))
        self.pushButton_exitScreen.setText(_translate("ApiKeyConfScreen", "Exit"))
        self.label_3.setText(_translate("ApiKeyConfScreen", "Status:"))
        self.label.setText(_translate("ApiKeyConfScreen", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Configure Api Key</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ApiKeyConfScreen = QtWidgets.QWidget()
    ui = Ui_ApiKeyConfScreen()
    ui.setupUi(ApiKeyConfScreen)
    ApiKeyConfScreen.show()
    sys.exit(app.exec_())
