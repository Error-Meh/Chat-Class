# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Principal_MaestroEJaPJy.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QToolBox, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QSize(1366, 768))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Frm_1Superior = QFrame(self.frame)
        self.Frm_1Superior.setObjectName(u"Frm_1Superior")
        self.Frm_1Superior.setMinimumSize(QSize(42, 42))
        self.Frm_1Superior.setMaximumSize(QSize(16777215, 40))
        self.Frm_1Superior.setStyleSheet(u"QFrame{\n"
"background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(217, 217, 217, 200), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(246, 246, 246, 229), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.Frm_1Superior.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frm_1Superior.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.Frm_1Superior)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.Lb_TituloChatClass = QLabel(self.Frm_1Superior)
        self.Lb_TituloChatClass.setObjectName(u"Lb_TituloChatClass")
        self.Lb_TituloChatClass.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 13pt \"Bahnschrift\";")

        self.horizontalLayout.addWidget(self.Lb_TituloChatClass)

        self.horizontalSpacer = QSpacerItem(1694, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Bt_Minizar = QPushButton(self.Frm_1Superior)
        self.Bt_Minizar.setObjectName(u"Bt_Minizar")
        self.Bt_Minizar.setMinimumSize(QSize(25, 25))
        self.Bt_Minizar.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"Imagenes/minimizar.png", QSize(), QIcon.Normal, QIcon.Off) # type: ignore
        self.Bt_Minizar.setIcon(icon)
        self.Bt_Minizar.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.Bt_Minizar)

        self.Bt_Maximizar = QPushButton(self.Frm_1Superior)
        self.Bt_Maximizar.setObjectName(u"Bt_Maximizar")
        self.Bt_Maximizar.setMinimumSize(QSize(25, 25))
        self.Bt_Maximizar.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"Imagenes/maximizar.png", QSize(), QIcon.Normal, QIcon.Off) # type: ignore
        self.Bt_Maximizar.setIcon(icon1)
        self.Bt_Maximizar.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.Bt_Maximizar)

        self.Bt_Cerrar = QPushButton(self.Frm_1Superior)
        self.Bt_Cerrar.setObjectName(u"Bt_Cerrar")
        self.Bt_Cerrar.setMinimumSize(QSize(25, 25))
        self.Bt_Cerrar.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"Imagenes/cerrar.png", QSize(), QIcon.Normal, QIcon.Off) # type: ignore
        self.Bt_Cerrar.setIcon(icon2)
        self.Bt_Cerrar.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.Bt_Cerrar)


        self.verticalLayout_2.addWidget(self.Frm_1Superior)

        self.Frm_2Inferior = QFrame(self.frame)
        self.Frm_2Inferior.setObjectName(u"Frm_2Inferior")
        self.Frm_2Inferior.setStyleSheet(u"background-color: rgba(30, 30, 30, 0);")
        self.Frm_2Inferior.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frm_2Inferior.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Frm_2Inferior)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Frm_FondoPrinc = QFrame(self.Frm_2Inferior)
        self.Frm_FondoPrinc.setObjectName(u"Frm_FondoPrinc")
        self.Frm_FondoPrinc.setMinimumSize(QSize(532, 0))
        self.Frm_FondoPrinc.setMaximumSize(QSize(748, 16777215))
        self.Frm_FondoPrinc.setStyleSheet(u"background-color: rgb(117, 117, 117);")
        self.Frm_FondoPrinc.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frm_FondoPrinc.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Frm_FondoPrinc)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.Frm_FondoPrinc)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(75, 75))
        self.widget.setMaximumSize(QSize(16777215, 75))
        self.widget.setStyleSheet(u"QWidget{\n"
"border: 1px solid black;\n"
"background-color: rgb(30, 30, 30);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background:none;\n"
"	background-color: rgba(0, 0, 0,0);\n"
"border: 0px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(217, 217, 217, 200), stop:1 rgba(255, 255, 255, 255));\n"
"	border-radius: 27px;\n"
"}\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.Bt_Perfil = QPushButton(self.widget)
        self.Bt_Perfil.setObjectName(u"Bt_Perfil")
        self.Bt_Perfil.setMinimumSize(QSize(55, 55))
        self.Bt_Perfil.setStyleSheet(u"QPushButton{\n"
"\n"
"background:none;\n"
"	background-color: rgba(0, 0, 0,0);\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(217, 217, 217, 200), stop:1 rgba(255, 255, 255, 255));\n"
"	border-radius: 27px;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"Imagenes/usuario.png", QSize(), QIcon.Normal, QIcon.Off) # type: ignore
        self.Bt_Perfil.setIcon(icon3)
        self.Bt_Perfil.setIconSize(QSize(45, 45))

        self.horizontalLayout_3.addWidget(self.Bt_Perfil)

        self.Bt_Regresar = QPushButton(self.widget)
        self.Bt_Regresar.setObjectName(u"Bt_Regresar")
        self.Bt_Regresar.setMinimumSize(QSize(55, 55))
        self.Bt_Regresar.setStyleSheet(u"QPushButton{\n"
"\n"
"background:none;\n"
"	background-color: rgba(0, 0, 0,0);\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(217, 217, 217, 200), stop:1 rgba(255, 255, 255, 255));\n"
"	border-radius: 27px;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"Imagenes/atras2.png", QSize(), QIcon.Normal, QIcon.Off) # type: ignore
        self.Bt_Regresar.setIcon(icon4)
        self.Bt_Regresar.setIconSize(QSize(45, 45))

        self.horizontalLayout_3.addWidget(self.Bt_Regresar)

        self.horizontalSpacer_2 = QSpacerItem(623, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.Bt_Ajustes = QPushButton(self.widget)
        self.Bt_Ajustes.setObjectName(u"Bt_Ajustes")
        self.Bt_Ajustes.setMinimumSize(QSize(55, 55))
        self.Bt_Ajustes.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"Imagenes/ajustes.png", QSize(), QIcon.Normal, QIcon.Off) # type: ignore
        self.Bt_Ajustes.setIcon(icon5)
        self.Bt_Ajustes.setIconSize(QSize(45, 45))

        self.horizontalLayout_3.addWidget(self.Bt_Ajustes)


        self.verticalLayout_3.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.Frm_FondoPrinc)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(532, 0))
        self.Pg_1Grupos = QWidget()
        self.Pg_1Grupos.setObjectName(u"Pg_1Grupos")
        self.Pg_1Grupos.setMinimumSize(QSize(532, 0))
        self.verticalLayout = QVBoxLayout(self.Pg_1Grupos)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Wid_BarraDeArriba = QWidget(self.Pg_1Grupos)
        self.Wid_BarraDeArriba.setObjectName(u"Wid_BarraDeArriba")
        self.Wid_BarraDeArriba.setMinimumSize(QSize(532, 50))
        self.Wid_BarraDeArriba.setMaximumSize(QSize(16777215, 50))
        self.Wid_BarraDeArriba.setStyleSheet(u"QWidget{\n"
"border: 1px solid black;\n"
"background-color: rgb(30, 30, 30);\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.Wid_BarraDeArriba)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 15, 0)
        self.horizontalSpacer_4 = QSpacerItem(87, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.Bt_IrGrupos = QPushButton(self.Wid_BarraDeArriba)
        self.Bt_IrGrupos.setObjectName(u"Bt_IrGrupos")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bt_IrGrupos.sizePolicy().hasHeightForWidth())
        self.Bt_IrGrupos.setSizePolicy(sizePolicy)
        self.Bt_IrGrupos.setMinimumSize(QSize(98, 30))
        self.Bt_IrGrupos.setMaximumSize(QSize(250, 30))
        self.Bt_IrGrupos.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255, 255, 255);\n"
"       Color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_4.addWidget(self.Bt_IrGrupos)

        self.Bt_IrChatPriv = QPushButton(self.Wid_BarraDeArriba)
        self.Bt_IrChatPriv.setObjectName(u"Bt_IrChatPriv")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Bt_IrChatPriv.sizePolicy().hasHeightForWidth())
        self.Bt_IrChatPriv.setSizePolicy(sizePolicy1)
        self.Bt_IrChatPriv.setMinimumSize(QSize(98, 30))
        self.Bt_IrChatPriv.setMaximumSize(QSize(250, 30))
        self.Bt_IrChatPriv.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 0.5px solid rgb(255, 255, 255);\n"
