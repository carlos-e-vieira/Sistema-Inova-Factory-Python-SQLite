# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_usuarios.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Tela_Usuarios(object):
    def setupUi(self, Tela_Usuarios):
        if not Tela_Usuarios.objectName():
            Tela_Usuarios.setObjectName(u"Tela_Usuarios")
        Tela_Usuarios.resize(790, 510)
        Tela_Usuarios.setMaximumSize(QSize(790, 510))
        self.Pages = QStackedWidget(Tela_Usuarios)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setGeometry(QRect(10, 70, 770, 431))
        self.Pages.setMinimumSize(QSize(770, 0))
        self.Pages.setMaximumSize(QSize(770, 16777215))
        self.Pages.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tela_form_cadastrar_usuario = QWidget()
        self.tela_form_cadastrar_usuario.setObjectName(u"tela_form_cadastrar_usuario")
        self.btn_cancelar_cadastro_usuario = QPushButton(self.tela_form_cadastrar_usuario)
        self.btn_cancelar_cadastro_usuario.setObjectName(u"btn_cancelar_cadastro_usuario")
        self.btn_cancelar_cadastro_usuario.setGeometry(QRect(180, 220, 155, 35))
        self.btn_cancelar_cadastro_usuario.setMinimumSize(QSize(155, 35))
        font = QFont()
        self.btn_cancelar_cadastro_usuario.setFont(font)
        self.btn_cancelar_cadastro_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar_cadastro_usuario.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	background-color: rgb(223, 0, 0);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(156, 0, 0);\n"
"\n"
"}")
        self.btn_salvar_cadastro_usuario = QPushButton(self.tela_form_cadastrar_usuario)
        self.btn_salvar_cadastro_usuario.setObjectName(u"btn_salvar_cadastro_usuario")
        self.btn_salvar_cadastro_usuario.setGeometry(QRect(10, 220, 155, 35))
        self.btn_salvar_cadastro_usuario.setMinimumSize(QSize(155, 35))
        self.btn_salvar_cadastro_usuario.setFont(font)
        self.btn_salvar_cadastro_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar_cadastro_usuario.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 170, 0);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 90, 0);\n"
