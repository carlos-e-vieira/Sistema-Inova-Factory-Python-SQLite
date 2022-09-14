# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Tela_Login(object):
    def setupUi(self, Tela_Login):
        if not Tela_Login.objectName():
            Tela_Login.setObjectName(u"Tela_Login")
        Tela_Login.resize(500, 400)
        Tela_Login.setMinimumSize(QSize(500, 0))
        Tela_Login.setMaximumSize(QSize(500, 400))
        Tela_Login.setStyleSheet(u"background-color: rgb(51, 51, 51);")
        self.layoutWidget = QWidget(Tela_Login)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 210, 328, 31))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(70, 0))

        self.horizontalLayout.addWidget(self.label)

        self.input_login = QLineEdit(self.layoutWidget)
        self.input_login.setObjectName(u"input_login")
        self.input_login.setMinimumSize(QSize(250, 0))
        font = QFont()
        font.setPointSize(14)
        self.input_login.setFont(font)
        self.input_login.setStyleSheet(u"background-color: rgb(90, 90, 90);\n"
"border: none;\n"
"color: rgb(255, 255, 255);\n"
"padding: 2px;")

        self.horizontalLayout.addWidget(self.input_login)

        self.layoutWidget_2 = QWidget(Tela_Login)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(60, 250, 328, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(70, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.input_senha = QLineEdit(self.layoutWidget_2)
        self.input_senha.setObjectName(u"input_senha")
        self.input_senha.setMinimumSize(QSize(250, 0))
        self.input_senha.setFont(font)
        self.input_senha.setStyleSheet(u"background-color: rgb(90, 90, 90);\n"
"border: none;\n"
"color: rgb(255, 255, 255);\n"
"padding: 2px;")
        self.input_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.input_senha)

        self.label_4 = QLabel(Tela_Login)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 120, 281, 41))
        font1 = QFont()
        font1.setPointSize(40)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"font: \"Myriad Pro\";")
        self.label_5 = QLabel(Tela_Login)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, 40, 100, 100))
        self.label_5.setMinimumSize(QSize(100, 100))
        self.label_3 = QLabel(Tela_Login)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(61, 291, 68, 26))
        self.label_3.setMinimumSize(QSize(68, 0))
        self.btn_login = QPushButton(Tela_Login)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(135, 291, 252, 35))
        self.btn_login.setMinimumSize(QSize(252, 35))
        font2 = QFont()
        self.btn_login.setFont(font2)
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 204, 0);\n"
"	border-radius: 1px;\n"
"	font-size: 14px;\n"
"	\n"
"	\n"
"	color: rgb(51, 51, 51);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgba(255, 204, 0, 200);\n"
"	\n"
"}")
        self.label_3.raise_()
        self.btn_login.raise_()
        self.label_5.raise_()
        self.label_4.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget_2.raise_()

        self.retranslateUi(Tela_Login)

        QMetaObject.connectSlotsByName(Tela_Login)
    # setupUi

    def retranslateUi(self, Tela_Login):
        Tela_Login.setWindowTitle(QCoreApplication.translate("Tela_Login", u"Form", None))
        self.label.setText(QCoreApplication.translate("Tela_Login", u"<html><head/><body><p align=\"right\"><span style=\" font-size:11pt; color:#ffffff;\">Usu\u00e1rio</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Tela_Login", u"<html><head/><body><p align=\"right\"><span style=\" font-size:11pt; color:#ffffff;\">Senha</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Tela_Login", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffcc00;\">inova</span><span style=\" font-size:28pt; font-weight:600; color:#f2f2f2;\">factory</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Tela_Login", u"<html><head/><body><p align=\"center\"><img src=\"View/imagens/icone-login.png\"></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Tela_Login", u"<html><head/><body><p align=\"right\"><br/></p></body></html>", None))
        self.btn_login.setText(QCoreApplication.translate("Tela_Login", u"Login", None))
    # retranslateUi

