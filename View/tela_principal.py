# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_principal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Tela_Principal(object):
    def setupUi(self, Tela_Principal):
        if not Tela_Principal.objectName():
            Tela_Principal.setObjectName(u"Tela_Principal")
        Tela_Principal.resize(910, 610)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Tela_Principal.sizePolicy().hasHeightForWidth())
        Tela_Principal.setSizePolicy(sizePolicy)
        Tela_Principal.setMinimumSize(QSize(910, 610))
        Tela_Principal.setMaximumSize(QSize(910, 610))
        self.centralwidget = QWidget(Tela_Principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setGeometry(QRect(10, 130, 890, 470))
        self.Pages.setMinimumSize(QSize(890, 470))
        self.Pages.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tela_sobre = QWidget()
        self.tela_sobre.setObjectName(u"tela_sobre")
        self.label_19 = QLabel(self.tela_sobre)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(9, 9, 79, 33))
        self.label_19.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(20)
        self.label_19.setFont(font)
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(self.tela_sobre)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(9, 65, 266, 150))
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_15.setWordWrap(True)
        self.Pages.addWidget(self.tela_sobre)
        self.tela_home = QWidget()
        self.tela_home.setObjectName(u"tela_home")
        self.verticalLayout = QVBoxLayout(self.tela_home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.tela_home)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Myriad Pro\";")

        self.verticalLayout.addWidget(self.label_3)

        self.Pages.addWidget(self.tela_home)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(780, 10, 119, 37))
        self.layout_menu_superior = QHBoxLayout(self.layoutWidget)
        self.layout_menu_superior.setObjectName(u"layout_menu_superior")
        self.layout_menu_superior.setContentsMargins(0, 0, 0, 0)
        self.btn_menu_sobre = QPushButton(self.layoutWidget)
        self.btn_menu_sobre.setObjectName(u"btn_menu_sobre")
        self.btn_menu_sobre.setMinimumSize(QSize(35, 35))
        font1 = QFont()
        font1.setFamily(u"Arial,Helvetica,sans-serif")
        font1.setBold(True)
        font1.setWeight(62)
        self.btn_menu_sobre.setFont(font1)
        self.btn_menu_sobre.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 153, 255);\n"
"	border-radius: 2px;\n"
"	font-weight: 500;\n"
"	font-size: 12px;\n"
"	font-family: Arial, Helvetica, sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 145, 218);\n"
"}")

        self.layout_menu_superior.addWidget(self.btn_menu_sobre)

        self.btn_menu_logof = QPushButton(self.layoutWidget)
        self.btn_menu_logof.setObjectName(u"btn_menu_logof")
        self.btn_menu_logof.setMinimumSize(QSize(35, 35))
        self.btn_menu_logof.setFont(font1)
        self.btn_menu_logof.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(51, 51, 51);\n"
"	border-radius: 2px;\n"
"	font-weight: 500;\n"
"	font-size: 12px;\n"
"	font-family: Arial, Helvetica, sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.layout_menu_superior.addWidget(self.btn_menu_logof)

        self.btn_menu_sair = QPushButton(self.layoutWidget)
        self.btn_menu_sair.setObjectName(u"btn_menu_sair")
        self.btn_menu_sair.setMinimumSize(QSize(35, 35))
        self.btn_menu_sair.setFont(font1)
        self.btn_menu_sair.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(227, 0, 0);\n"
"	border-radius: 2px;\n"
"	font-weight: 500;\n"
"	font-size: 12px;\n"
"	font-family: Arial, Helvetica, sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(203, 0, 0);\n"
"}")

        self.layout_menu_superior.addWidget(self.btn_menu_sair)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 10, 367, 37))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(11, 61, 908, 57))
        self.layout_menu = QHBoxLayout(self.widget1)
        self.layout_menu.setObjectName(u"layout_menu")
        self.layout_menu.setContentsMargins(0, 0, 20, 0)
        self.btn_menu_home = QPushButton(self.widget1)
        self.btn_menu_home.setObjectName(u"btn_menu_home")
        self.btn_menu_home.setMinimumSize(QSize(137, 55))
        self.btn_menu_home.setMaximumSize(QSize(135, 55))
        self.btn_menu_home.setFont(font1)
        self.btn_menu_home.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(220, 220, 220);\n"
"	border-radius: 2px;\n"
"	font-weight: 500;\n"
"	font-size: 12px;\n"
"	font-family: Arial, Helvetica, sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(203, 203, 203);\n"
"}")

        self.layout_menu.addWidget(self.btn_menu_home)

        self.btn_menu_clientes = QPushButton(self.widget1)
        self.btn_menu_clientes.setObjectName(u"btn_menu_clientes")
        self.btn_menu_clientes.setMinimumSize(QSize(137, 55))
        self.btn_menu_clientes.setMaximumSize(QSize(135, 55))
        self.btn_menu_clientes.setFont(font1)
        self.btn_menu_clientes.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(220, 220, 220);\n"
