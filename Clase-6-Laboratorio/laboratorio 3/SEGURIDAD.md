# 🛡️ Checklist de Seguridad - Laboratorio 3

## Guía Completa para Evaluar Repositorios y Apps

---

## 📋 FASE 1: Antes de Clonar

### Reputación del Proyecto

| Criterio | Sí | No | Notas |
|----------|----|----|-------|
| El repositorio tiene más de 100 stars | | | |
| El autor tiene historial de contributions | | | |
| Hay commits recientes (últimos 6 meses) | | | |
| El README está completo y claro | | | |
| Hay issues abiertos y respondidos | | | |
| Tiene licencia open source | | | |

### Análisis del README

| Pregunta | Sí | No |
|----------|----|----|
| ¿Explica qué hace el proyecto? | | |
| ¿Tiene instrucciones de instalación? | | |
| ¿Menciona requisitos previos? | | |
| ¿Tiene screenshots o demo? | | |
| ¿Indica cómo contribuir? | | |
| Tiene disclaimer de seguridad | | |

---

## 📋 FASE 2: Después de Clonar

### Estructura del Proyecto

| Elemento | Presente | Seguro |
|----------|----------|--------|
| `.gitignore` existe | | |
| No hay archivos `.env` en el repo | | |
| No hay API keys hardcodeadas | | |
| No hay contraseñas en el código | | |
| Los archivos de configuración están separados | | |

### Análisis de Código

| Criterio | Cumple | No Cumple |
|----------|--------|-----------|
| No hay `http://` (solo `https://`) | | |
| No hay tokens hardcodeados | | |
| Las dependencias están actualizadas | | |
| El código tiene comentarios | | |
| Hay tests unitarios | | |

---

## 📋 FASE 3: Permisos de Android

### Permisos Básicos (Necesarios)

| Permiso | Justificación | Aprobado |
|---------|---------------|----------|
| `INTERNET` | Conectar a YouTube Music | ☐ |
| `ACCESS_NETWORK_STATE` | Verificar conexión a internet | ☐ |
| `FOREGROUND_SERVICE` | Reproducir música en segundo plano | ☐ |

### Permisos Adicionales (Evaluar)

| Permiso | ¿Es necesario? | Riesgo | Aprobado |
|---------|----------------|--------|----------|
| `WAKE_LOCK` | Mantener pantalla activa | Bajo | ☐ |
| `POST_NOTIFICATIONS` | Mostrar notificaciones | Bajo | ☐ |
| `READ_EXTERNAL_STORAGE` | Acceder a música local | Medio | ☐ |
| `WRITE_EXTERNAL_STORAGE` | Descargar música | Alto | ☐ |
| `CAMARA` | No necesario | Alto | ☐ |
| `READ_CONTACTS` | No necesario | Crítico | ☐ |
| `ACCESS_FINE_LOCATION` | No necesario | Crítico | ☐ |

### Regla de Oro
> **Si una app pide permisos que no necesitas para su función principal, NO la instales.**

---

## 📋 FASE 4: Conexiones de Red

### URLs Identificadas

| URL | Protocolo | Propósito | Seguro |
|-----|-----------|-----------|--------|
| | | | |
| | | | |
| | | | |

### Verificaciones

| Criterio | Sí | No |
|----------|----|----|
| ¿Todas las conexiones usan HTTPS? | | |
| ¿Hay conexiones a servidores desconocidos? | | |
| ¿Envía datos personales a internet? | | |
| ¿Puede funcionar sin conexión? | | |

---

## 📋 FASE 5: Almacenamiento Local

### Datos que Guarda la App

| Tipo de Dato | ¿Es sensible? | ¿Está encriptado? |
|--------------|----------------|-------------------|
| | | |
| | | |
| | | |

### Verificaciones

| Criterio | Sí | No |
|----------|----|----|
| ¿Guarda contraseñas localmente? | | |
| ¿Guarda datos de ubicación? | | |
| ¿Guarda historial de navegación? | | |
| ¿Los datos están encriptados? | | |
| ¿Se puede borrar fácilmente? | | |

---

## 📋 FASE 6: Decisión de Instalación

### Puntuación de Seguridad

| Categoría | Puntos (1-10) |
|-----------|---------------|
| Reputación del proyecto | /10 |
| Calidad del código | /10 |
| Permisos de Android | /10 |
| Conexiones de red | /10 |
| Almacenamiento local | /10 |
| **TOTAL** | **/50** |

### Niveles de Riesgo

| Puntuación | Nivel | Recomendación |
|------------|-------|---------------|
| 45-50 | 🟢 Bajo | Instalar con confianza |
| 35-44 | 🟡 Medio | Instalar con precaución |
| 25-34 | 🟠 Alto | Considerar alternativas |
| <25 | 🔴 Crítico | NO instalar |

### Decisión Final

| Decisión | Marcar |
|----------|--------|
| ✅ Instalar | ☐ |
| ⚠️ Instalar con precauciones | ☐ |
| ❌ No instalar | ☐ |
| 🔄 Buscar alternativa | ☐ |

---

## 📋 FASE 7: Después de Instalar

### Monitoreo Inicial

| Criterio | Normal | Sospechoso |
|----------|--------|------------|
| La app funciona como se espera | | |
| No consume batería excesiva | | |
| No usa datos móviles innecesariamente | | |
| No muestra anuncios inesperados | | |
| No pide permisos adicionales | | |
| No tiene comportamiento extraño | | |

### Señales de Alerta

**Desinstala inmediatamente si:**

- [ ] La app pide permisos que no debería
- [ ] Consume batería o datos excesivamente
- [ ] Muestra comportamiento extraño
- [ ] Muestra anuncios sospechosos
- [ ] Tiene errores frecuentes
- [ ] Te pide datos personales innecesarios

---

## 📋 Checklist Rápido de Seguridad

### Antes de Clonar
- [ ] Verifiqué la reputación del proyecto
- [ ] Leí el README completamente
- [ ] Revisé los issues abiertos
- [ ] El proyecto tiene licencia

### Después de Clonar
- [ ] No hay API keys hardcodeadas
- [ ] No hay contraseñas en el código
- [ ] Las conexiones son HTTPS
- [ ] El código es legible

### Antes de Instalar
- [ ] Analicé los permisos
- [ ] Los permisos son necesarios
- [ ] No pide permisos excesivos
- [ ] Descargué del repositorio oficial

### Después de Instalar
- [ ] La app funciona correctamente
- [ ] No hay comportamiento sospechoso
- [ ] No consume recursos innecesariamente
- [ ] Sé cómo desinstalar si algo falla

---

## 🚨 Reglas de Oro

1. **Nunca instales** apps con permisos excesivos
2. **Siempre verifica** la fuente de descarga
3. **Analiza el código** antes de ejecutar
4. **Confía pero verifica** siempre
5. **Ten un plan** para desinstalar si algo falla

---

## 📚 Recursos Adicionales

- [OWASP Mobile Top 10](https://owasp.org/www-project-mobile-top-10/)
- [Android Permissions Guide](https://developer.android.com/guide/topics/permissions/overview)
- [GitHub Security Best Practices](https://docs.github.com/en/code-security)
