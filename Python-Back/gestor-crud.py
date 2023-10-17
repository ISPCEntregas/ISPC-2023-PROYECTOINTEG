from flask import Flask, request, jsonify
from flask_cors import CORS
from modulos_tienda import GestorTienda

app = Flask(__name__)
CORS(app) 

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'Emiliano29782978'
DB_DATABASE = 'TIENDA_ONLINE'

gestor = GestorTienda(DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE)

@app.route('/zapatillas', methods=['GET'])
def seleccionar_zapatillas():
    zapatillas = gestor.seleccionar_zapatillas()

    zapatillas_json = [{'id': zapatilla[0], 'nombre': zapatilla[1], 'marca': zapatilla[2], 'talla': zapatilla[3], 'precio': zapatilla[4], 'categoria': zapatilla[5]} for zapatilla in zapatillas]
    return jsonify(zapatillas_json)

@app.route('/zapatillas', methods=['POST'])
def crear_zapatilla():

    data = request.get_json()
    nombre = data['nombre']
    marca_id = data['marca_id']
    talla = data['talla']
    precio = data['precio']
    categoria_id = data['categoria_id']
    gestor.crear_zapatilla(nombre, marca_id, talla, precio, categoria_id)
    return 'Zapatilla creada con éxito'

@app.route('/zapatillas/<int:zapatilla_id>', methods=['PUT'])
def actualizar_zapatilla(zapatilla_id):

    data = request.get_json()
    nombre = data['nombre']
    marca_id = data['marca_id']
    talla = data['talla']
    precio = data['precio']
    categoria_id = data['categoria_id']
    gestor.actualizar_zapatilla(zapatilla_id, nombre, marca_id, talla, precio, categoria_id)
    return 'Zapatilla actualizada con éxito'

@app.route('/zapatillas/<int:zapatilla_id>', methods=['DELETE'])
def eliminar_zapatilla(zapatilla_id):
    gestor.eliminar_zapatilla(zapatilla_id)
    return 'Zapatilla eliminada con éxito'
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
    


# Modelo de Caso de Uso: Gestión de Zapatillas en la Tienda en Línea
# Este caso de uso describe cómo un usuario administrador interactúa con la funcionalidad de gestión de zapatillas.


# Flujo Básico - Caso de Uso CRUD:

# 1. Crear Zapatilla
#    - El usuario administrador selecciona la opción "Crear Zapatilla".
#    - El sistema muestra un formulario vacío para ingresar los detalles de la nueva zapatilla.
#    - El usuario administra completa los campos del formulario, como nombre, marca, talla, precio, categoría, etc.
#    - El usuario administra hace clic en el botón "Crear Zapatilla".
#    - El sistema valida la información ingresada y crea la nueva zapatilla en la base de datos.

# 2. Leer Zapatilla
#    - El usuario administrador selecciona la opción "Ver Lista de Zapatillas".
#    - El sistema muestra una lista de zapatillas disponibles con detalles básicos, como nombre, marca y precio.
#    - El usuario administrador puede hacer clic en una zapatilla de la lista para ver más detalles.

# 3. Actualizar Zapatilla
#    - El usuario administrador selecciona una zapatilla existente y elige la opción "Editar Zapatilla".
#    - El sistema muestra un formulario prellenado con los detalles actuales de la zapatilla.
#    - El usuario administra realiza cambios en los detalles de la zapatilla, como actualizar el nombre, la marca o el precio.
#    - El usuario administra hace clic en el botón "Guardar".
#    - El sistema valida la información ingresada y actualiza los detalles de la zapatilla en la base de datos.

# 4. Eliminar Zapatilla
#    - El usuario administrador selecciona una zapatilla existente y elige la opción "Eliminar Zapatilla".
#    - El sistema muestra una confirmación.
#    - El usuario administra confirma la eliminación.
#    - El sistema elimina la zapatilla de la base de datos.

# Flujo Alternativo:

# - En los flujos 1, 3 y 4, si se produce un error en la validación o en la base de datos, el sistema muestra un mensaje de error y permite al usuario administrador corregir la información.

# Poscondiciones:
# - Las zapatillas se crean, actualizan, leen y eliminan en la base de datos según las acciones realizadas por el usuario administrador.