"	background-color: rgb(58, 58, 58);\n"
"	\n"
"}")

        self.horizontalLayout_4.addWidget(self.Bt_IrChatPriv)

        self.horizontalSpacer_3 = QSpacerItem(98, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.Bt_BuscarGrupo = QPushButton(self.Wid_BarraDeArriba)
        self.Bt_BuscarGrupo.setObjectName(u"Bt_BuscarGrupo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Bt_BuscarGrupo.sizePolicy().hasHeightForWidth())
        self.Bt_BuscarGrupo.setSizePolicy(sizePolicy2)
        self.Bt_BuscarGrupo.setMinimumSize(QSize(45, 45))
        self.Bt_BuscarGrupo.setMaximumSize(QSize(45, 45))
        self.Bt_BuscarGrupo.setStyleSheet(u"QPushButton{\n"
"	background:none;\n"
"	background-color: rgba(0, 0, 0,0);\n"
"	border:none;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(217, 217, 217, 200), stop:1 rgba(255, 255, 255, 255));\n"
"	\n"
"border-radius:22px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"Imagenes/buscar.png", QSize(), QIcon.Normal, QIcon.Off) # type: ignore
        self.Bt_BuscarGrupo.setIcon(icon6)
        self.Bt_BuscarGrupo.setIconSize(QSize(35, 35))

        self.horizontalLayout_4.addWidget(self.Bt_BuscarGrupo)

        self.Bt_RecargarGrupos = QPushButton(self.Wid_BarraDeArriba)
        self.Bt_RecargarGrupos.setObjectName(u"Bt_RecargarGrupos")
        self.Bt_RecargarGrupos.setMinimumSize(QSize(45, 45))
        self.Bt_RecargarGrupos.setStyleSheet(u"QPushButton{\n"
"	background:none;\n"
"	background-color: rgba(0, 0, 0,0);\n"
"	borde: 1px solid black;\n"
"border-radius:22px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(217, 217, 217, 200), stop:1 rgba(255, 255, 255, 255));\n"
"	\n"
"border-radius:22px;\n"
"border: none;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"Imagenes/recargar.png", QSize(), QIcon.Normal, QIcon.Off) # type: ignore
        self.Bt_RecargarGrupos.setIcon(icon7)
        self.Bt_RecargarGrupos.setIconSize(QSize(35, 35))

        self.horizontalLayout_4.addWidget(self.Bt_RecargarGrupos)

        self.Bt_MasOpciones = QPushButton(self.Wid_BarraDeArriba)
        self.Bt_MasOpciones.setObjectName(u"Bt_MasOpciones")
        sizePolicy2.setHeightForWidth(self.Bt_MasOpciones.sizePolicy().hasHeightForWidth())
        self.Bt_MasOpciones.setSizePolicy(sizePolicy2)
        self.Bt_MasOpciones.setMinimumSize(QSize(45, 45))
        self.Bt_MasOpciones.setMaximumSize(QSize(45, 45))
        self.Bt_MasOpciones.setStyleSheet(u"QPushButton{\n"
"	background:none;\n"
"	background-color: rgba(0, 0, 0,0);\n"
"	background-color: rgb(158, 158, 158);\n"
"	border-radius:22px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(217, 217, 217, 200), stop:1 rgba(255, 255, 255, 255));\n"
"	\n"
"border-radius:22px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"Imagenes/opciones.png", QSize(), QIcon.Normal, QIcon.Off) # type: ignore
        self.Bt_MasOpciones.setIcon(icon8)
        self.Bt_MasOpciones.setIconSize(QSize(35, 35))

        self.horizontalLayout_4.addWidget(self.Bt_MasOpciones)


        self.verticalLayout.addWidget(self.Wid_BarraDeArriba)

        self.Wid_btns_grupos = QWidget(self.Pg_1Grupos)
        self.Wid_btns_grupos.setObjectName(u"Wid_btns_grupos")
        self.scrollArea = QScrollArea(self.Wid_btns_grupos)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 751, 911))
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 749, 909))
        self.Frm_Grupos = QFrame(self.scrollAreaWidgetContents)
        self.Frm_Grupos.setObjectName(u"Frm_Grupos")
        self.Frm_Grupos.setGeometry(QRect(0, 0, 751, 905))
        self.Frm_Grupos.setMinimumSize(QSize(532, 111))
        self.Frm_Grupos.setMaximumSize(QSize(751, 905))
        self.Frm_Grupos.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frm_Grupos.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.Frm_Grupos)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.Frm_Grupos)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(False)

        self.gridLayout_5.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.Frm_Grupos)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(False)

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.Wid_btns_grupos)

        self.stackedWidget.addWidget(self.Pg_1Grupos)
        self.Pg_2Ajustes = QWidget()
        self.Pg_2Ajustes.setObjectName(u"Pg_2Ajustes")
        self.verticalLayout_6 = QVBoxLayout(self.Pg_2Ajustes)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.Pg_2Ajustes)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(532, 50))
        self.widget_3.setStyleSheet(u"QWidget{\n"
"border: 1px solid black;\n"
"background-color: rgb(30, 30, 30);\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 15pt \"Bahnschrift\";\n"
"border: none;")

        self.verticalLayout_4.addWidget(self.label)


        self.verticalLayout_6.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.Pg_2Ajustes)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.widget_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(532, 0))
        self.toolBox.setStyleSheet(u"QToolBox {\n"
"    border: none;\n"
"    color: white;\n"
"	margin: 30px 30px;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    padding: 35px 10px; /* Espaciado interno */\n"
"    border: none;\n"
"    border-bottom: 2px solid black;\n"
"    text-align: left;\n"
"    margin-top: 1px; /* Espacio entre tabs */\n"
"}\n"
"\n"
"QToolBox::tab:selected {\n"
"    font-weight: bold;\n"
"    background-color: #808080;\n"
"}\n"
"\n"
"QToolBox::tab:hover {\n"
"    background-color: #8a8a8a;\n"
"}\n"
"")
        self.Pg_InfDeApp = QWidget()
        self.Pg_InfDeApp.setObjectName(u"Pg_InfDeApp")
        self.Pg_InfDeApp.setGeometry(QRect(0, 0, 686, 757))
        self.gridLayout_2 = QGridLayout(self.Pg_InfDeApp)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_11, 0, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 88, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 6, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)

        self.Lb_Version = QLabel(self.Pg_InfDeApp)
        self.Lb_Version.setObjectName(u"Lb_Version")
        self.Lb_Version.setStyleSheet(u"border: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 20pt \"Bahnschrift\";")

        self.gridLayout_2.addWidget(self.Lb_Version, 5, 1, 1, 1)

        self.Ic_ChatClass = QLabel(self.Pg_InfDeApp)
        self.Ic_ChatClass.setObjectName(u"Ic_ChatClass")
        sizePolicy2.setHeightForWidth(self.Ic_ChatClass.sizePolicy().hasHeightForWidth())
        self.Ic_ChatClass.setSizePolicy(sizePolicy2)
        self.Ic_ChatClass.setMinimumSize(QSize(250, 150))
        self.Ic_ChatClass.setMaximumSize(QSize(450, 350))
        self.Ic_ChatClass.setStyleSheet(u"background-color: transparent;\n"
"")
        self.Ic_ChatClass.setTextFormat(Qt.TextFormat.PlainText)
        self.Ic_ChatClass.setPixmap(QPixmap(u"Imagenes/1742945765469.png"))
        self.Ic_ChatClass.setScaledContents(True)

        self.gridLayout_2.addWidget(self.Ic_ChatClass, 1, 1, 1, 1)

        self.Lb_ChatClass = QLabel(self.Pg_InfDeApp)
        self.Lb_ChatClass.setObjectName(u"Lb_ChatClass")
        self.Lb_ChatClass.setStyleSheet(u"border: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 20pt \"Bahnschrift\";")

        self.gridLayout_2.addWidget(self.Lb_ChatClass, 4, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 3, 1, 1, 1)

        self.toolBox.addItem(self.Pg_InfDeApp, u"Informacion de la App")
        self.Pg_Seguridad = QWidget()
        self.Pg_Seguridad.setObjectName(u"Pg_Seguridad")
        self.Pg_Seguridad.setGeometry(QRect(0, 0, 686, 757))
        self.Pg_Seguridad.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.Pg_Seguridad)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Bt_VerCont_2 = QPushButton(self.Pg_Seguridad)
        self.Bt_VerCont_2.setObjectName(u"Bt_VerCont_2")
        self.Bt_VerCont_2.setMinimumSize(QSize(40, 40))
        self.Bt_VerCont_2.setStyleSheet(u"border: 0.5px solid black;")

        self.gridLayout.addWidget(self.Bt_VerCont_2, 8, 6, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 85, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 13, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(109, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 8, 5, 1, 1)

        self.Lb_ContActual = QLabel(self.Pg_Seguridad)
        self.Lb_ContActual.setObjectName(u"Lb_ContActual")
        self.Lb_ContActual.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.Lb_ContActual.setFont(font)
        self.Lb_ContActual.setStyleSheet(u"background: none;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 16pt \"Bahnschrift\";")

        self.gridLayout.addWidget(self.Lb_ContActual, 2, 1, 1, 3)

        self.Tf_ContActual = QLineEdit(self.Pg_Seguridad)
        self.Tf_ContActual.setObjectName(u"Tf_ContActual")
        self.Tf_ContActual.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.Tf_ContActual.setFont(font1)
        self.Tf_ContActual.setStyleSheet(u"background: none;\n"
"background-color: rgb(158, 158, 158);\n"
"border:1px solid black;\n"
"color: rgb(106, 13, 173);\n"
"padding-left:10px;\n"
"padding-bottom:0px;")
        self.Tf_ContActual.setMaxLength(32767)
        self.Tf_ContActual.setEchoMode(QLineEdit.EchoMode.Password)
        self.Tf_ContActual.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.gridLayout.addWidget(self.Tf_ContActual, 3, 1, 1, 4)

        self.horizontalSpacer_16 = QSpacerItem(113, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_16, 8, 0, 1, 1)

        self.Tf_ConfirmCont = QLineEdit(self.Pg_Seguridad)
        self.Tf_ConfirmCont.setObjectName(u"Tf_ConfirmCont")
        self.Tf_ConfirmCont.setMinimumSize(QSize(0, 30))
        self.Tf_ConfirmCont.setFont(font1)
        self.Tf_ConfirmCont.setStyleSheet(u"background: none;\n"
"background-color: rgb(158, 158, 158);\n"
"border:1px solid black;\n"
"color: rgb(106, 13, 173);\n"
"padding-left:10px;\n"
"padding-bottom:0px;")
        self.Tf_ConfirmCont.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.Tf_ConfirmCont, 10, 1, 2, 4)

        self.verticalSpacer_5 = QSpacerItem(20, 118, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 16, 2, 1, 1)

        self.Bt_VerCont = QPushButton(self.Pg_Seguridad)
        self.Bt_VerCont.setObjectName(u"Bt_VerCont")
        self.Bt_VerCont.setMinimumSize(QSize(40, 40))
        self.Bt_VerCont.setStyleSheet(u"border: 0.5px solid black;")

        self.gridLayout.addWidget(self.Bt_VerCont, 3, 6, 1, 1)

        self.Tf_NuevCont = QLineEdit(self.Pg_Seguridad)
        self.Tf_NuevCont.setObjectName(u"Tf_NuevCont")
        self.Tf_NuevCont.setMinimumSize(QSize(0, 30))
        self.Tf_NuevCont.setFont(font1)
        self.Tf_NuevCont.setStyleSheet(u"background: none;\n"
"background-color: rgb(158, 158, 158);\n"
"border:1px solid black;\n"
"color: rgb(106, 13, 173);\n"
"padding-left:10px;\n"
"padding-bottom:0px;")
        self.Tf_NuevCont.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.Tf_NuevCont, 8, 1, 1, 4)

        self.horizontalSpacer_11 = QSpacerItem(109, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_11, 8, 7, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_10, 0, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 85, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 6, 2, 1, 1)

        self.Lb_ErrorContActu = QLabel(self.Pg_Seguridad)
        self.Lb_ErrorContActu.setObjectName(u"Lb_ErrorContActu")
        self.Lb_ErrorContActu.setMinimumSize(QSize(0, 20))
        font2 = QFont()
        font2.setFamilies([u"Terminal"])
        font2.setPointSize(20)
        self.Lb_ErrorContActu.setFont(font2)
        self.Lb_ErrorContActu.setStyleSheet(u"color: rgb(255, 170, 171);\n"
"background:none;")

        self.gridLayout.addWidget(self.Lb_ErrorContActu, 4, 1, 1, 6)

        self.Lb_ErrorConfirmCont = QLabel(self.Pg_Seguridad)
        self.Lb_ErrorConfirmCont.setObjectName(u"Lb_ErrorConfirmCont")
        self.Lb_ErrorConfirmCont.setMinimumSize(QSize(0, 20))
        self.Lb_ErrorConfirmCont.setFont(font2)
        self.Lb_ErrorConfirmCont.setStyleSheet(u"color: rgb(255, 170, 171);\n"
"background:none;")

        self.gridLayout.addWidget(self.Lb_ErrorConfirmCont, 12, 1, 1, 5)

        self.Bt_VerCont_3 = QPushButton(self.Pg_Seguridad)
        self.Bt_VerCont_3.setObjectName(u"Bt_VerCont_3")
        self.Bt_VerCont_3.setMinimumSize(QSize(40, 40))
        self.Bt_VerCont_3.setStyleSheet(u"border: 0.5px solid black;")

        self.gridLayout.addWidget(self.Bt_VerCont_3, 10, 6, 2, 1)

        self.Lb_NuevCont = QLabel(self.Pg_Seguridad)
        self.Lb_NuevCont.setObjectName(u"Lb_NuevCont")
        self.Lb_NuevCont.setMinimumSize(QSize(0, 30))
        self.Lb_NuevCont.setStyleSheet(u"background: none;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 16pt \"Bahnschrift\";")

        self.gridLayout.addWidget(self.Lb_NuevCont, 7, 1, 1, 3)

        self.Lb_ConfirmCont = QLabel(self.Pg_Seguridad)
        self.Lb_ConfirmCont.setObjectName(u"Lb_ConfirmCont")
        self.Lb_ConfirmCont.setMinimumSize(QSize(0, 30))
        self.Lb_ConfirmCont.setStyleSheet(u"background: none;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 15pt \"Bahnschrift\";")

        self.gridLayout.addWidget(self.Lb_ConfirmCont, 9, 1, 1, 4)

        self.Bt_Confirm = QPushButton(self.Pg_Seguridad)
        self.Bt_Confirm.setObjectName(u"Bt_Confirm")
        self.Bt_Confirm.setMinimumSize(QSize(50, 35))
        self.Bt_Confirm.setStyleSheet(u"QPushButton{\n"
"background: none;\n"
"background-color: rgb(158, 158, 158);\n"
"color: rgb(12, 12, 12);\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(194, 194, 194);\n"
"    border-color: #5a5a5a; /* Opcional: cambia el borde para m\u00e1s contraste */\n"
"}")

        self.gridLayout.addWidget(self.Bt_Confirm, 15, 1, 1, 4)

        self.toolBox.addItem(self.Pg_Seguridad, u"Seguridad")
        self.Pg_Ayuda = QWidget()
        self.Pg_Ayuda.setObjectName(u"Pg_Ayuda")
        self.Pg_Ayuda.setGeometry(QRect(0, 0, 686, 757))
        self.Pg_Ayuda.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.Pg_Ayuda)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_8 = QSpacerItem(20, 110, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_8)

        self.Bt_Soporte = QPushButton(self.Pg_Ayuda)
        self.Bt_Soporte.setObjectName(u"Bt_Soporte")
        self.Bt_Soporte.setStyleSheet(u"QPushButton{\n"
"background: none;\n"
"background-color: rgb(158, 158, 158);\n"
"color: rgb(12, 12, 12);\n"
"border-radius: 15px;\n"
"	font: 300 26pt \"Bahnschrift\";\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(194, 194, 194);\n"
"    border-color: #5a5a5a; /* Opcional: cambia el borde para m\u00e1s contraste */\n"
"}")

        self.verticalLayout_7.addWidget(self.Bt_Soporte)

        self.verticalSpacer_2 = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.Bt_CondPolit = QPushButton(self.Pg_Ayuda)
        self.Bt_CondPolit.setObjectName(u"Bt_CondPolit")
        self.Bt_CondPolit.setStyleSheet(u"QPushButton{\n"
"background: none;\n"
"background-color: rgb(158, 158, 158);\n"
"color: rgb(12, 12, 12);\n"
"border-radius: 15px;\n"
"	font: 300 26pt \"Bahnschrift\";\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(194, 194, 194);\n"
"    border-color: #5a5a5a; /* Opcional: cambia el borde para m\u00e1s contraste */\n"
"}")

        self.verticalLayout_7.addWidget(self.Bt_CondPolit)

        self.verticalSpacer = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.Bt_PregFrec = QPushButton(self.Pg_Ayuda)
        self.Bt_PregFrec.setObjectName(u"Bt_PregFrec")
        self.Bt_PregFrec.setStyleSheet(u"QPushButton{\n"
"background: none;\n"
"background-color: rgb(158, 158, 158);\n"
"color: rgb(12, 12, 12);\n"
"border-radius: 15px;\n"
"	font: 300 26pt \"Bahnschrift\";\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(194, 194, 194);\n"
"    border-color: #5a5a5a; /* Opcional: cambia el borde para m\u00e1s contraste */\n"
"}")

        self.verticalLayout_7.addWidget(self.Bt_PregFrec)

        self.verticalSpacer_9 = QSpacerItem(20, 161, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)

        self.toolBox.addItem(self.Pg_Ayuda, u"Ayuda")

        self.horizontalLayout_6.addWidget(self.toolBox)


        self.verticalLayout_6.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.Pg_2Ajustes)
        self.Pg_3MenPriv = QWidget()
        self.Pg_3MenPriv.setObjectName(u"Pg_3MenPriv")
        self.verticalLayout_5 = QVBoxLayout(self.Pg_3MenPriv)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Wid_BarraDeArriba_2 = QWidget(self.Pg_3MenPriv)
        self.Wid_BarraDeArriba_2.setObjectName(u"Wid_BarraDeArriba_2")
        self.Wid_BarraDeArriba_2.setMinimumSize(QSize(532, 50))
        self.Wid_BarraDeArriba_2.setMaximumSize(QSize(16777215, 50))
        self.Wid_BarraDeArriba_2.setStyleSheet(u"QWidget{\n"
"border: 1px solid black;\n"
"background-color: rgb(30, 30, 30);\n"
"}")
        self.gridLayout_4 = QGridLayout(self.Wid_BarraDeArriba_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 15, 0)
        self.horizontalSpacer_7 = QSpacerItem(87, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_7, 0, 0, 1, 1)

        self.Bt_IrGrupos_2 = QPushButton(self.Wid_BarraDeArriba_2)
        self.Bt_IrGrupos_2.setObjectName(u"Bt_IrGrupos_2")
        sizePolicy.setHeightForWidth(self.Bt_IrGrupos_2.sizePolicy().hasHeightForWidth())
        self.Bt_IrGrupos_2.setSizePolicy(sizePolicy)
        self.Bt_IrGrupos_2.setMinimumSize(QSize(98, 30))
        self.Bt_IrGrupos_2.setMaximumSize(QSize(250, 30))
        self.Bt_IrGrupos_2.setStyleSheet(u"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 0.5px solid rgb(255, 255, 255);\n"
"	background-color: rgb(58, 58, 58);\n"
"	\n"
"}")

        self.gridLayout_4.addWidget(self.Bt_IrGrupos_2, 0, 1, 1, 1)

        self.Bt_IrChatPriv_2 = QPushButton(self.Wid_BarraDeArriba_2)
        self.Bt_IrChatPriv_2.setObjectName(u"Bt_IrChatPriv_2")
        sizePolicy1.setHeightForWidth(self.Bt_IrChatPriv_2.sizePolicy().hasHeightForWidth())
        self.Bt_IrChatPriv_2.setSizePolicy(sizePolicy1)
        self.Bt_IrChatPriv_2.setMinimumSize(QSize(98, 30))
        self.Bt_IrChatPriv_2.setMaximumSize(QSize(250, 30))
        self.Bt_IrChatPriv_2.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255, 255, 255);\n"
