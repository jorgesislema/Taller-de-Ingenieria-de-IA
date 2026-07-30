# Lineas Rojas — Seguridad del Proyecto

## PROHIBIDO (NUNCA hacer esto)

### Seguridad de llaves
1. **PROHIBIDO** guardar llaves de API en el codigo fuente.
2. **PROHIBIDO** subir el archivo `.env` a GitHub o cualquier repositorio.
3. **PROHIBIDO** compartir llaves por correo, chat, WhatsApp o cualquier medio.
4. **PROHIBIDO** usar la misma llave en multiples proyectos de producción.

### Seguridad del codigo
5. **PROHIBIDO** ejecutar codigo recibido de fuentes desconocidas sin revisarlo.
6. **PROHIBIDO** usar `eval()` o `exec()` con entrada del usuario.
7. **PROHIBIDO** guardar contraseñas en archivos de texto plano (excepto `.env`).

### Uso de la API
8. **PROHIBIDO** hacer miles de solicitudes por segundo (pueden bloquear tu cuenta).
9. **PROHIBIDO** usar la API para generar contenido ilegal o dañino.
10. **PROHIBIDO** intentar evadir los limites de uso de la API.

## OBLIGATORIO (Siempre hacer esto)

### Al crear un proyecto nuevo
1. **SIEMPRE** crear un `.gitignore` que incluya `.env` y `.venv/`.
2. **SIEMPRE** crear un `.env.example` con la estructura de llaves (sin valores reales).
3. **SIEMPRE** documentar como obtener cada llave de API.

### Al usar la API
4. **SIEMPRE** manejar errores con `try/except` para mensajes claros.
5. **SIEMPRE** usar `sys.exit(1)` cuando la llave no exista.
6. **SIEMPRE** mostrar mensajes de error comprensibles, no trazas tecnicas.

### Al compartir codigo
7. **SIEMPRE** incluir un README con instrucciones de instalacion.
8. **SIEMPRE** incluir el archivo `requirements.txt`.
9. **SIEMPRE** usar snake_case en nombres de archivos y variables.
10. **SIEMPRE** comentar el codigo en espanol.

## Si una llave se filtra

1. Ve al panel del proveedor (Google, OpenAI, etc.)
2. Elimina la llave comprometida inmediatamente
3. Crea una llave nueva
4. Actualiza tu archivo `.env`
5. Nunca uses la llave vieja de nuevo
