# Reglas para los Scripts de IA

## Reglas de codigo

1. **USA EXCLUSIVAMENTE snake_case** para todos los nombres de archivos y variables.
2. **COMENTA TODO EL CODIO en espanol.** Cada funcion debe tener su docstring explicando que hace.
3. **UNA FUNCION = UNA TAREA.** No crees funciones que hagan 5 cosas diferentes.
4. **MANEJA ERRORES.** Nunca dejes que el programa crashee sin un mensaje util.
5. **NO USES LIBRERIAS INNECESARIAS.** Solo importa lo que realmente necesitas.

## Reglas de seguridad

1. **NUNCA** pongas llaves de API directamente en el codigo.
2. **SIEMPRE** lee las llaves desde el archivo `.env` usando `os.getenv()`.
3. **NUNCA** subas el archivo `.env` a GitHub.
4. **NUNCA** compartas tus llaves por chat, correo o cualquier otro medio.
5. **SIEMPRE** incluye `.env` en el `.gitignore`.

## Reglas de nomenclatura

1. **Archivos:** `script_nombre_proveedor.py` (ej: `script_google_gemini.py`)
2. **Funciones:** `accion_objeto()` (ej: `hacer_pregunta()`, `mostrar_bienvenida()`)
3. **Variables:** `nombre_descriptivo` (ej: `api_key`, `historial`, `respuesta`)
4. **Constantes:** `NOMBRE_EN_MAYUSCULAS` (ej: `MODELOS_DISPONIBLES`)

## Reglas de documentacion

1. **Cada script** debe tener un docstring principal explicando que hace.
2. **Cada funcion** debe tener un docstring con Args y Returns.
3. **Los comentarios** explican el POR QUE, no el QUE (el codigo ya dice el QUE).
4. **Incluye instrucciones** de como obtener la llave de API en el docstring.

## Ejemplo de codigo correcto

```python
"""
Script para conectar con Google Gemini.
Lee la llave desde .env y permite hacer preguntas desde la terminal.
"""

import os
import sys

# La libreria de Google para usar Gemini
try:
    import google.generativeai as genai
except ImportError:
    print("ERROR: No tienes instalada google-generativeai")
    print("Ejecuta: pip install google-generativeai")
    sys.exit(1)


def obtener_llave():
    """
    Lee la llave de API desde el archivo .env.
    
    Returns:
        str: La llave de API o None si no existe
    """
    from dotenv import load_dotenv
    load_dotenv()
    return os.getenv("GOOGLE_API_KEY")
```
