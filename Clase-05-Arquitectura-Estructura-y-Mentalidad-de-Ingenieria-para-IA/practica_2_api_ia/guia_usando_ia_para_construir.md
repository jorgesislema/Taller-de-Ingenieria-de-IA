# Como Construir Este Proyecto Desde Cero Usando IA

## Introduccion

En clase viste el resultado: una carpeta con scripts que conectan con IA, archivos .md de configuracion, entorno virtual, etc.

Ahora vas a aprender a **construir eso mismo desde cero**, pero no copiando y pegando, sino **usando una IA como tu herramienta**. Tu eres el director. La IA es tu equipo tecnico.

**Objetivo:** Que al final de esta guia, tengas tu propio proyecto funcionando, igual al de clase, pero construido por ti usando IA.

---

## Paso 1: Abre una IA Externamente

Abre el navegador y ve a una de estas IAs:

| IA | URL | Nivel |
|----|-----|-------|
| **ChatGPT** | https://chatgpt.com | Facil |
| **Claude** | https://claude.ai | Facil |
| **DeepSeek** | https://chat.deepseek.com | Facil |
| **Gemini** | https://gemini.google.com | Facil |

**Cual elegir?** La que mas te guste. Todas funcionan para esta guia.

---

## Paso 2: Cuentale a la IA Que Quieres Hacer

Escribe el siguiente mensaje en el chat de la IA:

```
Quiero crear un proyecto en Python que me permita hacer preguntas 
a una IA desde la terminal de mi computadora.

El proyecto debe:
1. Usar la API de Google Gemini (que es gratis)
2. Tener un archivo .env donde guarde la llave de API
3. Tener un entorno virtual (.venv)
4. Tener archivos de configuracion (.md) para que la IA entienda el proyecto
5. Tener un .gitignore para no subir archivos secretos a GitHub

Soy principiante en Python. Explicame paso a paso como lo hago.
```

### Que busca la IA con este prompt?

La IA va a entender:
- Que quieres construir (un chat con Gemini)
- Que nivel tienes (principiante)
- Que restricciones tienes (gratis, .env, .venv)
- Que estructura necesitas (archivos .md, .gitignore)

### Que deberia responderte la IA?

La IA te deberia dar:
1. Una lista de pasos a seguir
2. La estructura de carpetas
3. Los comandos para crear el .venv
4. El codigo del script

**CRITICA:** Si la IA te da TODO de golpe sin explicarte, pide que te explique cada paso por separado.

---

## Paso 3: Pide la Estructura de Carpetas

Ahora se mas especifico. Escribe:

```
Dame la estructura de carpetas exacta que necesito para este proyecto.
Quiero que sea similar a esta:

practica_2_api_ia/
├── scripts/
├── docs/
├── .vscode/
├── .env.example
├── .gitignore
├── requirements.txt
├── CONTEXT.md
├── RULES.md
├── SECURITY.md
└── ARCHITECTURE.md

Pero adaptada a mi proyecto. Dame el arbol de carpetas y explica 
que va en cada una.
```

### Verificacion Critica

Comparalo con el proyecto de clase:

| Elemento | Debe existir | Donde |
|----------|--------------|-------|
| `scripts/` | SI | Carpetas de codigo |
| `docs/` | SI | Documentacion |
| `.vscode/` | SI | Configuracion de VS Code |
| `.env.example` | SI | Plantilla de llaves |
| `.gitignore` | SI | Lista negra |
| `requirements.txt` | SI | Dependencias |
| `CONTEXT.md` | SI | En la raiz |
| `RULES.md` | SI | En la raiz |
| `SECURITY.md` | SI | En la raiz |
| `ARCHITECTURE.md` | SI | En la raiz |

---

## Paso 4: Pide el Codigo del Script Principal

Escribe:

```
Ahora escribeme el script principal que conecte con Google Gemini.

Requisitos:
1. Lea la llave GOOGLE_API_KEY desde un archivo .env
2. Use la libreria google-generativeai
3. Permita hacer preguntas en un bucle infinito
4. Muestre las respuestas en pantalla
5. Permita salir escribiendo "salir" o "exit"
6. Guarde el historial de conversacion
7. Tenga manejo de errores con try/except
8. Todo comentado en espanol
9. Use snake_case para funciones y variables
10. Tenga un docstring principal explicando que hace

El script se llama script_google_gemini.py
```

### Verificacion Critica

Pide a la IA que te muestre el codigo y revisa:

| Elemento | Debe tener | Ejemplo |
|----------|------------|---------|
| Importaciones | `os`, `sys`, `google.generativeai`, `dotenv` | `import os` |
| Lectura de .env | `os.getenv("GOOGLE_API_KEY")` | `api_key = os.getenv(...)` |
| Conexion a Gemini | `genai.configure(api_key=...)` | `genai.configure(...)` |
| Bucle infinito | `while True:` | Para multiples preguntas |
| Salida | `if pregunta.lower() in ["salir", "exit"]` | Para cerrar |
| Historial | `chat = model.start_chat(history=[])` | Para recordar |
| Errores | `try/except` | Para que no crashee |
| Docstring | Al inicio del archivo | Explica que hace |

---

## Paso 5: Pide los Archivos de Configuracion (.md)

Escribe:

```
Crea los archivos de configuracion para mi proyecto:

1. CONTEXT.md - Quien soy, que estoy construyendo, para que sirve
2. RULES.md - Reglas de como debe ser el codigo (snake_case, comentarios, etc)
3. SECURITY.md - Que NO se puede hacer (nunca poner llaves en codigo, etc)
4. ARCHITECTURE.md - Estructura del proyecto y que va en cada carpeta

Todo en espanol, lenguaje simple, con ejemplos.
```

