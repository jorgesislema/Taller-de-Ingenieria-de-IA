# RULES.md - Reglas del Proyecto

## Reglas de Diseño
1. **Normalización:** Usa 3NF como estándar
2. **Foreign Keys:** SIEMPRE usa integridad referencial
3. **Nombres:** snake_case para tablas y columnas
4. **Tipos:** Usa tipos de datos apropiados
5. **Índices:** Crea índices en columnas de búsqueda frecuente

## Reglas de Seguridad
1. **Credenciales:** NUNCA las guardes en código
2. **Encriptación:** Contraseñas con bcrypt
3. **Acceso:** Principio de mínimo privilegio
4. **Auditoría:** Registra cambios en tablas sensibles
5. **Backups:** Diarios automáticos, retención 30 días

## Reglas de Rendimiento
1. **Consultas:** Usa EXPLAIN ANALYZE para optimizar
2. **Paginación:** Nunca hagas SELECT * sin LIMIT
3. **Pool:** Reutiliza conexiones
4. **Cache:** Implementa Redis para consultas frecuentes
5. **Archivado:** Mueve registros antiguos a tablas de archivado

## Reglas de Mantenimiento
1. **Migraciones:** Siempre reversibles
2. **Backups:** Prueba restores regularmente
3. **Monitoreo:** Alertas por uso de disco y CPU
4. **Documentación:** Documenta cada cambio
5. **Testing:** Pruebas unitarias para consultas críticas