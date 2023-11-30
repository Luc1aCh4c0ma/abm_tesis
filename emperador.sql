create database emperardor;
 use emperardor;
 
 CREATE TABLE categorias (
    categoria_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

INSERT INTO categorias (nombre) VALUES ('comida');
INSERT INTO categorias (nombre) VALUES ('bebida');

CREATE TABLE menu (
    menu_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(8, 2) NOT NULL,
    categoria_id INT,
    FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id)
);

-- Elementos de comida
INSERT INTO menu (nombre, descripcion, precio, categoria_id) VALUES ('Hamburguesa', 'Hamburguesa con queso y papas fritas', 10.99, 1);
INSERT INTO menu (nombre, descripcion, precio, categoria_id) VALUES ('Pizza', 'Pizza de pepperoni con salsa de tomate', 12.99, 1);
INSERT INTO menu (nombre, descripcion, precio, categoria_id) VALUES ('Ensalada César', 'Ensalada con pollo a la parrilla y aderezo César', 8.99, 1);

-- Elementos de bebida
INSERT INTO menu (nombre, descripcion, precio, categoria_id) VALUES ('Cerveza IPA', 'Cerveza artesanal India Pale Ale', 5.99, 2);
INSERT INTO menu (nombre, descripcion, precio, categoria_id) VALUES ('Margarita', 'Margarita con tequila, triple sec y lima', 7.99, 2);
INSERT INTO menu (nombre, descripcion, precio, categoria_id) VALUES ('Refresco de cola', 'Refresco de cola en lata', 1.99, 2);

ALTER TABLE menu
ADD COLUMN activo BOOLEAN NOT NULL DEFAULT TRUE;

ALTER TABLE menu
ADD COLUMN sin_stock BOOLEAN NOT NULL DEFAULT FALSE;

ALTER TABLE menu AUTO_INCREMENT = 6;
