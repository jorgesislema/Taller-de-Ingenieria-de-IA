# CLAUDE.md - Configuración para Claude

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

## Lo que NO debes hacer
- NO uses DROP TABLE sin confirmación
- NO guardes contraseñas en el código
- NO hagas SELECT * sin LIMIT
- NO ignores errores de conexión
- NO hagas migraciones sin backup previo