#Miranda Leyva Juan Manuel

import mysql.connector
from mysql.connector import Error

def crear_conexion():
    #Crear la conexion con la base de datos mysql
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='project2',
        )
        if conexion.is_connected():
           print("Conexion con Mysql establecida")
           return conexion
    except Error as e:
        print(f"Error al conectar a Mysql:{e}")
        return None


if __name__ == "__main__":
    conexion = crear_conexion()
    if conexion:
        conexion.close()