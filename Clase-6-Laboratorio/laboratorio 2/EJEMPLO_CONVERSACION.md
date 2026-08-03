# 💬 Ejemplo de Conversación con IA

## Cómo deberían verse las interacciones en el Laboratorio 2

---

## Ejemplo 1: Paso 1 - Definir la Lógica

### ✅ Buen ejemplo:
```
ALUMNO: Actúa como un Ingeniero de Datos y Docente. Estoy creando un 
proyecto llamado 'Vibe Check IA'. Debo analizar tweets de un dataset 
en español para saber si son positivos, negativos o neutrales. No sé 
programar. Ayúdame a definir la lógica paso a paso.

IA: ¡Claro! Vamos a definir la lógica sin código:
    1. Primero leemos un archivo CSV con tweets
    2. Luego enviamos cada tweet a la IA de Google Gemini
    3. La IA nos dice si es positivo, negativo, neutral u otra emoción
    4. Contamos cuántos hay de cada tipo
    5. Mostramos 3 gráficos: pastel, barras y línea de tiempo

ALUMNO: ¿Por qué 3 gráficos y no solo uno?

IA: ¡Buena pregunta! Cada gráfico muestra algo diferente:
    - Pastel: Ve la PROPORCIÓN (¿qué porcentaje es positivo?)
    - Barras: Ve la CANTIDAD EXACTA (¿cuántos hay de cada tipo?)
    - Línea: Ve la EVOLUCIÓN (¿cambian los sentimientos en el tiempo?)
    
    Los 3 juntos te dan una visión completa.

ALUMNO: ¿Qué pasa si un tweet es muy largo?

IA: ¡Excelente pregunta! La IA puede manejar textos largos, pero:
    - Podríamos truncar a 280 caracteres (como Twitter)
    - O dividir en partes
    - Para este laboratorio, usaremos tweets cortos
```

---

## Ejemplo 2: Paso 2 - Definir la Estructura

### ✅ Buen ejemplo:
```
ALUMNO: Basado en esa lógica, dime cómo debo organizar mi proyecto. 
Quiero una estructura profesional con carpetas src/ y tests/.

IA: ¡Perfecto! Te sugiero esta estructura:
    
    vibe_check_ia/
    ├── app.py                    ← Dashboard (lo que ve el usuario)
    ├── src/
    │   ├── analizador.py         ← Lógica con Gemini
    │   ├── datos.py              ← Lectura de CSV
    │   └── graficos.py           ← Los 3 gráficos
    ├── tests/
    │   ├── test_analizador.py    ← Tests del analizador
    │   ├── test_datos.py         ← Tests de datos
    │   └── test_graficos.py      ← Tests de gráficos
    ├── data/
    │   └── tweets_espanol.csv    ← Los tweets
    └── Documentación (.md)

ALUMNO: ¿Por qué separar analizador.py, datos.py y graficos.py?

IA: ¡Es el principio de "separación de responsabilidades"!
    
    - datos.py: Solo lee y limpia datos
    - analizador.py: Solo habla con la IA
    - graficos.py: Solo crea visualizaciones
    
    ¿Por qué? Porque si mañana quiero cambiar de Gemini a ChatGPT,
    solo cambio analizador.py, no necesito tocar los demás.

ALUMNO: ¿Y los tests por qué van aparte en tests/?

IA: Los tests son como un examen para tu código:
    - Verifican que todo funcione
    - Si cambias algo, sabes si rompiste algo
    - Van aparte porque NO son parte del programa que ejecuta el usuario
```

---

## Ejemplo 3: Paso 4 - Generando Código

