import pymysql
import os
from dotenv import load_dotenv
import csv
from datetime import datetime


load_dotenv()
host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
port = os.getenv('DB_PORT')

class DB:
    def __init__(self):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            port=int(port)
        )
        self.cursor = self.connection.cursor()
        print("Conexion Exitosa")


    def restartConnection(self):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            port=int(port)
        )
        self.cursor = self.connection.cursor()
        print("Conexion Reestablecida")


    def crearModelo(self):
        with open('./querys/Creacion Base de Datos.sql', 'r', encoding='utf-8') as archivo:
            SCRIPT = archivo.read()
        commands = SCRIPT.split(";")
        try:
            for command in commands:
                if command == "":
                    continue
                self.cursor.execute(command)
                self.connection.commit()


            return({"Mensaje": "Modelo Creado Exitosamente"})

        except Exception as e:
            raise


    def cargarTablaTemporal(self):
        # Crea las tablas temporales en la base de datos
        with open('./querys/Creacion Tablas Temporales.sql', 'r', encoding='utf-8') as archivo:
            SCRIPT = archivo.read()
        commands = SCRIPT.split(";")
        try:
            for command in commands:
                if command == "":
                    continue
                self.cursor.execute(command)
                self.connection.commit()
        except Exception as e:
            return ({"Mensaje": "Error al crear la tabla temporal -> " + str(e.args)})
            

        # Carga el archivo de votaciones a su tabla temporal
        with open('./carga/votaciones.csv', 'r', encoding='utf-8') as archivo_csv:
            leido = csv.reader(archivo_csv)
            next(leido) # Omite los encabezados al saltar la primera linea
            for registro in leido:
                id = int(registro[0])
                id_candidato = int(registro[1])
                dpi = int(registro[2])
                mesa_id = int(registro[3])
                fecha = registro[4]
                # Formatea la fecha en el formato YYYY/MM/DD HH:MM:SS
                fecha = datetime.strptime(fecha, "%d/%m/%Y %H:%M").strftime("%Y/%m/%d %H:%M:%S")
                query = f'INSERT INTO bd1_proyecto1.temp_votaciones VALUES ({id},{id_candidato},{dpi},{mesa_id},"{fecha}");'
                try:
                    self.cursor.execute(query) 
                    self.connection.commit()
                except Exception as e:
                    self.close()
                    return ({"Mensaje": "Error al cargar la tabla temporal -> " + str(e.args)})
        
        # Carga el archivo de partidos a su tabla temporal
        with open('./carga/partidos.csv', 'r', encoding='utf-8') as archivo_csv:
            leido = csv.reader(archivo_csv)
            next(leido) # Omite los encabezados al saltar la primera linea
            for registro in leido:
                id = int(registro[0])
                nombre = registro[1]
                siglas = registro[2]
                fundacion = registro[3]
                # Formatea la fecha en el formato YYYY/MM/DD
                fundacion = datetime.strptime(fundacion, "%d/%m/%Y").strftime("%Y/%m/%d")
                query = f'INSERT INTO bd1_proyecto1.temp_partido VALUES ({id},"{nombre}","{siglas}","{fundacion}");'
                try:
                    self.cursor.execute(query) 
                    self.connection.commit()
                except Exception as e:
                    self.close()
                    return ({"Mensaje": "Error al cargar la tabla temporal -> " + str(e.args)})


        # Carga el archivo de mesas a su tabla temporal
        with open('./carga/mesas.csv', 'r', encoding='utf-8') as archivo_csv:
            leido = csv.reader(archivo_csv)
            next(leido) # Omite los encabezados al saltar la primera linea
            for registro in leido:
                id = int(registro[0])
                departemento_id = int(registro[1])
                query = f"INSERT INTO bd1_proyecto1.temp_mesa VALUES ({id},{departemento_id});"
                try:
                    self.cursor.execute(query) 
                    self.connection.commit()
                except Exception as e:
                    self.close()
                    return ({"Mensaje": "Error al cargar la tabla temporal -> " + str(e.args)})

        
        # Carga el archivo de departamentos a su tabla temporal
        with open('./carga/departamentos.csv', 'r', encoding='utf-8') as archivo_csv:
            leido = csv.reader(archivo_csv)
            next(leido) # Omite los encabezados al saltar la primera linea
            for registro in leido:
                id = int(registro[0])
                nombre = registro[1]
                query = f'INSERT INTO bd1_proyecto1.temp_departamento VALUES ({id},"{nombre}");'
                try:
                    self.cursor.execute(query) 
                    self.connection.commit()
                except Exception as e:
                    self.close()
                    return ({"Mensaje": "Error al cargar la tabla temporal -> " + str(e.args)})
                    
            
        # Carga el archivo de ciudadanos a su tabla temporal
        with open('./carga/ciudadanos.csv', 'r', encoding='utf-8') as archivo_csv:
            leido = csv.reader(archivo_csv)
            next(leido) # Omite los encabezados al saltar la primera linea
            for registro in leido:
                dpi = int(registro[0])
                nombre = registro[1]
                apellido = registro[2]
                direccion = registro[3]
                telefono = registro[4]
                edad = int(registro[5])
                genero = registro[6]
                query = f"""INSERT INTO bd1_proyecto1.temp_ciudadano 
                            VALUES ({dpi},"{nombre}","{apellido}","{direccion}","{telefono}",{edad},"{genero}");"""
                try:
                    self.cursor.execute(query) 
                    self.connection.commit()
                except Exception as e:
                    self.close()
                    return ({"Mensaje": "Error al cargar la tabla temporal -> " + str(e.args)})
                    
        
        # Carga el archivo de cargos a su tabla temporal
        with open('./carga/cargos.csv', 'r', encoding='utf-8') as archivo_csv:
            leido = csv.reader(archivo_csv)
            next(leido) # Omite los encabezados al saltar la primera linea
            for registro in leido:
                id = int(registro[0])
                cargo = registro[1]
                query = f'INSERT INTO bd1_proyecto1.temp_cargo VALUES ({id},"{cargo}");'
                try:
                    self.cursor.execute(query) 
                    self.connection.commit()
                except Exception as e:
                    self.close()
                    return ({"Mensaje": "Error al cargar la tabla temporal -> " + str(e.args)})
                    

        # Carga el archivo de candidatos a su tabla temporal
        with open('./carga/candidatos.csv', 'r', encoding='utf-8') as archivo_csv:
            leido = csv.reader(archivo_csv)
            next(leido) # Omite los encabezados al saltar la primera linea
            for registro in leido:
                id = int(registro[0])
                nombre = registro[1]
                fecha = registro[2]
                # Formatea la fecha en el formato YYYY/MM/DD
                fecha = datetime.strptime(fecha, "%d/%m/%Y").strftime("%Y/%m/%d")
                partido_id = int(registro[3])
                cargo_id = int(registro[4])
                query = f"""INSERT INTO bd1_proyecto1.temp_candidato
                        VALUES ({id},"{nombre}","{fecha}",{partido_id},{cargo_id});"""
                try:
                    self.cursor.execute(query) 
                    self.connection.commit()
                except Exception as e:
                    self.close()
                    return ({"Mensaje": "Error al cargar la tabla temporal -> " + str(e.args)})
                    


        # Carga los datos de las tablas temporales a las tablas del modelo
        with open('./querys/Carga de Modelo.sql', 'r', encoding='utf-8') as archivo:
            SCRIPT = archivo.read()
        commands = SCRIPT.split(";")
        try:
            for command in commands:
                if command == "":
                    continue
                self.cursor.execute(command)
                self.connection.commit()
        except Exception as e:
            return ({"Mensaje": "Error al cargar los datos al modelo -> " + str(e.args)})
            
        
        self.close()
        self.restartConnection()
        return ({"Mensaje": "Se Cargaron los Datos de las Tablas Temporales hacia el Modelo"})

    
    def eliminarModelo(self):
        try:
            self.cursor.execute("DROP SCHEMA bd1_proyecto1;")
            self.connection.commit()
            return({"Mensaje": "Modelo Eliminado Exitosamente"})

        except Exception as e:
            raise
    
    
    def consulta1(self):
        with open('./querys/Consulta1.sql', 'r', encoding='utf-8') as archivo:
            try:
                self.cursor.execute(archivo.read())
                resultado = self.cursor.fetchall()
                datos = []
                for registro in resultado:
                    objeto = {
                        "Presidente" : registro[0],
                        "Vicepresidente" : registro[1],
                        "Partido" : registro[2]
                    }
                    datos.append(objeto)
                return (datos)
            except Exception as e:
                return ({"Mensaje": "Error al realizar la consulta -> " + str(e.args)})
    
    
    def consulta2(self):
        with open('./querys/Consulta2.sql', 'r', encoding='utf-8') as archivo:
            try:
                self.cursor.execute(archivo.read())
                resultado = self.cursor.fetchall()
                datos = []
                for registro in resultado:
                    objeto = {
                        "Cantidad" : int(registro[0]),
                        "Partido" : registro[1]
                    }
                    datos.append(objeto)
                return (datos)
            except Exception as e:
                return ({"Mensaje": "Error al realizar la consulta -> " + str(e.args)})
    
    
    def consulta3(self):
        with open('./querys/Consulta3.sql', 'r', encoding='utf-8') as archivo:
            try:
                self.cursor.execute(archivo.read())
                resultado = self.cursor.fetchall()
                datos = []
                for registro in resultado:
                    objeto = {
                        "Nombre" : registro[0],
                        "Partido" : registro[1]
                    }
                    datos.append(objeto)
                return (datos)
            except Exception as e:
                return ({"Mensaje": "Error al realizar la consulta -> " + str(e.args)})
            

    def consulta4(self):
        with open('./querys/Consulta4.sql', 'r', encoding='utf-8') as archivo:
            try:
                self.cursor.execute(archivo.read())
                resultado = self.cursor.fetchall()
                datos = []
                for registro in resultado:
                    objeto = {
                        "Cantidad" : int(registro[0]),
                        "Partido" : registro[1]
                    }
                    datos.append(objeto)
                return (datos)
            except Exception as e:
                return ({"Mensaje": "Error al realizar la consulta -> " + str(e.args)})
    

    def consulta5(self):
        with open('./querys/Consulta5.sql', 'r', encoding='utf-8') as archivo:
            try:
                self.cursor.execute(archivo.read())
                resultado = self.cursor.fetchall()
                datos = []
                for registro in resultado:
                    objeto = {
                        "Departamento" : registro[0],
                        "Cantidad de Votaciones" : registro[1]
                    }
                    datos.append(objeto)
                return (datos)
            except Exception as e:
                return ({"Mensaje": "Error al realizar la consulta -> " + str(e.args)})
    
    
    def consulta6(self):
        with open('./querys/Consulta6.sql', 'r', encoding='utf-8') as archivo:
            try:
                self.cursor.execute(archivo.read())
                resultado = self.cursor.fetchone()
                return (resultado[0])
            except Exception as e:
                return ({"Mensaje": "Error al realizar la consulta -> " + str(e.args)})

    
    def consulta7(self):
        with open('./querys/Consulta7.sql', 'r', encoding='utf-8') as archivo:
            try:
                self.cursor.execute(archivo.read())
                resultado = self.cursor.fetchall()
                datos = []
                for registro in resultado:
                    objeto = {
                        "Cantidad" : registro[0],
                        "Edad" : registro[1]
                    }
                    datos.append(objeto)
                return (datos)
            except Exception as e:
                return ({"Mensaje": "Error al realizar la consulta -> " + str(e.args)})
    

    def consulta8(self):
        with open('./querys/Consulta8.sql', 'r', encoding='utf-8') as archivo:
            try:
                self.cursor.execute(archivo.read())
                resultado = self.cursor.fetchall()
                datos = []
                for registro in resultado:
                    objeto = {
                        "Presidente" : registro[0],
                        "Vicepresidente" : registro[1],
                        "Votos Totales" : registro[2]
                    }
                    datos.append(objeto)
                return (datos)
            except Exception as e:
                return ({"Mensaje": "Error al realizar la consulta -> " + str(e.args)})
    

    def consulta9(self):
        with open('./querys/Consulta9.sql', 'r', encoding='utf-8') as archivo:
            try:
                self.cursor.execute(archivo.read())
                resultado = self.cursor.fetchall()
                datos = []
                for registro in resultado:
                    objeto = {
                        "Mesa" : registro[0],
                        "Departamento" : registro[1],
                        "Votos" : registro[2]
                    }
                    datos.append(objeto)
                return (datos)
            except Exception as e:
                return ({"Mensaje": "Error al realizar la consulta -> " + str(e.args)})
    

    def consulta10(self):
        with open('./querys/Consulta10.sql', 'r', encoding='utf-8') as archivo:
            commands = archivo.read().split(";")
            try:
                self.cursor.execute(commands[0])
                resultado = self.cursor.fetchall()
                datos = []
                for registro in resultado:
                    objeto = {
                        "Hora y Minuto" : registro[0].strftime("%H:%M"),
                        "Votos" : registro[1]
                    }
                    datos.append(objeto)
                
                self.cursor.execute(commands[1])
                resultado = self.cursor.fetchall()
                datos2 = []
                for registro in resultado:
                    objeto = {
                        "Hora" : str(registro[0])+":00",
                        "Votos" : registro[1]
                    }
                    datos2.append(objeto)
                return ({ "HM" : datos, "H" : datos2 })
            except Exception as e:
                return ({"Mensaje": "Error al realizar la consulta -> " + str(e.args)})
    
    
    def consulta11(self):
        with open('./querys/Consulta11.sql', 'r', encoding='utf-8') as archivo:
            try:
                self.cursor.execute(archivo.read())
                resultado = self.cursor.fetchall()
                datos = []
                for registro in resultado:
                    objeto = {
                        "Genero" : registro[0],
                        "Votos" : registro[1]
                    }
                    datos.append(objeto)
                return (datos)
            except Exception as e:
                return ({"Mensaje": "Error al realizar la consulta -> " + str(e.args)})
            

    def close(self):
        self.connection.close()