"	border-radius: 2px;\n"
"	font-weight: 500;\n"
"	font-size: 12px;\n"
"	font-family: Arial, Helvetica, sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(203, 203, 203);\n"
"}")

        self.layout_menu.addWidget(self.btn_menu_clientes)

        self.btn_menu_servicos = QPushButton(self.widget1)
        self.btn_menu_servicos.setObjectName(u"btn_menu_servicos")
        self.btn_menu_servicos.setMinimumSize(QSize(137, 55))
        self.btn_menu_servicos.setMaximumSize(QSize(135, 55))
        self.btn_menu_servicos.setFont(font1)
        self.btn_menu_servicos.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(220, 220, 220);\n"
"	border-radius: 2px;\n"
"	font-weight: 500;\n"
"	font-size: 12px;\n"
"	font-family: Arial, Helvetica, sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(203, 203, 203);\n"
"}")

        self.layout_menu.addWidget(self.btn_menu_servicos)

        self.btn_menu_relatorios = QPushButton(self.widget1)
        self.btn_menu_relatorios.setObjectName(u"btn_menu_relatorios")
        self.btn_menu_relatorios.setMinimumSize(QSize(137, 55))
        self.btn_menu_relatorios.setMaximumSize(QSize(135, 55))
        self.btn_menu_relatorios.setFont(font1)
        self.btn_menu_relatorios.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(220, 220, 220);\n"
"	border-radius: 2px;\n"
"	font-weight: 500;\n"
"	font-size: 12px;\n"
"	font-family: Arial, Helvetica, sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(203, 203, 203);\n"
"}")

        self.layout_menu.addWidget(self.btn_menu_relatorios)

        self.btn_menu_financeiro = QPushButton(self.widget1)
        self.btn_menu_financeiro.setObjectName(u"btn_menu_financeiro")
        self.btn_menu_financeiro.setMinimumSize(QSize(137, 55))
        self.btn_menu_financeiro.setFont(font1)
        self.btn_menu_financeiro.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(220, 220, 220);\n"
"	border-radius: 2px;\n"
"	font-weight: 500;\n"
"	font-size: 12px;\n"
"	font-family: Arial, Helvetica, sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(203, 203, 203);\n"
"}")

        self.layout_menu.addWidget(self.btn_menu_financeiro)

        self.btn_menu_usuarios = QPushButton(self.widget1)
        self.btn_menu_usuarios.setObjectName(u"btn_menu_usuarios")
        self.btn_menu_usuarios.setMinimumSize(QSize(137, 55))
        self.btn_menu_usuarios.setFont(font1)
        self.btn_menu_usuarios.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(220, 220, 220);\n"
"	border-radius: 2px;\n"
"	font-weight: 500;\n"
"	font-size: 12px;\n"
"	font-family: Arial, Helvetica, sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(203, 203, 203);\n"
"}")

        self.layout_menu.addWidget(self.btn_menu_usuarios)

        Tela_Principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(Tela_Principal)

        self.Pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Tela_Principal)
    # setupUi

    def retranslateUi(self, Tela_Principal):
        Tela_Principal.setWindowTitle(QCoreApplication.translate("Tela_Principal", u"MainWindow", None))
        self.label_19.setText(QCoreApplication.translate("Tela_Principal", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#0000a3;\">Sobre</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("Tela_Principal", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Bla bla bla</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Tela_Principal", u"<html><head/><body><p align=\"center\"><img src=\"View/imagens/logo.png\"/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_menu_sobre.setToolTip(QCoreApplication.translate("Tela_Principal", u"<html><head/><body><p><span style=\" font-size:9pt;\">Sobre o Sistema</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_menu_sobre.setText("")
#if QT_CONFIG(tooltip)
        self.btn_menu_logof.setToolTip(QCoreApplication.translate("Tela_Principal", u"<html><head/><body><p><span style=\" font-size:9pt;\">Trocar de Usu\u00e1rio</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_menu_logof.setText("")
#if QT_CONFIG(tooltip)
        self.btn_menu_sair.setToolTip(QCoreApplication.translate("Tela_Principal", u"<html><head/><body><p><span style=\" font-size:9pt;\">Sair do Sistema</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_menu_sair.setText("")
        self.label.setText(QCoreApplication.translate("Tela_Principal", u"<html><head/><body><p><img src=\"View/imagens/icone-header.png\"/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Tela_Principal", u"<html><head/><body><p><span style=\" font-size:10pt;\">Sistema Inova Factory - V 0.1 - By Carlos Eduardo Vieira</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_menu_home.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_menu_home.setText(QCoreApplication.translate("Tela_Principal", u"Home", None))
#if QT_CONFIG(tooltip)
        self.btn_menu_clientes.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_menu_clientes.setText(QCoreApplication.translate("Tela_Principal", u"Clientes", None))
#if QT_CONFIG(tooltip)
        self.btn_menu_servicos.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_menu_servicos.setText(QCoreApplication.translate("Tela_Principal", u"Servi\u00e7os", None))
#if QT_CONFIG(tooltip)
        self.btn_menu_relatorios.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_menu_relatorios.setText(QCoreApplication.translate("Tela_Principal", u"Relat\u00f3rios", None))
#if QT_CONFIG(tooltip)
        self.btn_menu_financeiro.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_menu_financeiro.setText(QCoreApplication.translate("Tela_Principal", u"Financeiro", None))
#if QT_CONFIG(tooltip)
        self.btn_menu_usuarios.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_menu_usuarios.setText(QCoreApplication.translate("Tela_Principal", u"Usu\u00e1rios", None))
    # retranslateUi

