# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Princ_IniSes_RegisFPbDsx.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1364, 908)
        MainWindow.setMinimumSize(QSize(1360, 768))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setSizeIncrement(QSize(0, 0))
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(u"Imagenes/1742945765469.png", QSize(), QIcon.Normal, QIcon.On) # type: ignore
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"background-image: url(\"Imagenes/Diseño sin título.jpg\");")
        MainWindow.setIconSize(QSize(30, 30))
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setDockOptions(QMainWindow.DockOption.AllowTabbedDocks|QMainWindow.DockOption.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.WidgetPrincipal = QWidget(MainWindow)
        self.WidgetPrincipal.setObjectName(u"WidgetPrincipal")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WidgetPrincipal.sizePolicy().hasHeightForWidth())
        self.WidgetPrincipal.setSizePolicy(sizePolicy)
        self.WidgetPrincipal.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.WidgetPrincipal)
        self.gridLayout.setObjectName(u"gridLayout")
        self.StW_Prin = QStackedWidget(self.WidgetPrincipal)
        self.StW_Prin.setObjectName(u"StW_Prin")
        self.StW_Prin.setEnabled(True)
        sizePolicy.setHeightForWidth(self.StW_Prin.sizePolicy().hasHeightForWidth())
        self.StW_Prin.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        self.StW_Prin.setFont(font)
        self.StW_Prin.setToolTipDuration(1)
        self.StW_Prin.setStyleSheet(u"")
        self.StW_Prin.setFrameShape(QFrame.Shape.WinPanel)
        self.Pg_Principal = QWidget()
        self.Pg_Principal.setObjectName(u"Pg_Principal")
        sizePolicy.setHeightForWidth(self.Pg_Principal.sizePolicy().hasHeightForWidth())
        self.Pg_Principal.setSizePolicy(sizePolicy)
        self.Pg_Principal.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Img_LogoPrincipal = QLabel(self.Pg_Principal)
        self.Img_LogoPrincipal.setObjectName(u"Img_LogoPrincipal")
        self.Img_LogoPrincipal.setGeometry(QRect(425, 150, 500, 340))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Img_LogoPrincipal.sizePolicy().hasHeightForWidth())
        self.Img_LogoPrincipal.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(11)
        self.Img_LogoPrincipal.setFont(font1)
        self.Img_LogoPrincipal.setStyleSheet(u"background: none;")
        self.Img_LogoPrincipal.setPixmap(QPixmap(u"Imagenes/1742945765469.png"))
        self.Img_LogoPrincipal.setScaledContents(True)
        self.Bt_InicioSesion = QPushButton(self.Pg_Principal)
        self.Bt_InicioSesion.setObjectName(u"Bt_InicioSesion")
        self.Bt_InicioSesion.setGeometry(QRect(345, 625, 325, 65))
        sizePolicy1.setHeightForWidth(self.Bt_InicioSesion.sizePolicy().hasHeightForWidth())
        self.Bt_InicioSesion.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(13)
        self.Bt_InicioSesion.setFont(font2)
        self.Bt_InicioSesion.setStyleSheet(u"QPushButton {\n"
"    background: none;\n"
"    background-color: #9e9e9e;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    padding: 5px;\n"
"    transition: 0.5s; /* Transici\u00f3n suave */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(194, 194, 194);\n"
"    border-color: #5a5a5a; /* Opcional: cambia el borde para m\u00e1s contraste */\n"
"}\n"
"")
        self.Bt_InicioSesion.setAutoDefault(False)
        self.Bt_InicioSesion.setFlat(False)
        self.Bt_CrearCuenta = QPushButton(self.Pg_Principal)
        self.Bt_CrearCuenta.setObjectName(u"Bt_CrearCuenta")
        self.Bt_CrearCuenta.setGeometry(QRect(670, 625, 325, 65))
        sizePolicy1.setHeightForWidth(self.Bt_CrearCuenta.sizePolicy().hasHeightForWidth())
        self.Bt_CrearCuenta.setSizePolicy(sizePolicy1)
        self.Bt_CrearCuenta.setFont(font2)
        self.Bt_CrearCuenta.setStyleSheet(u"QPushButton {\n"
"background: none;\n"
"    background-color: #9e9e9e;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 20px;\n"
"    border-bottom-right-radius: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(194, 194, 194);\n"
"    border-color: #5a5a5a; /* Opcional: cambia el borde para m\u00e1s contraste */\n"
"}\n"
"")
        self.StW_Prin.addWidget(self.Pg_Principal)
        self.Pg_InicSes = QWidget()
        self.Pg_InicSes.setObjectName(u"Pg_InicSes")
        self.LblCodigo = QLabel(self.Pg_InicSes)
        self.LblCodigo.setObjectName(u"LblCodigo")
        self.LblCodigo.setGeometry(QRect(160, 260, 90, 30))
        font3 = QFont()
        font3.setFamilies([u"Bahnschrift"])
        font3.setPointSize(19)
        font3.setBold(True)
        self.LblCodigo.setFont(font3)
        self.LblCodigo.setStyleSheet(u"background: none;\n"
"color: rgb(255, 255, 255);")
        self.Tf_Codigo = QLineEdit(self.Pg_InicSes)
        self.Tf_Codigo.setObjectName(u"Tf_Codigo")
        self.Tf_Codigo.setGeometry(QRect(150, 300, 381, 40))
        font4 = QFont()
        font4.setFamilies([u"Bahnschrift"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.Tf_Codigo.setFont(font4)
        self.Tf_Codigo.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.Tf_Codigo.setStyleSheet(u"background: none;\n"
"background-color: rgb(158, 158, 158);\n"
"border:1px solid black;\n"
"color: rgb(106, 13, 173);\n"
"padding-left:10px;\n"
"padding-bottom:0px;")
        self.Tf_Codigo.setMaxLength(9)
        self.Tf_Codigo.setEchoMode(QLineEdit.EchoMode.Normal)
        self.LblContrasena = QLabel(self.Pg_InicSes)
        self.LblContrasena.setObjectName(u"LblContrasena")
        self.LblContrasena.setGeometry(QRect(160, 430, 140, 30))
        self.LblContrasena.setFont(font3)
        self.LblContrasena.setStyleSheet(u"background: none;\n"
"color: rgb(255, 255, 255);")
        self.Tf_Contrasena = QLineEdit(self.Pg_InicSes)
        self.Tf_Contrasena.setObjectName(u"Tf_Contrasena")
        self.Tf_Contrasena.setGeometry(QRect(150, 470, 380, 40))
        self.Tf_Contrasena.setFont(font4)
        self.Tf_Contrasena.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.Tf_Contrasena.setStyleSheet(u"background: none;\n"
"background-color: rgb(158, 158, 158);\n"
"border:1px solid black;\n"
"color: rgb(106, 13, 173);\n"
"padding-left:10px;\n"
"padding-bottom:0px;")
        self.Tf_Contrasena.setEchoMode(QLineEdit.EchoMode.Password)
        self.IcoChatClass_2 = QLabel(self.Pg_InicSes)
        self.IcoChatClass_2.setObjectName(u"IcoChatClass_2")
        self.IcoChatClass_2.setGeometry(QRect(790, 320, 450, 290))
        self.IcoChatClass_2.setStyleSheet(u"background: none;")
        self.IcoChatClass_2.setPixmap(QPixmap(u"Imagenes/1742945765469.png"))
        self.IcoChatClass_2.setScaledContents(True)
        self.line_2 = QFrame(self.Pg_InicSes)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(660, 130, 21, 651))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.line_2.setFont(font5)
        self.line_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.Bt_InicarSesion = QPushButton(self.Pg_InicSes)
        self.Bt_InicarSesion.setObjectName(u"Bt_InicarSesion")
        self.Bt_InicarSesion.setGeometry(QRect(260, 640, 131, 41))
        font6 = QFont()
        font6.setFamilies([u"Bahnschrift"])
        font6.setPointSize(12)
        font6.setBold(True)
        self.Bt_InicarSesion.setFont(font6)
        self.Bt_InicarSesion.setStyleSheet(u"QPushButton{\n"
"background: none;\n"
"background-color: rgb(158, 158, 158);\n"
"color: rgb(12, 12, 12);\n"
"border-radius: 10%;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(194, 194, 194);\n"
"    border-color: #5a5a5a; /* Opcional: cambia el borde para m\u00e1s contraste */\n"
"}")
        self.Bt_RegresarIni_Princ = QPushButton(self.Pg_InicSes)
        self.Bt_RegresarIni_Princ.setObjectName(u"Bt_RegresarIni_Princ")
        self.Bt_RegresarIni_Princ.setGeometry(QRect(20, 30, 80, 80))
        self.Bt_RegresarIni_Princ.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.Bt_RegresarIni_Princ.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Bt_RegresarIni_Princ.setStyleSheet(u"QPushButton{\n"
"background: none;\n"
"background-color: rgba(191, 191, 191,0.8);\n"
"color: rgb(12, 12, 12);\n"
"border-radius:38px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(209, 209, 209);\n"
"	border-radious: 38px solid #5a5a5a;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"Imagenes/atras.png", QSize(), QIcon.Normal, QIcon.Off) # type: ignore
        self.Bt_RegresarIni_Princ.setIcon(icon1)
        self.Bt_RegresarIni_Princ.setIconSize(QSize(90, 90))
        self.Bt_RegresarIni_Princ.setAutoDefault(False)
        self.Lbl_ErrorEnInicioSesion = QLabel(self.Pg_InicSes)
        self.Lbl_ErrorEnInicioSesion.setObjectName(u"Lbl_ErrorEnInicioSesion")
        self.Lbl_ErrorEnInicioSesion.setGeometry(QRect(150, 360, 450, 20))
        font7 = QFont()
        font7.setFamilies([u"Terminal"])
        font7.setPointSize(20)
        self.Lbl_ErrorEnInicioSesion.setFont(font7)
        self.Lbl_ErrorEnInicioSesion.setStyleSheet(u"color: rgb(255, 170, 171);\n"
"background:none;")
        self.Lbl_ErrorEnInicioSesion_2 = QLabel(self.Pg_InicSes)
        self.Lbl_ErrorEnInicioSesion_2.setObjectName(u"Lbl_ErrorEnInicioSesion_2")
        self.Lbl_ErrorEnInicioSesion_2.setGeometry(QRect(150, 530, 450, 20))
        self.Lbl_ErrorEnInicioSesion_2.setFont(font7)
        self.Lbl_ErrorEnInicioSesion_2.setStyleSheet(u"color: rgb(255, 170, 171);\n"
"background:none;")
        self.StW_Prin.addWidget(self.Pg_InicSes)
        self.IcoChatClass_2.raise_()
        self.LblCodigo.raise_()
        self.Tf_Codigo.raise_()
        self.LblContrasena.raise_()
        self.Tf_Contrasena.raise_()
        self.line_2.raise_()
        self.Bt_InicarSesion.raise_()
        self.Bt_RegresarIni_Princ.raise_()
        self.Lbl_ErrorEnInicioSesion.raise_()
        self.Lbl_ErrorEnInicioSesion_2.raise_()
        self.Pg_Regist_Datos_Verfc = QWidget()
        self.Pg_Regist_Datos_Verfc.setObjectName(u"Pg_Regist_Datos_Verfc")
        self.line_3 = QFrame(self.Pg_Regist_Datos_Verfc)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(690, 110, 30, 681))
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.IcoChatClass_3 = QLabel(self.Pg_Regist_Datos_Verfc)
        self.IcoChatClass_3.setObjectName(u"IcoChatClass_3")
        self.IcoChatClass_3.setGeometry(QRect(790, 300, 450, 290))
        self.IcoChatClass_3.setStyleSheet(u"background: none;")
        self.IcoChatClass_3.setPixmap(QPixmap(u"Imagenes/1742945765469.png"))
        self.IcoChatClass_3.setScaledContents(True)
        self.Bt_RegresarIni_Princ_2 = QPushButton(self.Pg_Regist_Datos_Verfc)
        self.Bt_RegresarIni_Princ_2.setObjectName(u"Bt_RegresarIni_Princ_2")
        self.Bt_RegresarIni_Princ_2.setGeometry(QRect(20, 30, 80, 80))
        self.Bt_RegresarIni_Princ_2.setStyleSheet(u"QPushButton{\n"
"background: none;\n"
"background-color: rgba(191, 191, 191,0.8);\n"
"border-radius:38px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(209, 209, 209);\n"
"	border-radious: 38px solid #5a5a5a;\n"
"}")
        self.Bt_RegresarIni_Princ_2.setIcon(icon1)
        self.Bt_RegresarIni_Princ_2.setIconSize(QSize(90, 90))
        self.stackedWidget = QStackedWidget(self.Pg_Regist_Datos_Verfc)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(90, 110, 551, 691))
        self.stackedWidget.setStyleSheet(u"")
        self.Pg_Registro = QWidget()
        self.Pg_Registro.setObjectName(u"Pg_Registro")
        self.TexCod = QLabel(self.Pg_Registro)
        self.TexCod.setObjectName(u"TexCod")
        self.TexCod.setGeometry(QRect(90, 30, 91, 41))
        font8 = QFont()
        font8.setFamilies([u"Bahnschrift"])
        font8.setPointSize(19)
        font8.setBold(False)
        font8.setItalic(False)
        font8.setStyleStrategy(QFont.PreferDefault) # type: ignore
        self.TexCod.setFont(font8)
        self.TexCod.setStyleSheet(u"background: none;\n"
"color: rgb(255, 255, 255);")
        self.CodigoIngr = QLineEdit(self.Pg_Registro)
        self.CodigoIngr.setObjectName(u"CodigoIngr")
        self.CodigoIngr.setGeometry(QRect(60, 80, 391, 41))
        palette = QPalette()
        brush = QBrush(QColor(106, 13, 173, 255)) # type: ignore
        brush.setStyle(Qt.SolidPattern) # type: ignore
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush) # type: ignore
        brush1 = QBrush(QColor(158, 158, 158, 255))
        brush1.setStyle(Qt.SolidPattern) # type: ignore
        palette.setBrush(QPalette.Active, QPalette.Button, brush1) # type: ignore
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern) # type: ignore
        palette.setBrush(QPalette.Active, QPalette.Light, brush2) # type: ignore
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush2) # type: ignore
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2) # type: ignore
        palette.setBrush(QPalette.Active, QPalette.Mid, brush2) # type: ignore
        palette.setBrush(QPalette.Active, QPalette.Text, brush) # type: ignore
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush) # type: ignore
        palette.setBrush(QPalette.Active, QPalette.Base, brush1) # type: ignore
        palette.setBrush(QPalette.Active, QPalette.Window, brush1) # type: ignore
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush2) # type: ignore
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush2) # type: ignore
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush2) # type: ignore
        brush3 = QBrush(QColor(106, 13, 173, 128))
        brush3.setStyle(Qt.SolidPattern) # type: ignore
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3) # type: ignore
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush) # type: ignore
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1) # type: ignore
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2) # type: ignore
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush2) # type: ignore
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2) # type: ignore
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush2) # type: ignore
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush) # type: ignore
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush) # type: ignore
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1) # type: ignore
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1) # type: ignore
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush2) # type: ignore
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2) # type: ignore
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush2) # type: ignore
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3) # type: ignore
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush) # type: ignore
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1) # type: ignore
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2) # type: ignore
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush2) # type: ignore
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2) # type: ignore
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush2) # type: ignore
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush) # type: ignore
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush) # type: ignore
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1) # type: ignore
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1) # type: ignore
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush2) # type: ignore
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2) # type: ignore
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush2) # type: ignore
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3) # type: ignore
#endif
        self.CodigoIngr.setPalette(palette)
        font9 = QFont()
        font9.setFamilies([u"Bahnschrift"])
        font9.setPointSize(14)
        font9.setBold(False)
        font9.setStyleStrategy(QFont.PreferAntialias) # type: ignore
        self.CodigoIngr.setFont(font9)
        self.CodigoIngr.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.CodigoIngr.setStyleSheet(u"background: none;\n"
"background-color: rgb(158, 158, 158);\n"
"border:1px solid black;\n"
"color: rgb(106, 13, 173);\n"
"padding-left:10px;\n"
"padding-bottom:0px;")
        self.CodigoIngr.setDragEnabled(False)
        self.TexContr = QLabel(self.Pg_Registro)
        self.TexContr.setObjectName(u"TexContr")
        self.TexContr.setGeometry(QRect(90, 170, 140, 40))
        self.TexContr.setFont(font8)
        self.TexContr.setStyleSheet(u"background: none;\n"
"color: rgb(255, 255, 255);")
        self.ContrasenaIngr = QLineEdit(self.Pg_Registro)
        self.ContrasenaIngr.setObjectName(u"ContrasenaIngr")
        self.ContrasenaIngr.setGeometry(QRect(60, 210, 390, 40))
        self.ContrasenaIngr.setMaximumSize(QSize(16777215, 16777215))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush) # type: ignore
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1) # type: ignore
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2) # type: ignore
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush2) # type: ignore
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush2) # type: ignore
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush2) # type: ignore
        palette1.setBrush(QPalette.Active, QPalette.Text, brush) # type: ignore
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush) # type: ignore
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1) # type: ignore
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1) # type: ignore
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush2) # type: ignore
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush2) # type: ignore
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush2) # type: ignore
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3) # type: ignore
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush) # type: ignore
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1) # type: ignore
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush2) # type: ignore
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush2) # type: ignore
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush2) # type: ignore
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush2) # type: ignore
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush) # type: ignore
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush) # type: ignore
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1) # type: ignore
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1) # type: ignore
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush2) # type: ignore
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2) # type: ignore
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush2) # type: ignore
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3) # type: ignore
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush) # type: ignore
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1) # type: ignore
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2) # type: ignore
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush2) # type: ignore
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush2) # type: ignore
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush2) # type: ignore
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush) # type: ignore
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush) # type: ignore
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1) # type: ignore
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1) # type: ignore
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush2) # type: ignore
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2) # type: ignore
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush2) # type: ignore
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3) # type: ignore
#endif
        self.ContrasenaIngr.setPalette(palette1)
        self.ContrasenaIngr.setFont(font9)
        self.ContrasenaIngr.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.ContrasenaIngr.setStyleSheet(u"background: none;\n"
"background-color: rgb(158, 158, 158);\n"
"border:1px solid black;\n"
"color: rgb(106, 13, 173);\n"
"padding-left:10px;\n"
"padding-bottom:0px;")
        self.ContrasenaIngr.setEchoMode(QLineEdit.EchoMode.Password)
        self.TexConfContr = QLabel(self.Pg_Registro)
        self.TexConfContr.setObjectName(u"TexConfContr")
        self.TexConfContr.setGeometry(QRect(90, 270, 250, 40))
        self.TexConfContr.setFont(font8)
        self.TexConfContr.setStyleSheet(u"background: none;\n"
"color: rgb(255, 255, 255);")
        self.ConfirmContrasena = QLineEdit(self.Pg_Registro)
        self.ConfirmContrasena.setObjectName(u"ConfirmContrasena")
        self.ConfirmContrasena.setGeometry(QRect(60, 310, 400, 40))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush) # type: ignore
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1) # type: ignore
        palette2.setBrush(QPalette.Active, QPalette.Light, brush2) # type: ignore
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush2) # type: ignore
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush2) # type: ignore
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush2) # type: ignore
        palette2.setBrush(QPalette.Active, QPalette.Text, brush) # type: ignore
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush) # type: ignore
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1) # type: ignore
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1) # type: ignore
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush2) # type: ignore
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush2) # type: ignore
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush2) # type: ignore
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3) # type: ignore
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush) # type: ignore
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1) # type: ignore
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush2) # type: ignore
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush2) # type: ignore
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush2) # type: ignore
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush2) # type: ignore
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush) # type: ignore
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush) # type: ignore
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1) # type: ignore
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1) # type: ignore
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush2) # type: ignore
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2) # type: ignore
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush2) # type: ignore
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3) # type: ignore
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush) # type: ignore
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1) # type: ignore
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush2) # type: ignore
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush2) # type: ignore
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush2) # type: ignore
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush2) # type: ignore
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush) # type: ignore
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush) # type: ignore
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1) # type: ignore
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1) # type: ignore
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush2) # type: ignore
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2) # type: ignore
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush2) # type: ignore
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3) # type: ignore
#endif
        self.ConfirmContrasena.setPalette(palette2)
        self.ConfirmContrasena.setFont(font9)
        self.ConfirmContrasena.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.ConfirmContrasena.setStyleSheet(u"background: none;\n"
"background-color: rgb(158, 158, 158);\n"
"border:1px solid black;\n"
"color: rgb(106, 13, 173);\n"
"padding-left:10px;\n"
"padding-bottom:0px;")
        self.ConfirmContrasena.setEchoMode(QLineEdit.EchoMode.Password)
        self.TexCorr = QLabel(self.Pg_Registro)
        self.TexCorr.setObjectName(u"TexCorr")
        self.TexCorr.setGeometry(QRect(90, 430, 91, 40))
        self.TexCorr.setFont(font8)
        self.TexCorr.setStyleSheet(u"background: none;\n"
"color: rgb(255, 255, 255);")
        self.CorreoIngr = QLineEdit(self.Pg_Registro)
        self.CorreoIngr.setObjectName(u"CorreoIngr")
        self.CorreoIngr.setGeometry(QRect(60, 470, 401, 41))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush) # type: ignore
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1) # type: ignore
        palette3.setBrush(QPalette.Active, QPalette.Light, brush2) # type: ignore
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush2) # type: ignore
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush2) # type: ignore
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush2) # type: ignore
        palette3.setBrush(QPalette.Active, QPalette.Text, brush) # type: ignore
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush) # type: ignore
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1) # type: ignore
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1) # type: ignore
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush2) # type: ignore
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush2) # type: ignore
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush2) # type: ignore
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3) # type: ignore
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush) # type: ignore
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1) # type: ignore
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush2) # type: ignore
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush2) # type: ignore
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush2) # type: ignore
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush2) # type: ignore
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush) # type: ignore
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush) # type: ignore
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1) # type: ignore
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1) # type: ignore
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush2) # type: ignore
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2) # type: ignore
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush2) # type: ignore
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3) # type: ignore
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush) # type: ignore
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1) # type: ignore
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush2) # type: ignore
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush2) # type: ignore
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush2) # type: ignore
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush2) # type: ignore
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush) # type: ignore
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush) # type: ignore
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1) # type: ignore
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1) # type: ignore
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush2) # type: ignore
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2) # type: ignore
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush2) # type: ignore
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3) # type: ignore
#endif
        self.CorreoIngr.setPalette(palette3)
        self.CorreoIngr.setFont(font9)
        self.CorreoIngr.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.CorreoIngr.setStyleSheet(u"background: none;\n"
"background-color: rgb(158, 158, 158);\n"
"border:1px solid black;\n"
"color: rgb(106, 13, 173);\n"
"padding-left:10px;\n"
"padding-bottom:0px;")
        self.Bt_Regist = QPushButton(self.Pg_Registro)
        self.Bt_Regist.setObjectName(u"Bt_Regist")
        self.Bt_Regist.setGeometry(QRect(200, 610, 131, 41))
        self.Bt_Regist.setFont(font6)
        self.Bt_Regist.setStyleSheet(u"QPushButton{\n"
"background: none;\n"
"background-color: rgb(158, 158, 158);\n"
"color: rgb(12, 12, 12);\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(194, 194, 194);\n"
"    border-color: #5a5a5a; /* Opcional: cambia el borde para m\u00e1s contraste */\n"
"}")
        self.Lbl_ErrorRegistro = QLabel(self.Pg_Registro)
        self.Lbl_ErrorRegistro.setObjectName(u"Lbl_ErrorRegistro")
        self.Lbl_ErrorRegistro.setGeometry(QRect(60, 130, 450, 20))
        self.Lbl_ErrorRegistro.setFont(font7)
        self.Lbl_ErrorRegistro.setStyleSheet(u"color: rgb(255, 170, 171);\n"
"background:none;")
        self.Lbl_ErrorRegistro_2 = QLabel(self.Pg_Registro)
        self.Lbl_ErrorRegistro_2.setObjectName(u"Lbl_ErrorRegistro_2")
        self.Lbl_ErrorRegistro_2.setGeometry(QRect(60, 370, 450, 20))
        self.Lbl_ErrorRegistro_2.setFont(font7)
        self.Lbl_ErrorRegistro_2.setStyleSheet(u"color: rgb(255, 170, 171);\n"
"background:none;")
        self.Lbl_ErrorRegistro_3 = QLabel(self.Pg_Registro)
        self.Lbl_ErrorRegistro_3.setObjectName(u"Lbl_ErrorRegistro_3")
        self.Lbl_ErrorRegistro_3.setGeometry(QRect(60, 530, 450, 20))
        self.Lbl_ErrorRegistro_3.setFont(font7)
        self.Lbl_ErrorRegistro_3.setStyleSheet(u"color: rgb(255, 170, 171);\n"
"background:none;")
        self.stackedWidget.addWidget(self.Pg_Registro)
        self.Pg_RegDatos = QWidget()
        self.Pg_RegDatos.setObjectName(u"Pg_RegDatos")
        self.Pg_RegDatos.setStyleSheet(u"")
        self.Lb_Instrucciones = QLabel(self.Pg_RegDatos)
        self.Lb_Instrucciones.setObjectName(u"Lb_Instrucciones")
        self.Lb_Instrucciones.setGeometry(QRect(170, 30, 201, 41))
        font10 = QFont()
        font10.setFamilies([u"Bahnschrift"])
        font10.setPointSize(19)
        self.Lb_Instrucciones.setFont(font10)
        self.Lb_Instrucciones.setStyleSheet(u"background: none;\n"
"color: rgb(255, 255, 255);")
        self.Lb_Grado = QLabel(self.Pg_RegDatos)
        self.Lb_Grado.setObjectName(u"Lb_Grado")
        self.Lb_Grado.setGeometry(QRect(40, 150, 81, 41))
        font11 = QFont()
        font11.setFamilies([u"Bahnschrift"])
        font11.setPointSize(18)
        font11.setBold(False)
        font11.setItalic(False)
        self.Lb_Grado.setFont(font11)
        self.Lb_Grado.setStyleSheet(u"background: none;\n"
"color: rgb(255, 255, 255);")
        self.CB_Grado = QComboBox(self.Pg_RegDatos)
        self.CB_Grado.addItem("")
        self.CB_Grado.addItem("")
        self.CB_Grado.addItem("")
        self.CB_Grado.addItem("")
        self.CB_Grado.addItem("")
        self.CB_Grado.addItem("")
        self.CB_Grado.addItem("")
        self.CB_Grado.addItem("")
        self.CB_Grado.addItem("")
        self.CB_Grado.setObjectName(u"CB_Grado")
        self.CB_Grado.setGeometry(QRect(40, 200, 80, 30))
        self.CB_Grado.setFont(font10)
        self.CB_Grado.setStyleSheet(u"background: none;\n"
"background-color: rgb(158, 158, 158);\n"
"border:1px solid black;\n"
"color: rgb(106, 13, 173);\n"
"padding-left:10px;\n"
"padding-bottom:0px;")
        self.Lb_Grupo = QLabel(self.Pg_RegDatos)
        self.Lb_Grupo.setObjectName(u"Lb_Grupo")
        self.Lb_Grupo.setGeometry(QRect(210, 150, 101, 31))
        font12 = QFont()
        font12.setFamilies([u"Bahnschrift"])
        font12.setPointSize(18)
        font12.setBold(True)
        font12.setItalic(False)
        self.Lb_Grupo.setFont(font12)
        self.Lb_Grupo.setStyleSheet(u"background: none;\n"
"color: rgb(255, 255, 255);")
        self.CB_Grupo = QComboBox(self.Pg_RegDatos)
        self.CB_Grupo.addItem("")
        self.CB_Grupo.addItem("")
        self.CB_Grupo.addItem("")
        self.CB_Grupo.setObjectName(u"CB_Grupo")
        self.CB_Grupo.setGeometry(QRect(200, 200, 80, 30))
        font13 = QFont()
        font13.setFamilies([u"Bahnschrift"])
        font13.setPointSize(19)
        font13.setBold(False)
        font13.setItalic(False)
        self.CB_Grupo.setFont(font13)
        self.CB_Grupo.setStyleSheet(u"background: none;\n"
"background-color: rgb(158, 158, 158);\n"
"border:1px solid black;\n"
"color: rgb(106, 13, 173);\n"
"padding-left:10px;\n"
"padding-bottom:0px;")
        self.Lb_Turno = QLabel(self.Pg_RegDatos)
        self.Lb_Turno.setObjectName(u"Lb_Turno")
        self.Lb_Turno.setGeometry(QRect(380, 150, 71, 31))
        self.Lb_Turno.setFont(font10)
        self.Lb_Turno.setStyleSheet(u"background: none;\n"
"color: rgb(255, 255, 255);")
        self.CB_Turno = QComboBox(self.Pg_RegDatos)
        self.CB_Turno.addItem("")
        self.CB_Turno.addItem("")
        self.CB_Turno.addItem("")
        self.CB_Turno.setObjectName(u"CB_Turno")
        self.CB_Turno.setGeometry(QRect(350, 200, 150, 30))
        self.CB_Turno.setFont(font13)
        self.CB_Turno.setStyleSheet(u"background: none;\n"
"background-color: rgb(158, 158, 158);\n"
"border:1px solid black;\n"
"color: rgb(106, 13, 173);\n"
"padding-left:10px;\n"
"padding-bottom:0px;")
        self.Bt_CrearGrupo = QPushButton(self.Pg_RegDatos)
        self.Bt_CrearGrupo.setObjectName(u"Bt_CrearGrupo")
        self.Bt_CrearGrupo.setGeometry(QRect(170, 340, 141, 41))
        self.Bt_CrearGrupo.setFont(font6)
        self.Bt_CrearGrupo.setStyleSheet(u"QPushButton{\n"
"background: none;\n"
"background-color: rgb(158, 158, 158);\n"
"color: rgb(12, 12, 12);\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(194, 194, 194);\n"
"    border-color: #5a5a5a; /* Opcional: cambia el borde para m\u00e1s contraste */\n"
"}")
        self.Lbl_ErrorDatosCurso = QLabel(self.Pg_RegDatos)
        self.Lbl_ErrorDatosCurso.setObjectName(u"Lbl_ErrorDatosCurso")
        self.Lbl_ErrorDatosCurso.setGeometry(QRect(40, 280, 450, 20))
        self.Lbl_ErrorDatosCurso.setFont(font7)
        self.Lbl_ErrorDatosCurso.setStyleSheet(u"color: rgb(255, 170, 171);\n"
"background:none;")
        self.stackedWidget.addWidget(self.Pg_RegDatos)
        self.Pg_Verificacion = QWidget()
        self.Pg_Verificacion.setObjectName(u"Pg_Verificacion")
        self.stackedWidget.addWidget(self.Pg_Verificacion)
        self.StW_Prin.addWidget(self.Pg_Regist_Datos_Verfc)
        self.stackedWidget.raise_()
        self.line_3.raise_()
        self.IcoChatClass_3.raise_()
        self.Bt_RegresarIni_Princ_2.raise_()

        self.gridLayout.addWidget(self.StW_Prin, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.WidgetPrincipal)

        self.retranslateUi(MainWindow)

        self.StW_Prin.setCurrentIndex(0)
        self.Bt_InicioSesion.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Chat Class", None))
        self.Img_LogoPrincipal.setText("")
        self.Bt_InicioSesion.setText(QCoreApplication.translate("MainWindow", u"Iniciar Sesion ", None))
        self.Bt_CrearCuenta.setText(QCoreApplication.translate("MainWindow", u" Crear cuenta ", None))
        self.LblCodigo.setText(QCoreApplication.translate("MainWindow", u"Codigo", None))
        self.Tf_Codigo.setText("")
        self.Tf_Codigo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese su codigo", None))
        self.LblContrasena.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.Tf_Contrasena.setText("")
        self.Tf_Contrasena.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese su contrase\u00f1a", None))
        self.IcoChatClass_2.setText("")
        self.Bt_InicarSesion.setText(QCoreApplication.translate("MainWindow", u"Iniciar Sesion", None))
        self.Bt_RegresarIni_Princ.setText("")
        self.Lbl_ErrorEnInicioSesion.setText("")
        self.Lbl_ErrorEnInicioSesion_2.setText("")
        self.IcoChatClass_3.setText("")
        self.Bt_RegresarIni_Princ_2.setText("")
        self.TexCod.setText(QCoreApplication.translate("MainWindow", u"Codigo", None))
