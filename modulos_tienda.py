import mysql.connector

class Marca:
    def __init__(self, nombre):
        self.nombre = nombre

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

class Zapatilla:
    def __init__(self, nombre, marca, talla, precio, categoria):
        self.nombre = nombre
        self.marca = marca
        self.talla = talla
        self.precio = precio
        self.categoria = categoria

class Cliente:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

class Pedido:
    def __init__(self, cliente, zapatillas):
        self.cliente = cliente
        self.zapatillas = zapatillas
        self.estado = "Pendiente"  

class LineaPedido:
    def __init__(self, zapatilla, cantidad):
        self.zapatilla = zapatilla
        self.cantidad = cantidad

class GestorTienda:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            port=3306,  
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def cargar_base_de_datos_desde_sql(self, sql_file):
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        self.cursor.execute(sql_script)
        self.connection.commit()
        
    def insertar_marca(self, nombre):
        query = "INSERT INTO Marca (nombre) VALUES (%s)"
        values = (nombre,)
        self.cursor.execute(query, values)
        self.connection.commit()
        print("Marca insertada con éxito.")

    def insertar_categoria(self, nombre):
        query = "INSERT INTO Categoria (nombre) VALUES (%s)"
        values = (nombre,)
        self.cursor.execute(query, values)
        self.connection.commit()
        print("Categoría insertada con éxito.")

    def insertar_zapatilla(self, nombre, marca_id, talla, precio, categoria_id):
        query = "INSERT INTO Zapatilla (nombre, marca_id, talla, precio, categoria_id) VALUES (%s, %s, %s, %s, %s)"
        values = (nombre, marca_id, talla, precio, categoria_id)
        self.cursor.execute(query, values)
        self.connection.commit()
        print("Zapatilla insertada con éxito.")

    def insertar_cliente(self, nombre, direccion):
        query = "INSERT INTO Cliente (nombre, direccion) VALUES (%s, %s)"
        values = (nombre, direccion)
        self.cursor.execute(query, values)
        self.connection.commit()
        print("Cliente insertado con éxito.")

    def insertar_pedido(self, cliente_id, fecha_pedido, estado):
        query = "INSERT INTO Pedido (cliente_id, fecha_pedido, estado) VALUES (%s, %s, %s)"
        values = (cliente_id, fecha_pedido, estado)
        self.cursor.execute(query, values)
        self.connection.commit()
        print("Pedido insertado con éxito.")

    def insertar_linea_pedido(self, pedido_id, zapatilla_id, cantidad):
        query = "INSERT INTO LineaPedido (pedido_id, zapatilla_id, cantidad) VALUES (%s, %s, %s)"
        values = (pedido_id, zapatilla_id, cantidad)
        self.cursor.execute(query, values)
        self.connection.commit()
        print("Línea de pedido insertada con éxito.")

    def seleccionar_marcas(self):
        query = "SELECT * FROM Marca"
        self.cursor.execute(query)
        marcas = self.cursor.fetchall()
        if marcas:
            for marca in marcas:
                print(Marca(marca[1]))
        else:
            print("No se encontraron marcas.")

    def seleccionar_categorias(self):
        query = "SELECT * FROM Categoria"
        self.cursor.execute(query)
        categorias = self.cursor.fetchall()
        if categorias:
            for categoria in categorias:
                print(Categoria(categoria[1]))
        else:
            print("No se encontraron categorías.")

    def seleccionar_zapatillas(self):
        query = "SELECT * FROM Zapatilla"
        self.cursor.execute(query)
        zapatillas = self.cursor.fetchall()
        if zapatillas:
            for zapatilla in zapatillas:
                print(Zapatilla(zapatilla[1], zapatilla[2], zapatilla[3], zapatilla[4], zapatilla[5]))
        else:
            print("No se encontraron zapatillas.")

    def seleccionar_clientes(self):
        query = "SELECT * FROM Cliente"
        self.cursor.execute(query)
        clientes = self.cursor.fetchall()
        if clientes:
            for cliente in clientes:
                print(Cliente(cliente[1], cliente[2]))
        else:
            print("No se encontraron clientes.")

    def seleccionar_pedidos(self):
        query = "SELECT * FROM Pedido"
        self.cursor.execute(query)
        pedidos = self.cursor.fetchall()
        if pedidos:
            for pedido in pedidos:
                print(Pedido(pedido[1], pedido[2], pedido[3]))
        else:
            print("No se encontraron pedidos.")

    def seleccionar_lineas_pedido(self):
        query = "SELECT * FROM LineaPedido"
        self.cursor.execute(query)
        lineas_pedido = self.cursor.fetchall()
        if lineas_pedido:
            for linea_pedido in lineas_pedido:
                print(LineaPedido(linea_pedido[1], linea_pedido[2], linea_pedido[3]))
        else:
            print("No se encontraron líneas de pedido.")

    def actualizar_descripcion_zapatilla(self, nombre, nueva_descripcion):
        query = "UPDATE Zapatilla SET nombre = %s WHERE nombre = %s"
        values = (nueva_descripcion, nombre)
        self.cursor.execute(query, values)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Descripción de la zapatilla actualizada con éxito.")
        else:
            print("No se encontró la zapatilla.")

    def eliminar_zapatilla(self, nombre):
        query = "DELETE FROM Zapatilla WHERE nombre = %s"
        values = (nombre,)
        self.cursor.execute(query, values)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Zapatilla eliminada con éxito.")
        else:
            print("No se encontró la zapatilla.")


    def cerrar_conexion(self):
        self.connection.close()
