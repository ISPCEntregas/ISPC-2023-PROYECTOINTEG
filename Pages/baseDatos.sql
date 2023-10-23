CREATE TABLE Marca (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
);

CREATE TABLE Categoria (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
);

CREATE TABLE Zapatilla (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    marca_id INTEGER,
    talla REAL NOT NULL,
    precio REAL NOT NULL,
    categoria_id INTEGER,
    FOREIGN KEY (marca_id) REFERENCES Marca(id),
    FOREIGN KEY (categoria_id) REFERENCES Categoria(id)
);

CREATE TABLE Cliente (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    direccion TEXT
);

CREATE TABLE Pedido (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER NOT NULL,
    fecha_pedido DATE NOT NULL,
    estado TEXT NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Cliente(id)
);

CREATE TABLE LineaPedido (
    id INTEGER PRIMARY KEY,
    pedido_id INTEGER NOT NULL,
    zapatilla_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES Pedido(id),
    FOREIGN KEY (zapatilla_id) REFERENCES Zapatilla(id)
);
