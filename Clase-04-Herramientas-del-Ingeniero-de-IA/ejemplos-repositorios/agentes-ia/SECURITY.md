# SECURITY.md - Reglas de Seguridad

## PROHIBICIONES ABSOLUTAS
1. **NUNCA** ejecutes código sin verificación previa
2. **NUNCA** modifiques archivos sensibles (.env, .gitignore, .github/)
3. **NUNCA** accedas a archivos fuera del proyecto
4. **NUNCA** compartas credenciales o tokens de acceso
5. **NUNCA** ejecutes comandos del sistema operativo sin supervisión

## PROTECCIÓN DE ACCIONES
1. **Confirmación:** SIEMPRE pregunta antes de acciones destructivas
2. **Registro:** Cada acción debe quedar en auditoria_seguridad.md
3. **Límites:** Respeta los límites definidos en TOOLS.md
4. **Aislamiento:** Ejecuta código en sandbox, nunca en el sistema principal
5. **Rollback:** Siempre ten plan para deshacer una acción

## MANEJO DE ERRORES
1. **No expongas stack traces** en producción
2. **Loguea errores** con suficiente contexto para debug
3. **Maneja excepciones específicas**, no uses Exception genérico
4. **Proporciona mensajes amigables** al usuario final
5. **Notifica al equipo** ante errores críticos

## AUDITORÍA
1. **Registro completo:** Cada acción quedа en auditoria_seguridad.md
2. **Timestamps:** Incluye fecha y hora de cada acción
3. **Resultado:** Documenta si la acción fue exitosa o falló
4. **Impacto:** Describe qué archivos o datos se vieron afectados
5. **Revisión:** Revisa los registros diariamente