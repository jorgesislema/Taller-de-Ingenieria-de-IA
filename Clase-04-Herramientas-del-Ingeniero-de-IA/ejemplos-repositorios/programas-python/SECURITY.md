# SECURITY.md - Reglas de Seguridad

## PROHIBICIONES ABSOLUTAS
1. **NUNCA** guardes contraseñas, tokens o API keys en el código fuente
2. **NUNCA** ejecutes código de fuentes no confiables
3. **NUNCA** modifiques archivos del sistema operativo
4. **NUNCA** accedas a archivos fuera del proyecto
5. **NUNCA** compartas credenciales entre proyectos

## GESTIÓN DE DEPENDENCIAS
1. **Virtual environments:** Usa venv para aislar dependencias
2. **Fija versiones:** Usa requirements.txt con versiones específicas
3. **Escanea vulnerabilidades:** Usa pip-audit regularmente
4. **Actualiza:** Mantén dependencias actualizadas
5. **Evita abandonadas:** No uses librerías sin mantenimiento

## ENTRADAS Y SALIDAS
1. **Validación:** Valida todo input del usuario
2. **Sanitización:** Limpia datos antes de procesar
3. **Tipado:** Usa type hints para mayor seguridad
4. **Límites:** Implementa límites de tamaño y tiempo
5. **Escapes:** Escapa HTML para prevenir XSS

## LOGGING Y MONITOREO
1. **Usa logging:** En lugar de print()
2. **Niveles:** Usa niveles apropiados (INFO, WARNING, ERROR)
3. **Contexto:** Incluye suficiente contexto en logs
4. **No sensibles:** Nunca loguees contraseñas o datos personales
5. **Rotación:** Implementa rotación de logs

## ALMACENAMIENTO
1. **Variables de entorno:** Usa .env para credenciales
2. **Encriptación:** Encripta datos sensibles en disco
3. **Permisos:** Usa permisosrestrictivos en archivos
4. **Backups:** Mantén backups encriptados
5. **Retención:** Define políticas de eliminación