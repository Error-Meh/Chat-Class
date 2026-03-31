"""
Crear un grupo en la base de datos, con una tabla
"""
from asyncio.windows_events import NULL
from pickle import NONE
from tkinter import messagebox
import mysql.connector



class ManejoDeGrupos():

    def __init__(self):
        self.conexion = mysql.connector.connect( 
            host = "127.0.0.1",
            database = "chatclass",
            user = "root",
            password = ""
        )

    #crea las tablas de los grupos   
    def CrearReg(self, NomTabla):
        cur = self.conexion.cursor()
        try:
            sql = """CREATE TABLE `{}` (
                ID_Grupo varchar(6) NOT NULL,
                NombreMateria text NOT NULL,
                ID_Maestro int(7) NULL,
                ID_Alumno int(9) NULL,
                NomInteg varchar(30) NOT NULL
                );""".format(NomTabla)
            
            cur.execute(sql)
            self.conexion.commit()
            cur.close()
        except:
            cur.close()


#El Primer Integrante sera el maestro
    def InsertPart(self,NomTabla,NomMat,Grad,Grup,Turn,integ, CodInteg):
        cur = self.conexion.cursor()
        try:
            sql = """INSERT INTO `{}` (ID_Grupo,NombreMateria,ID_Maestro, NomInteg) VALUES (%(ID_Grup)s, %(NombreMat)s, %(CodInteg)s, %(integ)s)""".format(NomTabla)
            values = {'ID_Grup': NomTabla, 'NombreMat': NomMat+" "+Grad+"-"+Grup+" "+Turn, 'CodInteg': CodInteg, 'integ': integ}

            cur.execute(sql, values)

            self.conexion.commit()
            cur.close()
        except:
            cur.close()

# Actualizar el campo de Grupos en la tabla de maestro
    def ActualizarMaest(self,CodIteng,NomTabla):
        cur = self.conexion.cursor()
        try:
            sql = """ SELECT ID_GruposM FROM maestro WHERE CodigoM = %s """
            cur.execute(sql,(CodIteng,))
            Resultado = cur.fetchone()
            IdAnter = Resultado[0] if Resultado and Resultado[0] not in (None, '', 'NULL') else None
            if IdAnter:
                IdNuevo = IdAnter + "."+ NomTabla
                sql = """ UPDATE `maestro` SET `ID_GruposM` = %s  WHERE `maestro`.`CodigoM` = %s """
                values = (IdNuevo,CodIteng)
                cur.execute(sql,values)
            else:
                sql = """UPDATE maestro SET ID_GruposM = %s WHERE CodigoM = %s"""
                values = (NomTabla, CodIteng)
                cur.execute(sql, values)
                
            self.conexion.commit()
            cur.close()
        except:
            cur.close()


    def UnirseGrupo(self, CodInteg, NomInt, CodG):
        cur = self.conexion.cursor()
        NomTabla = CodG.lower()
        try:
            sql = """SELECT ID_Alumno FROM `{}`""".format(NomTabla) 
            cur.execute(sql)
            IDINT = cur.fetchall()
            num = len(IDINT) # type: ignore
            IN = []
            for N in range(num):
                IN.append(IDINT[N][0]) # type: ignore
            CD = int(CodInteg)
            if CD in IN:
                messagebox.showerror(title="ERROR", message="Ya estás registrado en este grupo")
                self.conexion.commit()
                cur.close()
                return 0
            else:
                sql = """INSERT INTO `{}` (ID_Alumno, NomInteg) VALUES (%s, %s)""".format(CodG)
                values = (CodInteg, NomInt)
                cur.execute(sql, values)
                self.conexion.commit()
                cur.close()
                return 1

        except:
            messagebox.showinfo(title="E R R O R", message="No se encontro el grupo")
            self.conexion.commit()
            cur.close()
            return 0


    def ActualizarAlumno(self,CodIteng, IDGrupo, Ver):
        if Ver == 1:
            cur = self.conexion.cursor()
            try:
                sql = """ SELECT Grupos FROM alumnos WHERE CodigoAlum = %s """
                cur.execute(sql,(CodIteng,))
                Resultado = cur.fetchone()
                IdAnter = Resultado[0] if Resultado and Resultado[0] not in (None, '', 'NULL') else None
                if IdAnter:
                    IdNuevo = IdAnter + "."+ IDGrupo
                    sql = """ UPDATE `alumnos` SET `Grupos` = %s  WHERE `alumnos`.`CodigoAlum` = %s """
                    values = (IdNuevo,CodIteng)
                    cur.execute(sql,values)
                else:
                    sql = """UPDATE alumnos SET Grupos = %s WHERE CodigoAlum = %s"""
                    values = (IDGrupo, CodIteng)
                    cur.execute(sql, values)
                    
                self.conexion.commit()
                cur.close()
            except:
                cur.close()


