# Guia Practica: IA mediante API — Paso a Paso

## Que vamos a hacer?

Vamos a crear un "chat" donde tu haces preguntas desde la terminal de tu computadora y una IA real (Google Gemini) te responde. Todo de forma segura usando `.venv` y `.env`.

## Duracion: 40 minutos

---

## PARTE 1: Preparar el Entorno (15 min)

### Paso 1: Verificar que tienes Python instalado

Abre la terminal y escribe:

```bash
python --version
```

Deberia decir algo como `Python 3.10.0` o superior.

**Si no tienes Python:**
- Ve a https://www.python.org/downloads/
- Descarga la version mas reciente
- **IMPORTANTE:** Al instalar, marca la casilla "Add Python to PATH"

---

### Paso 2: Crear el Entorno Virtual (.venv)

**¿Que es un .venv?** Es una "burbuja" aislada en tu computadora donde instalamos las librerias sin ensuciar el sistema operativo.

```bash
# Entra a la carpeta de esta practica
cd "H:\git\TAller de IA\para mi\Taller-de-especializaci-n-de-ia\Clase-05-Arquitectura-Estructura-y-Mentalidad-de-Ingenieria-para-IA\practica_2_api_ia"

# Crea el entorno virtual
python -m venv .venv
```

**¿Que acaba de pasar?** Se creo una carpeta `.venv/` con una instalacion limpia de Python.

---

### Paso 3: Activar el Entorno Virtual

```bash
# En Windows:
.venv\Scripts\activate

# En Mac/Linux:
source .venv/bin/activate
```

**Como sabes que funciono?** Veras que al inicio de la linea de la terminal aparece `(.venv)`:

```
(.venv) C:\Users\TuUsuario\practica_2_api_ia>
```

Eso significa que estas "dentro de la burbuja". Todo lo que instales ahora solo va para este proyecto.

---

### Paso 3.5: Configurar VS Code para que abra el .venv automaticamente

**¿Que es esto?** Si usas VS Code como editor, podemos configurarlo para que cada vez que abras esta carpeta, el entorno virtual se active solo. No tendras que escribir `activate` manualmente.

**Como funciona:**
- VS Code tiene un archivo de configuracion llamado `.vscode/settings.json`
- En ese archivo le decimos: "Usa el Python que esta dentro de `.venv`"
- Cuando abras la terminal de VS Code (Ctrl+`), el `.venv` ya estara activado

**Paso a paso:**

1. Abre VS Code en esta carpeta:
```bash
# Desde la terminal (con el .venv activado):
code .
```

2. VS Code detectara que hay un `.venv` y mostrara un mensaje en la esquina inferior derecha. **Haz clic en "Yes"**.

3. Si no aparece el mensaje, configuralo manualmente:
   - Presiona `Ctrl + Shift + P`
   - Escribe "Python: Select Interpreter"
   - Selecciona el interprete que dice: `('.venv': venv) Python 3.x.x`

4. Verifica que funciono:
   - Abre la terminal de VS Code con `Ctrl + `` (control + tilde)
   - Deberia decir `(.venv)` al inicio de la linea automaticamente

**¿Que se creó?**
Se creo un archivo `.vscode/settings.json` con esta configuracion:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
    "python.terminal.activateEnvironment": true,
    "terminal.integrated.defaultProfile.windows": "PowerShell",
    "python.terminal.activateEnvInCurrentTerminal": true
}
```

**Explicacion de cada linea:**
| Linea | Que hace |
|-------|----------|
| `python.defaultInterpreterPath` | Le dice a VS Code donde esta el Python del `.venv` |
| `python.terminal.activateEnvironment` | Activa el `.venv` cuando abres una terminal |
| `terminal.integrated.defaultProfile.windows` | Usa PowerShell en Windows |
| `python.terminal.activateEnvInCurrentTerminal` | Activa el `.venv` en la terminal actual |

**IMPORTANTE:** El archivo `.vscode/settings.json` NO se sube a GitHub (esta en `.gitignore`). Cada quien configura su propio VS Code.

#### Errores comunes al abrir VS Code desde la terminal

**Error: `'code' no se reconoce como nombre de un cmdlet`**

Esto significa que VS Code no esta en el "PATH" de tu computadora. Es decir, la terminal no sabe donde encontrarlo. Tienes 3 soluciones:

---

**Solucion 1: Abrir VS Code desde el menu de Windows (la mas facil)**

1. Abre **VS Code** desde el menu de Windows (donde buscas apps)
2. Presiona `Ctrl + K` y luego `Ctrl + O` (esto abre la ventana "Abrir carpeta")
3. Navega hasta la carpeta `practica_2_api_ia`
4. Haz clic en "Seleccionar carpeta"
5. VS Code abrira la carpeta correcta

**Cuando hacer esto:** Si no quieres complicarte con configuraciones. Funciona siempre.

---

**Solucion 2: Agregar VS Code al PATH (permanente)**

Esto hace que `code .` funcione siempre en cualquier terminal.

1. Presiona `Win + R`, escribe `sysdm.cpl` y presiona Enter
2. Ve a la pestana **"Avanzado"**
3. Haz clic en **"Variables de entorno"**
4. En la seccion **"Variables del sistema"**, busca `Path` y haz doble clic
5. Haz clic en **"Nuevo"** y pega esta ruta:
```
C:\Users\TU_USUARIO\AppData\Local\Programs\Microsoft VS Code\bin
```
*(Reemplaza `TU_USUARIO` con el nombre de tu usuario de Windows)*
6. Haz clic en "Aceptar" en todas las ventanas
7. **Cierra y vuelve a abrir la terminal**
8. Prueba de nuevo: `code .`

**Para encontrar tu ruta exacta de VS Code:**
```powershell
# En la terminal, escribe:
Get-Command code -ErrorAction SilentlyContinue | Select-Object Source

