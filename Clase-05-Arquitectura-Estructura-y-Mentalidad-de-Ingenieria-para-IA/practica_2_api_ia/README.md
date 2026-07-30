# Practica 2: IA mediante API — Creacion de Llaves y Uso de .venv

## Resumen

En esta practica aprenderemos a conectar nuestra computadora con servicios de IA en la nube usando **APIs** (llaves de acceso). Crearemos un entorno virtual seguro (`.venv`) y un archivo de configuracion (`.env`) para guardar nuestras llaves. Al final, tendremos un script funcional que nos permita hacer preguntas a una IA directamente desde la terminal.

## Objetivos

1. **Crear** un entorno virtual (`.venv`) desde cero
2. **Entender** que es una API key y como protegerla
3. **Configurar** el archivo `.env` con llaves de diferentes proveedores
4. **Ejecutar** un script que conecte con IA real usando Google Gemini (gratuito)
5. **Explorar** ejemplos con DeepSeek, OpenRouter, GPT y Claude

## Duracion estimada: 40 minutos

## Estructura de la carpeta

```
practica_2_api_ia/
│
├── README.md                          # Este archivo
├── guia_practica.md                   # Guia paso a paso (como ejecutar)
├── guia_usando_ia_para_construir.md   # COMO USAR IA PARA CREAR PROYECTOS
├── .env.example                       # Plantilla de llaves (NUNCA subir a GitHub)
├── .gitignore                         # Lista negra de archivos secretos
├── requirements.txt                   # Librerias que necesitamos instalar
│
├── .vscode/                           # Configuracion de VS Code
│   └── settings.json                  # Activa el .venv automaticamente
│
├── scripts/                           # Scripts de esta practica
│   ├── script_google_gemini.py        # SCRIPT PRINCIPAL — Google Gemini (GRATIS)
│   ├── script_deepseek.py             # Ejemplo con DeepSeek
│   ├── script_openrouter.py           # Ejemplo con OpenRouter (multiples IAs)
│   ├── script_openai_gpt.py           # Ejemplo con OpenAI GPT
│   └── script_claude.py               # Ejemplo con Claude (Anthropic)
│
├── docs/                              # Documentacion
│   └── notas_seguridad.md             # Reglas de seguridad para llaves API
│
├── CONTEXT.md                         # Quienes somos y que hacemos
├── RULES.md                           # Reglas de codigo y comportamiento
├── SECURITY.md                        # Lineas rojas de seguridad
└── ARCHITECTURE.md                    # Estructura del proyecto
```

## Guia: Como Usar IA para Construir Proyectos

El archivo **`guia_usando_ia_para_construir.md`** ensena a los alumnos a ser "directores de IA":

- **Paso 1:** Tener la idea clara (tu trabajo)
- **Paso 2:** Seleccionar el experto correcto (que IA para que tarea)
- **Paso 3:** Hacer las preguntas correctas (5 tipos de prompts)
- **Paso 4:** Evaluar la respuesta con criterio (5 preguntas criticas)
- **Paso 5:** Pedir ajustes y mejoras
- **Paso 6:** Unir las piezas
- **Paso 7:** Probar y verificar

**Incluye:**
- Tabla de seleccion de expertos (que IA para que tarea)
- 5 tipos de prompt con ejemplos reales
- Señales de alerta (cuando la IA se equivoca)
- Ejercicio completo para construir un proyecto propio
- Errores comunes de principiantes

## Como replicar esta estructura en tu propio proyecto

Esta carpeta es un **ejemplo replicable**. Cuando crees tu propio proyecto de IA, copia esta estructura:

1. **Crea la carpeta** de tu proyecto con snake_case
2. **Copia los archivos `.md`** (CONTEXT.md, RULES.md, SECURITY.md, ARCHITECTURE.md)
3. **Modifica el contenido** de cada `.md` segun tu proyecto
4. **Crea tu `.venv`**: `python -m venv .venv`
5. **Activa el `.venv`**: `.venv\Scripts\activate`
6. **Crea tu `.env`** con tus propias llaves (copia de `.env.example`)
7. **Crea tus scripts** basandote en los ejemplos

**Los archivos que SI se comparten (suben a GitHub):**
- `*.md` (CONTEXT, RULES, SECURITY, ARCHITECTURE)
- `.vscode/settings.json`
- `.gitignore`
- `requirements.txt`
- `scripts/*.py`

**Los archivos que NUNCA se comparten:**
- `.env` (contiene llaves secretas)
- `.venv/` (entorno virtual local)

## Configuracion de VS Code

Al abrir esta carpeta en VS Code, el entorno virtual `.venv` se activa **automaticamente** en la terminal. No necesitas escribir `activate` cada vez.

**Para probarlo:**
1. Abre VS Code en esta carpeta (`code .`)
2. Abre la terminal con `Ctrl + `` (control + tilde)
3. Veras `(.venv)` al inicio de la linea — eso significa que ya esta activo

Si no funciona, ve a la guia completa en `guia_practica.md` (Paso 3.5).
