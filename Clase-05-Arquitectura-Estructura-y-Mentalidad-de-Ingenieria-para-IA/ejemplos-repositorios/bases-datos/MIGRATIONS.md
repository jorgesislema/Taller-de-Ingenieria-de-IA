# MIGRATIONS.md - Historial de Migraciones

## 001 - Crear tabla usuarios (2024-01-10)
- **Autor:** Juan Pérez
- **Cambios:** Creación inicial de la tabla usuarios
- **Script:** `001_crear_tabla_usuarios.sql`
- **Reversible:** Sí (DROP TABLE usuarios)
- **Rollback:** Eliminar la tabla usuarios

## 002 - Agregar columna email (2024-01-12)
- **Autor:** María García
- **Cambios:** Se agrega columna email con constraint UNIQUE
- **Script:** `002_agregar_columna_email.sql`
- **Reversible:** Sí (ALTER TABLE usuarios DROP COLUMN email)
- **Rollback:** Eliminar la columna email

## 003 - Crear tabla transacciones (2024-01-15)
- **Autor:** Juan Pérez
- **Cambios:** Creación de tabla transacciones con foreign keys
- **Script:** `003_crear_tabla_transacciones.sql`
- **Reversible:** Sí (DROP TABLE transacciones)
- **Rollback:** Eliminar la tabla transacciones

## 004 - Agregar índices (2024-01-18)
- **Autor:** María García
- **Cambios:** Índices en email, usuario_id, producto_id
- **Script:** `004_agregar_indices.sql`
- **Reversible:** Sí (DROP INDEX)
- **Rollback:** Eliminar los índices creados

## 005 - Crear tabla inventario (2024-01-20)
- **Autor:** Juan Pérez
- **Cambios:** Creación de tabla inventario con foreign key a productos
- **Script:** `005_crear_tabla_inventario.sql`
- **Reversible:** Sí (DROP TABLE inventario)
- **Rollback:** Eliminar la tabla inventario

## 006 - Agregar vistas (2024-01-22)
- **Autor:** María García
- **Cambios:** Creación de vistas para reportes
- **Script:** `006_agregar_vistas.sql`
- **Reversible:** Sí (DROP VIEW)
- **Rollback:** Eliminar las vistas creadas

## Proceso de Migración
1. **Antes de migrar:** Haz backup de la base de datos
2. **Ejecuta el script:** En orden numérico
3. **Verifica:** Revisa que los cambios se aplicaron correctamente
4. **Documenta:** Actualiza este archivo con el resultado
5. **Si falla:** Ejecuta el rollback correspondiente

## Comandos Útiles
```bash
# Backup antes de migrar
pg_dump -U usuario -d base_datos > backup_$(date +%Y%m%d).sql

# Ejecutar migración
psql -U usuario -d base_datos -f migrations/001_crear_tabla_usuarios.sql

# Verificar migración
psql -U usuario -d base_datos -c "\dt"

# Rollback (si es necesario)
psql -U usuario -d base_datos -c "DROP TABLE IF EXISTS usuarios;"
```