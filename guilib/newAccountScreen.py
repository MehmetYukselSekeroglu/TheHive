# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raw_ui_files/configureNewAccoıunts.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConfigureAccounts(object):
    def setupUi(self, ConfigureAccounts):
        ConfigureAccounts.setObjectName("ConfigureAccounts")
        ConfigureAccounts.resize(480, 520)
        self.verticalLayout = QtWidgets.QVBoxLayout(ConfigureAccounts)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_title = QtWidgets.QFrame(ConfigureAccounts)
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_title)
        self.gridLayout.setObjectName("gridLayout")
        self.label_title = QtWidgets.QLabel(self.frame_title)
        self.label_title.setStyleSheet("font: 15pt \"Hack\";")
        self.label_title.setObjectName("label_title")
        self.gridLayout.addWidget(self.label_title, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_title)
        self.frame_username = QtWidgets.QFrame(ConfigureAccounts)
        self.frame_username.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_username.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_username.setObjectName("frame_username")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_username)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_username = QtWidgets.QLabel(self.frame_username)
        self.label_username.setStyleSheet("font: 14pt \"Hack\";")
        self.label_username.setObjectName("label_username")
        self.gridLayout_2.addWidget(self.label_username, 0, 0, 1, 1)
        self.lineEdit_getNewUsername = QtWidgets.QLineEdit(self.frame_username)
        self.lineEdit_getNewUsername.setMinimumSize(QtCore.QSize(341, 27))
        self.lineEdit_getNewUsername.setMaximumSize(QtCore.QSize(341, 27))
        self.lineEdit_getNewUsername.setStyleSheet("font: 12pt \"Hack\";")
        self.lineEdit_getNewUsername.setObjectName("lineEdit_getNewUsername")
        self.gridLayout_2.addWidget(self.lineEdit_getNewUsername, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_username)
        self.frame_password_input = QtWidgets.QFrame(ConfigureAccounts)
        self.frame_password_input.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_password_input.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_password_input.setObjectName("frame_password_input")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_password_input)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_password = QtWidgets.QLabel(self.frame_password_input)
        self.label_password.setStyleSheet("font: 14pt \"Hack\";")
        self.label_password.setObjectName("label_password")
        self.gridLayout_3.addWidget(self.label_password, 0, 0, 1, 1)
        self.lineEdit_getNewPassword = QtWidgets.QLineEdit(self.frame_password_input)
        self.lineEdit_getNewPassword.setMinimumSize(QtCore.QSize(341, 27))
        self.lineEdit_getNewPassword.setMaximumSize(QtCore.QSize(341, 27))
        self.lineEdit_getNewPassword.setStyleSheet("font: 12pt \"Hack\";")
        self.lineEdit_getNewPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_getNewPassword.setObjectName("lineEdit_getNewPassword")
        self.gridLayout_3.addWidget(self.lineEdit_getNewPassword, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_password_input)
        self.frame_passwordVerify = QtWidgets.QFrame(ConfigureAccounts)
        self.frame_passwordVerify.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_passwordVerify.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_passwordVerify.setObjectName("frame_passwordVerify")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_passwordVerify)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit_getNewPasswordVerify = QtWidgets.QLineEdit(self.frame_passwordVerify)
        self.lineEdit_getNewPasswordVerify.setMinimumSize(QtCore.QSize(341, 27))
        self.lineEdit_getNewPasswordVerify.setMaximumSize(QtCore.QSize(341, 27))
        self.lineEdit_getNewPasswordVerify.setStyleSheet("font: 12pt \"Hack\";")
        self.lineEdit_getNewPasswordVerify.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_getNewPasswordVerify.setObjectName("lineEdit_getNewPasswordVerify")
        self.gridLayout_4.addWidget(self.lineEdit_getNewPasswordVerify, 2, 0, 1, 1)
        self.label_passwordVerify = QtWidgets.QLabel(self.frame_passwordVerify)
        self.label_passwordVerify.setStyleSheet("font: 14pt \"Hack\";")
        self.label_passwordVerify.setObjectName("label_passwordVerify")
        self.gridLayout_4.addWidget(self.label_passwordVerify, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_passwordVerify)
        self.frame_buttons = QtWidgets.QFrame(ConfigureAccounts)
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons.setObjectName("frame_buttons")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_buttons)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_exit_app = QtWidgets.QPushButton(self.frame_buttons)
        self.pushButton_exit_app.setStyleSheet("font: 14pt \"Hack\";")
        self.pushButton_exit_app.setObjectName("pushButton_exit_app")
        self.gridLayout_5.addWidget(self.pushButton_exit_app, 1, 1, 1, 1)
        self.pushButton_confirmAccount = QtWidgets.QPushButton(self.frame_buttons)
        self.pushButton_confirmAccount.setStyleSheet("font: 14pt \"Hack\";")
        self.pushButton_confirmAccount.setObjectName("pushButton_confirmAccount")
        self.gridLayout_5.addWidget(self.pushButton_confirmAccount, 1, 0, 1, 1)
        self.label_status_info = QtWidgets.QLabel(self.frame_buttons)
        self.label_status_info.setStyleSheet("font: 12pt \"Hack\";")
        self.label_status_info.setObjectName("label_status_info")
        self.gridLayout_5.addWidget(self.label_status_info, 2, 0, 1, 2)
        self.verticalLayout.addWidget(self.frame_buttons)

        self.retranslateUi(ConfigureAccounts)
        QtCore.QMetaObject.connectSlotsByName(ConfigureAccounts)

    def retranslateUi(self, ConfigureAccounts):
        _translate = QtCore.QCoreApplication.translate
        ConfigureAccounts.setWindowTitle(_translate("ConfigureAccounts", "Form"))
        self.label_title.setText(_translate("ConfigureAccounts", "<html><head/><body><p align=\"center\">Prepare Local Account</p></body></html>"))
        self.label_username.setText(_translate("ConfigureAccounts", "NEW USERNAME:"))
        self.label_password.setText(_translate("ConfigureAccounts", "NEW PASSOWRD:"))
        self.label_passwordVerify.setText(_translate("ConfigureAccounts", "VERIFY PASSWORD:"))
        self.pushButton_exit_app.setText(_translate("ConfigureAccounts", "exit application"))
        self.pushButton_confirmAccount.setText(_translate("ConfigureAccounts", "confirm"))
        self.label_status_info.setText(_translate("ConfigureAccounts", "Status:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConfigureAccounts = QtWidgets.QWidget()
    ui = Ui_ConfigureAccounts()
    ui.setupUi(ConfigureAccounts)
    ConfigureAccounts.show()
    sys.exit(app.exec_())
