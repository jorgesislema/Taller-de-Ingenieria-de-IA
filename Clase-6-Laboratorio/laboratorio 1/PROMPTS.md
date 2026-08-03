# 🤖 Prompts Listos para Usar en la Clase 6

## 📋 PROMPT 1: Reconocimiento del Repositorio

```
Eres un profesor de programación para principiantes.

Revisa la siguiente estructura de archivos de un repositorio y explica 
la función de cada uno de forma sencilla:

ARCHIVOS:
- chatbot.py
- deepseek_chatbot.py
- test_chatbot.py
- test_deepseek_chatbot.py
- requirements.txt
- context.md
- arquitectura.md
- README.md
- .gitignore
- LICENSE

Para cada archivo explica:
1. Qué es (documento, código, configuración)
2. Para qué sirve
3. Quién lo usa (desarrollador, Python, GitHub)
```

---

## 📋 PROMPT 2: Análisis de Código Python

```
Soy un estudiante principiante. Explica el siguiente código Python 
de forma muy sencilla, como si tuvieras 10 años.

El código es un chatbot que se conecta a la API de DeepSeek.

CÓDIGO:
import os
from dotenv import load_dotenv
from openai import OpenAI

MODELO = "deepseek-v4-flash"

def cargar_api_key():
    load_dotenv()
    clave = os.getenv("GEMINI_API_KEY")
    return clave

def configurar_modelo():
    cliente = OpenAI(
        api_key=cargar_api_key(),
        base_url="https://api.deepseek.com"
    )
    return cliente

Explica:
1. Qué hace cada línea importante
2. Para qué sirve cada función
3. Si ves algún error, dime cuál es
```

---

## 📋 PROMPT 3: Encontrar el Error (Versión Sencilla)

```
Revisa este código y dime si tiene algún error.

El código debería conectar con DeepSeek pero no funciona.

def cargar_api_key():
    """Lee la llave secreta desde el archivo .env"""
    load_dotenv()
    clave = os.getenv("GEMINI_API_KEY")
    return clave

¿Qué está mal? Explícalo como si fuera un error de ortografía.
```

---

## 📋 PROMPT 4: Encontrar el Error (Versión Detallada)

```
Actúa como un ingeniero de software senior revisando código.

El archivo deepseek_chatbot.py debería conectarse a la API de DeepSeek,
pero tiene un error que causa un problema de autenticación.

El error está en la función cargar_api_key().

Tarea:
1. Identifica el error exacto
2. Explica por qué es un error
3. Muestra la corrección
4. Explica las consecuencias si no se corrige

Contexto:
- DeepSeek usa su propia API key: DEEPSEEK_API_KEY
- Google Gemini usa: GEMINI_API_KEY
- El archivo .env contiene ambas variables
```

---

## 📋 PROMPT 5: Verificar la Corrección

```
¿Es correcto este código ahora?

def cargar_api_key():
    """Lee la llave secreta (API Key) desde el archivo .env."""
    load_dotenv()
    clave = os.getenv("DEEPSEEK_API_KEY")
    return clave

El archivo se llama deepseek_chatbot.py y usa la API de DeepSeek.

Si está correcto, explica por qué. Si hay algún problema, indícalo.
```

---

## 📋 PROMPT 6: Resumen para Exposición

```
Actúa como un estudiante que va a presentar su trabajo en clase.

Resume en 5 puntos lo que aprendí en el laboratorio de hoy:
1. Qué es un repositorio
2. Para qué sirve Git
3. Qué son las variables de entorno
4. Qué error encontré y cómo lo resolví
5. Cómo la IA me ayudó

Explica cada punto de forma sencilla y clara.
```

---

## 💡 Consejos para Usar los Prompts

1. **Copia el código exacto** del archivo cuando lo pidas
2. **No tengas miedo de preguntar** "no entendí, explícalo otra vez"
3. **Pide ejemplos** si algo no está claro
4. **Verifica siempre** la respuesta de la IA con tu propio criterio
5. **Guarda los prompts** que te funcionaron para usarlos después