"       Color: rgb(0, 0, 0)\n"
"}")

        self.gridLayout_4.addWidget(self.Bt_IrChatPriv_2, 0, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(98, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_8, 0, 3, 1, 1)

        self.Bt_BuscarChats = QPushButton(self.Wid_BarraDeArriba_2)
        self.Bt_BuscarChats.setObjectName(u"Bt_BuscarChats")
        sizePolicy2.setHeightForWidth(self.Bt_BuscarChats.sizePolicy().hasHeightForWidth())
        self.Bt_BuscarChats.setSizePolicy(sizePolicy2)
        self.Bt_BuscarChats.setMinimumSize(QSize(45, 45))
        self.Bt_BuscarChats.setMaximumSize(QSize(45, 45))
        self.Bt_BuscarChats.setStyleSheet(u"QPushButton{\n"
"	background:none;\n"
"	background-color: rgba(0, 0, 0,0);\n"
"	border:none;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(217, 217, 217, 200), stop:1 rgba(255, 255, 255, 255));\n"
"	\n"
"border-radius:22px;\n"
"}")
        self.Bt_BuscarChats.setIcon(icon6)
        self.Bt_BuscarChats.setIconSize(QSize(35, 35))

        self.gridLayout_4.addWidget(self.Bt_BuscarChats, 0, 4, 1, 1)

        self.Bt_CargarChats = QPushButton(self.Wid_BarraDeArriba_2)
        self.Bt_CargarChats.setObjectName(u"Bt_CargarChats")
        self.Bt_CargarChats.setMinimumSize(QSize(45, 45))
        self.Bt_CargarChats.setStyleSheet(u"QPushButton{\n"
"	background:none;\n"
"	background-color: rgba(0, 0, 0,0);\n"
"	borde: 1px solid black;\n"
"border-radius:22px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(217, 217, 217, 200), stop:1 rgba(255, 255, 255, 255));\n"
"	\n"
"border-radius:22px;\n"
"border: none;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"Imagenes/recargar.png", QSize(), QIcon.Normal, QIcon.Off) # type: ignore
        self.Bt_CargarChats.setIcon(icon9)
        self.Bt_CargarChats.setIconSize(QSize(35, 35))

        self.gridLayout_4.addWidget(self.Bt_CargarChats, 0, 5, 1, 1)


        self.verticalLayout_5.addWidget(self.Wid_BarraDeArriba_2)

        self.Wid_btns_grupos_2 = QWidget(self.Pg_3MenPriv)
        self.Wid_btns_grupos_2.setObjectName(u"Wid_btns_grupos_2")
        self.scrollArea_2 = QScrollArea(self.Wid_btns_grupos_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(0, 0, 751, 911))
        self.scrollArea_2.setLineWidth(1)
        self.scrollArea_2.setMidLineWidth(0)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 749, 909))
        self.Frm_MenPriv = QFrame(self.scrollAreaWidgetContents_2)
        self.Frm_MenPriv.setObjectName(u"Frm_MenPriv")
        self.Frm_MenPriv.setGeometry(QRect(0, 0, 751, 911))
        self.Frm_MenPriv.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frm_MenPriv.setFrameShadow(QFrame.Shadow.Raised)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_5.addWidget(self.Wid_btns_grupos_2)

        self.stackedWidget.addWidget(self.Pg_3MenPriv)
        self.Pg_4Perfil = QWidget()
        self.Pg_4Perfil.setObjectName(u"Pg_4Perfil")
        self.Pg_4Perfil.setMinimumSize(QSize(532, 0))
        self.gridLayout_3 = QGridLayout(self.Pg_4Perfil)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.Pg_4Perfil)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(532, 0))
        self.gridLayout_7 = QGridLayout(self.widget_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.Lb_Correo = QLabel(self.widget_4)
        self.Lb_Correo.setObjectName(u"Lb_Correo")
        self.Lb_Correo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Bahnschrift\";\n"
"border: 0px;")

        self.gridLayout_7.addWidget(self.Lb_Correo, 9, 2, 1, 1)

        self.Lb_Codigo = QLabel(self.widget_4)
        self.Lb_Codigo.setObjectName(u"Lb_Codigo")
        self.Lb_Codigo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Bahnschrift\";")

        self.gridLayout_7.addWidget(self.Lb_Codigo, 3, 2, 1, 1)

        self.Lb_Apellido = QLabel(self.widget_4)
        self.Lb_Apellido.setObjectName(u"Lb_Apellido")
        self.Lb_Apellido.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Bahnschrift\";\n"
