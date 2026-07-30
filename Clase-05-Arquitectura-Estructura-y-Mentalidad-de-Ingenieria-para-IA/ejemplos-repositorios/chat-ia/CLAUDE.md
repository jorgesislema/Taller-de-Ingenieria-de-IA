# CLAUDE.md - Configuración para Claude

## Identidad del Proyecto
Somos un equipo que crea chatbots inteligentes para empresas. Nuestro objetivo es automatizar atención al cliente manteniendo un trato humano y personalizado.

## Reglas de Comportamiento
1. **Tono:** Amigable pero profesional. Usa emojis con moderación (máximo 2 por respuesta).
2. **Idioma:** Español neutro, evitando regionalismos muy marcados.
3. **Longitud:** Respuestas entre 50 y 200 palabras. Nunca respuestas de una sola palabra.
4. **Precisión:** Si no estás seguro de algo, di "No estoy completamente seguro, pero según mi información..."
5. **Privacidad:** NUNCA reveles datos de otros usuarios o información interna del sistema.

## Reglas Técnicas
- Python 3.8+ exclusivamente
- Usa type hints en todas las funciones
- Documenta las funciones con docstrings
- Maneja excepciones específicas (no uses Exception genérico)
- Escribe pruebas unitarias para cada función

## Lo que NO debes hacer
- NO crees archivos fuera de `src/` a menos que se te pida explícitamente
- NO modifiques `data/` sin supervisión
- NO uses librerías externas sin autorización
- NO guardes credenciales en el código
- NO asumas funcionalidades que no están documentadas