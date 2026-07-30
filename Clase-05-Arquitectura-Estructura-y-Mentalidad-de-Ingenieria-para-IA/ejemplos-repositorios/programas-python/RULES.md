# RULES.md - Reglas del Proyecto

## Reglas de Código
1. **Python:** Usa Python 3.8+ con type hints
2. **Estilo:** Sigue PEP 8 (guía de estilo de Python)
3. **Documentación:** Docstrings en todas las funciones públicas
4. **Imports:** Ordenados (stdlib → third-party → local)
5. **Variables:** Nombres descriptivos, snake_case

## Reglas de Estructura
1. **Funciones:** Máximo 20 líneas, una responsabilidad
2. **Clases:** Máximo 5 métodos públicos
3. **Archivos:** Máximo 300 líneas
4. **Módulos:** Un archivo por módulo lógico
5. **Paquetes:** Organiza por funcionalidad

## Reglas de Seguridad
1. **Credenciales:** NUNCA las guardes en código
2. **Entradas:** Valida y sanitiza todo input
3. **Dependencias:** Escanea vulnerabilidades regularmente
4. **Logs:** Nunca loguees datos sensibles
5. **Actualizaciones:** Mantén dependencias actualizadas

## Reglas de Testing
1. **Cobertura:** Mínimo 80% del código
2. **Unitarias:** Para cada función aislada
3. **Integración:** Para endpoints de API
4. **Mocks:** Para servicios externos
5. **Automatización:** Ejecuta tests en CI/CD