#################################################################
#                  Borrar el Grupo                              #
#################################################################

    def ObtenerAlumnosDelGrupo(self, IdGrupo):
        try:
            cur = self.conexion.cursor()
            
            sql = """SELECT ID_Alumno FROM `{}`""".format(IdGrupo) 
            cur.execute(sql)
            resultado = cur.fetchall()
            listDat = []

            # alumnos = [101, 102, 103]

            alumnos = [fila[0] for fila in resultado[1:] if fila[0] is not None] # type: ignore

            cur.close()
            return alumnos

        except:
            cur.close()
            return []
        
    def eliminarAlumnos(self, codigoAlms, codigoG, CodM):
        try:
            cur = self.conexion.cursor()
            NumC = len(codigoAlms)
            listacodigosG = []
            listacodigosGM = []
            if NumC > 1:
                n = 0
                for n in range(NumC):
                    sql = f" SELECT Grupos FROM alumnos WHERE CodigoAlum = {codigoAlms[n]} "
                    cur.execute(sql)
                    resultado = cur.fetchone()
                    Cods = resultado[0] # type: ignore
                    if "." in Cods:
                        listacodigosG = Cods.split('.')
                        if codigoG in listacodigosG:
                            listacodigosG.remove(codigoG)
                        actualz = ".".join(listacodigosG)
                    else:
                        actualz = None

                    sql = """UPDATE alumnos SET Grupos = %s WHERE CodigoAlum = %s"""
                    values = (actualz, codigoAlms[n])
                    cur.execute(sql, values)
                    self.conexion.commit()

            elif NumC == 1:
                sql = f" SELECT Grupos FROM alumnos WHERE CodigoAlum = {codigoAlms[0]} "
                cur.execute(sql)
                resultado = cur.fetchone()
                Cods = resultado[0] # type: ignore
                if "." in Cods:
                    listacodigosG = Cods.split('.')
                    if codigoG in listacodigosG:
                        listacodigosG.remove(codigoG)
                    actualz = ".".join(listacodigosG)
                else:
                    actualz = None

                sql = """UPDATE alumnos SET Grupos = %s WHERE CodigoAlum = %s"""
                values = (actualz, codigoAlms[0])
                cur.execute(sql, values)
                self.conexion.commit()
                


            sql = f" SELECT ID_GruposM FROM maestro WHERE CodigoM = {CodM} "
            cur.execute(sql)
            resultado = cur.fetchone()
            Cods = resultado[0] # type: ignore
            if "." in Cods:
                listacodigosGM = Cods.split('.')
                if codigoG in listacodigosGM:
                    listacodigosGM.remove(codigoG)
                actualz = ".".join(listacodigosGM)
            else:
                actualz = None

            sql = """UPDATE maestro SET ID_GruposM = %s WHERE CodigoM = %s"""
            values = (actualz, CodM)
            cur.execute(sql, values)
            self.conexion.commit()

            sql = f"DROP TABLE IF EXISTS `{codigoG}`"
            cur.execute(sql)
            self.conexion.commit()
            
            cur.close()
        except:
            cur.close()