#if QT_CONFIG(tooltip)
        self.CodigoIngr.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.CodigoIngr.setText("")
        self.CodigoIngr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingresa su Codigo", None))
        self.TexContr.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.ContrasenaIngr.setInputMask("")
        self.ContrasenaIngr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingresa una Contrase\u00f1a", None))
        self.TexConfContr.setText(QCoreApplication.translate("MainWindow", u"Confirmar Contrase\u00f1a", None))
        self.ConfirmContrasena.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirme la Contrase\u00f1a ", None))
        self.TexCorr.setText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.CorreoIngr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese su Correo", None))
        self.Bt_Regist.setText(QCoreApplication.translate("MainWindow", u"Registrarse", None))
        self.Lbl_ErrorRegistro.setText("")
        self.Lbl_ErrorRegistro_2.setText("")
        self.Lbl_ErrorRegistro_3.setText("")
        self.Lb_Instrucciones.setText(QCoreApplication.translate("MainWindow", u"Datos del Alumno", None))
        self.Lb_Grado.setText(QCoreApplication.translate("MainWindow", u"Grado", None))
        self.CB_Grado.setItemText(0, "")
        self.CB_Grado.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.CB_Grado.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.CB_Grado.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.CB_Grado.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.CB_Grado.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.CB_Grado.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.CB_Grado.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.CB_Grado.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))

        self.Lb_Grupo.setText(QCoreApplication.translate("MainWindow", u"Grupo", None))
        self.CB_Grupo.setItemText(0, "")
        self.CB_Grupo.setItemText(1, QCoreApplication.translate("MainWindow", u"A", None))
        self.CB_Grupo.setItemText(2, QCoreApplication.translate("MainWindow", u"B", None))

        self.Lb_Turno.setText(QCoreApplication.translate("MainWindow", u"Turno", None))
        self.CB_Turno.setItemText(0, "")
        self.CB_Turno.setItemText(1, QCoreApplication.translate("MainWindow", u"Matutino", None))
        self.CB_Turno.setItemText(2, QCoreApplication.translate("MainWindow", u"Vespertino", None))

        self.Bt_CrearGrupo.setText(QCoreApplication.translate("MainWindow", u"Ingresar Datos", None))
        self.Lbl_ErrorDatosCurso.setText("")
    # retranslateUi

