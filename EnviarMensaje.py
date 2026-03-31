import mysql.connector
from mysql.connector.errors import Error
import time

class EnviarMensajes():
 #Realizar la conexion a la Base de datos
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect( 
            host = "127.0.0.1",
            database = "chatclassms",
            user = "root",
            password = ""
            )
            
            self.conex = mysql.connector.connect(
            host = "127.0.0.1",
            database = "chatclass",
            user = "root",
            password = ""
            )

        except mysql.connector.Error as e:
            #xd ubo un error jaja
            ""


    def EnvMensaje(self, ID_Grupo, ID_Tabla, ID_Mensaje, Mensaje, Emisor, Fecha):
        try:
            cur = self.conexion.cursor()
            sql = """INSERT INTO chatsgrupos (ID_Grupo, ID_Tabla, ID_Mensaje, Mensaje, Emisor, Fecha) VALUES (%s, %s, %s, %s, %s, %s)"""
            values = (ID_Grupo, ID_Tabla, ID_Mensaje, Mensaje, Emisor, Fecha)
            cur.execute(sql, values)
            self.conexion.commit()
            cur.close()
        except:
            cur.close()
    
    def verificar_mensajes_enviados(self):
        try:
            cur = self.conexion.cursor()
            sql = "SELECT COUNT(*) FROM chatsgrupos"
            cur.execute(sql)
            result = cur.fetchone()
            num_mensajes = result[0] if result else 0
            cur.close()
            return num_mensajes
        except:
            cur.close()
        
    def obtener_mensajes(self, ID_Chat,IdGrup):
        try:
            cur = self.conexion.cursor()
            sql = """SELECT Emisor, Mensaje FROM chatsgrupos
                     WHERE ID_Tabla = %s AND ID_Grupo = %s"""
            cur.execute(sql, (ID_Chat, IdGrup,))
            mensajes = cur.fetchall()
            cur.close()
            return mensajes
        except:
            cur.close()

    