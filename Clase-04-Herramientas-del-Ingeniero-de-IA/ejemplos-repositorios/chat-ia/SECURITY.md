# SECURITY.md - Reglas de Seguridad

## PROHIBICIONES ABSOLUTAS
1. **NUNCA** guardes contraseñas, tokens o API keys en el código fuente
2. **NUNCA** compartas datos personales de usuarios con terceros
3. **NUNCA** ejecutes código de fuentes no confiables
4. **NUNCA** modifiques archivos del sistema operativo
5. **NUNCA** accedas a archivos fuera del directorio del proyecto

## PROTECCIÓN DE DATOS
1. **Encriptación:** Usa bcrypt para contraseñas, AES para datos sensibles
2. **Anonimización:** Elimina datos personales de logs y pruebas
3. **Acceso:** Implementa autenticación y autorización
4. **Auditoría:** Registra todos los accesos a datos sensibles
5. **Retención:** Define políticas de eliminación de datos

## MANEJO DE ERRORES
1. **No expongas stack traces** en producción
2. **Loguea errores** con suficiente contexto para debug
3. **Maneja excepciones específicas**, no uses Exception genérico
4. **Proporciona mensajes amigables** al usuario final
5. **Notifica al equipo** ante errores críticos

## DEPENDENCIAS
1. **Usa virtual environments** para aislar dependencias
2. **Fija versiones** en requirements.txt
3. **Escanea vulnerabilidades** regularmente
4. **Actualiza dependencias** cuando haya parches de seguridad
5. **Evita dependencias** no mantenidas o abandonadas

## DESPLIEGUE
1. **NUNCA** despliegues desde tu máquina personal
2. **Usa CI/CD** para automatizar pruebas y despliegue
3. **Implementa rollback** en caso de errores
4. **Monitorea** el rendimiento y errores en producción
5. **Haz backups** antes de cada despliegue importante