# O busca manualmente en:
C:\Users\TU_USUARIO\AppData\Local\Programs\Microsoft VS Code\bin
```

---

**Solucion 3: Abrir VS Code desde la terminal con la ruta completa**

Si no quieres modificar el PATH, puedes usar la ruta completa:

```powershell
# En Windows, la ruta comun es:
& "C:\Users\$env:USERNAME\AppData\Local\Programs\Microsoft VS Code\Code.exe" .
```

O si tienes VS Code en otra ubicacion, buscalo asi:

```powershell
# Busca donde esta VS Code
Get-ChildItem "C:\Users\$env:USERNAME\AppData\Local\Programs\Microsoft VS Code" -Filter "Code.exe" -Recurse
```

---

**Solucion 4: Verificar la instalacion de VS Code**

Si ninguna solucion funciona, verifica que VS Code este bien instalado:

```powershell
# 1. Verifica que VS Code existe en tu computadora
Test-Path "C:\Users\$env:USERNAME\AppData\Local\Programs\Microsoft VS Code\Code.exe"

# 2. Si es FALSE, significa que VS Code no esta instalado o esta en otra ruta
#    Descargalo de: https://code.visualstudio.com/download

# 3. Si es TRUE pero `code .` no funciona, es un problema de PATH
#    Usa la Solucion 2 o Solucion 3
```

---

**Resumen rapido:**

| Solucion | Cuando usarla | Dificultad |
|----------|---------------|------------|
| Abrir desde menu | Siempre funciona | Facil |
| Agregar al PATH | Para que funcione para siempre | Media |
| Ruta completa | Si no quieres cambiar el PATH | Facil |
| Verificar instalacion | Si nada funciona | Facil |

---

### Paso 4: Instalar las librerias

```bash
# Instala todas las librerias que necesitamos
pip install -r requirements.txt
```

Esto tarda 1-2 minutos. Instala:
- `google-generativeai` — Para conectar con Gemini
- `openai` — Para DeepSeek, GPT y OpenRouter
- `anthropic` — Para Claude
- `python-dotenv` — Para leer el archivo .env

---

## PARTE 2: Obtener la Llave de API (10 min)

### Paso 5: Crear tu llave de Google Gemini (GRATIS)

1. Abre tu navegador y ve a: **https://aistudio.google.com/apikey**

2. Inicia sesion con tu cuenta de Google (la misma del Gmail)

3. Haz clic en el boton **"Create API Key"**

4. Selecciona o crea un proyecto

5. Se generara una llave larga que empieza con `AIza...`

6. **COPIA ESA LLAVE** (click derecho > Copiar)

**IMPORTANTE:** Esta llave es GRATIS pero tiene limites:
- 1500 solicitudes por dia
- 1 millon de tokens por dia
- No necesitas tarjeta de credito

---

### Paso 6: Crear el archivo .env

1. En la carpeta de esta practica, crea un archivo nuevo llamado `.env`

2. Abre el archivo con un editor de texto (VS Code, Bloc de notas)

3. Pega este contenido:

```env
GOOGLE_API_KEY=AIzaSyC_pega_tu_llave_aqui
```

4. Reemplaza `AIzaSyC_pega_tu_llave_aqui` con tu llave real

5. Guarda el archivo

**VERIFICACION:** Abre la terminal y verifica que el archivo existe:

```bash
# En Windows:
dir .env

