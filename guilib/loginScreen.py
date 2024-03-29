# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raw_ui_files/authenticate.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuthenticationScreen(object):
    def setupUi(self, AuthenticationScreen):
        AuthenticationScreen.setObjectName("AuthenticationScreen")
        AuthenticationScreen.resize(685, 197)
        AuthenticationScreen.setMaximumSize(QtCore.QSize(685, 197))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/private_icon/private_logo_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AuthenticationScreen.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(AuthenticationScreen)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(AuthenticationScreen)
        self.label.setMinimumSize(QtCore.QSize(521, 23))
        self.label.setMaximumSize(QtCore.QSize(521, 23))
        self.label.setStyleSheet("font: 11pt \"Hack\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 4)
        self.label_2 = QtWidgets.QLabel(AuthenticationScreen)
        self.label_2.setMinimumSize(QtCore.QSize(139, 27))
        self.label_2.setMaximumSize(QtCore.QSize(139, 27))
        self.label_2.setStyleSheet("font: 11pt \"Hack\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.lineEdit_initralAuth_password = QtWidgets.QLineEdit(AuthenticationScreen)
        self.lineEdit_initralAuth_password.setMinimumSize(QtCore.QSize(370, 27))
        self.lineEdit_initralAuth_password.setMaximumSize(QtCore.QSize(370, 27))
        self.lineEdit_initralAuth_password.setStyleSheet("font: 11pt \"Hack\";")
        self.lineEdit_initralAuth_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_initralAuth_password.setObjectName("lineEdit_initralAuth_password")
        self.gridLayout.addWidget(self.lineEdit_initralAuth_password, 4, 3, 1, 2)
        self.pushButton_initralAuth_authenticateButton = QtWidgets.QPushButton(AuthenticationScreen)
        self.pushButton_initralAuth_authenticateButton.setMinimumSize(QtCore.QSize(182, 31))
        self.pushButton_initralAuth_authenticateButton.setMaximumSize(QtCore.QSize(182, 31))
        self.pushButton_initralAuth_authenticateButton.setStyleSheet("font: 11pt \"Hack\";")
        self.pushButton_initralAuth_authenticateButton.setObjectName("pushButton_initralAuth_authenticateButton")
        self.gridLayout.addWidget(self.pushButton_initralAuth_authenticateButton, 6, 3, 1, 1)
        self.pushButton_initralAuth_exitButton = QtWidgets.QPushButton(AuthenticationScreen)
        self.pushButton_initralAuth_exitButton.setMinimumSize(QtCore.QSize(182, 31))
        self.pushButton_initralAuth_exitButton.setMaximumSize(QtCore.QSize(182, 31))
        self.pushButton_initralAuth_exitButton.setStyleSheet("font: 11pt \"Hack\";")
        self.pushButton_initralAuth_exitButton.setObjectName("pushButton_initralAuth_exitButton")
        self.gridLayout.addWidget(self.pushButton_initralAuth_exitButton, 6, 4, 1, 1)
        self.lineEdit_initralAuth_username = QtWidgets.QLineEdit(AuthenticationScreen)
        self.lineEdit_initralAuth_username.setMinimumSize(QtCore.QSize(370, 27))
        self.lineEdit_initralAuth_username.setMaximumSize(QtCore.QSize(370, 27))
        self.lineEdit_initralAuth_username.setStyleSheet("font: 11pt \"Hack\";")
        self.lineEdit_initralAuth_username.setObjectName("lineEdit_initralAuth_username")
        self.gridLayout.addWidget(self.lineEdit_initralAuth_username, 2, 3, 1, 2)
        self.label_4_authenticate_status = QtWidgets.QLabel(AuthenticationScreen)
        self.label_4_authenticate_status.setMinimumSize(QtCore.QSize(515, 19))
        self.label_4_authenticate_status.setMaximumSize(QtCore.QSize(515, 19))
        self.label_4_authenticate_status.setStyleSheet("font: 12pt \"Hack\";")
        self.label_4_authenticate_status.setObjectName("label_4_authenticate_status")
        self.gridLayout.addWidget(self.label_4_authenticate_status, 7, 2, 1, 3)
        self.label_3 = QtWidgets.QLabel(AuthenticationScreen)
        self.label_3.setMinimumSize(QtCore.QSize(139, 27))
        self.label_3.setMaximumSize(QtCore.QSize(139, 27))
        self.label_3.setStyleSheet("font: 11pt \"Hack\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 2, 1, 1)
        self.widget = QtWidgets.QWidget(AuthenticationScreen)
        self.widget.setMinimumSize(QtCore.QSize(140, 179))
        self.widget.setMaximumSize(QtCore.QSize(140, 179))
        self.widget.setStyleSheet("image: url(:/mainLogo/logo.png);")
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 0, 8, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)

        self.retranslateUi(AuthenticationScreen)
        QtCore.QMetaObject.connectSlotsByName(AuthenticationScreen)

    def retranslateUi(self, AuthenticationScreen):
        _translate = QtCore.QCoreApplication.translate
        AuthenticationScreen.setWindowTitle(_translate("AuthenticationScreen", "Form"))
        self.label.setText(_translate("AuthenticationScreen", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Authorization Required</span></p></body></html>"))
        self.label_2.setText(_translate("AuthenticationScreen", "USERNAME:"))
        self.pushButton_initralAuth_authenticateButton.setText(_translate("AuthenticationScreen", "authenticate"))
        self.pushButton_initralAuth_exitButton.setText(_translate("AuthenticationScreen", "exit"))
        self.label_4_authenticate_status.setText(_translate("AuthenticationScreen", "Status:"))
        self.label_3.setText(_translate("AuthenticationScreen", "PASSWORD:"))
import main_icon_files_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AuthenticationScreen = QtWidgets.QWidget()
    ui = Ui_AuthenticationScreen()
    ui.setupUi(AuthenticationScreen)
    AuthenticationScreen.show()
    sys.exit(app.exec_())
