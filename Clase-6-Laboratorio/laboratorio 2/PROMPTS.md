# 🤖 Guía de Prompts para el Laboratorio 2

## 📋 PROMPTS ORIGINALES (Los 4 Pasos)

---

### 🧠 PASO 1: Definir la Lógica

```
Actúa como un Ingeniero de Datos y Docente. Estoy creando un proyecto 
llamado 'Vibe Check IA'. Debo analizar comentarios de un influencer 
ficticio para saber si su audiencia es positiva o negativa. No sé programar.

Ayúdame a definir la lógica paso a paso (en lenguaje sencillo). Dime qué 
debe hacer el programa desde que lee el archivo CSV hasta que muestra los 
gráficos en pantalla. No escribas código todavía, solo la lógica y los pasos.
```

---

### 📁 PASO 2: Definir la Estructura

```
Basado en esa lógica, dime cómo debo organizar mi proyecto en VS Code. 
Dame el esquema exacto de carpetas y archivos. Quiero que el código visual 
(el dashboard con gráficos) vaya en app.py y el código que habla con la 
IA vaya en analizador.py. Incluye una carpeta llamada data para mi archivo 
comentarios_ficticios.csv. También incluye los archivos de documentación 
(context.md, arquitectura.md, estado.md) y el archivo de pruebas 
test_analizador.py. Explica para qué sirve cada archivo.
```

---

### 🧪 PASO 3: Definir Tests

```
Ahora vamos a definir las métricas de calidad y los tests. Escribe en una 
tabla los tests automatizados (para el archivo test_analizador.py) usando 
pytest. Debemos probar: 1) Que lea bien el CSV. 2) Que un comentario vacío 
no rompa el programa. 3) Que la API de Gemini clasifique bien 
(Positivo/Negativo/Neutral) usando un 'mock' para no gastar tokens. 

Especifica que la cobertura de código (coverage) debe ser mínimo del 90% y 
la tasa de tests aprobados (pass rate) del 90%. Dime qué casos de prueba 
son vitales.
```

---

### 💻 PASO 4: Generar Código

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

## 🤖 PROMPTS ADICIONALES PARA MOMENTOS ESPECÍFICOS

---

### 📄 Cuando no entiendes un concepto

```
Estoy aprendiendo sobre programación. Explica qué es [CONCEPTO] 
de forma muy sencilla, con un ejemplo de la vida real.

[CONCEPTO] = 
- API
- Variable de entorno
- Mock en testing
- Gráfico de pastel
- Streamlit
```

---

### 🐛 Cuando el código tiene un error

```
Tengo un error en mi código y no sé por qué ocurre.

Error que obtengo:
[PEGA EL ERROR AQUÍ]

Archivo donde ocurre: [NOMBRE_DEL_ARCHIVO]

Código de la función:
[PEGA EL CÓDIGO AQUÍ]

Explícame:
1. Por qué ocurre este error
2. Cómo lo corrijo
3. Qué aprendí para evitarlo en el futuro
```

---

### 🔧 Cuando necesitas que el código tenga comentarios

```
Revisa este código y agrégale comentarios explicativos como si 
le explicaras a alguien de 10 años qué hace cada línea.

Código:
[PEGA EL CÓDIGO AQUÍ]

Formato de comentarios:
# Esta línea hace [X] porque [RAZÓN]
```

---

### 🧪 Cuando los tests fallan

```
Mis tests están fallando. Analiza por qué y ayúdame a corregirlo.

Resultado del test:
[PEGA LA SALIDA DEL TEST]

Código del test:
[PEGA EL CÓDIGO DEL TEST]

Código que se está testeando:
[PEGA EL CÓDIGO AQUÍ]

Dime:
1. Por qué falla
2. Cómo corrijo el código o el test
3. Qué caso no estoy considerando
```

---

### 📊 Cuando Streamlit no funciona

```
Mi app de Streamlit no muestra los gráficos correctamente.

Qué esperaba ver: [DESCRIBE QUÉ QUERÍAS]
Qué veo en pantalla: [DESCRIBE QUÉ VES]
Código de app.py:
[PEGA EL CÓDIGO]

Ayúdame a:
1. Identificar el problema
2. Corregirlo
3. Explicarme por qué no funcionaba
```

---

### 📝 Cuando necesitas documentación

```
Crea la documentación de mi proyecto Vibe Check IA.

El proyecto hace:
- Lee un CSV con comentarios de un influencer
- Usa la API de Gemini para clasificar sentimientos
- Muestra gráficos de pastel con Streamlit

Archivos que necesito:
1. context.md - Qué es y para qué sirve
2. arquitectura.md - Cómo está construido (incluye diagrama Mermaid)
3. estado.md - Versión 1.0, estado actual, próximas mejoras

Explica todo en lenguaje sencillo.
```

---

### 🎯 Cuando quieres mejorar el código

```
Tengo este código funcionando pero quiero mejorarlo.

Código actual:
[PEGA EL CÓDIGO]

Sugiere 3 mejoras que pueda hacer:
1. Una que haga el código más rápido
2. Una que lo haga más fácil de entender
3. Una que agregue una funcionalidad nueva

Explica cada mejora con código de ejemplo.
```

---

## 💡 Consejos para Conversation Efectiva con IA

### ✅ Buenas prácticas

1. **Sé específico:** "Revisa la función `cargar_api_key()`" vs "Revisa el código"
2. **Da contexto:** "Estoy en el Paso 2 del laboratorio" vs "Ayúdame"
3. **Pide explicaciones:** "Explícame por qué" vs solo "Corrígelo"
4. **Verifica siempre:** La IA a veces se equivoca
5. **Guarda prompts que funcionaron**

### ❌ Evita esto

1. Copiar sin leer
2. No preguntar "¿por qué?"
3. No verificar la respuesta
4. Pedir todo de golpe
5. No guardar tu progreso

---

## 🔄 Flujo de Conversación Efectiva

```
TÚ: [Prompt inicial]
IA: [Respuesta]
TÚ: "¿Por qué haces eso?"
IA: [Explicación]
TÚ: "¿Qué pasaría si cambio X?"
IA: [Predicción]
TÚ: "Prueba eso"
IA: [Nuevo código]
TÚ: "¿Cómo verifico que funciona?"
IA: [Instrucciones de prueba]
```
