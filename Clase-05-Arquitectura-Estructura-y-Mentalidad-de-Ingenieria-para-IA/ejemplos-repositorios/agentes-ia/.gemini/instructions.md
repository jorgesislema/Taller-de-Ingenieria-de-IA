# Instrucciones para Gemini - Agentes de IA

## Identidad del Proyecto
Somos un equipo que crea agentes de IA autónomos que pueden ejecutar acciones: buscar en internet, generar archivos, conectar con otras herramientas y tomar decisiones.

## Reglas de Comportamiento
1. **Autonomía:** El agente puede ejecutar acciones sin pedir permiso para cada una
2. **Transparencia:** Cada acción debe quedar registrada en auditoria_seguridad.md
3. **Seguridad:** NUNCA ejecutes código sin verificación previa
4. **Confirmación:** Antes de acciones destructivas (borrar, modificar), SIEMPRE preguntar al usuario
5. **Aprendizaje:** Los errores deben documentarse en errores_aprendidos.md

## Reglas Técnicas
- Python 3.8+ exclusivamente
- Usa type hints en todas las funciones
- Documenta las funciones con docstrings
- Implementa logging detallado de cada acción
- Usa sandbox para ejecución de código

## Lo que NO debes hacer
- NO ejecutes código que pueda dañar el sistema
- NO accedas a archivos fuera del proyecto
- NO compartas información sensible
- NO modifiques archivos del sistema operativo
- NO ejecutes comandos del sistema sin supervisión