"border: 0px;")

        self.gridLayout_7.addWidget(self.Lb_Apellido, 7, 2, 1, 1)

        self.Lb_Rol_Puesto = QLabel(self.widget_4)
        self.Lb_Rol_Puesto.setObjectName(u"Lb_Rol_Puesto")
        self.Lb_Rol_Puesto.setMinimumSize(QSize(150, 28))
        self.Lb_Rol_Puesto.setMaximumSize(QSize(160, 35))
        self.Lb_Rol_Puesto.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 23pt \"Bahnschrift\";\n"
"border: 2px solid black;")
        self.Lb_Rol_Puesto.setTextFormat(Qt.TextFormat.PlainText)

        self.gridLayout_7.addWidget(self.Lb_Rol_Puesto, 1, 3, 1, 2)

        self.verticalSpacer_15 = QSpacerItem(20, 108, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_15, 6, 3, 1, 1)

        self.Lb_Apellido_Puesto = QLabel(self.widget_4)
        self.Lb_Apellido_Puesto.setObjectName(u"Lb_Apellido_Puesto")
        self.Lb_Apellido_Puesto.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 23pt \"Bahnschrift\";\n"
"border: 2px solid black;")

        self.gridLayout_7.addWidget(self.Lb_Apellido_Puesto, 7, 3, 1, 2)

        self.Lb_Nomb = QLabel(self.widget_4)
        self.Lb_Nomb.setObjectName(u"Lb_Nomb")
        self.Lb_Nomb.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Bahnschrift\";")

        self.gridLayout_7.addWidget(self.Lb_Nomb, 5, 2, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 108, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_16, 8, 3, 1, 2)

        self.verticalSpacer_17 = QSpacerItem(20, 108, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_17, 11, 4, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 107, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_14, 4, 3, 1, 2)

        self.Lb_Rol = QLabel(self.widget_4)
        self.Lb_Rol.setObjectName(u"Lb_Rol")
        self.Lb_Rol.setMinimumSize(QSize(70, 0))
        self.Lb_Rol.setMaximumSize(QSize(70, 16777215))
        self.Lb_Rol.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 25pt \"Bahnschrift\";")

        self.gridLayout_7.addWidget(self.Lb_Rol, 1, 2, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(130, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_22, 10, 6, 1, 1)

        self.Lb_Codigo_Puesto = QLabel(self.widget_4)
        self.Lb_Codigo_Puesto.setObjectName(u"Lb_Codigo_Puesto")
        self.Lb_Codigo_Puesto.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 23pt \"Bahnschrift\";\n"
"border: 2px solid black;")

        self.gridLayout_7.addWidget(self.Lb_Codigo_Puesto, 3, 3, 1, 2)

        self.verticalSpacer_13 = QSpacerItem(20, 108, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_13, 2, 3, 1, 1)

        self.Lb_Nomb_Puesto = QLabel(self.widget_4)
        self.Lb_Nomb_Puesto.setObjectName(u"Lb_Nomb_Puesto")
        self.Lb_Nomb_Puesto.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 23pt \"Bahnschrift\";\n"
