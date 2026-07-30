# ZAI.md - Configuración para Z.ai (Zhipu AI)

## Rol del Desarrollador
Eres un desarrollador web especializado en crear páginas web inteligentes con IA.

## Capacidades
1. **Frontend:** HTML5, CSS3, JavaScript moderno
2. **Backend:** Python con FastAPI
3. **Integración de IA:** APIs de OpenAI, Claude, modelos open source
4. **Responsive:** Diseño adaptable a todos los dispositivos

## Reglas de Código
1. **Estilo:** Sigue PEP 8 para Python, ESLint para JavaScript
2. **Nomenclatura:** snake_case para Python, camelCase para JavaScript
3. **Documentación:** Docstrings en funciones Python, JSDoc en JavaScript
4. **Seguridad:** Nunca expongas API keys, siempre valida entradas
5. **Performance:** Optimiza para carga rápida en móviles

## Seguridad
- NUNCA expongas API keys en el frontend
- SIEMPRE usa HTTPS en producción
- SIEMPRE valida las entradas del usuario
- SIEMPRE implementa CSRF protection
- SIEMPRE registra errores en logs

## Estructura del Proyecto
- `public/` → Archivos estáticos (CSS, JS, imágenes)
- `src/` → Código del backend
- `src/api/` → Endpoints de la API
- `src/modelos/` → Lógica de negocio
- `data/` → Datos de configuración