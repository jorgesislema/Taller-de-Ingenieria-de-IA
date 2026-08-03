# 📌 Guía Rápida - Laboratorio 2: Vibe Check IA

## 🗂️ Comandos Esenciales

| Comando | Qué hace |
|---------|----------|
| `python -m venv venv` | Crea entorno virtual |
| `venv\Scripts\activate` | Activa entorno (Windows) |
| `source venv/bin/activate` | Activa entorno (Mac/Linux) |
| `pip install -r requirements.txt` | Instala librerías |
| `pytest tests/ --cov=src --cov-report=term-missing` | Ejecuta tests con cobertura |
| `streamlit run app.py` | Lanza la app web |

---

## 📁 Estructura del Proyecto

```
vibe_check_ia/
├── app.py                    → Dashboard Streamlit
├── src/
│   ├── __init__.py
│   ├── analizador.py         → Lógica con Google Gemini
│   ├── datos.py              → Lectura de CSV con Pandas
│   └── graficos.py           → 3 gráficos con Plotly
├── tests/
│   ├── __init__.py
│   ├── test_analizador.py    → Tests del analizador
│   ├── test_datos.py         → Tests de datos
│   └── test_graficos.py      → Tests de gráficos
├── data/
│   └── tweets_espanol.csv    → 15 tweets de ejemplo
├── requirements.txt          → Librerías
├── .env                      → API Key (SECRETA)
├── .gitignore                → Archivos ocultos
├── context.md                → Qué es el proyecto
├── arquitectura.md           → Cómo está construido
├── estado.md                 → Estado actual
└── README.md                 → Documentación principal
```

---

## 🤖 Los 4 Prompts Clave

### PASO 1 - Lógica:
```
Actúa como un Ingeniero de Datos y Docente. Estoy creando un proyecto 
llamado 'Vibe Check IA'. Debo analizar tweets de un dataset en español 
para saber si son positivos, negativos o neutrales. No sé programar.

Ayúdame a definir la lógica paso a paso (en lenguaje sencillo). Dime qué 
debe hacer el programa desde que lee el archivo CSV hasta que muestra los 
gráficos en pantalla. No escribas código todavía, solo la lógica y los pasos.
```

### PASO 2 - Estructura:
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

### PASO 3 - Tests:
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

### PASO 4 - Código:
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

## 📊 Los 3 Gráficos

| Gráfico | Tipo | Qué muestra | Colores sugeridos |
|---------|------|-------------|-------------------|
| Pastel | Pie Chart | Distribución porcentual | Verde (pos), Rojo (neg), Azul (neut) |
| Barras | Bar Chart | Conteo exacto por emoción | Colores variados por emoción |
| Línea | Line Chart | Evolución temporal | Línea con puntos de datos |

---

## 🐛 Errores Comunes y Soluciones

| Error | Causa | Solución |
|-------|-------|----------|
| `ModuleNotFoundError` | No instalaste dependencias | `pip install -r requirements.txt` |
| `FileNotFoundError` | No estás en la carpeta correcta | `cd vibe_check_ia` |
| `API key not found` | Falta archivo .env | Crear `.env` con `GOOGLE_API_KEY=xxx` |
| `Streamlit no abre` | Puerto ocupado | `streamlit run app.py --server.port 8502` |
| `Tests fallan` | Error de código | Preguntar a la IA con el error |
| `Gráficos pequeños` | No configuraste layout | Usar `st.set_page_config(layout="wide")` |

---

## 🧪 Checklist de Calidad

- [ ] `requirements.txt` tiene todas las dependencias
- [ ] `.env` tiene la API key correcta (`GOOGLE_API_KEY`)
- [ ] Todos los archivos .py en src/ tienen comentarios
- [ ] Tests pasan con 90%+ cobertura
- [ ] App Streamlit funciona
- [ ] Los 3 gráficos se ven GRANDES
- [ ] Los gráficos están en VERTICAL (uno debajo del otro)
- [ ] Documentación está completa

---

## 💡 Consejos para Hablar con IA

1. **Sé específico**: "¿Qué hace la línea 15 de analizador.py?"
2. **Da contexto**: "Estoy en el Paso 2 del laboratorio"
3. **Pide ejemplos**: "Explícame con un ejemplo de la vida real"
4. **Verifica siempre**: La IA a veces se equivoca
5. **Guarda prompts útiles**: Para usarlos después

---

## 🆕 Si Te Atascas

1. **No entiendo la respuesta de la IA** → Pide: "Explícalo más simple"
2. **El código no funciona** → Pega el error y pregunta
3. **Los tests fallan** → Ejecuta `pytest -v` y pega la salida
4. **Streamlit no abre** → Verifica que esté instalado: `pip show streamlit`
5. **Los gráficos se ven pequeños** → Agrega `st.set_page_config(layout="wide")`
6. **No sé qué hacer** → Vuelve al Paso anterior y repásalo
