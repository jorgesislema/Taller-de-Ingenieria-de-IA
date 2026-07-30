# CLAUDE.md - Configuración para Claude

## Arquitectura del Proyecto
- **Patrón:** MVC (Model-View-Controller)
- **Dependencias:** Inyección de dependencias
- **Configuración:** Variables de entorno (.env)
- **Logging:** Python logging module
- **Testing:** pytest con fixtures

## Reglas de Código
1. **Funciones:** Máximo 20 líneas, una responsabilidad
2. **Clases:** Máximo 5 métodos públicos
3. **Archivos:** Máximo 300 líneas
4. **Imports:** Ordenados (stdlib → third-party → local)
5. **Nombres:** Descriptivos, snake_case, sin abreviaciones

## Seguridad
1. **Dependencias:** Usa pip-audit para escanear vulnerabilidades
2. **Entradas:** Valida y sanitiza todo input del usuario
3. **Salidas:** Escapa HTML para prevenir XSS
4. **Credenciales:** Usa vault o variables de entorno
5. **Logs:** Nunca loguees datos sensibles

## Testing
1. **Cobertura:** Mínimo 80% del código
2. **Unitarias:** Para cada función aislada
3. **Integración:** Para endpoints de API
4. **E2E:** Para flujos críticos del usuario
5. **Mocks:** Para servicios externos

## Lo que NO debes hacer
- NO guardes contraseñas en el código
- NO ejecutes código de fuentes no confiables
- NO modifiques archivos del sistema
- NO accedas a archivos fuera del proyecto
- NO uses librerías no mantenidas