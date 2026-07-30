# RULES.md - Reglas del Proyecto

## Reglas Generales
1. **Idioma:** Todo el código y comentarios en español
2. **Estilo:** Sigue PEP 8 para Python, ESLint para JavaScript
3. **Documentación:** Docstrings en Python, JSDoc en JavaScript
4. **Type hints:** Usa anotaciones de tipo en Python
5. **Pruebas:** Cada endpoint debe tener al menos una prueba

## Reglas de Frontend
1. **Responsive:** Diseño mobile-first
2. **Accesibilidad:** Cumple WCAG 2.1 nivel AA
3. **Performance:** Carga máxima de 3 segundos
4. **Seguridad:** No expongas API keys ni datos sensibles
5. **Modularidad:** Separa el JavaScript en archivos independientes

## Reglas de Backend
1. **API REST:** Usa verbos HTTP correctos (GET, POST, PUT, DELETE)
2. **Validación:** Valida todas las entradas del usuario
3. **Errores:** Maneja errores con códigos HTTP apropiados
4. **Logs:** Registra todos los errores y eventos importantes
5. **Seguridad:** Implementa autenticación y autorización

## Reglas de IA
1. **Fallback:** Siempre implementa un plan B si la IA falla
2. **Timeout:** Nunca hagas llamadas a la IA sin límite de tiempo
3. **Cache:** Almacena respuestas frecuentes para mejorar rendimiento
4. **Costos:** Monitorea el uso de tokens para controlar gastos
5. **Privacidad:** Nunca envíes datos personales a la API de IA