# En Mac/Linux:
ls -la .env
```

---

## PARTE 3: Ejecutar el Chat (10 min)

### Paso 7: Ejecutar el script

Asegurate de que:
- El entorno virtual esta activado (ves `(.venv)` en la terminal)
- Estas en la carpeta correcta

```bash
python script_google_gemini.py
```

**Si todo sale bien, veras:**

```
============================================================
  CHAT CON GOOGLE GEMINI (IA de Google)
============================================================

  Escribe tu pregunta y presiona Enter.
  Para salir, escribe 'salir' o 'exit'.
  Para borrar el historial, escribe 'limpiar'.

------------------------------------------------------------

Tu pregunta:
```

### Paso 8: Haz tu primera pregunta

Escribe algo como:

```
Tu pregunta: Explica que es una base de datos en palabras simples
```

Espera 2-3 segundos y Gemini te respondiera.

### Paso 9: Prueba mas preguntas

```
Tu pregunta: Dame 3 ideas para un negocio de comida
Tu pregunta: Como funciona el phishing?
Tu pregunta: Escribe un poema sobre la programacion
```

### Paso 10: Prueba las funciones especiales

```
Tu pregunta: limpiar    (borra el historial)
Tu pregunta: salir      (cierra el programa)
```

---

## PARTE 4: Errores Comunes y Soluciones

### Error: "No se encontro la llave de API"

**Causa:** El archivo `.env` no tiene la llave o esta mal escrito.

**Solucion:**
1. Abre `.env` con un editor de texto
2. Verifica que la linea sea: `GOOGLE_API_KEY=AIzaSy...`
3. No debe haber espacios alrededor del `=`
4. La llave debe empezar con `AIza`

---

### Error: "ModuleNotFoundError: No module named 'google.generativeai'"

**Causa:** No instalaste las librerias o no activaste el `.venv`.

**Solucion:**
```bash
# Activa el entorno virtual primero
.venv\Scripts\activate

