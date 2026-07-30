# RULES.md - Reglas del Proyecto

## Reglas Generales
1. **Idioma:** Todo el código y comentarios en español
2. **Estilo:** Sigue PEP 8 para Python
3. **Documentación:** Docstrings en todas las funciones públicas
4. **Type hints:** Usa anotaciones de tipo en todas las funciones
5. **Pruebas:** Cada función debe tener al menos una prueba unitaria

## Reglas del Agente
1. **Transparencia:** Cada acción debe quedar registrada en auditoria_seguridad.md
2. **Confirmación:** Antes de acciones destructivas, SIEMPRE preguntar al usuario
3. **Aprendizaje:** Los errores deben documentarse en errores_aprendidos.md
4. **Límites:** Respeta los límites definidos en TOOLS.md
5. **Memoria:** Usa la memoria de forma responsable (MEMORY.md)

## Reglas de Seguridad
1. **Credenciales:** NUNCA las guardes en código fuente
2. **Datos sensibles:** Usa variables de entorno (.env)
3. **Logs:** Nunca loguees información personal identificable
4. **Dependencias:** Actualiza las dependencias mensualmente
5. **Backups:** Mantén backups de la memoria diarios

## Reglas de Trabajo en Equipo
1. **Commits:** Mensajes claros y descriptivos en español
2. **Branches:** Usa prefijos (feature/, bugfix/, hotfix/)
3. **Pull Requests:** Siempre incluye descripción de cambios
4. **Reviews:** Revisa al menos 2 PRs antes de merging
5. **Documentación:** Actualiza README.md con cada cambio significativo