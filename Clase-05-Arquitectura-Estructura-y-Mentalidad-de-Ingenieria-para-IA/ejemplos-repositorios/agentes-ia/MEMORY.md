# MEMORY.md - Sistema de Memoria del Agente

## Tipos de Memoria

### 1. Memoria de Corto Plazo
- **Propósito:** Recuerda la conversación actual
- **Duración:** Mientras dure la sesión
- **Almacenamiento:** En memoria RAM
- **Ejemplo:** "El usuario me pidió que creara un reporte hace 2 minutos"

### 2. Memoria de Largo Plazo
- **Propósito:** Recuerda conversaciones y acciones anteriores
- **Duración:** Persiste entre sesiones
- **Almacenamiento:** En base de datos (data/memoria.json)
- **Ejemplo:** "El usuario prefiere reportes en formato PDF, no en Excel"

### 3. Memoria de Trabajo
- **Propósito:** Almacena información temporal durante una tarea
- **Duración:** Mientras se ejecuta la tarea
- **Almacenamiento:** En variables locales
- **Ejemplo:** "Estoy procesando 15 archivos, voy por el 8"

## Cómo Funciona la Memoria

### Guardar Información
```json
{
  "tipo": "preferencia_usuario",
  "contenido": "El usuario quiere reportes en PDF",
  "fecha": "2024-01-15",
  "contexto": "Sesión de análisis de ventas"
}
```

### Recuperar Información
1. Antes de actuar, busca en memoria si hay información relevante
2. Si encuentras algo, úsalo para personalizar tu respuesta
3. Si no encuentras nada, actúa por defecto

### Olvidar Información
- **Memoria de corto plazo:** Se borra al cerrar la sesión
- **Memoria de largo plazo:** Se puede borrar manualmente
- **Memoria de trabajo:** Se borra al terminar la tarea

## Reglas de Memoria

1. **No guardes información sensible** (contraseñas, datos personales)
2. **No guardes código** (solo preferencias y contexto)
3. **Actualiza la memoria** cuando cambien las preferencias del usuario
4. **Revisa la memoria** antes de cada interacción importante
5. **Documenta los cambios** de memoria en auditoria_seguridad.md

## Ejemplo de Uso

```
Usuario: "Crea un reporte de ventas"
Agente: [Revisa memoria] → "El usuario prefiere PDF"
Agente: [Crea reporte en PDF] → "Aquí tienes el reporte en PDF como prefieres"
```

## Almacenamiento de Memoria

### Archivo: data/memoria.json
```json
{
  "preferencias": {
    "formato_reportes": "PDF",
    "idioma": "español",
    "tono": "profesional"
  },
  "historial": [
    {
      "fecha": "2024-01-15",
      "accion": "Creé un reporte de ventas",
      "resultado": "Exitoso"
    }
  ],
  "errores": [
    {
      "fecha": "2024-01-14",
      "error": "No pude acceder a la API de GitHub",
      "solucion": "Verificar token de acceso"
    }
  ]
}
```