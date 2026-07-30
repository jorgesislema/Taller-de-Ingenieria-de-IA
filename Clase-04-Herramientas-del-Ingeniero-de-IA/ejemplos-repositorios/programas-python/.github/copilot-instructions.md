# Instrucciones para GitHub Copilot - Programas Python

## Identidad del Proyecto
Somos un equipo de desarrollo Python que crea scripts, automatizaciones, procesamiento de archivos, utilidades, APIs y análisis de datos.

## Reglas de Comportamiento
1. **Código limpio:** Sigue PEP 8 (guía de estilo de Python)
2. **Documentación:** Docstrings en todas las funciones públicas
3. **Type hints:** Usa anotaciones de tipo en todas las funciones
4. **Pruebas:** Cada función debe tener al menos una prueba unitaria
5. **Seguridad:** Nunca guardes credenciales en el código

## Reglas Técnicas
- Python 3.8+ exclusivamente
- Usa virtual environments para dependencias
- Maneja excepciones específicas (no uses Exception genérico)
- USA logging en lugar de print()
- Usa context managers para archivos y conexiones

## Lo que NO debes hacer
- NO guardes contraseñas en el código fuente
- NO ejecutes código de fuentes no confiables
- NO modifiques archivos del sistema operativo
- NO accedas a archivos fuera del proyecto
- NO uses librerías no mantenidas o abandonadas