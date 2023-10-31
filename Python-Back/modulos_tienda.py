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


class GestorTienda:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()
        
    def seleccionar_zapatillas(self):
        query = "SELECT * FROM Zapatilla"
        self.cursor.execute(query)
        zapatillas = self.cursor.fetchall()
        return zapatillas
        
    def mostrar_zapatillas(gestor_tienda):
        zapatillas = gestor_tienda.seleccionar_zapatillas()
        for zapatilla in zapatillas:
            print(f"ID: {zapatilla[0]}, Nombre: {zapatilla[1]}, Marca: {zapatilla[2]}, Talla: {zapatilla[3]}, Precio: {zapatilla[4]}, Categoría: {zapatilla[5]}")


    def crear_zapatilla(self, nombre, marca, talla, precio, categoria_id):
        query = "INSERT INTO Zapatilla (nombre, marca, talla, precio, categoria_id) VALUES (%s, %s, %s, %s, %s)"
        values = (nombre, marca, talla, precio, categoria_id)
        self.cursor.execute(query, values)
        self.connection.commit()
        print("Zapatilla creada con éxito.")
    
    def actualizar_zapatilla(gestor_tienda):
        zapatilla_id = input("ID de la zapatilla a actualizar: ")
        zapatilla = gestor_tienda.leer_zapatilla(zapatilla_id)
        if zapatilla:
            nombre = input(f"Nuevo nombre ({zapatilla.nombre}): ")
            marca = input(f"Nuevo ID de marca ({zapatilla.marca}): ")
            talla = input(f"Nueva talla ({zapatilla.talla}): ")
            precio = input(f"Nuevo precio ({zapatilla.precio}): ")
            categoria_id = input(f"Nuevo ID de categoría ({zapatilla.categoria_id}): ")
            gestor_tienda.actualizar_zapatilla(zapatilla_id, nombre, marca, talla, precio, categoria_id)
            print("Zapatilla actualizada con éxito.")
        else:
            print("Zapatilla no encontrada.")

    def leer_zapatilla(self, zapatilla_id):
        query = "SELECT * FROM Zapatilla WHERE id = %s"
        values = (zapatilla_id,)
        self.cursor.execute(query, values)
        zapatilla = self.cursor.fetchone()
        if zapatilla:
            return Zapatilla(zapatilla[0], zapatilla[1], zapatilla[2], zapatilla[3], zapatilla[4], zapatilla[5])
        else:
            return None
    
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
        
def main():
    host = 'localhost'
    user = 'root'
    password = 'Emiliano29782978'
    database = 'TIENDA_ONLINE'
    gestor_tienda = GestorTienda(host, user, password, database)


    while True:
        print("\nMenú:")
        print("1. Mostrar zapatillas")
        print("2. Crear zapatilla")
        print("3. Actualizar zapatilla")
        print("4. Eliminar zapatilla")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestor_tienda.mostrar_zapatillas()
        elif opcion == "2":
            nombre = input("Nombre de la zapatilla: ")
            marca = input(" marca: ")
            talla = input("Talla: ")
            precio = input("Precio: ")
            categoria_id = input("ID de la categoría: ")
            gestor_tienda.crear_zapatilla(nombre, marca, talla, precio, categoria_id)
        elif opcion == "3":
            zapatilla_id = input("ID de la zapatilla a actualizar: ")
            nombre = input("Nuevo nombre: ")
            marca = input(" marca: ")
            talla = input("Nueva talla: ")
            precio = input("Nuevo precio: ")
            categoria_id = input("Nuevo ID de categoría: ")
            gestor_tienda.actualizar_zapatilla(zapatilla_id, nombre, marca, talla, precio, categoria_id)
        elif opcion == "4":
            zapatilla_id = input("ID de la zapatilla a eliminar: ")
            gestor_tienda.eliminar_zapatilla(zapatilla_id)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()