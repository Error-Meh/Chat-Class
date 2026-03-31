from tkinter import messagebox
import mysql.connector

class ChatPrivado():
    def __init__(self):
        self.conexion = mysql.connector.connect( 
            host = "127.0.0.1",
            database = "chatclass",
            user = "root",
            password = ""
        )

        self.conex = mysql.connector.connect( 
            host = "127.0.0.1",
            database = "chatclassms",
            user = "root",
            password = ""
        )

    def VerificarALumno(self,CodIng):
        cur = self.conexion.cursor()
        try:
            sql = """ SELECT CodigoAlum FROM alumnos"""
            cur.execute(sql)
            C = cur.fetchall()
            Cods = len(C) # type: ignore
            CodAd = []
            for n in range(Cods):
                CodAd.append(C[n][0]) # type: ignore
            CI = int(CodIng)
            for Co in CodAd:
                if Co == CI:
                    return Co
                else:
                    pass
            cur.close()
            messagebox.showinfo(title="E R R O R", message="El codigo ingresado no existe")
        except:
            cur.close()
            pass


    def VerificarMaestro(self,CodIng):
        cur = self.conexion.cursor()
        try:
            sql = """ SELECT CodigoM FROM maestro"""
            cur.execute(sql)
            C = cur.fetchall()
            Cods = len(C) # type: ignore
            CodAd = []
            for n in range(Cods):
                CodAd.append(C[n][0]) # type: ignore
            CI = int(CodIng)
            for Co in CodAd:
                if Co == CI:
                    return Co
                else:
                    pass
            cur.close()
            messagebox.showinfo(title="E R R O R", message="El codigo ingresado no existe")
        except:
            cur.close()
            pass


    def ActuEmisor(self, CodJ,CodE):
        cur = self.conexion.cursor()
        try:
            LCodE = len(CodE)

            if LCodE == 7:

                sql = """ SELECT ChatsPrivM FROM maestro WHERE CodigoM = %s """
                cur.execute(sql,(CodE,))
                Resultado = cur.fetchone()
                IdAnter = Resultado[0] if Resultado and Resultado[0] not in (None, '', 'NULL') else None
                if IdAnter:
                    IdNuevo = IdAnter + ","+ CodJ
                    sql = "UPDATE maestro SET ChatsPrivM = %s WHERE CodigoM = %s"
                    values = (IdNuevo,CodE)
                    cur.execute(sql,values)
                else:
                    sql = """UPDATE maestro SET ChatsPrivM = %s WHERE CodigoM = %s"""
                    values = (CodJ, CodE)
                    cur.execute(sql, values)

            elif LCodE == 9:

                sql = """ SELECT Chats_Priv FROM alumnos WHERE CodigoAlum = %s """
                cur.execute(sql,(CodE,))
                Resultado = cur.fetchone()
                IdAnter = Resultado[0] if Resultado and Resultado[0] not in (None, '', 'NULL') else None
                if IdAnter:
                    IdNuevo = IdAnter + ","+ CodJ
                    sql = "UPDATE alumnos SET Chats_Priv = %s WHERE CodigoAlum = %s"
                    values = (IdNuevo,CodE)
                    cur.execute(sql,values)
                else:
                    sql = """UPDATE alumnos SET Chats_Priv = %s WHERE CodigoAlum = %s"""
                    values = (CodJ, CodE)
                    cur.execute(sql, values)


            self.conexion.commit()
            cur.close()
        except:
            cur.close()
            pass

        
    def ActuReceptor(self, CodJ, CodR):
        cur = self.conexion.cursor()
        try:
            LCodE = len(CodR)

            if LCodE == 7:

                sql = """ SELECT ChatsPrivM FROM maestro WHERE CodigoM = %s """
                cur.execute(sql,(CodR,))
                Resultado = cur.fetchone()
                IdAnter = Resultado[0] if Resultado and Resultado[0] not in (None, '', 'NULL') else None
                if IdAnter:
                    IdNuevo = IdAnter + ","+ CodJ
                    sql = "UPDATE maestro SET ChatsPrivM = %s WHERE CodigoM = %s"
                    values = (IdNuevo,CodR)
                    cur.execute(sql,values)
                else:
                    sql = """UPDATE maestro SET ChatsPrivM = %s WHERE CodigoM = %s"""
                    values = (CodJ, CodR)
                    cur.execute(sql, values)

            elif LCodE == 9:

                sql = """ SELECT Chats_Priv FROM alumnos WHERE CodigoAlum = %s """
                cur.execute(sql,(CodR,))
                Resultado = cur.fetchone()
                IdAnter = Resultado[0] if Resultado and Resultado[0] not in (None, '', 'NULL') else None
                if IdAnter:
                    IdNuevo = IdAnter + ","+ CodJ
                    sql = "UPDATE alumnos SET Chats_Priv = %s WHERE CodigoAlum = %s"
                    values = (IdNuevo,CodR)
                    cur.execute(sql,values)
                else:
                    sql = """UPDATE alumnos SET Chats_Priv = %s WHERE CodigoAlum = %s"""
                    values = (CodJ, CodR)
                    cur.execute(sql, values)

            self.conexion.commit()
            cur.close()
        except:
            cur.close()
            pass

    def VerifChatPrEx(self, CodR, CodE, Codder):
        cur = self.conexion.cursor()
        try:
            CodRev = CodR + "-" + CodE
            CodVer = [(Codder),(CodRev)]
            if len(CodE) == 7:
                sql = """ SELECT ChatsPrivM FROM maestro WHERE CodigoM = %s """
                cur.execute(sql,(CodE,))
                Resultado = cur.fetchone()
                IdAnter = Resultado[0] if Resultado and Resultado[0] not in (None, '', 'NULL') else None            
                if IdAnter:
                    if CodVer[0] in IdAnter:
                        messagebox.showinfo(title="E R R O R", message="Ya existe un chat con este codigos")
                        cur.close()
                        return 0
                    elif CodVer[1] in IdAnter:
                        messagebox.showinfo(title="E R R O R", message="Ya existe un chat con este codigos")
                        cur.close()
                        return 0

            elif len(CodE) ==9:
                sql = """ SELECT Chats_Priv FROM alumnos WHERE CodigoAlum = %s """
                cur.execute(sql,(CodE,))
                Resultado = cur.fetchone()
                IdAnter = Resultado[0] if Resultado and Resultado[0] not in (None, '', 'NULL') else None
                if IdAnter:
                    if CodVer[0] in IdAnter:
                        messagebox.showinfo(title="E R R O R", message="Ya existe un chat con este codigos")
                        cur.close()
                        return 0
                    elif CodVer[1] in IdAnter:
                        messagebox.showinfo(title="E R R O R", message="Ya existe un chat con este codigos")
                        cur.close()
                        return 0
            cur.close()
        except:
            cur.close()
            pass

    def BusNomUsuario(self, CodUs):         
        Log = len(CodUs)
        cur = self.conexion.cursor()

        try:    
            NomsObt = []
            for n in range(Log):
                if len(CodUs[n]) == 7:
                    sql = "SELECT NombreM, ApellidoPatM FROM maestro WHERE CodigoM = %s"
                    cur.execute(sql,(CodUs[n],))
                    R = cur.fetchone()
                    NomsObt.append(R[0] + " " + R[1]) # type: ignore
                    
                elif len(CodUs[n]) == 9:
                    sql = "SELECT NombreAlum, ApellidoPatAlum FROM alumnos WHERE CodigoAlum = %s"
                    cur.execute(sql,(CodUs[n],))
                    R = cur.fetchone()
                    NomsObt.append(R[0] + " " + R[1]) # type: ignore

            cur.close()
            return NomsObt
        except:
            cur.close()
            pass

    ########################################################################
    ##                      Enviar y Cargar Mensajes                      ##
    ########################################################################





    def EnvMenChatPriv(self, ID_Canal, ID_Mensaje, Mensaje, Emisor, Fecha):
        try:
            cur = self.conex.cursor()
            sql = """INSERT INTO chats_priv (ID_Canal, ID_Mensaje, Mensaje, Emisor, Fecha) VALUES (%s, %s, %s, %s, %s)"""
            values = (ID_Canal, ID_Mensaje, Mensaje, Emisor, Fecha)
            cur.execute(sql, values)
            self.conexion.commit()
            cur.close()
        except:
            cur.close()

    def verificar_mensajes_enviados_Chats(self):
        try:
            cur = self.conex.cursor()
            sql = "SELECT COUNT(*) FROM chats_priv"
            cur.execute(sql)
            result = cur.fetchone()
            num_mensajes = result[0] if result else 0
            cur.close()
            return num_mensajes
        except:
            cur.close()
        
    def ObtenerMensajesPriv(self, ID_Chat):
        try:
            cur = self.conex.cursor()
            sql = """SELECT Emisor, Mensaje FROM chats_priv
                     WHERE ID_Canal = %s"""
            cur.execute(sql, (ID_Chat,))
            mensajes = cur.fetchall()
            cur.close()
            return mensajes
        except:
            cur.close()