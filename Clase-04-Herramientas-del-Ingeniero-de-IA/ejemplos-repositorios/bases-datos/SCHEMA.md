# SCHEMA.md - Diagrama de la Base de Datos

## Tabla: usuarios
```sql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE,
    rol VARCHAR(20) DEFAULT 'usuario'
);
```

## Tabla: productos
```sql
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    stock INTEGER DEFAULT 0,
    categoria VARCHAR(50),
    activo BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Tabla: transacciones
```sql
CREATE TABLE transacciones (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id),
    producto_id INTEGER REFERENCES productos(id),
    cantidad INTEGER NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    estado VARCHAR(20) DEFAULT 'pendiente',
    fecha_transaccion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Tabla: inventario
```sql
CREATE TABLE inventario (
    id SERIAL PRIMARY KEY,
    producto_id INTEGER REFERENCES productos(id),
    cantidad INTEGER NOT NULL,
    ubicacion VARCHAR(100),
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Relaciones
- Un **usuario** puede tener muchas **transacciones**
- Un **producto** puede estar en muchas **transacciones**
- Un **producto** tiene un registro en **inventario**
- Cada **transacción** pertenece a un **usuario** y un **producto**

## Índices
```sql
-- Índices para búsquedas frecuentes
CREATE INDEX idx_usuarios_email ON usuarios(email);
CREATE INDEX idx_transacciones_usuario ON transacciones(usuario_id);
CREATE INDEX idx_transacciones_producto ON transacciones(producto_id);
CREATE INDEX idx_transacciones_fecha ON transacciones(fecha_transaccion);
CREATE INDEX idx_productos_categoria ON productos(categoria);
```

## Vistas Útiles
```sql
-- Vista de ventas por usuario
CREATE VIEW ventas_por_usuario AS
SELECT 
    u.nombre,
    COUNT(t.id) as num_transacciones,
    SUM(t.total) as total_ventas
FROM usuarios u
JOIN transacciones t ON u.id = t.usuario_id
GROUP BY u.id, u.nombre;

-- Vista de productos más vendidos
CREATE VIEW productos_mas_vendidos AS
SELECT 
    p.nombre,
    SUM(t.cantidad) as total_vendido,
    SUM(t.total) as ingreso_total
FROM productos p
JOIN transacciones t ON p.id = t.producto_id
GROUP BY p.id, p.nombre
ORDER BY total_vendido DESC;
```