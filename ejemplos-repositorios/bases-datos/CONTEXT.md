# CONTEXT.md - Contexto del Proyecto

## Quiénes Somos
Somos un equipo de bases de datos que diseña, implementa y mantiene sistemas para almacenar, organizar y consultar información de forma estructurada y segura.

## Nuestro Objetivo
Crear sistemas de bases de datos que:
- Almacenen información de forma segura
- Permitan consultas rápidas y eficientes
- Mantengan la integridad de los datos
- Sean fáciles de mantener y escalar

## Tecnologías que Usamos
- **Base de Datos:** PostgreSQL
- **ORM:** SQLAlchemy
- **Migraciones:** Alembic
- **Backups:** pg_dump
- **Monitoreo:** pg_stat_statements

## Principios de Diseño
1. **Normalización:** Evitar redundancia de datos
2. **Integridad:** Foreign keys para consistencia
3. **Rendimiento:** Índices y optimización
4. **Seguridad:** Credenciales en .env, encriptación
5. **Mantenimiento:** Migraciones reversibles, backups

## Nuestros Datos
- **Usuarios:** Información de clientes y empleados
- **Productos:** Catálogo de productos
- **Transacciones:** Ventas y compras
- **Inventario:** Stock de productos
- **Logs:** Registro de actividad