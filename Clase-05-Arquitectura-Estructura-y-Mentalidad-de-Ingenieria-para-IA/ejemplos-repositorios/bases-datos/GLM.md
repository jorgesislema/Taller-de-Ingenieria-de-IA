# GLM.md - Configuración para ChatGLM (GLM)

## Identidad del Proyecto
Somos un equipo de bases de datos que diseña, implementa y mantiene sistemas para almacenar, organizar y consultar información de forma estructurada y segura.

## Reglas de Generación
1. **SQL:** Usa SQL estándar (ANSI SQL)
2. **Migraciones:** Escribe migraciones reversibles
3. **Seguridad:** Nunca guardes contraseñas en código
4. **Rendimiento:** Crea índices para búsquedas frecuentes
5. **Documentación:** Documenta cada cambio en MIGRATIONS.md

## Principios de Diseño
- Normalización (1NF, 2NF, 3NF)
- Integridad referencial
- Rendimiento con índices
- Seguridad con credenciales en .env
- Backups automáticos

## Formato de Salida
- Código SQL en bloques ````sql`
- Código Python en bloques ````python`
- Explicaciones en texto plano antes y después del código
- Usa markdown para organizar la información

## Restricciones
- NO uses DROP TABLE sin confirmación
- NO guardes contraseñas en el código
- NO hagas SELECT * sin LIMIT
- NO ignores errores de conexión
- SIEMPRE haz migraciones reversibles