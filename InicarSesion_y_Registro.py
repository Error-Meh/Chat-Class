#Aqui es el funcionamiento de Verificacion de Inicio de Sesion del Usuario [Alumno | Maestro]
#Verificar si el usario existe en la Base de Datos

import click
from Interfaces.Login_Interfaz import *
import Conexion
import sys
from VentPrinc_Maestro import Ini
from VentanaPrinc import VentAlum

class Iniciar(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        #Inizalizacion de las instacias para uso posterior
        self.Codigo = None
        self.Nom_entry = None
        self.Apell_entry = None
        self.correo_entry = None
        self.pass_entry = None


        # Declarar las funciones de los botones
        self.ui.Bt_InicarSesion.clicked.connect(self.iniciar_sesion)

        self.ui.Tf_Contrasena.returnPressed.connect(self.iniciar_sesion)
        
        self.ui.Bt_CrearCuenta.clicked.connect(self.CamReg)
        self.ui.Bt_Regist.clicked.connect(self.Reg)
        self.ui.Bt_InicioSesion.clicked.connect(self.CamRIn)
        self.ui.Bt_CrearGrupo.clicked.connect(self.DatosExtrasAl)

        self.ui.Bt_RegresarIni_Princ.clicked.connect(self.RegresarInicio)
        self.ui.Bt_RegresarIni_Princ_2.clicked.connect(self.RegresarInicio)

        # Crear una instancia de Conexion 
        self.datos = Conexion.RegistroDatos()


    def iniciar_sesion(self):
        try:
            self.ui.Lbl_ErrorEnInicioSesion.setText("")
            self.ui.Lbl_ErrorEnInicioSesion_2.setText("")

            # Obtener el texto Ingresado
            user_entry = self.ui.Tf_Codigo.text()
            pass_entry = self.ui.Tf_Contrasena.text()

            VerUser = str("'" + user_entry + "'")
            VerPass = str("'" + pass_entry + "'")

            # verificar si es Alumno o Maestro
            if len(user_entry) == 9:
                dato1 = self.datos.BuscarUser_Alum(VerUser)
                dato2 = self.datos.BuscarCont_Alum(VerPass)
            elif len(user_entry) == 7:
                dato1 = self.datos.BuscarUser_Maes(VerUser)
                dato2 = self.datos.BuscarCont_Maes(VerPass)
            else:
                self.ui.Lbl_ErrorEnInicioSesion.setText("Error con el Codigo")

            # Verificar si los datos de inicio de sesión son válidos
            if not dato1 or not dato2:
                self.ui.Lbl_ErrorEnInicioSesion.setText("Error con el Codigo o la Contraseña")
            else:
                if len(user_entry) == 9:
                    user_data = self.datos.iniciar_sesion(user_entry)
                    if user_data:
                        self.close()
                        CodUser, RolUser, NomUser, ApellUser, CorreoUser = user_data
                        self.VentanaAlum = VentAlum(CodUser, RolUser, NomUser, ApellUser, CorreoUser)
                        self.VentanaAlum.show()
                        

                elif len(user_entry) == 7:
                    user_data = self.datos.iniciar_sesion(user_entry)
                    if user_data:
                        self.close()
                        CodUser, RolUser, NomUser, ApellUser, CorreoUser = user_data
                        self.VentanaMaes = Ini(CodUser, RolUser, NomUser, ApellUser, CorreoUser)
                        self.VentanaMaes.show()
        except UnboundLocalError:
            self.ui.Lbl_ErrorEnInicioSesion.setText("Error con el Codigo o la Contraseña")


    #Verificar si el Correo coincide con el codigo
    def VerificarCor_YCod(self):
        correo = self.ui.CorreoIngr.text()
        cod = self.ui.CodigoIngr.text()

        # Obtener los últimos 4 dígitos del correo
        verCorA = correo.split('@')[0][-4:]
        
        # Obtener los últimos 4 dígitos del código
        verCodA = cod[-5:-1]

        # Obtener el dominio del correo electrónico
        dominio = correo.split('@')[-1]

        #verificacion de codigo de estudiante tenga 9 digitos 
        if verCorA == verCodA:
            if len(cod) == 9 and dominio == "alumnos.udg.mx":
                return True   
            #verificacion de codigo de maestro tenga 7 digitos  
            elif len(cod) == 7 and dominio == "academicos.udg.mx":
                return True
            else:
                return False
        else:
            return False      

    def Reg(self):
        self.ui.Lbl_ErrorRegistro.setText("")
        self.ui.Lbl_ErrorRegistro_2.setText("")
        self.ui.Lbl_ErrorRegistro_3.setText("")

        Codigo = self.ui.CodigoIngr.text()
        pass_entry = self.ui.ContrasenaIngr.text()
        passConfirm_entry = self.ui.ConfirmContrasena.text()
        correo_entry = self.ui.CorreoIngr.text()

        try:
            # Obtener el nombre, apellido y dominio del correo electrónico      
            nombre_apellido, dominio = correo_entry.split('@')

            # Obtener Nombre y Apellido por separado
            nombre, apellido = nombre_apellido.split('.')
            apellido = apellido[:-4]

            # Poner en mayúscula la primera letra
            Nom_entry = nombre.capitalize()
            Apell_entry = apellido.capitalize()

            #verificacion que en el nombre tenga un punto antes del @

            if nombre_apellido.count('.') > 1 or nombre_apellido.count('.') == 0:
                raise ValueError("Correo no aceptado")


            # Registrar Dominios
            dom = ["alumnos.udg.mx", "academicos.udg.mx"]

            #verificar si el dominio del correo es institucional 
            if dominio not in dom:
                raise ValueError("El Correo no es Institucional")



            #verificar si el codigo de alumno ya fue registrado 
            if len(Codigo) == 9:
                if not self.datos.VerificarCodEstud(Codigo):
                    self.ui.Lbl_ErrorRegistro.setText("Codigo ya registrado")
                    
                else:
                    if len(pass_entry) < 8 or len(pass_entry) > 16:
                        self.ui.Lbl_ErrorRegistro_2.setText("Contraseña demasiado corta o larga")
                        
                    else:
                        #verificar si la contraseña coincide con la hecha 
                        if pass_entry != passConfirm_entry:
                            self.ui.Lbl_ErrorRegistro_2.setText("La contraseña no coinside")
                            
                        else:
                            #Verifica que el correo no este ya registrado
                            if not self.datos.VerificarCorEstud(correo_entry):
                                self.ui.Lbl_ErrorRegistro_3.setText("Correo ya registrado")
                                
                            else:
                                #verificacion cuando ingrese un correo o codigo erroneo 
                                if not self.VerificarCor_YCod():
                                    self.ui.Lbl_ErrorRegistro_3.setText("El Correo o Codigo estan mal ingresados")
                                    
                                else:
                                    #Manda los datos para el ingreso a la tabla
                                    self.ui.stackedWidget.setCurrentIndex(1)
                                    self.Codigo = Codigo
                                    self.Nom_entry = Nom_entry
                                    self.Apell_entry = Apell_entry
                                    self.correo_entry = correo_entry
                                    self.pass_entry = pass_entry
                                    

            #verificacion de codigo de Profesores ya fue registrado
            elif len(Codigo) == 7:
                if not self.datos.VerificarCodMaest(Codigo):
                    self.ui.Lbl_ErrorRegistro.setText("Codigo ya registrado")
                else:
                    if len(pass_entry) < 8 or len(pass_entry) > 16:
                        self.ui.Lbl_ErrorRegistro_2.setText("Contraseña demasiado corta o larga")
                    else:
                    #verificar si la contraseña coincide con la hecha
                        if pass_entry != passConfirm_entry:
                            self.ui.Lbl_ErrorRegistro_2.setText("La contraseña no coinside")
                        else:
                            #Verifica que el correo sea institucional
                            if dominio not in dom:
                                self.ui.Lbl_ErrorRegistro_3.setText("El Correo no es Institucional")
                            else:
                                #Verifica que el correo no este ya registrado
                                if not self.datos.VerificarCorrMaest(correo_entry):
                                    self.ui.Lbl_ErrorRegistro_3.setText("Correo ya registrado")
                                else:
                                    #verificacion cuando ingrese un correo o codigo erroneo 
                                    if not self.VerificarCor_YCod():
                                        self.ui.Lbl_ErrorRegistro_3.setText("El Correo o Codigo estan mal ingresados")
                                    else:
                                        #Manda los datos para el ingreso a la tabla
                                        self.datos.RegistroDeDatosMaestro(Codigo,Nom_entry,Apell_entry,correo_entry,pass_entry)
                                        user_data = self.datos.iniciar_sesion(Codigo)
                                        if user_data:
                                            self.close() 
                                            CodUser, RolUser, NomUser, ApellUser, CorreoUser = user_data
                                            self.VentanaMaes = Ini(CodUser, RolUser, NomUser, ApellUser, CorreoUser)
                                            self.VentanaMaes.show()

            else:
                self.ui.Lbl_ErrorRegistro.setText("Codigo Ingresado Incorrecto")

        except ValueError as e:
                self.ui.Lbl_ErrorRegistro_3.setText("Faltan datos o algun dato es erroneo")


    def DatosExtrasAl(self):
        self.ui.Lbl_ErrorDatosCurso.setText("")
        if self.Codigo and self.Nom_entry and self.Apell_entry and self.correo_entry and self.pass_entry:
            Grad = self.ui.CB_Grado.currentText() 
            Grup = self.ui.CB_Grupo.currentText()
            Turn = self.ui.CB_Turno.currentText()
            if Grad == "":
                self.ui.Lbl_ErrorDatosCurso.setText("Falta seleccionar el Grado")
            elif Grup == "":
                self.ui.Lbl_ErrorDatosCurso.setText("Falta seleccionar el Grupo")
            elif Turn == "":
                self.ui.Lbl_ErrorDatosCurso.setText("Falta seleccionar el Turno")
            else:
                GradGrup = Grad + Grup
                self.datos.RegistroDeDatos(self.Codigo, self.Nom_entry, self.Apell_entry, self.correo_entry, self.pass_entry, GradGrup, Turn)
                user_data = self.datos.iniciar_sesion(self.Codigo)
                if user_data:
                    CodUser, RolUser, NomUser, ApellUser, CorreoUser = user_data
                    self.VentanaAlum = VentAlum(CodUser, RolUser, NomUser, ApellUser, CorreoUser)
                    self.VentanaAlum.show()                 
                    self.close()


    def CamReg(self):
        self.ui.StW_Prin.setCurrentIndex(2)

    def CamRIn(self):
        self.ui.StW_Prin.setCurrentIndex(1)

    def RegresarInicio(self):
        self.ui.StW_Prin.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = Iniciar()   
    mi_app.show()
    sys.exit(app.exec())