"	\n"
"}")
        self.frame = QFrame(self.tela_form_cadastrar_usuario)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 50, 751, 151))
        self.frame.setStyleSheet(u"background-color: rgb(242, 242, 242);\n"
"border: 1px solid #ccc;\n"
"border-radius: 2px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 20, 70, 20))
        self.label_7.setMinimumSize(QSize(70, 0))
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"border: none;")
        self.input_cadastrar_nome_usuario = QLineEdit(self.frame)
        self.input_cadastrar_nome_usuario.setObjectName(u"input_cadastrar_nome_usuario")
        self.input_cadastrar_nome_usuario.setGeometry(QRect(80, 20, 431, 25))
        self.input_cadastrar_nome_usuario.setMinimumSize(QSize(0, 0))
        self.input_cadastrar_nome_usuario.setStyleSheet(u"font-size: 16px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 50, 70, 16))
        self.label_14.setMinimumSize(QSize(70, 0))
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"border: none;")
        self.input_cadastrar_login_usuario = QLineEdit(self.frame)
        self.input_cadastrar_login_usuario.setObjectName(u"input_cadastrar_login_usuario")
        self.input_cadastrar_login_usuario.setGeometry(QRect(80, 50, 431, 25))
        self.input_cadastrar_login_usuario.setStyleSheet(u"font-size: 16px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 80, 70, 20))
        self.label_15.setMinimumSize(QSize(70, 0))
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"border: none;")
        self.input_cadastrar_senha_usuario = QLineEdit(self.frame)
        self.input_cadastrar_senha_usuario.setObjectName(u"input_cadastrar_senha_usuario")
        self.input_cadastrar_senha_usuario.setGeometry(QRect(80, 80, 150, 25))
        self.input_cadastrar_senha_usuario.setMinimumSize(QSize(150, 0))
        self.input_cadastrar_senha_usuario.setStyleSheet(u"font-size: 16px;\n"
"background-color: rgb(255, 255, 255);")
        self.input_cadastrar_senha_usuario.setEchoMode(QLineEdit.Password)
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(240, 80, 111, 20))
        self.label_16.setMinimumSize(QSize(70, 0))
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"border: none;")
        self.input_cadastrar_senha_2_usuario = QLineEdit(self.frame)
        self.input_cadastrar_senha_2_usuario.setObjectName(u"input_cadastrar_senha_2_usuario")
        self.input_cadastrar_senha_2_usuario.setGeometry(QRect(360, 80, 150, 25))
        self.input_cadastrar_senha_2_usuario.setMinimumSize(QSize(150, 0))
        self.input_cadastrar_senha_2_usuario.setStyleSheet(u"font-size: 16px;\n"
"background-color: rgb(255, 255, 255);")
        self.input_cadastrar_senha_2_usuario.setEchoMode(QLineEdit.Password)
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 110, 101, 20))
        self.label_17.setMinimumSize(QSize(70, 0))
        self.label_17.setFont(font1)
        self.label_17.setStyleSheet(u"border: none;")
        self.cb_cadastrar_acesso_usuario = QComboBox(self.frame)
        self.cb_cadastrar_acesso_usuario.addItem("")
        self.cb_cadastrar_acesso_usuario.addItem("")
        self.cb_cadastrar_acesso_usuario.setObjectName(u"cb_cadastrar_acesso_usuario")
        self.cb_cadastrar_acesso_usuario.setGeometry(QRect(140, 110, 371, 25))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_cadastrar_acesso_usuario.sizePolicy().hasHeightForWidth())
        self.cb_cadastrar_acesso_usuario.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(11)
        self.cb_cadastrar_acesso_usuario.setFont(font2)
        self.cb_cadastrar_acesso_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 5px;")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(560, 20, 151, 110))
        self.label.setMinimumSize(QSize(110, 110))
        self.label.setStyleSheet(u"border: none;")
        self.label_2 = QLabel(self.tela_form_cadastrar_usuario)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 221, 21))
        self.Pages.addWidget(self.tela_form_cadastrar_usuario)
        self.tela_form_alterar_usuario = QWidget()
        self.tela_form_alterar_usuario.setObjectName(u"tela_form_alterar_usuario")
        self.btn_salvar_alterar_usuario = QPushButton(self.tela_form_alterar_usuario)
        self.btn_salvar_alterar_usuario.setObjectName(u"btn_salvar_alterar_usuario")
        self.btn_salvar_alterar_usuario.setGeometry(QRect(10, 230, 155, 35))
        self.btn_salvar_alterar_usuario.setMinimumSize(QSize(155, 35))
        self.btn_salvar_alterar_usuario.setFont(font)
        self.btn_salvar_alterar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar_alterar_usuario.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(44, 153, 255);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 85, 255);\n"
