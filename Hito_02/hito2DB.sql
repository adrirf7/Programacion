drop database if exists HITO_02;
create database HITO_02;
use HITO_02;

CREATE TABLE Clientes (
    idCliente INT AUTO_INCREMENT PRIMARY KEY,
	correo VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL
);

CREATE TABLE Categorias (
    idCategoria INT AUTO_INCREMENT PRIMARY KEY,
    nombreCategoria VARCHAR(50) NOT NULL
);

CREATE TABLE Productos (
    idProducto INT AUTO_INCREMENT PRIMARY KEY,
    nombreProducto VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    idCategoria INT,
    FOREIGN KEY (idCategoria) REFERENCES Categorias(idCategoria)
);

CREATE TABLE Pedidos (
    idPedido INT AUTO_INCREMENT PRIMARY KEY,
    idCliente INT,
    fechaPedido DATETIME NOT NULL,
    fechaEntrega DATETIME NOT NULL,
    direccionEntrega varchar(255),
    totalPedido DECIMAL(10, 2),
    FOREIGN KEY (idCliente) REFERENCES Clientes(idCliente)
);

CREATE TABLE Detalles_Pedido (
    idDetalle INT AUTO_INCREMENT PRIMARY KEY,
    idPedido INT,
    idProducto INT,
    cantidad INT NOT NULL,
    precioUnitario DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(10, 2),
    FOREIGN KEY (idPedido) REFERENCES Pedidos(idPedido),
    FOREIGN KEY (idProducto) REFERENCES Productos(idProducto)
);
CREATE TABLE Carrito (
    idCliente INT NOT NULL,
    idProducto INT,
    cantidad INT NOT NULL,
    precioUnitario DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(10, 2),
    FOREIGN KEY (idCliente) REFERENCES Clientes(idCliente),
    FOREIGN KEY (idProducto) REFERENCES Productos(idProducto)
);


INSERT INTO Categorias (nombreCategoria)
VALUES 
    ('Electrónica'),
    ('Ropa'),
    ('Hogar'),
    ('Juguetes'),
    ('Libros');

-- Productos de la categoría Electrónica
INSERT INTO Productos (nombreProducto, precio, stock, idCategoria)
VALUES 
    ('Smartphone XYZ', 499.99, 50, 1),
    ('Laptop ABC', 899.99, 30, 1),
    ('Auriculares Bluetooth', 59.99, 100, 1),
    ('Televisor 4K 55 pulgadas', 799.99, 20, 1),
    ('Tablet 10 pulgadas', 299.99, 40, 1),
    ('Reloj Inteligente', 149.99, 60, 1),
    ('Cámara Digital', 349.99, 25, 1),
    ('Consola de Videojuegos', 499.99, 15, 1),
    ('Altavoz Portátil', 79.99, 80, 1),
    ('Cargador Inalámbrico', 29.99, 120, 1),
    ('Disco Duro Externo 1TB', 89.99, 70, 1);

-- Productos de la categoría Ropa
INSERT INTO Productos (nombreProducto, precio, stock, idCategoria)
VALUES 
    ('Camiseta Unisex', 19.99, 100, 2),
    ('Sudadera con Capucha', 29.99, 80, 2),
    ('Jeans para Hombre', 39.99, 60, 2),
    ('Falda Plisada', 24.99, 50, 2),
    ('Chaqueta de Cuero', 99.99, 40, 2),
    ('Zapatillas Deportivas', 49.99, 90, 2),
    ('Calcetines de Algodón (Pack de 5)', 9.99, 150, 2),
    ('Gorra Unisex', 14.99, 120, 2),
    ('Guantes de Invierno', 12.99, 110, 2),
    ('Bufanda de Lana', 19.99, 100, 2);

-- Productos de la categoría Hogar
INSERT INTO Productos (nombreProducto, precio, stock, idCategoria)
VALUES 
    ('Sofá 3 Plazas', 299.99, 15, 3),
    ('Set de Ollas', 79.99, 25, 3),
    ('Mesa de Centro', 59.99, 30, 3),
    ('Lámpara de Techo', 45.99, 50, 3),
    ('Cafetera Eléctrica', 39.99, 40, 3),
    ('Silla de Oficina', 89.99, 35, 3),
    ('Juego de Sábanas Queen', 29.99, 60, 3),
    ('Almohada Ergonómica', 19.99, 100, 3),
    ('Cuchillos de Cocina (Set de 6)', 24.99, 70, 3),
    ('Espejo Decorativo', 49.99, 40, 3),
    ('Ventilador de Torre', 69.99, 20, 3),
    ('Estante de Pared', 34.99, 45, 3);

-- Productos de la categoría Juguetes
INSERT INTO Productos (nombreProducto, precio, stock, idCategoria)
VALUES 
    ('Muñeca Interactiva', 39.99, 40, 4),
    ('Juego de Construcción', 49.99, 35, 4),
    ('Pelota de Fútbol', 19.99, 70, 4),
    ('Rompecabezas de 1000 Piezas', 14.99, 60, 4),
    ('Pista de Coches', 29.99, 50, 4),
    ('Set de Plastilina', 9.99, 90, 4),
    ('Dinosaurio de Juguete', 24.99, 80, 4),
    ('Libro para Colorear', 4.99, 120, 4),
    ('Bloques de Construcción', 19.99, 85, 4),
    ('Avión a Control Remoto', 59.99, 20, 4),
    ('Patinete Infantil', 69.99, 25, 4),
    ('Peluche Grande', 29.99, 40, 4);

-- Productos de la categoría Libros
INSERT INTO Productos (nombreProducto, precio, stock, idCategoria)
VALUES 
    ('Novela Misterio', 15.99, 80, 5),
    ('Manual de SQL', 29.99, 50, 5),
    ('Libro de Cocina Saludable', 19.99, 40, 5),
    ('Guía de Viaje a Europa', 24.99, 30, 5),
    ('Cuentos para Niños', 9.99, 100, 5),
    ('Enciclopedia de Ciencia', 49.99, 20, 5),
    ('Historia del Arte', 39.99, 25, 5),
    ('Diccionario Inglés-Español', 14.99, 60, 5),
    ('Autobiografía Famosa', 19.99, 45, 5),
    ('Novela de Ciencia Ficción', 12.99, 70, 5),
    ('Guía de Jardinería', 17.99, 35, 5),
    ('Libro de Autoayuda', 13.99, 80, 5),
    ('Revista de Tecnología', 5.99, 120, 5);





