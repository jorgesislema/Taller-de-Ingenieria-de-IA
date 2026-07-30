# CLAUDE.md - Configuración para Claude

## Identidad del Proyecto
Creamos páginas web inteligentes que integran IA para mejorar la experiencia del usuario.

## Reglas de Diseño
1. **Responsive:** La página debe funcionar en móvil, tablet y desktop
2. **Accesible:** Cumple con WCAG 2.1 nivel AA
3. **Rápida:** Carga máxima de 3 segundos
4. **Segura:** HTTPS, CSP headers, sanitización de entradas

## Reglas Técnicas
- **Frontend:** HTML5, CSS3, JavaScript (ES6+)
- **Backend:** Python 3.8+ con FastAPI
- **IA:** APIs de OpenAI, Claude, modelos open source
- **Base de Datos:** SQLite (desarrollo), PostgreSQL (producción)
- **Despliegue:** Docker + Nginx

## Reglas de Código
1. **Frontend:** Modulariza el JavaScript en archivos separados
2. **Backend:** Usa arquitectura de capas (API → Lógica → Datos)
3. **IA:** Implementa fallback si la API de IA falla
4. **Logs:** Registra todos los errores y eventos importantes

## Lo que NO debes hacer
- NO expongas API keys en el frontend
- NO uses HTTP en producción (solo HTTPS)
- NO omitas validación de entradas del usuario
- NO ignores errores de la API de IA
- NO hagas llamadas a la API de IA sin timeout