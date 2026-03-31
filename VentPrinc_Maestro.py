from EnviarMensaje import EnviarMensajes
from CambCont import CambiarCont
from ChatPrivado import ChatPrivado
from CrearGrupos import ManejoDeGrupos
from Conexion import *

from Interfaces.CrearBorrarGru_Interfaz import Ui_OpcionesPrf
from Interfaces.VentPrinc_Maestro_interfaz import *
from Interfaces.BuscarGrupoUsuario_Interfaz import *

from asyncio.windows_events import NULL
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton, QApplication, QLineEdit, QLabel, QDialog, QMainWindow, QFrame, QSizePolicy, QHBoxLayout, QWidget
from PySide6.QtCore import QDateTime, QTimer, Qt
import sys
import string
import random
import webbrowser
import mysql.connector

NomMat = NULL
Grad = NULL
Grup = NULL
Turn = NULL
Carr = NULL

class Ini(QMainWindow):
    def __init__(self, CodUser, RolUser, NomUser, ApellUser, CorreoUser):
        super(Ini, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.setWindowFlags(Qt.FramelessWindowHint)  # type: ignore # Esto oculta la barra de título
        self.setAttribute(Qt.WA_TranslucentBackground, True) # type: ignore

    #Botones Cerrar, mininzar, maximizar, y achicar
        self.ui.Bt_Cerrar.clicked.connect(self.close)
        self.ui.Bt_Minizar.clicked.connect(self.showMinimized)
        self.ui.Bt_Maximizar.clicked.connect(self.toggle_max_restore)

        self.MensajeEnviar = EnviarMensajes()
        self.CambiarCon = CambiarCont()
        self.ChPriv = ChatPrivado()
        
    #esconder boton inecesario
        self.ui.Bt_BuscarGrupo.hide()
        self.ui.Bt_Regresar.hide()
        self.ui.Bt_CargarChats.hide()

        self.CodUser = str(CodUser)
        self.RolUser = RolUser
        self.NomUser = NomUser
        self.ApellUser = ApellUser
        self.CorreoUser = CorreoUser
        
        self.MenGrup = None
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_mensajes)
        self.timer.start(1000)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.CargarGrupo)
        self.timer.start(1000)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.CargarChats)
        self.timer.start(1000)

        self.ui.Bt_VerCont.setCheckable(True)
        self.ui.Bt_VerCont_2.setCheckable(True)
        self.ui.Bt_VerCont_3.setCheckable(True)

        # Spacer para empujar mensajes hacia arriba
        self.spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding) # type: ignore
        self.ui.verticalLayout_9.addItem(self.spacer)

        
        # Cargar Chats y Grupos
        self.CargarGrupo()
        self.CargarChats()
    
    #Botones de mostrar y ocultar contraseña
        self.ui.Bt_VerCont.setIcon(QIcon("Imagenes/mostrar.png"))
        self.ui.Bt_VerCont.setIconSize(QSize(50,50))

        self.ui.Bt_VerCont_2.setIcon(QIcon("Imagenes/mostrar.png"))
        self.ui.Bt_VerCont_2.setIconSize(QSize(50,50))
        
        self.ui.Bt_VerCont_3.setIcon(QIcon("Imagenes/mostrar.png"))
        self.ui.Bt_VerCont_3.setIconSize(QSize(50,50))


        self.ui.Bt_VerCont.clicked.connect(self.CamIcoMosCont)
        self.ui.Bt_VerCont_2.clicked.connect(self.CamIcoMosCont)
        self.ui.Bt_VerCont_3.clicked.connect(self.CamIcoMosCont)

    # Botones para retroceder en Ajustes
        self.ui.Bt_Regresar.clicked.connect(self.RegresarGrupos)

    # Botones para cambiar entre los ajustes 
        self.ui.Bt_Ajustes.clicked.connect(self.CamA_Ajustes)
        self.ui.Bt_Perfil.clicked.connect(self.CamAjustes_Perfil)


    # Botones para cambiar entre el chat y los grupos
        self.ui.Bt_IrChatPriv.clicked.connect(self.CamChatPriv)
        self.ui.Bt_IrGrupos_2.clicked.connect(self.CamChatA_Grupo)

    # Botones para cambiar entre los chats
        self.ui.Bt_ChatAvisos.clicked.connect(self.ChatAvisos)
        self.ui.Bt_ChatGeneral.clicked.connect(self.ChatGeneral)
        self.ui.Bt_ChatFueraDelTema.clicked.connect(self.ChatFuera)

    # Boton para crear grupos
        self.ui.Bt_MasOpciones.clicked.connect(self.VentCrearGrup)
    #
        self.ui.Bt_Confirm.clicked.connect(self.CamCont)
    #
        self.ui.Bt_Enviar.clicked.connect(self.EnvMen)
        self.ui.LE_Mensaje.returnPressed.connect(self.EnvMen) 

        self.ui.Bt_CondPolit.clicked.connect(self.AbrirCondiciones)
        self.ui.Bt_PregFrec.clicked.connect(self.AbrirPregFrec)
        self.ui.Bt_Soporte.clicked.connect(self.AbrirSoporte) 

    #
        self.ui.Bt_CargarChats.clicked.connect(self.ObtenerChats)

    #
        self.ui.Bt_BuscarChats.clicked.connect(self.BuscarUsuario)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.ui.Frm_1Superior.underMouse(): # type: ignore
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.ui.Frm_1Superior.underMouse(): # type: ignore
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()