"\n"
"}")
        self.frame_2 = QFrame(self.tela_form_alterar_usuario)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 60, 751, 151))
        self.frame_2.setStyleSheet(u"background-color: rgb(242, 242, 242);\n"
"border: 1px solid #ccc;\n"
"border-radius: 2px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 20, 70, 20))
        self.label_9.setMinimumSize(QSize(70, 0))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"border: none;")
        self.input_alterar_nome_usuario = QLineEdit(self.frame_2)
        self.input_alterar_nome_usuario.setObjectName(u"input_alterar_nome_usuario")
        self.input_alterar_nome_usuario.setGeometry(QRect(80, 20, 431, 25))
        self.input_alterar_nome_usuario.setMinimumSize(QSize(0, 0))
        self.input_alterar_nome_usuario.setStyleSheet(u"font-size: 16px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 50, 70, 16))
        self.label_18.setMinimumSize(QSize(70, 0))
        self.label_18.setFont(font1)
        self.label_18.setStyleSheet(u"border: none;")
        self.input_alterar_login_usuario = QLineEdit(self.frame_2)
        self.input_alterar_login_usuario.setObjectName(u"input_alterar_login_usuario")
        self.input_alterar_login_usuario.setGeometry(QRect(80, 50, 431, 25))
        self.input_alterar_login_usuario.setStyleSheet(u"font-size: 16px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 80, 70, 20))
        self.label_19.setMinimumSize(QSize(70, 0))
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"border: none;")
        self.input_alterar_senha_usuario = QLineEdit(self.frame_2)
        self.input_alterar_senha_usuario.setObjectName(u"input_alterar_senha_usuario")
        self.input_alterar_senha_usuario.setGeometry(QRect(80, 80, 150, 25))
        self.input_alterar_senha_usuario.setMinimumSize(QSize(150, 0))
        self.input_alterar_senha_usuario.setStyleSheet(u"font-size: 16px;\n"
"background-color: rgb(255, 255, 255);")
        self.input_alterar_senha_usuario.setEchoMode(QLineEdit.Normal)
        self.label_20 = QLabel(self.frame_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(240, 80, 111, 20))
        self.label_20.setMinimumSize(QSize(70, 0))
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"border: none;")
        self.input_alterar_senha_2_usuario = QLineEdit(self.frame_2)
        self.input_alterar_senha_2_usuario.setObjectName(u"input_alterar_senha_2_usuario")
        self.input_alterar_senha_2_usuario.setGeometry(QRect(360, 80, 150, 25))
        self.input_alterar_senha_2_usuario.setMinimumSize(QSize(150, 0))
        self.input_alterar_senha_2_usuario.setStyleSheet(u"font-size: 16px;\n"
"background-color: rgb(255, 255, 255);")
        self.input_alterar_senha_2_usuario.setEchoMode(QLineEdit.Normal)
        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(20, 110, 101, 20))
        self.label_21.setMinimumSize(QSize(70, 0))
        self.label_21.setFont(font1)
        self.label_21.setStyleSheet(u"border: none;")
        self.cb_alterar_acesso_usuario = QComboBox(self.frame_2)
        self.cb_alterar_acesso_usuario.addItem("")
        self.cb_alterar_acesso_usuario.addItem("")
        self.cb_alterar_acesso_usuario.setObjectName(u"cb_alterar_acesso_usuario")
        self.cb_alterar_acesso_usuario.setGeometry(QRect(140, 110, 371, 25))
        sizePolicy.setHeightForWidth(self.cb_alterar_acesso_usuario.sizePolicy().hasHeightForWidth())
        self.cb_alterar_acesso_usuario.setSizePolicy(sizePolicy)
        self.cb_alterar_acesso_usuario.setFont(font2)
        self.cb_alterar_acesso_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 5px;")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(560, 20, 151, 110))
        self.label_4.setMinimumSize(QSize(110, 110))
        self.label_4.setStyleSheet(u"border: none;")
        self.btn_cancelar_alterar_usuario = QPushButton(self.tela_form_alterar_usuario)
        self.btn_cancelar_alterar_usuario.setObjectName(u"btn_cancelar_alterar_usuario")
        self.btn_cancelar_alterar_usuario.setGeometry(QRect(180, 230, 155, 35))
        self.btn_cancelar_alterar_usuario.setMinimumSize(QSize(155, 35))
        self.btn_cancelar_alterar_usuario.setMaximumSize(QSize(155, 16777215))
        self.btn_cancelar_alterar_usuario.setFont(font)
        self.btn_cancelar_alterar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cancelar_alterar_usuario.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	background-color: rgb(223, 0, 0);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(156, 0, 0);\n"
