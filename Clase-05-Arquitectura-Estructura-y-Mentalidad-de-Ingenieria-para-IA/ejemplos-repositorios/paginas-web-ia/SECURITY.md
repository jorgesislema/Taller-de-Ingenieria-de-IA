# SECURITY.md - Reglas de Seguridad

## PROHIBICIONES ABSOLUTAS
1. **NUNCA** expongas API keys en el frontend (HTML, JavaScript)
2. **NUNCA** uses HTTP en producción (solo HTTPS)
3. **NUNCA** omitas validación de entradas del usuario
4. **NUNCA** guardes contraseñas en texto plano
5. **NUNCA** compartas datos personales con servicios externos

## PROTECCIÓN DEL USUARIO
1. **CSRF Protection:** Implementa tokens CSRF en todos los formularios
2. **XSS Prevention:** Sanitiza todo el contenido del usuario
3. **SQL Injection:** Usa queries parametrizados
4. **Rate Limiting:** Limita las peticiones por usuario
5. **Input Validation:** Valida y sanitiza todas las entradas

## SEGURIDAD DE LA API
1. **Autenticación:** Usa JWT o sesiones seguras
2. **Autorización:** Verifica permisos en cada endpoint
3. **Rate Limiting:** Limita llamadas a la API de IA
4. **Timeout:** Nunca hagas llamadas a la IA sin límite de tiempo
5. **Logging:** Registra todos los intentos de acceso no autorizado

## SEGURIDAD DE DATOS
1. **Encriptación:** Usa HTTPS para todas las comunicaciones
2. **Almacenamiento:** Encripta datos sensibles en la base de datos
3. **Backups:** Mantén backups diarios en ubicación segura
4. **Retención:** Define políticas de eliminación de datos
5. **Anonimización:** Anonimiza datos para análisis y reportes