# Maximizar y Minizar la ventana    
    def toggle_max_restore(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def CamA_Ajustes(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.Bt_Ajustes.hide()
        self.ui.Bt_Regresar.show()

# Cambiar entre las interfaces 
    def RegresarGrupos(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.Lb_ErrorContActu.setText("")
        self.ui.Lb_ErrorConfirmCont.setText("")

        self.ui.Tf_ContActual.setText("")
        self.ui.Tf_NuevCont.setText("")
        self.ui.Tf_ConfirmCont.setText("")
        self.ui.Bt_Ajustes.show()
        self.ui.Bt_Perfil.show()
        self.ui.Bt_Regresar.hide()

    def CamAjustes_Perfil(self):
        self.ui.Lb_Rol_Puesto.setText(self.RolUser)
        self.ui.Lb_Codigo_Puesto.setText(self.CodUser)
        self.ui.Lb_Nomb_Puesto.setText(self.NomUser)
        self.ui.Lb_Apellido_Puesto.setText(self.ApellUser)
        self.ui.Lb_Correo_Puesto.setText(self.CorreoUser)
        self.ui.Bt_Ajustes.hide()
        self.ui.Bt_Perfil.hide()

        self.ui.Bt_Regresar.show()

        self.ui.stackedWidget.setCurrentIndex(3)

    def AbrirCondiciones(self):
        webbrowser.open("https://sites.google.com/alumnos.udg.mx/chatclass-preguntasfrecuentes/terminos-y-condiciones?authuser=0")

    def AbrirPregFrec(self):
        webbrowser.open("https://sites.google.com/alumnos.udg.mx/chatclass-preguntasfrecuentes/inicio")

    def AbrirSoporte(self):
        webbrowser.open("https://sites.google.com/alumnos.udg.mx/chatclass-preguntasfrecuentes/soporte?authuser=0")
    
# Mostrar la ventana emergente de Crear Grupos y Buscar Usuario (Chat Privado)
    def VentCrearGrup(self):
        self.Vent = VentCrearGrup(self.CodUser, self.NomUser, self.ApellUser)

    def BuscarUsuario(self):
        self.Vent = BuscarUsuario(self.CodUser)

    def CamChatA_Grupo(self):
        self.ui.stackedWidget.setCurrentIndex(0)


    def CamChatPriv(self):
        self.ui.stackedWidget.setCurrentIndex(2)

# Cambiar entre los chats    
    def ChatAvisos(self):
            self.ui.stackedWidget_2.setCurrentIndex(1)
            self.ui.Lb_NombreCanal.setText("Avisos")
            self.cargar_mensajes("01")
            
    def ChatGeneral(self):
            self.ui.stackedWidget_2.setCurrentIndex(1)
            self.ui.Lb_NombreCanal.setText("Chat General")
            self.cargar_mensajes("02")
            
    def ChatFuera(self):
            self.ui.stackedWidget_2.setCurrentIndex(1)
            self.ui.Lb_NombreCanal.setText("Fuera del Tema")
            self.cargar_mensajes("03")

# Generar Codigo
    def generar_codigo(self):
        longitud = 6
        caracteres = string.digits 
        codigo = ''.join(random.choice(caracteres) for _ in range(longitud))
        return codigo
    
    def crear_burbuja_mensaje(self, mensaje, tipo, emisor=None, fecha=None):
        contenedor = QWidget()
        layout_contenedor = QHBoxLayout(contenedor)
        layout_contenedor.setContentsMargins(5, 2, 5, 2)
        layout_contenedor.setSpacing(0)

        burbuja = QWidget()
        burbuja.setStyleSheet(f"""
            background: none;
            background-color: {'#DCF8C6' if tipo == 'enviado' else '#FFFFFF'};
            border-radius: 15px;
        """)
        burbuja.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum) # type: ignore

        layout_burbuja = QVBoxLayout(burbuja)
        layout_burbuja.setContentsMargins(12, 8, 12, 8)
        layout_burbuja.setSpacing(4)

        # Agregar encabezado con nombre y fecha SOLO si es grupo y mensaje recibido
        if self.MenGrup == 1 and tipo == "recibido" and emisor and fecha:
            encabezado = QWidget()
            layout_encabezado = QHBoxLayout(encabezado)
            layout_encabezado.setContentsMargins(0, 0, 0, 0)
            layout_encabezado.setSpacing(6)

            L_emisor = QLabel(emisor)
            L_emisor.setStyleSheet("font-weight: bold; font-size: 11px; color: #1A73E8;")

            L_fecha = QLabel(fecha)
            L_fecha.setStyleSheet("font-size: 10px; color: gray;")

            layout_encabezado.addWidget(L_emisor)
            layout_encabezado.addWidget(L_fecha)
            layout_encabezado.addStretch()

            layout_burbuja.addWidget(encabezado)

        elif tipo == "enviado" and fecha:
            L_fecha = QLabel(fecha)
            L_fecha.setStyleSheet("font-size: 10px; color: gray;")
            L_fecha.setAlignment(Qt.AlignRight) # type: ignore
            layout_burbuja.addWidget(L_fecha)
        
        elif self.MenGrup == 0 and tipo == "recibido" and fecha:
            L_fecha = QLabel(fecha)
            L_fecha.setStyleSheet("font-size: 10px; color: gray;")
            L_fecha.setAlignment(Qt.AlignRight) # type: ignore
            layout_burbuja.addWidget(L_fecha)

        # Contenido del mensaje
        L_mensaje = QLabel(mensaje)
        L_mensaje.setWordWrap(True)
        L_mensaje.setMaximumWidth(300)
        L_mensaje.setStyleSheet("font-size: 13px; color: black;")
        layout_burbuja.addWidget(L_mensaje)

        # Alineación de la burbuja
        if tipo == "enviado":
            layout_contenedor.addStretch()
            layout_contenedor.addWidget(burbuja)
        else:
            layout_contenedor.addWidget(burbuja)
            layout_contenedor.addStretch()

        return contenedor


    
    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            elif child.layout():
                self.clear_layout(child.layout())

# Funcion de Enviar Mensajes
    def EnvMen(self):
        mensaje = self.ui.LE_Mensaje.text().strip()
        if mensaje:
            tipo = 'enviado'
            User = self.NomUser + " " + self.ApellUser
            fecha = QDateTime.currentDateTime().toString("yyyy/MM/dd hh:mm:ss")
            fecha_chida = QDateTime.currentDateTime().toString("dd/MM/yyyy hh:mm")
            
            
            # LIMPIA el input
            self.ui.LE_Mensaje.clear()

            # Quitar spacer
            self.ui.verticalLayout_9.removeItem(self.spacer)

            # Agregar mensaje
            layout_burbuja = self.crear_burbuja_mensaje(mensaje, tipo, User, fecha_chida)
            self.ui.verticalLayout_9.addWidget(layout_burbuja)

            # Volver a poner el spacer
            self.ui.verticalLayout_9.addItem(self.spacer)


            # ENVÍA el mensaje a la base de datos (grupo o privado)
            if self.MenGrup == 1:
                ChatAct = self.ui.Lb_NombreCanal.text()
                self.ChatIDs = {"Avisos": "01", "Chat General": "02", "Fuera del Tema": "03"} 
                Chat_ID = self.ChatIDs.get(ChatAct)

                if Chat_ID:
                    ID_Grupo = self.IDG
                    num_mensajes_enviados = self.MensajeEnviar.verificar_mensajes_enviados() 
                    if num_mensajes_enviados is not None:
                        id_mensaje = f"{num_mensajes_enviados + 1:05d}"
                        self.MensajeEnviar.EnvMensaje(ID_Grupo, Chat_ID, id_mensaje, mensaje, User, fecha)

            if self.MenGrup == 0:
                Chat_ID = self.ObtIDChat()
                if Chat_ID:
                    num_mensajes_enviados = self.ChPriv.verificar_mensajes_enviados_Chats() 
                    if num_mensajes_enviados is not None:
                        id_mensaje = f"{num_mensajes_enviados + 1:05d}"
                        self.ChPriv.EnvMenChatPriv(Chat_ID, id_mensaje, mensaje, User, fecha)


 # Cargar Mensajes 
    def cargar_mensajes(self, ID_Chat):
        while self.ui.verticalLayout_9.count() > 0:
            item = self.ui.verticalLayout_9.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                self.clear_layout(item.layout())

        if self.MenGrup == 1:
            try:
                IdGrup = self.IDG
                mensajes = self.MensajeEnviar.obtener_mensajes(ID_Chat, IdGrup)
                fechachida = QDateTime.currentDateTime().toString("dd/MM/yyyy hh:mm")
                for emisor, mensaje in mensajes: # type: ignore
                    tipo = "enviado" if emisor == f"{self.NomUser} {self.ApellUser}" else "recibido"
                    # Quitar spacer
                    self.ui.verticalLayout_9.removeItem(self.spacer)

                    # Agregar mensaje
                    layout_burbuja = self.crear_burbuja_mensaje(mensaje, tipo, emisor, fechachida)
                    self.ui.verticalLayout_9.addWidget(layout_burbuja)

                    # Volver a poner el spacer
                    self.ui.verticalLayout_9.addItem(self.spacer)
            except TypeError:
                pass

        elif self.MenGrup == 0:
            try:
                Chat_ID = self.ObtIDChat()
                mensajes = self.ChPriv.ObtenerMensajesPriv(Chat_ID)
                fechachida = QDateTime.currentDateTime().toString("dd/MM/yyyy hh:mm")
                for emisor, mensaje in mensajes: # type: ignore
                    tipo = "enviado" if emisor == f"{self.NomUser} {self.ApellUser}" else "recibido"
                    self.ui.verticalLayout_9.removeItem(self.spacer)

                    layout_burbuja = self.crear_burbuja_mensaje(mensaje, tipo, emisor, fechachida)
                    self.ui.verticalLayout_9.addWidget(layout_burbuja)

                    self.ui.verticalLayout_9.addItem(self.spacer)
            except TypeError:
                pass



#Cambia los mensajes  al cambiar de chat
    def IrACanales(self, NomGrup,IdGru):
        self.MenGrup = 1
        ID = IdGru.split(" ")
        self.IDG = ID[3]
        self.ui.Lb_NombreMat.setText(NomGrup)
        self.ui.Lb_NombreCanal.setText("")
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.Bt_Regresar.show()
        self.actualizar_mensajes()


    def actualizar_mensajes(self):
        if self.MenGrup == 1:  # Si estás en un grupo
            ChatAct = self.ui.Lb_NombreCanal.text()
            self.ChatIDs = {"Avisos": "01", "Chat General": "02", "Fuera del Tema": "03"} 
            Chat_ID = self.ChatIDs.get(ChatAct)
            if Chat_ID:
                self.cargar_mensajes(Chat_ID)
        elif self.MenGrup == 0:  # Si estás en un chat privado
            Chat_ID = self.ObtIDChat()
            if Chat_ID:
                self.cargar_mensajes(Chat_ID)

#Crear los botones de los grupos
    def CargarGrupo(self):
        try:
            Coduser = self.CodUser
            grupos,CodGrup = self.ObtenerGrupos(Coduser)

            # Coordenadas iniciales para colocar los botones
            x, y = 70, 20  
            espacio_vertical = 190

            num_grupos = len(grupos) # type: ignore

            # Calcular la altura necesaria para Frm_Grupos dependiendo del número de botones
            altura_necesaria = num_grupos * espacio_vertical + 10
            self.ui.Frm_Grupos.setMinimumHeight(altura_necesaria)
            
            Datos = []

            C = CodGrup.split('.') # type: ignore
            for n in range(num_grupos):
                Datos.append(grupos[n] + "\nCodigo del grupo: " + C[n]) # type: ignore

            # Agregar botones de grupos
            for dat in Datos:
                nombre_grupo = dat.split("\n")[0]
                id_grupo = dat.split("\n")[1]
                label = QLabel(dat, self.ui.Frm_Grupos)
                label.setGeometry(x, y, 600, 130)
                label.setStyleSheet("""
                                    QLabel{
                                        color: #000000;
                                        background-color: #9e9e9e;
                                        font: 700 18pt "Arial Narrow";
                                        border: 5px solid #000000;
                                        border-radius: 16px;
                                        text-align: left;
                                        padding-left: 50px;
                                    }
                                    QLabel:hover{
                                        background-color: #424242;
                                        color: #FFFFFF
                                    }
                                    """)
                label.mousePressEvent = lambda event, nombre_grupo=nombre_grupo, id_grupo=id_grupo: self.IrACanales(nombre_grupo,id_grupo) # type: ignore
                label.setWordWrap(True)
                label.setMinimumHeight(60)
                label.show()
                y += espacio_vertical

            # Actualizar la interfaz
            self.ui.scrollAreaWidgetContents.setMinimumHeight(altura_necesaria)
            self.ui.scrollAreaWidgetContents.update()
        except:
            pass

    def ObtenerGrupos(self, Coduser):
            self.conexion = mysql.connector.connect(
            host="127.0.0.1",
            database="chatclass",
            user="root",
            password=""
            )
        
            try:
                cur = self.conexion.cursor()
                
                sql = "SELECT  	ID_GruposM FROM maestro WHERE CodigoM = %s"
                cur.execute(sql, (Coduser,))
                res = cur.fetchone()
                
                if res is None:
                    return None, None
                
                resul = res[0]
                cod = tuple(resul.split('.'))
                
                ListDat = []
                
                for Codi in cod:
                    sql = "SELECT NombreMateria FROM `{}`".format(Codi)
                    cur.execute(sql)
                    datos = cur.fetchall()
                    
                    
                    if datos:
                        D = list(datos[0])
                        DI = D[0].split(',')
                        ListDat.append(DI[0])
                
                cur.close()
                self.conexion.close()
                DatosBT = tuple(ListDat) if ListDat else ()
                
                
                return DatosBT, resul
            
            except:
                cur.close()
                return None, None
            
            finally:
                if self.conexion.is_connected():
                    self.conexion.close()

    def CargarChats(self):
        try:
            ListNomChat, ListCodChat = self.ObtenerChats() # type: ignore

            x, y = 150, 20 
            espacio_vertical = 150

            num_Chats = len(ListCodChat) # type: ignore

            altura_necesaria = num_Chats * espacio_vertical + 10
            self.ui.Frm_MenPriv.setMinimumHeight(altura_necesaria)

            Datos = []
            for n in range(num_Chats):
                Datos.append(ListNomChat[n] + "\nCodigo del Chat: " + ListCodChat[n]) # type: ignore
                
            for dat in Datos:
                nombre_chat = dat.split("\n")[0]
                id_chat = dat.split("\n")[1]
                MosID = ListCodChat[n] # type: ignore
                label = QLabel(dat, self.ui.Frm_MenPriv)
                label.setGeometry(x, y, 390, 80)
                label.setStyleSheet("""
                                    QLabel{
                                        color: #000000;
                                        background-color: #9e9e9e;
                                        font: 700 16pt "Arial Narrow";
                                        border: 5px solid #000000;
                                        border-radius: 16px;
                                        text-align: left;
                                        padding-left: 70px;
                                    }
                                    QLabel:hover{   
                                        background-color: #424242;
                                    }
                                    """)
                label.mousePressEvent = lambda event, nombre_chat=nombre_chat, id_chat=id_chat: self.CamChat(nombre_chat,id_chat) # type: ignore
                label.setWordWrap(True)
                label.setMinimumHeight(60)
                label.show()
                y += espacio_vertical

            self.ui.scrollAreaWidgetContents_2.setMinimumHeight(altura_necesaria)
            self.ui.scrollAreaWidgetContents_2.update()
        except:
            pass


    def CamChat(self,nombre_chat,id_chat):
        self.MenGrup = 0
        self.Id_Chat = id_chat
        self.ui.stackedWidget_2.setCurrentIndex(1)
        self.ui.Lb_NombreMat.setText(nombre_chat)
        self.ui.Lb_NombreCanal.setText(id_chat)
        self.cargar_mensajes(id_chat)

    def ObtIDChat(self):
        ID = self.Id_Chat.split(": ")
        
        Idchat = ID[1]

        Derecho = self.CodUser + "-" + Idchat
        Reves = Idchat + "-" + self.CodUser

        IDS = self.CODIGS.split(",")
        Tam = len(IDS)
        for n in range(Tam):
            if Derecho in IDS[n] or Reves in IDS[n]:
                Id_Canal = IDS[n]
                return Id_Canal

#Obtiene los nombres de los 
    def ObtenerChats(self):
        self.conexion = mysql.connector.connect(
            host="127.0.0.1",
            database="chatclass",
            user="root",
            password=""
            )

        cur = self.conexion.cursor()
        try:
            sql = "SELECT ChatsPrivM FROM maestro WHERE CodigoM = %s"
            cur.execute(sql, (self.CodUser,))
            res = cur.fetchone()
                    
            if res is None:
                return None, None
            
            resul = res[0]
            self.CODIGS = resul
            pares = resul.split(',')
            COD = [codigo for par in pares for codigo in par.split('-')]
            CodsChats = []
            Lon = len(COD)

            for n in range(Lon):
                if self.CodUser == COD[n]:
                    pass
                else:
                    CodsChats.append(COD[n])
            cur.close()
            self.conexion.close()
            return self.ChPriv.BusNomUsuario(CodsChats), CodsChats
        except:
            cur.close()
            self.conexion.close()

#Cambiar la contraseña del usuario
    def CamCont(self):
        self.ui.Lb_ErrorContActu.setText("")
        self.ui.Lb_ErrorConfirmCont.setText("")

        ContAct = self.ui.Tf_ContActual.text().strip()
        NCont = self.ui.Tf_NuevCont.text().strip()
        ConCont = self.ui.Tf_ConfirmCont.text().strip()
        

        # Buscar la contraseña actual en la base de datos
        stored_password = self.CambiarCon.BuscarCont_Maes(ContAct)

        if stored_password is None:
            self.ui.Lb_ErrorContActu.setText("La Contraseña no coindcide")
        else:
            if len(NCont) < 8 or len(NCont) > 16:
                self.ui.Lb_ErrorConfirmCont.setText("Contraseña corta. Debe ser mayor a 8")
            else:
                if NCont != ConCont:
                    self.ui.Lb_ErrorConfirmCont.setText("Las nuevas contraseñas no coinciden.")
                else:
                # Aquí se actualiza la contraseña en la base de datos
                    self.ui.Tf_ContActual.clear()
                    self.ui.Tf_NuevCont.clear()
                    self.ui.Tf_ConfirmCont.clear()
                    self.CambiarCon.ActualizarContMaes(NCont, self.CodUser)
                    self.ui.Lb_ErrorConfirmCont.setText("Contraseña actualizada con éxito.")


    def CamIcoMosCont(self):
        # Contraseña Antigua
            if self.ui.Bt_VerCont.isChecked():
                self.ui.Tf_ContActual.setEchoMode(QLineEdit.EchoMode.Normal)
                self.ui.Bt_VerCont.setIcon(QIcon("Imagenes/esconder.png"))
            else:
                self.ui.Tf_ContActual.setEchoMode(QLineEdit.EchoMode.Password)
                self.ui.Bt_VerCont.setIcon(QIcon("Imagenes/mostrar.png"))

        # Nueva Contraseña
            if self.ui.Bt_VerCont_2.isChecked():
                self.ui.Tf_NuevCont.setEchoMode(QLineEdit.EchoMode.Normal)
                self.ui.Bt_VerCont_2.setIcon(QIcon("Imagenes/esconder.png"))
            else:
                self.ui.Tf_NuevCont.setEchoMode(QLineEdit.EchoMode.Password)
                self.ui.Bt_VerCont_2.setIcon(QIcon("Imagenes/mostrar.png"))
        # Confirmar nueva contraseña
            if self.ui.Bt_VerCont_3.isChecked():
                self.ui.Tf_ConfirmCont.setEchoMode(QLineEdit.EchoMode.Normal)
                self.ui.Bt_VerCont_3.setIcon(QIcon("Imagenes/esconder.png"))            
            else:
                self.ui.Tf_ConfirmCont.setEchoMode(QLineEdit.EchoMode.Password)
                self.ui.Bt_VerCont_3.setIcon(QIcon("Imagenes/mostrar.png"))


class BuscarUsuario(QMainWindow):

    def __init__(self, CodUser):
        super(Ui_Buscar).__init__()
        self.dialogo =QDialog()
        self.ui = Ui_Buscar()
        self.ui.setupUi(self.dialogo)

        self.ui.StackBuscar.setCurrentIndex(0)
        
        self.CodUserX = CodUser

        self.ChPriv = ChatPrivado()

        self.ui.Bt_BuscarUs.clicked.connect(self.ObtenerDatosP)

        self.dialogo.exec()

    def ObtenerDatosP(self):
        self.ui.Lb_ErrorCod.setText("")
        CodBusc = self.ui.LE_CodigoBuscar.text()
        if not CodBusc == self.CodUserX:
            if CodBusc.isdigit():
                if len(CodBusc) == 7:
                    CodObt = str(self.ChPriv.VerificarMaestro(CodBusc))
                    CodJ = self.CodUserX+"-"+CodObt
                    if not self.ChPriv.VerifChatPrEx(CodObt, self.CodUserX, CodJ) == 0:
                        self.ChPriv.ActuEmisor(CodJ, self.CodUserX)
                        self.ChPriv.ActuReceptor(CodJ, CodObt)
                    self.dialogo.accept()
                elif len(CodBusc) == 9:
                    CodObt = str(self.ChPriv.VerificarALumno(CodBusc))
                    CodJ = self.CodUserX+"-"+CodObt
                    if not self.ChPriv.VerifChatPrEx(CodObt, self.CodUserX, CodJ) == 0:
                        self.ChPriv.ActuEmisor(CodJ, self.CodUserX)
                        self.ChPriv.ActuReceptor(CodJ, CodObt)
                    self.dialogo.accept()

                else:
                    self.ui.Lb_ErrorCod.setText("El código ingresado\nno existe")
            else:
                self.ui.Lb_ErrorCod.setText("El texto ingresado contiene \nletras")
        else:
            self.ui.Lb_ErrorCod.setText("No puedes buscar tu\npropio código")


#Ventana de Crear Grupos
class VentCrearGrup(QMainWindow):
    def __init__(self, CodUser, NomUser, ApellUser):
        super(VentCrearGrup, self).__init__()
        self.dialogo = QDialog()
        self.ui = Ui_OpcionesPrf()
        self.ui.setupUi(self.dialogo)
        self.dialogo.setWindowTitle("Crear/Borrar Grupo")

        self.NomUser = NomUser
        self.ApellUser = ApellUser
        self.CodUserX = CodUser

        RolUser = None
        CorreoUser = None

        self.ui.Bt_crear.clicked.connect(self.cambiarCrearG)
        self.ui.Bt_CrearGrupo.clicked.connect(self.ObtenerDatos)
        self.ui.Bt_borrar.clicked.connect(self.cambiarBorrarG)

        self.ui.Bt_BorrarGrupo.clicked.connect(self.obtener_grupos_seleccionados)

        self.crear = ManejoDeGrupos()
        
        self.VenPr = Ini(CodUser, RolUser, NomUser, ApellUser, CorreoUser)

        self.dialogo.exec()

    # --------------------------- Funciones para crear grupo ----------------------------------------

    def cambiarCrearG(self):
        self.dialogo.resize(600, 360)
        self.ui.stackedWidget.setCurrentIndex(1)

    def cambiarBorrarG(self):
        self.dialogo.resize(480, 480)
        self.ui.stackedWidget.setCurrentIndex(2)
        self.Borrar_grupos()

    def generar_codigo(self):
        longitud = 6
        signos = "#!%*"
        caracteres = string.ascii_letters + string.digits + signos * 4 +  "#!%*" * 1
        codigo = ''.join(random.choice(caracteres) for _ in range(longitud))
        return codigo

    def ObtenerDatos(self):
        self.ui.Lb_Error.setText("")

        NomMat = self.ui.LE_Nombregrup.text()
        Grad = self.ui.Cb_Grado.currentText()
        if self.ui.Rb_GA.isChecked():
            Grup = "A"
        elif self.ui.Rb_GB.isChecked():
            Grup = "B"
        Turn = self.ui.Cb_Turno.currentText()


        Nomtabla = self.generar_codigo()

        NomTabla = Nomtabla.lower()


        if NomMat == "" and len(NomMat) == 0:
            self.ui.Lb_Error.setText("Falta llenar algun campo")
        else:
            if len(Grad) == 0 or len(Grup) == 0 or len(Turn) == 0:
                self.ui.Lb_Error.setText("Falta llenar algun campo")
            else:
                integ = self.NomUser + " " + self.ApellUser
                CodInteg = self.CodUserX
                self.crear.CrearReg(NomTabla)
                self.crear.InsertPart(NomTabla,NomMat,Grad,Grup,Turn,integ, CodInteg)
                self.crear.ActualizarMaest(CodInteg,NomTabla)
                self.dialogo.accept()


    # -----------------  Funciones para borrar grupos  --------------------------------------------------

    def Borrar_grupos(self):
        Coduser = self.CodUserX
        grupos, CodGrup = self.VenPr.ObtenerGrupos(Coduser)
        if grupos:

            self.Lb_Select = None

            gruposList = list(grupos)
            x, y = 50, 20
            espacio_vertical = 100
            num_grupos = len(grupos)

            altura_necesaria = num_grupos * espacio_vertical + 10
            self.ui.scrollAreaWidgetContents.setMinimumHeight(altura_necesaria)

            Datos = []
            C = CodGrup.split('.') # type: ignore
            for n in range(num_grupos):
                Datos.append(grupos[n] + "\nCodigo del grupo: " + C[n])

            for dat in Datos:
                label = QLabel(dat, self.ui.scrollAreaWidgetContents)
                label.setGeometry(x, y, 320, 80)
                label.setStyleSheet("""
                    QLabel {
                        color: #000000;
                        background-color: #9e9e9e;
                        font: 700 16pt "Arial Narrow";
                        border: 5px solid #000000;
                        text-align: left;
                        padding-left: 15px;
                    }
                    QLabel:hover {
                        background-color: #424242;
                        color: #FFFFFF;
                    }
                """)

                def toggle_unico(lbl):
                    # Si ya hay uno seleccionado, lo deseleccionamos
                    if self.Lb_Select and self.Lb_Select != lbl:
                        self.Lb_Select.setStyleSheet("""
                            QLabel {
                                color: #000000;
                                background-color: #9e9e9e;
                                font: 700 16pt "Arial Narrow";
                                border: 5px solid #000000;
                                text-align: left;
                                padding-left: 15px;
                            }
                            QLabel:hover {
                                background-color: #424242;
                                color: #FFFFFF;
                            }
                        """)
                    # Marcar como seleccionado el nuevo
                    self.Lb_Select = lbl
                    lbl.setStyleSheet("""
                        QLabel {
                            background-color: #fe6f71;
                            color: white;
                            font: 700 16pt "Arial Narrow";
                            border: 5px solid #000000;
                            text-align: left;
                            padding-left: 15px;
                        }
                    """)
                label.mousePressEvent = lambda event, lbl=label: toggle_unico(lbl) # type: ignore
                label.setWordWrap(True)
                label.setMinimumHeight(60)
                label.show()
                y += espacio_vertical

            self.ui.scrollAreaWidgetContents.update()
        else:
            self.ui.LB_errorBR.setText("No hay grupo para borrar")


    def obtener_grupos_seleccionados(self):
        if self.Lb_Select:
            texto = self.Lb_Select.text()
            partes = texto.split("\n")
            if len(partes) == 2:
                nombre = partes[0].strip()
                codigo = partes[1].replace("Codigo del grupo:", "").strip()
                Codigos_Alum = self.crear.ObtenerAlumnosDelGrupo(codigo)
                self.crear.eliminarAlumnos(Codigos_Alum, codigo, self.CodUserX)
                self.VenPr.CargarGrupo()
                self.Borrar_grupos()
        self.dialogo.accept()

if __name__ == "__main__":

    CodUser = 123456789
    RolUser = "Rol"
    NomUser = "Nombre"
    ApellUser = "Apellido"
    CorreoUser = "Correo"

    app = QApplication(sys.argv)
    mi_app = Ini(CodUser, RolUser, NomUser, ApellUser, CorreoUser)   
    mi_app.show()
    sys.exit(app.exec())