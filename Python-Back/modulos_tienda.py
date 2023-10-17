import mysql.connector


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
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def crear_zapatilla(self, nombre, marca_id, talla, precio, categoria_id):
        query = "INSERT INTO Zapatilla (nombre, marca_id, talla, precio, categoria_id) VALUES (%s, %s, %s, %s, %s)"
        values = (nombre, marca_id, talla, precio, categoria_id)
        self.cursor.execute(query, values)
        self.connection.commit()
        print("Zapatilla creada con éxito.")
    
    def seleccionar_zapatillas(self):
        query = "SELECT Zapatilla.id, Zapatilla.nombre, Marca.nombre, Zapatilla.talla, Zapatilla.precio, Categoria.nombre FROM Zapatilla JOIN Marca ON Zapatilla.marca_id = Marca.id JOIN Categoria ON Zapatilla.categoria_id = Categoria.id"
        self.cursor.execute(query)
        zapatillas = self.cursor.fetchall()
        return zapatillas
    

    def leer_zapatilla(self, zapatilla_id):
        query = "SELECT * FROM Zapatilla WHERE id = %s"
        values = (zapatilla_id,)
        self.cursor.execute(query, values)
        zapatilla = self.cursor.fetchone()
        if zapatilla:
            return Zapatilla(zapatilla[0], zapatilla[1], zapatilla[2], zapatilla[3], zapatilla[4], zapatilla[5])
        else:
            return None

    def actualizar_zapatilla(self, zapatilla_id, nombre, marca_id, talla, precio, categoria_id):
        query = "UPDATE Zapatilla SET nombre = %s, marca_id = %s, talla = %s, precio = %s, categoria_id = %s WHERE id = %s"
        values = (nombre, marca_id, talla, precio, categoria_id, zapatilla_id)
        self.cursor.execute(query, values)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Zapatilla actualizada con éxito.")
        else:
            print("No se encontró la zapatilla.")

    def eliminar_zapatilla(self, zapatilla_id):
        query = "DELETE FROM Zapatilla WHERE id = %s"
        values = (zapatilla_id,)
        self.cursor.execute(query, values)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Zapatilla eliminada con éxito.")
        else:
            print("No se encontró la zapatilla.")

    def crear_pedido(self, cliente_id, fecha_pedido, estado):
        query = "INSERT INTO Pedido (cliente_id, fecha_pedido, estado) VALUES (%s, %s, %s)"
        values = (cliente_id, fecha_pedido, estado)
        self.cursor.execute(query, values)
        self.connection.commit()
        print("Pedido creado con éxito.")

    def leer_pedido(self, pedido_id):
        query = "SELECT * FROM Pedido WHERE id = %s"
        values = (pedido_id,)
        self.cursor.execute(query, values)
        pedido = self.cursor.fetchone()
        if pedido:
            return Pedido(pedido[0], pedido[1], pedido[2], pedido[3])
        else:
            return None

    def actualizar_pedido(self, pedido_id, cliente_id, fecha_pedido, estado):
        query = "UPDATE Pedido SET cliente_id = %s, fecha_pedido = %s, estado = %s WHERE id = %s"
        values = (cliente_id, fecha_pedido, estado, pedido_id)
        self.cursor.execute(query, values)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Pedido actualizado con éxito.")
        else:
            print("No se encontró el pedido.")

    def eliminar_pedido(self, pedido_id):
        query = "DELETE FROM Pedido WHERE id = %s"
        values = (pedido_id,)
        self.cursor.execute(query, values)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Pedido eliminado con éxito.")
        else:
            print("No se encontró el pedido.")    
   