"\n"
"}")
        self.layoutWidget = QWidget(self.tela_form_alterar_usuario)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(12, 20, 270, 27))
        self.layout_titulo_form_alt = QHBoxLayout(self.layoutWidget)
        self.layout_titulo_form_alt.setObjectName(u"layout_titulo_form_alt")
        self.layout_titulo_form_alt.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.layout_titulo_form_alt.addWidget(self.label_3)

        self.input_alterar_id_usuario = QLineEdit(self.layoutWidget)
        self.input_alterar_id_usuario.setObjectName(u"input_alterar_id_usuario")
        self.input_alterar_id_usuario.setEnabled(False)
        self.input_alterar_id_usuario.setMinimumSize(QSize(80, 0))
        self.input_alterar_id_usuario.setMaximumSize(QSize(80, 16777215))
        self.input_alterar_id_usuario.setStyleSheet(u"font-size: 16px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.input_alterar_id_usuario.setDragEnabled(False)

        self.layout_titulo_form_alt.addWidget(self.input_alterar_id_usuario)

        self.Pages.addWidget(self.tela_form_alterar_usuario)
        self.tela_principal_usuarios = QWidget()
        self.tela_principal_usuarios.setObjectName(u"tela_principal_usuarios")
        self.frame_3 = QFrame(self.tela_principal_usuarios)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 10, 751, 411))
        self.frame_3.setStyleSheet(u"background-color: rgb(242, 242, 242);\n"
"border: 1px solid #ccc;\n"
"border-radius: 2px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.btn_form_cadastrar_usuario = QPushButton(self.frame_3)
        self.btn_form_cadastrar_usuario.setObjectName(u"btn_form_cadastrar_usuario")
        self.btn_form_cadastrar_usuario.setGeometry(QRect(20, 20, 155, 35))
        self.btn_form_cadastrar_usuario.setMinimumSize(QSize(155, 35))
        self.btn_form_cadastrar_usuario.setFont(font)
        self.btn_form_cadastrar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_form_cadastrar_usuario.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 170, 0);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(76, 191, 41);\n"
"	\n"
"}")
        self.input_pesquisar_usuario = QLineEdit(self.frame_3)
        self.input_pesquisar_usuario.setObjectName(u"input_pesquisar_usuario")
        self.input_pesquisar_usuario.setGeometry(QRect(319, 21, 241, 35))
        self.input_pesquisar_usuario.setMinimumSize(QSize(200, 35))
        font3 = QFont()
        font3.setPointSize(10)
        self.input_pesquisar_usuario.setFont(font3)
        self.input_pesquisar_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"border: 1px solid #999;")
        self.input_pesquisar_usuario.setAlignment(Qt.AlignCenter)
        self.btn_pesquisar_usuario = QPushButton(self.frame_3)
        self.btn_pesquisar_usuario.setObjectName(u"btn_pesquisar_usuario")
        self.btn_pesquisar_usuario.setGeometry(QRect(598, 21, 135, 35))
        self.btn_pesquisar_usuario.setMinimumSize(QSize(135, 35))
        self.btn_pesquisar_usuario.setFont(font)
        self.btn_pesquisar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pesquisar_usuario.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	background-color: rgb(130, 130, 130);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(88, 88, 88);\n"
"\n"
"}")
        self.btn_excluir_usuario = QPushButton(self.frame_3)
        self.btn_excluir_usuario.setObjectName(u"btn_excluir_usuario")
        self.btn_excluir_usuario.setGeometry(QRect(600, 120, 135, 35))
        self.btn_excluir_usuario.setMinimumSize(QSize(135, 35))
        self.btn_excluir_usuario.setFont(font)
        self.btn_excluir_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_usuario.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	background-color: rgb(223, 0, 0);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(156, 0, 0);\n"
"\n"
"}")
        self.btn_form_alterar_usuario = QPushButton(self.frame_3)
        self.btn_form_alterar_usuario.setObjectName(u"btn_form_alterar_usuario")
        self.btn_form_alterar_usuario.setGeometry(QRect(600, 80, 135, 35))
        self.btn_form_alterar_usuario.setMinimumSize(QSize(135, 35))
        self.btn_form_alterar_usuario.setFont(font)
        self.btn_form_alterar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_form_alterar_usuario.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(44, 153, 255);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 85, 255);\n"
