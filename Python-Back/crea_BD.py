import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Emiliano29782978"
)

cursor = mydb.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS TIENDA_ONLINE")
print("Base de datos 'TIENDA-ONLINE' creada con éxito.")

cursor.execute("USE TIENDA_ONLINE")

cursor.execute("""
CREATE TABLE Marca (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
)
""")
print("Tabla 'Marca' creada.")

cursor.execute("""
CREATE TABLE Categoria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
)
""")
print("Tabla 'Categoria' creada.")

cursor.execute("""
CREATE TABLE Zapatilla (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    marca VARCHAR(255) NOT NULL,  
    talla FLOAT NOT NULL,
    precio FLOAT NOT NULL,
    categoria_id INT
)
""")
print("Tabla 'Zapatilla' creada.")

cursor.execute("""
CREATE TABLE Cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    direccion TEXT
)
""")
print("Tabla 'Cliente' creada.")

cursor.execute("""
CREATE TABLE Pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    fecha_pedido DATE NOT NULL,
    estado VARCHAR(255) NOT NULL
)
""")
print("Tabla 'Pedido' creada.")

cursor.execute("""
CREATE TABLE LineaPedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT NOT NULL,
    zapatilla_id INT NOT NULL,
    cantidad INT NOT NULL
)
""")
print("Tabla 'LineaPedido' creada.")

cursor.executemany("INSERT INTO Marca (nombre) VALUES (%s)", [("ADIDAS",), ("PUMA",), ("TOPPER",)])
print("Registros de Marca insertados con éxito.")

cursor.executemany("INSERT INTO Categoria (nombre) VALUES (%s)", [("Categoria 1",), ("Categoria 2",), ("Categoria 3",)])
print("Registros de Categoria insertados con éxito.")

zapatillas = [
    ("Zapatilla Ejemplo 1", "ADIDAS", 42.5, 99.99, 1),
    ("Zapatilla Ejemplo 2", "PUMA", 40.0, 79.99, 2),
    ("Zapatilla Ejemplo 3", "TOPPER", 39.0, 119.99, 1)
]
cursor.executemany("INSERT INTO Zapatilla (nombre, marca, talla, precio, categoria_id) VALUES (%s, %s, %s, %s, %s)", zapatillas)
print("Registros de Zapatilla insertados con éxito.")

mydb.commit()

cursor.close()
mydb.close()
