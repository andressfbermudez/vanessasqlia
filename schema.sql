-- ============================================
-- CREACIÓN DE TABLAS
-- ============================================

CREATE TABLE empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    puesto VARCHAR(50),
    salario DECIMAL(10,2),
    fecha_contratacion DATE
);

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefono VARCHAR(20),
    direccion VARCHAR(150)
);

CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    precio DECIMAL(10,2),
    stock INT
);

CREATE TABLE vehiculos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    año INT,
    precio DECIMAL(10,2)
);

CREATE TABLE ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_empleado INT,
    id_producto INT,
    fecha DATE,
    cantidad INT,
    total DECIMAL(10,2),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id),
    FOREIGN KEY (id_empleado) REFERENCES empleados(id),
    FOREIGN KEY (id_producto) REFERENCES productos(id)
);

-- ============================================
-- INSERTAR DATOS DE EJEMPLO
-- ============================================

INSERT INTO empleados (nombre, puesto, salario, fecha_contratacion) VALUES
('Carlos Pérez', 'Vendedor', 1200.00, '2021-03-10'),
('Ana Gómez', 'Gerente', 2500.00, '2019-06-15'),
('Luis Torres', 'Mecánico', 1500.00, '2020-08-20'),
('María López', 'Contadora', 1800.00, '2021-11-05'),
('Pedro Sánchez', 'Recepcionista', 1000.00, '2022-01-10'),
('Lucía Díaz', 'Vendedora', 1300.00, '2023-04-22'),
('José Ruiz', 'Supervisor', 2000.00, '2020-02-28'),
('Elena García', 'Asistente', 1100.00, '2022-09-12'),
('Miguel Rojas', 'Jefe Taller', 2200.00, '2018-12-01'),
('Laura Romero', 'Analista', 1600.00, '2021-05-18');

INSERT INTO clientes (nombre, email, telefono, direccion) VALUES
('Juan Herrera', 'juan.herrera@mail.com', '555-1234', 'Calle 1 #123'),
('Rosa Martínez', 'rosa.martinez@mail.com', '555-2345', 'Av. Las Flores 45'),
('David Ramírez', 'david.ramirez@mail.com', '555-3456', 'Calle Luna 89'),
('Claudia Vargas', 'claudia.vargas@mail.com', '555-4567', 'Calle Sol 102'),
('Andrés Castro', 'andres.castro@mail.com', '555-5678', 'Av. Norte 300'),
('Patricia León', 'patricia.leon@mail.com', '555-6789', 'Calle Sur 21'),
('Ricardo Ortiz', 'ricardo.ortiz@mail.com', '555-7890', 'Av. Central 56'),
('Marta Pérez', 'marta.perez@mail.com', '555-8901', 'Calle Este 200'),
('Sergio Molina', 'sergio.molina@mail.com', '555-9012', 'Calle Oeste 99'),
('Natalia Fuentes', 'natalia.fuentes@mail.com', '555-0123', 'Av. Colón 15');

INSERT INTO productos (nombre, categoria, precio, stock) VALUES
('Aceite Motor 5W30', 'Lubricantes', 25.50, 100),
('Filtro de Aire', 'Filtros', 12.00, 80),
('Batería 12V', 'Eléctrico', 80.00, 50),
('Neumático 195/65R15', 'Llantas', 95.00, 60),
('Freno de Disco', 'Frenos', 45.00, 40),
('Anticongelante', 'Líquidos', 18.00, 70),
('Filtro de Combustible', 'Filtros', 14.00, 90),
('Limpiaparabrisas', 'Accesorios', 10.00, 120),
('Aceite Caja Automática', 'Lubricantes', 30.00, 40),
('Bujía NGK', 'Motor', 8.00, 200);

INSERT INTO vehiculos (marca, modelo, año, precio) VALUES
('Toyota', 'Corolla', 2020, 18000.00),
('Honda', 'Civic', 2019, 17500.00),
('Ford', 'Focus', 2021, 19000.00),
('Chevrolet', 'Onix', 2020, 16500.00),
('Nissan', 'Versa', 2022, 17000.00),
('Mazda', '3', 2021, 19500.00),
('Hyundai', 'Elantra', 2020, 18500.00),
('Kia', 'Rio', 2022, 16000.00),
('Volkswagen', 'Jetta', 2019, 17800.00),
('Renault', 'Logan', 2021, 15500.00);

INSERT INTO ventas (id_cliente, id_empleado, id_producto, fecha, cantidad, total) VALUES
(1, 1, 1, '2023-01-15', 2, 51.00),
(2, 2, 3, '2023-02-10', 1, 80.00),
(3, 3, 4, '2023-02-25', 4, 380.00),
(4, 1, 2, '2023-03-05', 3, 36.00),
(5, 5, 5, '2023-03-12', 2, 90.00),
(6, 4, 7, '2023-04-01', 5, 70.00),
(7, 6, 8, '2023-04-18', 10, 100.00),
(8, 7, 9, '2023-05-03', 3, 90.00),
(9, 8, 10, '2023-05-15', 8, 64.00),
(10, 9, 6, '2023-06-10', 2, 36.00);