"\n"
"}")
        self.tb_lista_usuarios = QTableWidget(self.frame_3)
        if (self.tb_lista_usuarios.columnCount() < 5):
            self.tb_lista_usuarios.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_lista_usuarios.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_lista_usuarios.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_lista_usuarios.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_lista_usuarios.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_lista_usuarios.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tb_lista_usuarios.setObjectName(u"tb_lista_usuarios")
        self.tb_lista_usuarios.setGeometry(QRect(20, 80, 571, 311))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tb_lista_usuarios.sizePolicy().hasHeightForWidth())
        self.tb_lista_usuarios.setSizePolicy(sizePolicy1)
        self.btn_gerar_excel_usuario = QPushButton(self.frame_3)
        self.btn_gerar_excel_usuario.setObjectName(u"btn_gerar_excel_usuario")
        self.btn_gerar_excel_usuario.setGeometry(QRect(600, 160, 135, 35))
        self.btn_gerar_excel_usuario.setMinimumSize(QSize(135, 35))
        self.btn_gerar_excel_usuario.setFont(font)
        self.btn_gerar_excel_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gerar_excel_usuario.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 130, 0);\n"
"	border-radius: 2px;\n"
"	font-size: 14px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 100, 0);\n"
"}")
        self.btn_limpa_pesquisar_usuario = QPushButton(self.frame_3)
        self.btn_limpa_pesquisar_usuario.setObjectName(u"btn_limpa_pesquisar_usuario")
        self.btn_limpa_pesquisar_usuario.setGeometry(QRect(557, 21, 35, 35))
        self.btn_limpa_pesquisar_usuario.setMinimumSize(QSize(35, 35))
        self.btn_limpa_pesquisar_usuario.setMaximumSize(QSize(35, 35))
        font4 = QFont()
        font4.setBold(True)
        font4.setWeight(75)
        self.btn_limpa_pesquisar_usuario.setFont(font4)
        self.btn_limpa_pesquisar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_limpa_pesquisar_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"border: 1px solid #999;")
        self.Pages.addWidget(self.tela_principal_usuarios)
        self.widget = QWidget(Tela_Usuarios)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(12, 12, 413, 52))
        self.lyout_titulo_usuarios = QHBoxLayout(self.widget)
        self.lyout_titulo_usuarios.setObjectName(u"lyout_titulo_usuarios")
        self.lyout_titulo_usuarios.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(50, 50))
        self.label_8.setMaximumSize(QSize(50, 50))

        self.lyout_titulo_usuarios.addWidget(self.label_8)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 8pt \"Open Sans\";")

        self.lyout_titulo_usuarios.addWidget(self.label_6)


        self.retranslateUi(Tela_Usuarios)

        self.Pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Tela_Usuarios)
    # setupUi

    def retranslateUi(self, Tela_Usuarios):
        Tela_Usuarios.setWindowTitle(QCoreApplication.translate("Tela_Usuarios", u"Usu\u00e1rios", None))
        self.btn_cancelar_cadastro_usuario.setText(QCoreApplication.translate("Tela_Usuarios", u"Cancelar", None))
        self.btn_salvar_cadastro_usuario.setText(QCoreApplication.translate("Tela_Usuarios", u"Salvar", None))
        self.label_7.setText(QCoreApplication.translate("Tela_Usuarios", u"<html><head/><body><p><span style=\" font-size:11pt;\">Nome</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("Tela_Usuarios", u"<html><head/><body><p><span style=\" font-size:11pt;\">Usu\u00e1rio</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("Tela_Usuarios", u"<html><head/><body><p><span style=\" font-size:11pt;\">Senha</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("Tela_Usuarios", u"<html><head/><body><p align=\"right\"><span style=\" font-size:11pt;\">Confirmar Senha</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("Tela_Usuarios", u"<html><head/><body><p align=\"right\"><span style=\" font-size:11pt;\">N\u00edvel de Acesso</span></p></body></html>", None))
        self.cb_cadastrar_acesso_usuario.setItemText(0, QCoreApplication.translate("Tela_Usuarios", u"Usu\u00e1rio", None))
        self.cb_cadastrar_acesso_usuario.setItemText(1, QCoreApplication.translate("Tela_Usuarios", u"Administrador", None))

        self.label.setText(QCoreApplication.translate("Tela_Usuarios", u"<html><head/><body><p align=\"center\"><img src=\"View/imagens/cadastrar-usuario.png\"></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Tela_Usuarios", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#737373;\">CADASTRAR USU\u00c1RIO</span></p></body></html>", None))
        self.btn_salvar_alterar_usuario.setText(QCoreApplication.translate("Tela_Usuarios", u"Salvar", None))
        self.label_9.setText(QCoreApplication.translate("Tela_Usuarios", u"<html><head/><body><p><span style=\" font-size:11pt;\">Nome</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("Tela_Usuarios", u"<html><head/><body><p><span style=\" font-size:11pt;\">Usu\u00e1rio</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("Tela_Usuarios", u"<html><head/><body><p><span style=\" font-size:11pt;\">Senha</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("Tela_Usuarios", u"<html><head/><body><p align=\"right\"><span style=\" font-size:11pt;\">Confirmar Senha</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("Tela_Usuarios", u"<html><head/><body><p align=\"right\"><span style=\" font-size:11pt;\">N\u00edvel de Acesso</span></p></body></html>", None))
        self.cb_alterar_acesso_usuario.setItemText(0, QCoreApplication.translate("Tela_Usuarios", u"Usu\u00e1rio", None))
        self.cb_alterar_acesso_usuario.setItemText(1, QCoreApplication.translate("Tela_Usuarios", u"Administrador", None))

        self.label_4.setText(QCoreApplication.translate("Tela_Usuarios", u"<html><head/><body><p align=\"center\"><img src=\"View/imagens/editar-usuario.png\"></p></body></html>", None))
        self.btn_cancelar_alterar_usuario.setText(QCoreApplication.translate("Tela_Usuarios", u"Cancelar", None))
        self.label_3.setText(QCoreApplication.translate("Tela_Usuarios", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#004264;\">ALTERAR USU\u00c1RIO - </span><span style=\" font-size:11pt; font-weight:600; color:#00689c;\">ID:</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.input_alterar_id_usuario.setToolTip(QCoreApplication.translate("Tela_Usuarios", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_form_cadastrar_usuario.setText(QCoreApplication.translate("Tela_Usuarios", u"+ Inserir Usu\u00e1rio", None))
        self.input_pesquisar_usuario.setPlaceholderText(QCoreApplication.translate("Tela_Usuarios", u"Pesquisar Usu\u00e1rio", None))
        self.btn_pesquisar_usuario.setText(QCoreApplication.translate("Tela_Usuarios", u"Pesquisar", None))
        self.btn_excluir_usuario.setText(QCoreApplication.translate("Tela_Usuarios", u"Excluir", None))
        self.btn_form_alterar_usuario.setText(QCoreApplication.translate("Tela_Usuarios", u"Alterar", None))
        ___qtablewidgetitem = self.tb_lista_usuarios.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Tela_Usuarios", u"ID", None));
        ___qtablewidgetitem1 = self.tb_lista_usuarios.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Tela_Usuarios", u"NOME", None));
        ___qtablewidgetitem2 = self.tb_lista_usuarios.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Tela_Usuarios", u"LOGIN", None));
        ___qtablewidgetitem3 = self.tb_lista_usuarios.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Tela_Usuarios", u"SENHA", None));
        ___qtablewidgetitem4 = self.tb_lista_usuarios.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Tela_Usuarios", u"N\u00cdVEL DE ACESSO", None));
        self.btn_gerar_excel_usuario.setText(QCoreApplication.translate("Tela_Usuarios", u"Gerar Excel", None))
#if QT_CONFIG(tooltip)
        self.btn_limpa_pesquisar_usuario.setToolTip(QCoreApplication.translate("Tela_Usuarios", u"<html><head/><body><p><span style=\" font-weight:400;\">Limpar filtro de pesquisa</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_limpa_pesquisar_usuario.setText(QCoreApplication.translate("Tela_Usuarios", u"x", None))
        self.label_8.setText(QCoreApplication.translate("Tela_Usuarios", u"<html><head/><body><p align=\"center\"><img src=\"View/imagens/usuarios-titulo.png\"></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Tela_Usuarios", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Usu\u00e1rios</span><span style=\" font-size:22pt; font-weight:600;\"/><span style=\" font-size:12pt;\">\u00a0\u00a0\u00a0\u00a0\u00a0Gerenciar usu\u00e1rios do sistema</span></p></body></html>", None))
    # retranslateUi

