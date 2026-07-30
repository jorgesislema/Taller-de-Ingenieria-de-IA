# Instrucciones para Gemini - Bases de Datos

## Identidad del Proyecto
Somos un equipo de bases de datos que diseña, implementa y mantiene sistemas para almacenar, organizar y consultar información de forma estructurada y segura.

## Reglas de Comportamiento
1. **Seguridad:** Las contraseñas NUNCA se guardan en texto plano
2. **Integridad:** Las foreign keys evitan datos huérfanos
3. **Rendimiento:** Los índices aceleran las consultas
4. **Backups:** Si no tienes backup, no tienes datos
5. **Migraciones:** Los cambios en la BD deben ser reversibles

## Reglas Técnicas
- Usa SQL estándar (ANSI SQL)
- Escribe migraciones reversibles
- USA ORM (SQLAlchemy) para el código Python
- Implementa pool de conexiones
- Usa transacciones para operaciones críticas

## Lo que NO debes hacer
- NO uses DROP TABLE sin confirmación
- NO guardes contraseñas en el código
- NO hagas SELECT * sin LIMIT
- NO ignores errores de conexión
- NO hagas migraciones sin backup previo