### Verificacion Critica

Revisa que cada archivo `.md` tenga:

| Archivo | Debe contener |
|---------|---------------|
| `CONTEXT.md` | Quien eres, que construyes, para que sirve, que NO haces |
| `RULES.md` | Reglas de codigo (snake_case, comentarios, errores, librerias) |
| `SECURITY.md` | Lineas rojas (nunca llaves en codigo, nunca .env en GitHub) |
| `ARCHITECTURE.md` | Arbol de carpetas, que va en cada una, reglas de la arquitectura |

---

## Paso 6: Pide el .gitignore y .env.example

Escribe:

```
Crea el .gitignore que incluya:
- .venv/ y carpetas de entorno virtual
- .env y archivos de variables de entorno
- __pycache__/ y archivos temporales de Python
- .vscode/ (opcional, para configuracion local)
- .DS_Store y archivos de sistema

Y crea el .env.example con:
- GOOGLE_API_KEY=tu_llave_aqui
- Con instrucciones de como obtener la llave gratis
```

---

## Paso 7: Pide el requirements.txt

Escribe:

```
Crea el requirements.txt con las librerias necesarias:
- google-generativeai (para Gemini)
- python-dotenv (para leer .env)

Incluye versiones minimas.
```

---

## Paso 8: Arma Todo en tu Computadora

Ahora que la IA te dio todo, crea los archivos en tu computadora:

```bash
# 1. Crea la carpeta del proyecto
mkdir mi_chat_ia
cd mi_chat_ia

# 2. Crea el entorno virtual
python -m venv .venv

# 3. Activa el entorno virtual
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# 4. Crea los archivos (copia el contenido que te dio la IA)
# Usa VS Code o Bloc de notas para crear cada archivo

# 5. Instala las dependencias
pip install -r requirements.txt

# 6. Prueba el script
python scripts/script_google_gemini.py
```

---

## Paso 9: Prueba y Verifica

### Prueba Basica

```bash
# Ejecuta el script
python scripts/script_google_gemini.py

# Deberia aparecer algo como:
# ============================================================
#   CHAT CON GOOGLE GEMINI (IA de Google)
# ============================================================
#
#   Escribe tu pregunta y presiona Enter.
#   Para salir, escribe 'salir' o 'exit'.
#   Para borrar el historial, escribe 'limpiar'.
#
# ------------------------------------------------------------

# Haz una pregunta de prueba
Tu pregunta: Explica que es una variable en Python

# Espera la respuesta
# Escribe "salir" para terminar
```

### Prueba de Seguridad

```bash
# Verifica que .env NO este en git
git status

# Deberia mostrar .env como "untracked"
# NUNCA hagas: git add .env
```

### Comparacion con el Proyecto de Clase

| Elemento | Proyecto de Clase | Tu Proyecto | Iguales? |
|----------|-------------------|-------------|----------|
| Estructura de carpetas | Si | ? | ? |
| .venv funciona | Si | ? | ? |
| .env tiene la llave | Si | ? | ? |
| Script ejecuta | Si | ? | ? |
| IA responde | Si | ? | ? |
| Se puede salir | Si | ? | ? |
| .gitignore funciona | Si | ? | ? |
| Archivos .md existen | Si | ? | ? |

---

## Errores Comunes y Soluciones

| Error | Causa | Solucion |
|-------|-------|----------|
| "No se encontro la llave" | .env no tiene la llave | Abre .env y pega tu llave |
| "ModuleNotFoundError" | No instalaste librerias | Ejecuta `pip install -r requirements.txt` |
| "No se reconoce 'code'" | VS Code no esta en PATH | Abre VS Code desde el menu de Windows |
| La IA no te da el codigo completo | Pide "Dame el codigo completo, listo para copiar" | Pide mas detalle |
| El script no funciona | La IA se equivoco | Pide que lo corrija mostrando el error |

---

## Ejercicio Final: Replicalo sin Mirar

**El verdadero aprendizaje es poder hacerlo SIN mirar la solucion.**

1. Abre una IA (ChatGPT, Claude, etc.)
2. Describe el proyecto desde cero
3. Pide la estructura de carpetas
4. Pide el codigo del script
5. Pide los archivos .md
6. Arma todo en tu computadora
7. Prueba que funcione

**Si en algun paso te atascas:**
- No mires la solucion
- Preguntale a la IA "No entiendo esto, explicamelo de otra forma"
- La IA es tu profesor particular

**Tiempo estimado:** 30-40 minutos

---

## Preguntas de Reflexion

1. **¿Fue mas facil copiar el proyecto o construirlo desde cero con IA?**
   Copiar es mas facil, pero no aprendes. Construir con IA te ensena a ser director.

2. **¿En que paso te atascaste mas?**
   Identifica tu punto debil para mejorar.

3. **¿Que pasaria si la IA te da codigo con errores?**
   Tu debes detectarlos y pedir que los corrija. Eso es ser director.

4. **¿Podrias hacer esto sin la IA?**
   Si, pero te tomaria horas investigar. La IA acelera el proceso, pero tu diriges.

5. **¿Cual es la diferencia entre usar la IA como herramienta y usarla como dependencia?**
   Herramienta = tu sabes que quieres, la IA ejecuta. Dependencia = tu no sabes que quieres, la IA decide por ti.
