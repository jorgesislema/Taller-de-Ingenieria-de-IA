# 🧪 Laboratorio 2: Vibe Check IA - Analizador de Sentimientos

## 🎯 Objetivo
Crear un programa que analice sentimientos de tweets usando IA, generando gráficos interactivos con Streamlit.

## 🧠 Lo que aprenderás
- A conversar con IA de forma estructurada (no solo copiar y pegar)
- A definir la lógica de un programa antes de programar
- A organizar un proyecto de software
- A usar Streamlit para crear dashboards
- A escribir tests automáticos

---

## 📋 Requisitos Previos
- Python 3.10+ instalado
- VS Code instalado
- API Key de Google Gemini (gratis en [Google AI Studio](https://aistudio.google.com/))
- Haber completado el Laboratorio 1

---

## ⏱ Duración Estimada: 90 minutos

---

# 🚀 PASO 1: Define la Lógica (El "Qué")

**Objetivo:** Antes de programar, debemos entender QUÉ debe hacer el programa.

## Instrucciones

1. Abre tu navegador y ve a [Gemini](https://gemini.google.com/) o usa ChatGPT
2. **Copia y pega** el siguiente prompt tal como está
3. **Lee** la respuesta que te da la IA
4. **No saltes al siguiente paso** hasta entender la lógica

## 📝 Prompt 1 - Copia y pega esto:

```
Actúa como un Ingeniero de Datos y Docente. Estoy creando un proyecto 
llamado 'Vibe Check IA'. Debo analizar tweets de un dataset en español 
para saber si son positivos, negativos o neutrales. No sé programar.

Ayúdame a definir la lógica paso a paso (en lenguaje sencillo). Dime qué 
debe hacer el programa desde que lee el archivo CSV hasta que muestra los 
gráficos en pantalla. No escribas código todavía, solo la lógica y los pasos.
```

## ✅ Verificación del Paso 1

Después de leer la respuesta, asegúrate de entender:
- [ ] Qué es un CSV
- [ ] Qué hace una API de IA
- [ ] Qué es un gráfico de pastel, barras y línea de tiempo
- [ ] El flujo: Leer → Analizar → Mostrar

---

# 📁 PASO 2: Define las Partes y Carpetas (El "Dónde")

**Objetivo:** Aprender a organizar un proyecto de software.

## Instrucciones

1. **Copia y pega** el siguiente prompt
2. **Observa** cómo la IA organiza los archivos
3. **Toma notas** de la estructura que te sugiere

## 📝 Prompt 2 - Copia y pega esto:

```
Basado en esa lógica, dime cómo debo organizar mi proyecto en VS Code. 
Dame el esquema exacto de carpetas y archivos. Quiero que el proyecto 
tenga esta estructura profesional:

- Carpeta src/ con los archivos de lógica
- Carpeta tests/ con los tests automáticos
- Carpeta data/ con el dataset
- Archivos de documentación (context.md, arquitectura.md, estado.md)
- Archivo app.py en la raíz para el dashboard

Los archivos en src/ deben ser:
- analizador.py (habla con la API de Gemini)
- datos.py (lee y limpia el CSV)
- graficos.py (crea los gráficos con Plotly)

Los archivos en tests/ deben ser:
- test_analizador.py
- test_datos.py
- test_graficos.py

Explica para qué sirve cada archivo.
```

## ✅ Verificación del Paso 2

Tu estructura debería verse así:
```
vibe_check_ia/
├── .env                          # API Key secreta
├── .gitignore                    # Archivos ocultos
├── requirements.txt              # Librerías necesarias
├── app.py                        # Dashboard principal
├── context.md                    # Qué es el proyecto
├── arquitectura.md               # Cómo está construido
├── estado.md                     # Estado del proyecto
├── README.md                     # Documentación principal
├── src/
│   ├── __init__.py               # Hace que src/ sea paquete
│   ├── analizador.py             # Lógica con Gemini
│   ├── datos.py                  # Lectura del CSV
│   └── graficos.py               # Gráficos con Plotly
├── tests/
│   ├── __init__.py               # Hace que tests/ sea paquete
│   ├── test_analizador.py        # Tests del analizador
│   ├── test_datos.py             # Tests de datos
│   └── test_graficos.py          # Tests de gráficos
└── data/
    └── tweets_espanol.csv        # Dataset de ejemplo
```

---

# 🧪 PASO 3: Define las Métricas de Calidad (El "Cuánto")

**Objetivo:** Entender que el software debe ser probado.

## Instrucciones

1. **Copia y pega** el siguiente prompt
2. **Lee** los casos de prueba que la IA sugiere
3. **Entiende** por qué cada test es importante

## 📝 Prompt 3 - Copia y pega esto:

```
Ahora vamos a definir las métricas de calidad y los tests. Escribe en una 
tabla los tests automatizados (para los archivos en tests/) usando pytest. 

Debemos probar:
1) test_analizador.py: Que la IA clasifique bien (Positivo/Negativo/Neutral) 
   usando un 'mock' para no gastar tokens
2) test_datos.py: Que lea bien el CSV y que un archivo vacío no rompa el programa
3) test_graficos.py: Que genere los gráficos correctamente

Especifica que la cobertura de código (coverage) debe ser mínimo del 90% y 
la tasa de tests aprobados (pass rate) del 90%. Dime qué casos de prueba 
son vitales.
```

## ✅ Verificación del Paso 3

Los tests vitales son:
| # | Test | Por qué es importante |
|---|------|----------------------|
| 1 | Leer CSV | Sin datos no hay análisis |
| 2 | Comentario vacío | No debe crashear |
| 3 | Clasificación con mock | No gastar tokens reales |
| 4 | Respuesta de la IA | Formato correcto |
| 5 | Generación de gráficos | Que muestre datos |

---

# 💻 PASO 4: Generación del Código (El "Cómo")

**Objetivo:** Recién aquí pedimos el código, ya sabiendo qué queremos.

## Instrucciones

1. **Copia y pega** el siguiente prompt
2. **Pide** que te dé el código por partes si es muy largo
3. **Crea** cada archivo en VS Code
4. **No copies ciegamente** - lee cada comentario

## 📝 Prompt 4 - Copia y pega esto:

```
¡Excelente! Ahora que tenemos la lógica, la estructura y los tests, 
procede a escribir el código.

Entrégame el resultado en las siguientes secciones:

1. El contenido del archivo data/tweets_espanol.csv (crea 15 tweets 
   de ejemplo en español sobre un influencer llamado 'NeoMax', con 
   sentimientos variados: positivo, negativo, neutral, y otros como 
   sorprendido, confundido, asustado).

2. El código de src/analizador.py (usa google-generativeai con el modelo 
   "gemini-flash-latest" y lee la API Key desde .env).

3. El código de src/datos.py (usa pandas para leer y limpiar el CSV).

4. El código de src/graficos.py (usa plotly para crear 3 gráficos:
   - Gráfico de PASTEL (pie chart) con distribución de sentimientos
   - Gráfico de BARRAS con conteo por cada emoción
   - Gráfico de LÍNEA DE TIEMPO mostrando evolución temporal
   
   REGLAS PARA GRÁFICOS:
   - Cada gráfico en su propia función
   - Usar height=600 y width=800 para que sean GRANDES
   - Colores llamativos y diferenciados
   - Títulos claros en español

5. El código de app.py (usa streamlit para crear el dashboard):
   - Título principal: "🎭 Vibe Check IA - Analizador de Sentimientos"
   - Sidebar con filtros de sentimiento
   - Botón "Analizar Tweets"
   - Mostrar los 3 gráficos DEBAJO uno del otro (vertical), NO lado a lado
   - Usar st.set_page_config(layout="wide") para pantalla completa

6. El código de tests/ (test_analizador.py, test_datos.py, test_graficos.py)

7. El archivo requirements.txt

8. Archivos de documentación: context.md, arquitectura.md, estado.md, README.md

Agrega comentarios con # en cada archivo explicando qué hace cada bloque 
como si tuviera 10 años. Asegúrate de que el código cumpla con los tests 
del Paso 3.
```

---

# 🚀 FASE 5: Ejecución y Prueba (El "Wow")

**Objetivo:** Ver funcionar todo lo que construiste.

## Paso 5.1: Crear entorno virtual

```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

## Paso 5.2: Instalar dependencias

```bash
pip install -r requirements.txt
```

## Paso 5.3: Configurar API Key

Crea el archivo `.env` en la raíz del proyecto:

```
GOOGLE_API_KEY=tu_llave_de_gemini_aquí
```

## Paso 5.4: Ejecutar tests

```bash
pytest tests/ --cov=src --cov-report=term-missing --cov-fail-under=90
```

**Meta:** Cobertura mínima del 90%

## Paso 5.5: Lanzar la App

```bash
streamlit run app.py
```

**¡Se abrirá tu navegador con el Dashboard!**

## Paso 5.6: Probar la App

1. Selecciona un filtro de sentimiento en el sidebar
2. Haz clic en "Analizar Tweets"
3. Espera a que la IA clasifique cada tweet
4. Observa los 3 gráficos:
   - 🥧 Pastel: distribución de sentimientos
   - 📊 Barras: conteo de emociones
   - 📈 Línea de tiempo: evolución temporal

---

# 📝 FASE 6: Documentación

Crea los archivos de documentación pidiéndole a la IA:

## Prompt 5 - Documentación:

```
Crea los siguientes archivos de documentación para mi proyecto Vibe Check IA:

1. context.md - Explica qué es el proyecto y qué problema resuelve
2. arquitectura.md - Incluye un diagrama Mermaid del flujo de datos
3. estado.md - Versión 1.0, funcional, próximas mejoras
4. README.md - Instrucciones de instalación y uso

Explica todo en lenguaje sencillo como si fuera para un estudiante 
de primer año.
```

---

# ✅ Checklist Final

Marca con ✓ cuando completés:

- [ ] Fui capaz de definir la lógica ANTES de programar
- [ ] Organicé mi proyecto en carpetas correctamente
- [ ] Definí métricas de calidad y tests
- [ ] El código tiene comentarios explicativos
- [ ] Los tests pasan con 90% de cobertura
- [ ] La app Streamlit funciona correctamente
- [ ] Los 3 gráficos se ven GRANDES y en vertical
- [ ] Puedo explicar qué hace cada archivo
- [ ] Documenté el proyecto con los archivos .md

---

# 🤖 Consejos para Conversar con IA

| ❌ Mal prompt | ✅ Buen prompt |
|--------------|---------------|
| "Hazme un programa" | "Actúa como docente, ayúdame a definir la lógica de..." |
| "Ponme el código" | "Escribe el código con comentarios que expliquen cada bloque" |
| "¿Qué está mal?" | "Revisa esta función y dime si usa la variable correcta" |
| "No funciona" | "Obtengo este error: [pega el error], ¿qué puede ser?" |

---

**⏱ Tiempo total: 90 minutos**