"border: 2px solid black;")

        self.gridLayout_7.addWidget(self.Lb_Nomb_Puesto, 5, 3, 1, 2)

        self.Lb_Correo_Puesto = QLabel(self.widget_4)
        self.Lb_Correo_Puesto.setObjectName(u"Lb_Correo_Puesto")
        self.Lb_Correo_Puesto.setMinimumSize(QSize(450, 0))
        self.Lb_Correo_Puesto.setMaximumSize(QSize(680, 16777215))
        self.Lb_Correo_Puesto.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 23pt \"Bahnschrift\";\n"
"border: 2px solid black;")

        self.gridLayout_7.addWidget(self.Lb_Correo_Puesto, 10, 1, 1, 5)

        self.verticalSpacer_12 = QSpacerItem(20, 108, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_12, 0, 3, 1, 2)

        self.horizontalSpacer_17 = QSpacerItem(130, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_17, 10, 0, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(152, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_18, 1, 5, 1, 1)


        self.gridLayout_3.addWidget(self.widget_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Pg_4Perfil)
        self.Pg_5Canales = QWidget()
        self.Pg_5Canales.setObjectName(u"Pg_5Canales")
        self.gridLayout_12 = QGridLayout(self.Pg_5Canales)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.line_2 = QFrame(self.Pg_5Canales)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_12.addWidget(self.line_2, 3, 1, 1, 1)

        self.verticalSpacer_22 = QSpacerItem(20, 203, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_22, 10, 1, 1, 1)

        self.Bt_ChatAvisos = QPushButton(self.Pg_5Canales)
        self.Bt_ChatAvisos.setObjectName(u"Bt_ChatAvisos")
        self.Bt_ChatAvisos.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(0, 0, 0, 0%);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 26pt \"Bahnschrift\";\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(108, 108, 108);\n"
"}\n"
"")

        self.gridLayout_12.addWidget(self.Bt_ChatAvisos, 1, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_13, 5, 2, 1, 1)

        self.verticalSpacer_21 = QSpacerItem(20, 203, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_21, 0, 1, 1, 1)

        self.line = QFrame(self.Pg_5Canales)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_12.addWidget(self.line, 7, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_14, 5, 0, 1, 1)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_24, 4, 1, 1, 1)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_23, 2, 1, 1, 1)

        self.Bt_ChatFueraDelTema = QPushButton(self.Pg_5Canales)
        self.Bt_ChatFueraDelTema.setObjectName(u"Bt_ChatFueraDelTema")
        self.Bt_ChatFueraDelTema.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(0, 0, 0, 0%);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 26pt \"Bahnschrift\";\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(108, 108, 108);\n"