# Luego instala las librerias
pip install -r requirements.txt
```

---

### Error: "Quota exceeded" o "Limite excedido"

**Causa:** Agotaste las solicitudes gratuitas del dia.

**Solucion:**
- Espera 24 horas (el limite se renueva diariamente)
- O usa otra llave de otro proyecto de Google

---

### Error: "Permission denied" o "Acceso denegado"

**Causa:** La llave no tiene permisos o fue revocada.

**Solucion:**
1. Ve a https://aistudio.google.com/apikey
2. Elimina la llave vieja
3. Crea una nueva
4. Actualiza tu archivo `.env`

---

## PARTE 5: Explorar Otros Proveedores (Opcional)

Si terminaste antes o quieres experimentar, prueba los otros scripts:

### DeepSeek (Muy barato)
```bash
# 1. Obtener llave en https://platform.deepseek.com
# 2. Agregar en .env: DEEPSEEK_API_KEY=tu_llave
python script_deepseek.py
```

### OpenRouter (Multiples IAs)
```bash
# 1. Obtener llave en https://openrouter.ai
# 2. Agregar en .env: OPENROUTER_API_KEY=tu_llave
python script_openrouter.py
```

### OpenAI GPT (El mas conocido)
```bash
# 1. Obtener llave en https://platform.openai.com/api-keys
# 2. Agregar en .env: OPENAI_API_KEY=tu_llave
# NOTA: Necesitas credito de pago ($5 minimo)
python script_openai_gpt.py
```

### Claude (Anthropic)
```bash
# 1. Obtener llave en https://console.anthropic.com
# 2. Agregar en .env: ANTHROPIC_API_KEY=tu_llave
python script_claude.py
```

---

## Resultado Esperado

Al finalizar esta practica:

- [x] Tienes un entorno virtual `.venv` funcionando
- [x] Tienes un archivo `.env` con tu llave de Google
- [x] Puedes hacer preguntas a una IA real desde tu terminal
- [x] Entiendes que es una API key y como protegerla
- [x] Sabes como obtener llaves de otros proveedores

---

## Preguntas de Reflexion

1. **¿Por qué no ponemos la llave directamente en el codigo?**
   Porque si el codigo se comparte (GitHub, correo), la llave se filtra y cualquiera puede usarla (y gastar tu dinero).

2. **¿Por qué usamos .venv en lugar de instalar todo en la computadora?**
   Porque si dos proyectos necesitan versiones diferentes de una libreria, chocarian. El `.venv` mantiene cada proyecto aislado.

3. **¿Que pasa si alguien obtiene mi llave de OpenAI?**
   Puede hacer preguntas a la IA a tu costa. Si no tienes limite de gasto, te pueden dejar sin saldo.

4. **¿Cual es la diferencia entre Google Gemini y las demas?**
   Google Gemini es el unico que ofrece uso genuinamente gratis sin tarjeta de credito. Las demas requieren pago.

5. **¿Que archivo NUNCA debes subir a GitHub?**
   El `.env`. Contiene tus llaves secretas.

---

## PARTE 6: Como Replicar Esta Estructura en Tu Propio Proyecto

Esta practica es un **ejemplo replicable**. Cuando crees tu propio proyecto de IA, sigue estos pasos:

### Paso 1: Crea la carpeta de tu proyecto

```bash
# Usa snake_case, sin espacios
mkdir mi_proyecto_de_ia
cd mi_proyecto_de_ia
```

### Paso 2: Copia los archivos `.md` de configuracion

Copia estos archivos de esta practica a tu proyecto:

| Archivo | Que contiene | Que hacer |
|---------|--------------|-----------|
| `CONTEXT.md` | Quien eres y que haces | Modifica el contenido para tu proyecto |
| `RULES.md` | Reglas de codigo | Modifica segun tus necesidades |
| `SECURITY.md` | Lineas rojas | Adapta a tu caso de uso |
| `ARCHITECTURE.md` | Estructura del proyecto | Actualiza las carpetas |

### Paso 3: Crea el entorno virtual

```bash
# Crea la "burbuja"
python -m venv .venv

# Activa la "burbuja"
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```

### Paso 4: Crea el archivo `.gitignore`

```bash
# Crea el archivo
echo ".venv/" > .gitignore
echo ".env" >> .gitignore
echo "__pycache__/" >> .gitignore
```

### Paso 5: Crea el archivo `.env.example`

```bash
# Crea la plantilla de llaves
echo "GOOGLE_API_KEY=tu_llave_aqui" > .env.example
echo "DEEPSEEK_API_KEY=tu_llave_aqui" >> .env.example
```

### Paso 6: Crea tu propio `.env`

```bash
# Copia la plantilla
cp .env.example .env

# Abre .env y pegar tus llaves reales
```

### Paso 7: Inicializa Git

```bash
git init
git add .
git commit -m "Initial commit: estructura del proyecto"
```

### Paso 8: Sube a GitHub

```bash
# Crea el repositorio en GitHub primero, luego:
git remote add origin https://github.com/TU_USUARIO/mi_proyecto_de_ia.git
git push -u origin main
```

### Checklist final

- [ ] La carpeta tiene snake_case (sin espacios)
- [ ] Existe `.gitignore` que incluye `.env` y `.venv/`
- [ ] Existe `.env.example` (sin llaves reales)
- [ ] Existe `.env` (con llaves reales, NO subido a GitHub)
- [ ] Existe `.venv/` (entorno virtual activado)
- [ ] Los archivos `.md` estan personalizados para mi proyecto
- [ ] Los scripts funcionan con `python script_nombre.py`

### ¿Que archivos SI subo a GitHub?

| Archivo | Se sube | Razon |
|---------|---------|-------|
| `*.md` (CONTEXT, RULES, etc.) | SI | Documentacion compartida |
| `.vscode/settings.json` | SI | Configuracion del editor |
| `.gitignore` | SI | Reglas del repositorio |
| `requirements.txt` | SI | Dependencias del proyecto |
| `scripts/*.py` | SI | Codigo fuente |
| `.env` | **NO** | Contiene llaves secretas |
| `.venv/` | **NO** | Entorno virtual local |
