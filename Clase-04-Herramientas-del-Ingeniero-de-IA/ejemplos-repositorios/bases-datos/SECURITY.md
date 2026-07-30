# SECURITY.md - Reglas de Seguridad

## PROHIBICIONES ABSOLUTAS
1. **NUNCA** guardes contraseñas en texto plano
2. **NUNCA** uses credenciales de root en producción
3. **NUNCA** permitas conexiones desde cualquier IP
4. **NUNCA** hagas backup sin encriptar
5. **NUNCA** compartas credenciales de base de datos

## AUTENTICACIÓN Y AUTORIZACIÓN
1. **Credenciales:** Usa variables de entorno (.env)
2. **Encriptación:** Contraseñas con bcrypt (salt rounds: 12)
3. **Roles:** Implementa roles con mínimo privilegio
4. **Auditoría:** Registra todos los accesos
5. **Timeout:** Sesiones expiran después de 30 minutos

## PROTECCIÓN DE DATOS
1. **Encriptación en reposo:** AES-256 para datos sensibles
2. **Encriptación en tránsito:** SSL/TLS para conexiones
3. **Anonimización:** Para datos de prueba y desarrollo
4. **Retención:** Políticas de eliminación de datos
5. **Backup encriptado:** GPG para backups

## MONITOREO Y ALERTAS
1. **Logs de acceso:** Registra todos los intentos
2. **Alertas de seguridad:** Intentos fallidos de acceso
3. **Monitoreo de consultas:** Consultas lentas o sospechosas
4. **Uso de disco:** Alertas al 80% de capacidad
5. **Conexiones concurrentes:** Alertas por exceso

## RECUPERACIÓN DE DESASTRES
1. **Backups diarios:** Automáticos a las 2:00 AM
2. **Retención:** 30 días de backups diarios
3. **Testing de restore:** Mensual
4. **Documentación:** Procedimientos de recuperación
5. **RTO:** Tiempo objetivo de recuperación: 4 horas
6. **RPO:** Pérdida máxima aceptable: 1 hora