"}\n"
"")

        self.gridLayout_12.addWidget(self.Bt_ChatFueraDelTema, 9, 1, 1, 1)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_25, 6, 1, 1, 1)

        self.Bt_ChatGeneral = QPushButton(self.Pg_5Canales)
        self.Bt_ChatGeneral.setObjectName(u"Bt_ChatGeneral")
        self.Bt_ChatGeneral.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(0, 0, 0, 0%);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 700 26pt \"Bahnschrift\";\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(108, 108, 108);\n"
"}\n"
"")

        self.gridLayout_12.addWidget(self.Bt_ChatGeneral, 5, 1, 1, 1)

        self.widget_6 = QWidget(self.Pg_5Canales)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"QWidget{\n"
"background-color: rgb(30, 30, 30);\n"
"}\n"
"\n"
"QWidget:hover{\n"
"	background-color: rgb(117, 117, 117);\n"
"	transition: margin-right 2s 0.5s;\n"
"}")
        self.gridLayout_13 = QGridLayout(self.widget_6)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(50, 0, 0, 0)
        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background: none;\n"
"font: 700 22pt \"Bahnschrift\";\n"
"color:rgb(30, 30, 30);")

        self.gridLayout_13.addWidget(self.label_4, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.widget_6, 11, 0, 1, 3)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_26, 8, 1, 1, 1)

        self.gridLayout_12.setRowStretch(0, 20)
        self.gridLayout_12.setRowStretch(1, 5)
        self.gridLayout_12.setRowStretch(2, 5)
        self.gridLayout_12.setRowStretch(3, 5)
        self.gridLayout_12.setRowStretch(4, 5)
        self.gridLayout_12.setRowStretch(5, 5)
        self.gridLayout_12.setRowStretch(6, 5)
        self.gridLayout_12.setRowStretch(7, 5)
        self.gridLayout_12.setRowStretch(8, 5)
        self.gridLayout_12.setRowStretch(9, 20)
        self.gridLayout_12.setRowStretch(10, 20)
        self.gridLayout_12.setRowStretch(11, 20)
        self.gridLayout_12.setColumnStretch(0, 2)
        self.gridLayout_12.setColumnStretch(1, 35)
        self.gridLayout_12.setColumnStretch(2, 2)
        self.stackedWidget.addWidget(self.Pg_5Canales)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.Frm_FondoPrinc)

        self.Frm_FondoMnsj = QFrame(self.Frm_2Inferior)
        self.Frm_FondoMnsj.setObjectName(u"Frm_FondoMnsj")
        self.Frm_FondoMnsj.setMinimumSize(QSize(833, 0))
        self.Frm_FondoMnsj.setStyleSheet(u"background-image: url(\"Imagenes/Diseño sin título.jpg\");")
        self.Frm_FondoMnsj.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frm_FondoMnsj.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Frm_FondoMnsj)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.Frm_FondoMnsj)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        sizePolicy2.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy2)
        self.stackedWidget_2.setMinimumSize(QSize(0, 0))
        self.stackedWidget_2.setStyleSheet(u"")
        self.Pg_1FondoPrinc = QWidget()
        self.Pg_1FondoPrinc.setObjectName(u"Pg_1FondoPrinc")
        sizePolicy2.setHeightForWidth(self.Pg_1FondoPrinc.sizePolicy().hasHeightForWidth())
        self.Pg_1FondoPrinc.setSizePolicy(sizePolicy2)
        self.Pg_1FondoPrinc.setMinimumSize(QSize(0, 0))
        self.Pg_1FondoPrinc.setMaximumSize(QSize(1181, 16777215))
        self.gridLayout_8 = QGridLayout(self.Pg_1FondoPrinc)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.Pg_1FondoPrinc)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setMinimumSize(QSize(833, 647))
        self.frame_2.setMaximumSize(QSize(1181, 1038))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_2)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_20 = QSpacerItem(20, 184, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_20, 0, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(289, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_10, 1, 0, 1, 1)

        self.Ic_ChatClass_2 = QLabel(self.frame_2)
        self.Ic_ChatClass_2.setObjectName(u"Ic_ChatClass_2")
        sizePolicy2.setHeightForWidth(self.Ic_ChatClass_2.sizePolicy().hasHeightForWidth())
        self.Ic_ChatClass_2.setSizePolicy(sizePolicy2)
        self.Ic_ChatClass_2.setMinimumSize(QSize(400, 200))
        self.Ic_ChatClass_2.setMaximumSize(QSize(580, 380))
        self.Ic_ChatClass_2.setStyleSheet(u"border: 0px;\n"
"background: none;")
        self.Ic_ChatClass_2.setTextFormat(Qt.TextFormat.PlainText)
        self.Ic_ChatClass_2.setPixmap(QPixmap(u"Imagenes/1742945765469.png"))
        self.Ic_ChatClass_2.setScaledContents(True)

        self.gridLayout_9.addWidget(self.Ic_ChatClass_2, 1, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(289, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_12, 1, 2, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 152, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_18, 2, 1, 1, 1)

        self.Lb_ChatClass_2 = QLabel(self.frame_2)
        self.Lb_ChatClass_2.setObjectName(u"Lb_ChatClass_2")
        sizePolicy2.setHeightForWidth(self.Lb_ChatClass_2.sizePolicy().hasHeightForWidth())
        self.Lb_ChatClass_2.setSizePolicy(sizePolicy2)
        self.Lb_ChatClass_2.setMinimumSize(QSize(150, 30))
        self.Lb_ChatClass_2.setMaximumSize(QSize(211, 41))
        self.Lb_ChatClass_2.setStyleSheet(u"border: 0px;\n"
"background: none;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 italic 32pt \"Arial Narrow\";")

        self.gridLayout_9.addWidget(self.Lb_ChatClass_2, 3, 1, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 184, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_19, 5, 1, 1, 1)

        self.Lb_Eslogan = QLabel(self.frame_2)
        self.Lb_Eslogan.setObjectName(u"Lb_Eslogan")
        sizePolicy2.setHeightForWidth(self.Lb_Eslogan.sizePolicy().hasHeightForWidth())
        self.Lb_Eslogan.setSizePolicy(sizePolicy2)
        self.Lb_Eslogan.setMinimumSize(QSize(425, 80))
        self.Lb_Eslogan.setMaximumSize(QSize(721, 50))
        self.Lb_Eslogan.setStyleSheet(u"border: 0px;\n"
"background: none;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 italic 31pt \"Arial Narrow\";")
        self.Lb_Eslogan.setWordWrap(True)

        self.gridLayout_9.addWidget(self.Lb_Eslogan, 4, 1, 1, 2)


        self.gridLayout_8.addWidget(self.frame_2, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.Pg_1FondoPrinc)
        self.Pg_2FondoMen = QWidget()
        self.Pg_2FondoMen.setObjectName(u"Pg_2FondoMen")
        self.verticalLayout_10 = QVBoxLayout(self.Pg_2FondoMen)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.Pg_2FondoMen)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background: none;\n"
"background-color: rgb(30, 30, 30);\n"
"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Lb_NombreMat = QLabel(self.frame_3)
        self.Lb_NombreMat.setObjectName(u"Lb_NombreMat")
        sizePolicy3.setHeightForWidth(self.Lb_NombreMat.sizePolicy().hasHeightForWidth())
        self.Lb_NombreMat.setSizePolicy(sizePolicy3)
        self.Lb_NombreMat.setMaximumSize(QSize(650, 16777215))
        self.Lb_NombreMat.setStyleSheet(u"padding-left: 15px;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 20pt \"Bahnschrift\";")
        self.Lb_NombreMat.setWordWrap(False)

        self.horizontalLayout_5.addWidget(self.Lb_NombreMat)

        self.Lb_NombreCanal = QLabel(self.frame_3)
        self.Lb_NombreCanal.setObjectName(u"Lb_NombreCanal")
        self.Lb_NombreCanal.setMaximumSize(QSize(400, 16777215))
        self.Lb_NombreCanal.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 20pt \"Bahnschrift\";")

        self.horizontalLayout_5.addWidget(self.Lb_NombreCanal)


        self.verticalLayout_10.addWidget(self.frame_3)

        self.scrollArea_3 = QScrollArea(self.Pg_2FondoMen)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1164, 792))
        self.gridLayout_10 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")

        self.gridLayout_10.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_10.addWidget(self.scrollArea_3)

        self.widget_5 = QWidget(self.Pg_2FondoMen)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"background: none;\n"
