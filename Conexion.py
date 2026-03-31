"""
Conexion con la Base de datos.
Verificar el inicio de sesion.
Realizar e importar los datos a la Base de datos
"""

import mysql.connector
from Interfaces.Login_Interfaz import *


class RegistroDatos():

 #Realizar la conexion a la Base de datos
    def __init__(self):
        self.conexion = mysql.connector.connect( 
            host = "127.0.0.1",
            database = "chatclass",
            user = "root",
            password = ""
            )




 ################################################################
 # Buscar Codigo y Contraseña del Alumno para el Inicio de Sesion
 ###############################################################

    #Busca el codigo del alumno
    def BuscarUser_Alum(self, users):
        cur = self.conexion.cursor()
        try:
            sql = "SELECT * FROM alumnos WHERE CodigoAlum = {}".format(users)
            cur.execute(sql)
            usersx = cur.fetchall()
            cur.close()
            return usersx
        except:
            cur.close()

    #Busca la contraseña del alumno

    def BuscarCont_Alum(self, password):
        cur = self.conexion.cursor()
        try:
            sql = "SELECT * FROM alumnos WHERE AES_DECRYPT(ContraseñaAlum, 'clave') = {}".format(password)
            cur.execute(sql)
            passwordx = cur.fetchall()
            cur.close()
            return passwordx
        except:
            cur.close()


    #Buscar Codigo y Contraseña de Maestro para el Inicio de Sesion

    # Buscar el Codigo de Maestro
    def BuscarUser_Maes(self, users):
        cur = self.conexion.cursor()
        try:
            sql = "SELECT * FROM maestro WHERE CodigoM = {}".format(users)
            cur.execute(sql)
            usersx = cur.fetchall()
            cur.close()
            return usersx
        except:
            cur.close()

    # Buscar la Contraseña de Maestro

    def BuscarCont_Maes(self, password):
        cur = self.conexion.cursor()
        try:
            sql = "SELECT * FROM maestro WHERE  AES_DECRYPT(ContraseñaM, 'clave') = {}".format(password)
            cur.execute(sql)
            passwordx = cur.fetchall()
            cur.close()
            return passwordx
        except:
            cur.close()


#################################################################  
# Verificar que no se repitan datos (Codigo y Correo) del alumno y maestro
#################################################################

    #Verificar que si el codigo no este registrado
    def VerificarCodEstud(self, user):
        try:
            cur = self.conexion.cursor()
            sql = "SELECT * FROM alumnos WHERE CodigoAlum = %s"
            cur.execute(sql, (user,))  # Placeholder %s se usa aquí
            usersx = cur.fetchall()  # Obtener todos los resultados
        except mysql.connector.Error as e:
            cur.close()
            return False
        finally:
            cur.close()  # Asegurarse de cerrar el cursor

        return not usersx
    
    # Verificar si el correo no este registrado
    def VerificarCorEstud(self, correo):
        try:
            cur = self.conexion.cursor()
            sql = "SELECT * FROM alumnos WHERE CorreoAlum = %s"
            cur.execute(sql, (correo,))
            correox = cur.fetchall()
        except mysql.connector.Error as e:
            cur.close()
            return False
        finally:
            cur.close()  

        return not correox



        
    # Verificar que no se repitan datos (Codigo y Correo) del Maestro

    #Verificar que si el codigo no este registrado
    def VerificarCodMaest(self, user):
        try:
            cur = self.conexion.cursor()
            sql = "SELECT * FROM maestro WHERE CodigoM = %s"
            cur.execute(sql, (user,))
            usersx = cur.fetchall()
        except mysql.connector.Error as e:
            cur.close()
            return False
        finally:
            cur.close()  
        return not usersx


    def VerificarCorrMaest(self, correo):
        try:
            cur = self.conexion.cursor()
            sql = "SELECT * FROM maestro WHERE CorreoM = %s"
            cur.execute(sql, (correo,))
            correox = cur.fetchall()
        except mysql.connector.Error as e:
            cur.close()
            return False
        finally:
            cur.close()  
        return not correox



#################################################
# Registro de Maestro y Alumnos   
################################################  

    #Alumnos

    def RegistroDeDatos(self, CodAlum, NomAlum, ApellPatAlum, CorreoAlum, ContAlum, GradGrup, Turn):
        cur = self.conexion.cursor()
        try:
            sql = """INSERT INTO alumnos (CodigoAlum, RolA, NombreAlum, ApellidoPatAlum, CorreoAlum, ContraseñaAlum, GraGru, Turno) VALUES (%s, %s, %s, %s, %s, (AES_ENCRYPT(%s, 'clave')), %s, %s)"""
            values = (CodAlum, "Alumno", NomAlum, ApellPatAlum, CorreoAlum, ContAlum, GradGrup, Turn)
            cur.execute(sql, values)
            self.conexion.commit()
            cur.close()
        except:
            cur.close()

    #Maestros

    def RegistroDeDatosMaestro(self, CodM, NomM, ApellPatM, CorreoM, ContM):
        cur = self.conexion.cursor()
        try:
            sql = """INSERT INTO maestro (CodigoM, RolM, NombreM, ApellidoPatM, CorreoM, ContraseñaM) VALUES (%s, %s, %s, %s, %s, (AES_ENCRYPT(%s, 'clave')))"""
            values = (CodM, "Maestro",NomM, ApellPatM, CorreoM, ContM)
            cur.execute(sql, values)
            self.conexion.commit()
            cur.close()
        except:
            cur.close()

#########################################################
## 
########################################################

    def iniciar_sesion(self,Codigo):
        cur = self.conexion.cursor()
        try:
                # Verificar las credenciales de inicio de sesión en la tabla correspondiente (maestros o alumnos)
            if len(Codigo) == 7:
                cur.execute("SELECT CodigoM, RolM, NombreM, ApellidoPatM,CorreoM FROM maestro WHERE CodigoM = %s", (Codigo,))
            elif len(Codigo) == 9:
                cur.execute("SELECT CodigoAlum, RolA, NombreAlum, ApellidoPatAlum, CorreoAlum FROM alumnos WHERE CodigoAlum = %s", (Codigo,))

            resultado = cur.fetchone()

            cur.close()
            
            if resultado:
                return resultado
            else:
                return None
        except:
            cur.close()