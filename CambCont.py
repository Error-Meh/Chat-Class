import mysql.connector

class CambiarCont():
    def __init__(self):
        self.conexion = mysql.connector.connect( 
            host = "127.0.0.1",
            database = "chatclass",
            user = "root",
            password = ""
            )
    
    
    #Busca la contraseña del alumno
    def BuscarCont_Alum(self, password):
        cur = self.conexion.cursor()
        try:
            sql = "SELECT AES_DECRYPT(ContraseñaAlum, 'clave') FROM alumnos WHERE AES_DECRYPT(ContraseñaAlum, 'clave') = %s"
            cur.execute(sql, (password,))
            result = cur.fetchone()
            cur.close()
            return result[0] if result else None
        except:
            cur.close()
            pass
    


    def BuscarCont_Maes(self, password):
        cur = self.conexion.cursor()
        try:
            sql = "SELECT AES_DECRYPT(ContraseñaM, 'clave') FROM maestro WHERE AES_DECRYPT(ContraseñaM, 'clave') = %s"
            cur.execute(sql, (password,))
            result = cur.fetchone()
            cur.close()
            return result[0] if result else None
        except:
            cur.close()
            pass
    


    def ActualizarContAlum(self, NCont, Cod):
        cur = self.conexion.cursor()
        try:
            sql = "UPDATE alumnos SET ContraseñaAlum = (AES_ENCRYPT(%s, 'clave')) WHERE CodigoAlum = %s"
            cur.execute(sql, (NCont, Cod))
            self.conexion.commit()
            cur.close()
        except:
            cur.close()
            pass


    def ActualizarContMaes(self, NCont, Cod):
        cur = self.conexion.cursor()
        try:    
            sql = "UPDATE maestro SET ContraseñaM = (AES_ENCRYPT(%s, 'clave')) WHERE CodigoM = %s"
            cur.execute(sql, (NCont, Cod))
            self.conexion.commit()
            cur.close()
        except:
            cur.close()
            pass