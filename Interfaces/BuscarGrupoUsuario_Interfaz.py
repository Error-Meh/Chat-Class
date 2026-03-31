# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BuscarbiMVWA.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QStackedWidget, QWidget)

class Ui_Buscar(object):
    def setupUi(self, Buscar):
        if not Buscar.objectName():
            Buscar.setObjectName(u"Buscar")
        Buscar.resize(500, 300)
        Buscar.setMinimumSize(QSize(500, 300))
        Buscar.setMaximumSize(QSize(500, 300))
        self.StackBuscar = QStackedWidget(Buscar)
        self.StackBuscar.setObjectName(u"StackBuscar")
        self.StackBuscar.setGeometry(QRect(0, 0, 500, 300))
        self.StackBuscar.setMaximumSize(QSize(500, 300))
        self.StackBuscar.setStyleSheet(u"background-color: rgb(18, 18, 18);")
        self.Pag0 = QWidget()
        self.Pag0.setObjectName(u"Pag0")
        self.Lb_Cod = QLabel(self.Pag0)
        self.Lb_Cod.setObjectName(u"Lb_Cod")
        self.Lb_Cod.setGeometry(QRect(50, 30, 411, 51))
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(16)
        self.Lb_Cod.setFont(font)
        self.Lb_Cod.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LE_CodigoBuscar = QLineEdit(self.Pag0)
        self.LE_CodigoBuscar.setObjectName(u"LE_CodigoBuscar")
        self.LE_CodigoBuscar.setGeometry(QRect(130, 110, 251, 41))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(14)
        self.LE_CodigoBuscar.setFont(font1)
        self.LE_CodigoBuscar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.LE_CodigoBuscar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Lb_ErrorCod = QLabel(self.Pag0)
        self.Lb_ErrorCod.setObjectName(u"Lb_ErrorCod")
        self.Lb_ErrorCod.setGeometry(QRect(70, 180, 371, 31))
        font2 = QFont()
        font2.setFamilies([u"Terminal"])
        font2.setPointSize(11)
        self.Lb_ErrorCod.setFont(font2)
        self.Lb_ErrorCod.setStyleSheet(u"color: rgb(249, 44, 47);")
        self.Bt_BuscarUs = QPushButton(self.Pag0)
        self.Bt_BuscarUs.setObjectName(u"Bt_BuscarUs")
        self.Bt_BuscarUs.setGeometry(QRect(190, 230, 131, 41))
        font3 = QFont()
        font3.setFamilies([u"Bahnschrift"])
        font3.setPointSize(12)
        self.Bt_BuscarUs.setFont(font3)
        self.Bt_BuscarUs.setStyleSheet(u"background-color: rgb(158, 158, 158);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.StackBuscar.addWidget(self.Pag0)
        self.Pag1 = QWidget()
        self.Pag1.setObjectName(u"Pag1")
        self.Lb_CodGru = QLabel(self.Pag1)
        self.Lb_CodGru.setObjectName(u"Lb_CodGru")
        self.Lb_CodGru.setGeometry(QRect(90, 40, 311, 51))
        self.Lb_CodGru.setFont(font)
        self.Lb_CodGru.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LE_CodigoBuscarG = QLineEdit(self.Pag1)
        self.LE_CodigoBuscarG.setObjectName(u"LE_CodigoBuscarG")
        self.LE_CodigoBuscarG.setGeometry(QRect(120, 105, 251, 41))
        self.LE_CodigoBuscarG.setFont(font1)
        self.LE_CodigoBuscarG.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.LE_CodigoBuscarG.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Lb_ErrorCodG = QLabel(self.Pag1)
        self.Lb_ErrorCodG.setObjectName(u"Lb_ErrorCodG")
        self.Lb_ErrorCodG.setGeometry(QRect(70, 170, 371, 31))
        self.Lb_ErrorCodG.setFont(font2)
        self.Lb_ErrorCodG.setStyleSheet(u"color: rgb(249, 44, 47);")
        self.Bt_BuscarGr = QPushButton(self.Pag1)
        self.Bt_BuscarGr.setObjectName(u"Bt_BuscarGr")
        self.Bt_BuscarGr.setGeometry(QRect(170, 230, 131, 41))
        self.Bt_BuscarGr.setFont(font3)
        self.Bt_BuscarGr.setStyleSheet(u"background-color: rgb(158, 158, 158);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.StackBuscar.addWidget(self.Pag1)

        self.retranslateUi(Buscar)

        self.StackBuscar.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Buscar)
    # setupUi

    def retranslateUi(self, Buscar):
        Buscar.setWindowTitle(QCoreApplication.translate("Buscar", u"Dialog", None))
        self.Lb_Cod.setText(QCoreApplication.translate("Buscar", u"Ingresa el codigo de quien deseas buscar", None))
        self.LE_CodigoBuscar.setText("")
        self.Lb_ErrorCod.setText("")
        self.Bt_BuscarUs.setText(QCoreApplication.translate("Buscar", u"Buscar usuario", None))
        self.Lb_CodGru.setText(QCoreApplication.translate("Buscar", u"Ingrese el codigo del grupo", None))
        self.LE_CodigoBuscarG.setText("")
        self.Lb_ErrorCodG.setText("")
        self.Bt_BuscarGr.setText(QCoreApplication.translate("Buscar", u"Buscar Grupo", None))
    # retranslateUi