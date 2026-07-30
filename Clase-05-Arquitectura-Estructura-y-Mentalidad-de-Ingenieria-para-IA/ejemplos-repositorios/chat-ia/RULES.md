# RULES.md - Reglas del Proyecto

## Reglas Generales
1. **Idioma:** Todo el código y comentarios en español
2. **Estilo:** Sigue PEP 8 para Python
3. **Documentación:** Docstrings en todas las funciones públicas
4. **Type hints:** Usa anotaciones de tipo en todas las funciones
5. **Pruebas:** Cada función debe tener al menos una prueba unitaria

## Reglas de Código
1. **Funciones:** Máximo 20 líneas por función
2. **Archivos:** Máximo 300 líneas por archivo
3. **Clases:** Una clase por archivo (excepto helpers pequeños)
4. **Imports:** Ordena: estándar → externos → locales
5. **Variables:** Usa nombres descriptivos, nunca abreviaciones crípticas

## Reglas de Seguridad
1. **Credenciales:** NUNCA las guardes en código fuente
2. **Datos sensibles:** Usa variables de entorno (.env)
3. **Logs:** Nunca loguees información personal identificable
4. **Dependencias:** Actualiza las dependencias mensualmente
5. **Backups:** Mantén backups de la base de datos diarios

## Reglas de Trabajo en Equipo
1. **Commits:** Mensajes claros y descriptivos en español
2. **Branches:** Usa prefijos (feature/, bugfix/, hotfix/)
3. **Pull Requests:** Siempre incluye descripción de cambios
4. **Reviews:** Revisa al menos 2 PRs antes de merging
5. **Documentación:** Actualiza README.md con cada cambio significativo