### ✅ Buen ejemplo:
```
ALUMNO: Ahora necesito el código de los gráficos. ¿Cómo deberían verse?

IA: ¡Vamos a definir los 3 gráficos! Te sugiero:
    
    1. PASTEL: Muestra porcentajes (positivo 40%, negativo 30%, etc.)
    2. BARRAS: Muestra conteos exactos (5 positivos, 3 negativos, etc.)
    3. LÍNEA: Muestra cómo cambian en el tiempo
    
    ¿Qué colores prefieres para cada emoción?

ALUMNO: ¿Cómo hago que los gráficos se vean grandes?

IA: ¡Buena pregunta! En Streamlit puedes:
    
    1. Usar st.set_page_config(layout="wide") al inicio
    2. Configurar height=600 y width=800 en cada gráfico
    3. Mostrarlos UNO DEBAJO DEL OTRO (vertical)
    
    Así se verán llenando toda la pantalla.

ALUMNO: ¿Puedo ver un ejemplo de código?

IA: ¡Claro! Aquí tienes un ejemplo básico:
    
    import plotly.express as px
    
    def crear_grafico_pastel(datos):
        fig = px.pie(datos, names='sentimiento', title='Distribución')
        fig.update_layout(height=600, width=800)
        return fig
    
    ¿Quieres que te muestre los 3 gráficos completos?
```

---

## Ejemplo 4: Cuando Hay un Error

### ✅ Buen ejemplo:
```
ALUMNO: Obtengo este error cuando ejecuto python app.py:
        
        ModuleNotFoundError: No module named 'streamlit'
        
        ¿Qué puedo hacer?

IA: ¡Falta instalar Streamlit! Ejecuta en tu terminal:
    
    pip install streamlit
    
    Si tienes entorno virtual activo, asegúrate de que esté activado.

ALUMNO: Ya lo instalé pero ahora sale otro error:
        
        FileNotFoundError: data/tweets_espanol.csv not found

IA: El archivo CSV no está en la ubicación correcta. Verifica:
    
    1. ¿Existe la carpeta data/?
    2. ¿El archivo se llama exactamente tweets_espanol.csv?
    3. ¿Está dentro de data/?
    
    Puedes verificar con:
    dir data\ (Windows)
    ls data/ (Mac/Linux)

ALUMNO: ¡Ya funciona! Gracias

IA: ¡Excelente! Recuerda: cuando veas un error, siempre:
    1. Lee el mensaje completo
    2. Identifica qué archivo falla
    3. Busca la causa raíz
```

---

## Ejemplo 5: Verificando Comprensión

### ✅ Buen ejemplo:
```
ALUMNO: Ya tengo el código funcionando. ¿Puedo explicarte qué hace 
cada archivo para verificar que entendí?

IA: ¡Por favor! Me encanta que quieras verificar tu comprensión.

ALUMNO: 
- app.py: Es la parte visual, usa Streamlit para mostrar gráficos
- src/analizador.py: Es la lógica, habla con la API de Gemini
- src/datos.py: Lee y limpia el CSV con pandas
- src/graficos.py: Crea los 3 gráficos con Plotly
- tests/: Son pruebas que verifican que todo funcione
- .env: Guarda la API key de forma segura

IA: ¡Muy bien! Solo una precisión:
    
    .env no es parte del código, es configuración.
    La diferencia es:
    - Código: Lo que el programa HACE
    - Configuración: Datos que el programa USA
    
    ¿Sabes por qué .env no se sube a GitHub?

ALUMNO: Porque tiene información secreta

IA: ¡Exacto! Es como no subir fotos de tu contraseña a internet.
    La API key es como una contraseña para usar la IA.
```

---

## 📋 Resumen: Características de una Buena Conversación

| Característica | Ejemplo |
|----------------|---------|
| Pregunta específica | "¿Qué hace la línea 15 de analizador.py?" |
| Da contexto | "Estoy en el Paso 2 del laboratorio" |
| Pide explicaciones | "¿Por qué se hace así?" |
| Verifica comprensión | "Déjame explicarte qué entendí" |
| Pregunta cuando no entiende | "No me quedó claro, explícalo otra vez" |

---

## 🚫 Evita Esto

| ❌ No hagas | ✅ Mejor haz |
|-------------|-------------|
| Copiar sin leer | Leer y entender cada línea |
| "No funciona" | "Obtengo este error: [error]" |
| "Hazme todo" | "Ayúdame a entender paso a paso" |
| No preguntar | "¿Por qué haces eso?" |
| No verificar | "¿Cómo puedo probar que funciona?" |
