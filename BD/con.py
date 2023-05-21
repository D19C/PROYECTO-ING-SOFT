import mysql.connector

# Conexión a la base de datos
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

# Creación de la base de datos si no existe
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS empleos")

# Conexión a la base de datos "empleos"
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="empleos"
)

# Creación de la tabla si no existe
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), apellido VARCHAR(255), tipo_doc VARCHAR(255), num_doc VARCHAR(255), correo VARCHAR(255), contrasena VARCHAR(255))")