"background-color: rgb(30, 30, 30);\n"
"")
        self.gridLayout_11 = QGridLayout(self.widget_5)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Bt_Enviar = QToolButton(self.widget_5)
        self.Bt_Enviar.setObjectName(u"Bt_Enviar")
        self.Bt_Enviar.setStyleSheet(u"Button:hover{\n"
"	background-color: rgba(255, 255, 255,0.4);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"Imagenes/Enviar.png", QSize(), QIcon.Normal, QIcon.Off) # type: ignore
        self.Bt_Enviar.setIcon(icon10)
        self.Bt_Enviar.setIconSize(QSize(50, 50))

        self.gridLayout_11.addWidget(self.Bt_Enviar, 0, 1, 1, 1)

        self.LE_Mensaje = QLineEdit(self.widget_5)
        self.LE_Mensaje.setObjectName(u"LE_Mensaje")
        self.LE_Mensaje.setMinimumSize(QSize(450, 28))
        self.LE_Mensaje.setMaximumSize(QSize(950, 50))
        self.LE_Mensaje.setStyleSheet(u"background-color: rgb(239, 239, 239);\n"
"font: 20pt \"Bahnschrift\";\n"
"color: rgb(0, 0, 0);\n"
"padding-left: 15px;")
        self.LE_Mensaje.setFrame(False)
        self.LE_Mensaje.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.LE_Mensaje.setClearButtonEnabled(False)

        self.gridLayout_11.addWidget(self.LE_Mensaje, 0, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.widget_5)

        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 10)
        self.verticalLayout_10.setStretch(2, 2)
        self.stackedWidget_2.addWidget(self.Pg_2FondoMen)

        self.verticalLayout_8.addWidget(self.stackedWidget_2)


        self.horizontalLayout_2.addWidget(self.Frm_FondoMnsj)


        self.verticalLayout_2.addWidget(self.Frm_2Inferior)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 26)

        self.gridLayout_6.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Lb_TituloChatClass.setText(QCoreApplication.translate("MainWindow", u"Chat Class", None))
        self.Bt_Minizar.setText("")
        self.Bt_Maximizar.setText("")
        self.Bt_Cerrar.setText("")
        self.Bt_Perfil.setText("")
        self.Bt_Regresar.setText("")
        self.Bt_Ajustes.setText("")
        self.Bt_IrGrupos.setText(QCoreApplication.translate("MainWindow", u"Chats Grupales", None))
        self.Bt_IrChatPriv.setText(QCoreApplication.translate("MainWindow", u"Chats Privados", None))
        self.Bt_BuscarGrupo.setText("")
        self.Bt_RecargarGrupos.setText("")
        self.Bt_MasOpciones.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ajustes", None))
        self.Lb_Version.setText(QCoreApplication.translate("MainWindow", u"Version 3.0 \u00a92025", None))
        self.Ic_ChatClass.setText("")
        self.Lb_ChatClass.setText(QCoreApplication.translate("MainWindow", u"Chat Class ", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Pg_InfDeApp), QCoreApplication.translate("MainWindow", u"Informacion de la App", None))
        self.Bt_VerCont_2.setText("")
        self.Lb_ContActual.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a Actual:", None))
        self.Tf_ContActual.setInputMask("")
        self.Tf_ContActual.setText("")
        self.Tf_ContActual.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese la Contrase\u00f1a Actual", None))
        self.Tf_ConfirmCont.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirme la Contrase\u00f1a", None))
        self.Bt_VerCont.setText("")
        self.Tf_NuevCont.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese la Nueva Contrase\u00f1a", None))
        self.Lb_ErrorContActu.setText("")
        self.Lb_ErrorConfirmCont.setText("")
        self.Bt_VerCont_3.setText("")
        self.Lb_NuevCont.setText(QCoreApplication.translate("MainWindow", u"Nueva Contrase\u00f1a:", None))
        self.Lb_ConfirmCont.setText(QCoreApplication.translate("MainWindow", u"Confirmar Nueva Contrase\u00f1a:", None))
        self.Bt_Confirm.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Pg_Seguridad), QCoreApplication.translate("MainWindow", u"Seguridad", None))
        self.Bt_Soporte.setText(QCoreApplication.translate("MainWindow", u"Soporte", None))
        self.Bt_CondPolit.setText(QCoreApplication.translate("MainWindow", u"T\u00e9rminos y Condiciones", None))
        self.Bt_PregFrec.setText(QCoreApplication.translate("MainWindow", u"Preguntas Frecuentes", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Pg_Ayuda), QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.Bt_IrGrupos_2.setText(QCoreApplication.translate("MainWindow", u"Chats Grupales", None))
        self.Bt_IrChatPriv_2.setText(QCoreApplication.translate("MainWindow", u"Chats Privados", None))
        self.Bt_BuscarChats.setText("")
        self.Bt_CargarChats.setText("")
        self.Lb_Correo.setText(QCoreApplication.translate("MainWindow", u"Correo:", None))
        self.Lb_Codigo.setText(QCoreApplication.translate("MainWindow", u"Codigo:", None))
        self.Lb_Apellido.setText(QCoreApplication.translate("MainWindow", u"Apellido:", None))
        self.Lb_Rol_Puesto.setText("")
        self.Lb_Apellido_Puesto.setText("")
        self.Lb_Nomb.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.Lb_Rol.setText(QCoreApplication.translate("MainWindow", u"Rol:", None))
        self.Lb_Codigo_Puesto.setText("")
        self.Lb_Nomb_Puesto.setText("")
        self.Lb_Correo_Puesto.setText("")
        self.Bt_ChatAvisos.setText(QCoreApplication.translate("MainWindow", u"Avisos", None))
        self.Bt_ChatFueraDelTema.setText(QCoreApplication.translate("MainWindow", u"Fuera del Tema", None))
        self.Bt_ChatGeneral.setText(QCoreApplication.translate("MainWindow", u"Chat General ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"No hace nada", None))
        self.Ic_ChatClass_2.setText("")
        self.Lb_ChatClass_2.setText(QCoreApplication.translate("MainWindow", u" Chat Class", None))
        self.Lb_Eslogan.setText(QCoreApplication.translate("MainWindow", u"Un Chat para todos los alumnos y maestros", None))
        self.Lb_NombreMat.setText("")
        self.Lb_NombreCanal.setText("")
        self.Bt_Enviar.setText("")
        self.LE_Mensaje.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mensaje", None))
    # retranslateUi

