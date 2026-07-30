# Ejemplo: Bases de Datos

## ¿Qué es una Base de Datos?

Un sistema para almacenar, organizar y consultar información de forma estructurada. Es el "cerebro" que recuerda todo lo que pasa en tu aplicación.

## Estructura del Repositorio

```
mi_base_datos_ia/
│
├── .github/
│   └── copilot-instructions.md    # GitHub Copilot lee esto automáticamente
│
├── .gemini/
│   └── instructions.md            # Gemini lee esto automáticamente
│
├── CODEX.md                       # Codex (OpenAI) lee esto automáticamente
├── CLAUDE.md                      # Claude lee esto automáticamente
├── GLM.md                         # ChatGLM lee esto automáticamente
├── ZAI.md                         # Z.ai (Zhipu) lee esto automáticamente
├── GROK.md                        # Grok (xAI) lee esto automáticamente
│
├── CONTEXT.md                     # ESTÁNDAR: Lo leen todas las plataformas
├── RULES.md                       # ESTÁNDAR: Lo leen todas las plataformas
├── SECURITY.md                    # ESTÁNDAR: CRÍTICO para bases de datos
│
├── SCHEMA.md                      # NUEVO: Diagrama de la estructura de tablas
├── MIGRATIONS.md                  # NUEVO: Historial de cambios en la estructura
│
├── data/
│   ├── schema/
│   │   ├── crear_tablas.sql       # Script para crear la estructura
│   │   ├── datos_iniciales.sql    # Datos de prueba
│   │   └── vistas.sql             # Vistas útiles
│   ├── backups/
│   │   ├── backup_2024_01_15.sql  # Copia de seguridad
│   │   └── backup_semanal.sql
│   └── seeds/
│       ├── usuarios_ejemplo.csv
│       └── productos_ejemplo.csv
│
├── src/
│   ├── __init__.py
│   ├── conexion.py                # Conexión a la base de datos
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── usuario.py             # Modelo de usuario
│   │   ├── producto.py            # Modelo de producto
│   │   ├── transaccion.py         # Modelo de transacción
│   │   └── base.py                # Modelo base con métodos comunes
│   ├── consultas/
│   │   ├── __init__.py
│   │   ├── busqueda.py            # Consultas de búsqueda
│   │   ├── reportes.py            # Consultas para reportes
│   │   └── estadisticas.py        # Consultas estadísticas
│   └── utilidades/
│       ├── __init__.py
│       ├── validacion.py          # Validación de datos
│       ├── encriptacion.py        # Encriptación de contraseñas
│       └── logger.py              # Registro de actividad
│
├── migrations/                    # Cambios en la estructura de la BD
│   ├── 001_crear_tabla_usuarios.py
│   ├── 002_agregar_columna_email.py
│   ├── 003_crear_tabla_transacciones.py
│   └── 004_agregar_indices.py
│
├── tests/
│   ├── test_conexion.py
│   ├── test_modelos.py
│   ├── test_consultas.py
│   └── test_migraciones.py
│
├── .gitignore
├── .env
├── requirements.txt
└── README.md
```

## Archivos de Configuración para IA

### CODEX.md (Para Codex/OpenAI)
```markdown
Eres un desarrollador de bases de datos especializado en PostgreSQL.

REGLAS:
1. USA SQL estándar (ANSI SQL)
2. ESCRIBE migraciones reversibles
3. NUNCA uses DROP TABLE sin confirmación
4. SIEMPRE crea índices para búsquedas frecuentes
5. USA transacciones para operaciones críticas
6. DOCUMENTA cada cambio en MIGRATIONS.md
7. USA ORM (SQLAlchemy) para el código Python
```

### CLAUDE.md (Para Claude)
```markdown
## Principios de Diseño de BD

### Normalización
1. **1NF:** Cada columna tiene un solo valor atómico
2. **2NF:** No hay dependencias parciales
3. **3NF:** No hay dependencias transitivas

### Seguridad
1. **Credenciales:** NUNCA las guardes en código, usa .env
2. **Encriptación:** Contraseñas con bcrypt, datos sensibles con AES
3. **Backups:** Diarios automáticos, retención de 30 días
4. **Acceso:** Principio de mínimo privilegio
5. **Auditoría:** Registra todos los cambios en tablas sensibles

### Rendimiento
1. **Índices:** Crea índices en columnas de búsqueda frecuente
2. **Consultas:** Usa EXPLAIN ANALYZE para optimizar
3. **Pool de conexiones:** Reutiliza conexiones, no crees nuevas
4. **Cache:** Implementa Redis para consultas frecuentes
5. **Paginación:** Nunca hagas SELECT * sin LIMIT

### Mantenimiento
1. **Migraciones:** Siempre reversibles, nunca pierdas datos
2. **Backups:** Prueba restores regularmente
3. **Monitoreo:** Alertas por uso de disco y CPU
4. **Limpieza:** Archiva registros antiguos periódicamente
```

### SCHEMA.md (Nuevo: Diagrama de la BD)
```markdown
# Diagrama de la Base de Datos

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

## Relaciones
- Un **usuario** puede tener muchas **transacciones**
- Un **producto** puede estar en muchas **transacciones**
- Cada **transacción** pertenece a un **usuario** y un **producto**
```

### MIGRATIONS.md (Nuevo: Historial de Cambios)
```markdown
# Historial de Migraciones

## 001 - Crear tabla usuarios (2024-01-10)
- **Autor:** Juan Pérez
- **Cambios:** Creación inicial de la tabla usuarios
- **Reversible:** Sí (DROP TABLE usuarios)

## 002 - Agregar columna email (2024-01-12)
- **Autor:** María García
- **Cambios:** Se agrega columna email con constraint UNIQUE
- **Reversible:** Sí (ALTER TABLE usuarios DROP COLUMN email)

## 003 - Crear tabla transacciones (2024-01-15)
- **Autor:** Juan Pérez
- **Cambios:** Creación de tabla transacciones con foreign keys
- **Reversible:** Sí (DROP TABLE transacciones)

## 004 - Agregar índices (2024-01-18)
- **Autor:** María García
- **Cambios:** Índices en email, usuario_id, producto_id
- **Reversible:** Sí (DROP INDEX)
```

## Ejemplo de Uso

```
Desarrollador →
1. Diseña el esquema en SCHEMA.md
2. Crea la BD con data/schema/crear_tablas.sql
3. Implementa modelos en src/modelos/
4. Escribe consultas en src/consultas/
5. Crea migraciones en migrations/
6. Ejecuta pruebas en tests/
7. Genera backup en data/backups/
```

## Nota para el Instructor

Las bases de datos son fundamentales para cualquier aplicación. Enseñar:

1. **Seguridad:** Las contraseñas NUNCA se guardan en texto plano
2. **Integridad:** Las foreign keys evitan datos huérfanos
3. **Rendimiento:** Los índices aceleran las consultas
4. **Backups:** Si no tienes backup, no tienes datos
5. **Migraciones:** Los cambios en la BD deben ser reversibles