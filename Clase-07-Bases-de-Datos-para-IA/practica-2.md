# Práctica 2 — Clase 7: Análisis de Sentimientos con Google Sheets + Looker

> Ejercicio práctico: Usar una hoja de cálculo como base de datos, aplicar un complemento de IA para análisis de sentimientos, y visualizar los resultados.

---

## ¿Por qué esta práctica?

En los apuntes aprendiste que **Google Sheets también es una base de datos**: organiza información en filas y columnas, se puede consultar, filtrar y conectar con otras herramientas. Hoy vas a comprobarlo en carne propia.

> **Dato clave:** Muchas empresas medianas y pequeñas gestionan TODOS sus datos en Google Sheets. Saber conectar una "base de datos de oficina" con herramientas de IA y visualización te convierte en el puente entre el mundo analógico y el digital. **Eso hace un Ingeniero de IA.**

---

## Antes de empezar

Necesitás:
- Una cuenta de Google (Gmail). Si no tenés, creá una gratis en [gmail.com](https://gmail.com).
- El archivo [`tweets_espanol.csv`](tweets_espanol.csv) que está en esta misma carpeta.
- 15 minutos de tu tiempo.

---

## Paso 1: Abrí el archivo en Google Sheets

### 1.1 Descargá el CSV
El archivo `tweets_espanol.csv` está en esta carpeta. Contiene 15 tweets en español con su sentimiento ya clasificado manualmente. Hoy vamos a hacer que una IA los clasifique automáticamente y comparar resultados.

### 1.2 Subilo a Google Sheets

1. Abrí [sheets.google.com](https://sheets.google.com)
2. Clic en **+ En blanco** para crear una hoja nueva
3. Menú **Archivo → Importar**
4. Seleccioná la pestaña **Subir** y arrastrá el archivo `tweets_espanol.csv`
5. En el menú que aparece, elegí **Reemplazar hoja actual**
6. Clic en **Importar datos**

Deberías ver algo así:

```
┌────┬──────────────┬──────────────────────────────────────────────┬────────────┬──────────────┐
│ id │   usuario    │                    tweet                     │   fecha    │ sentimiento  │
├────┼──────────────┼──────────────────────────────────────────────┼────────────┼──────────────┤
│ 1  │ maria_luz    │ ¡NeoMax eres el mejor! Tus tutoriales me...  │ 2024-01-15 │ positivo     │
│ 2  │ carlos_dev   │ Contenido muy útil para aprender...          │ 2024-01-16 │ positivo     │
│ 3  │ ana_tech     │ No me gustó el último video, muy básico...   │ 2024-01-16 │ negativo     │
│... │ ...          │ ...                                          │ ...        │ ...          │
│ 15 │ sofia_dev    │ El contenido está bien pero los gráficos...  │ 2024-01-22 │ neutral      │
└────┴──────────────┴──────────────────────────────────────────────┴────────────┴──────────────┘
```

> **Esto es una base de datos.** Columnas = campos. Filas = registros. Ya estás usando una sin darte cuenta.

### 1.3 Renombrá la hoja
Doble clic en "Hoja 1" abajo a la izquierda y poné: `dataset_original`

---

## Paso 2: Instalá el complemento de Análisis de Sentimientos

Google Sheets tiene una "tienda de extensiones" con herramientas que agregan superpoderes. Una de ellas hace análisis de sentimientos con IA **sin escribir código**.

### 2.1 Instalar

1. Menú **Extensiones → Complementos → Descargar complementos**
2. En el buscador, escribí: `Sentiment Analysis`
3. Buscá uno que se llame **"Sentiment Analysis for Google Sheets"** o **"Text Analysis"** o **"MonkeyLearn"**
4. Clic en **Instalar** y aceptá los permisos

> **⚠️ Por si no encontrás el complemento exacto:** Algunas opciones alternativas que funcionan igual:
> - **MonkeyLearn** — tiene prueba gratuita
> - **Text Analysis by AYLIEN** — tiene capa gratuita
> - **GPT for Sheets** — usa la API de OpenAI directamente (requiere API key, pero es la más potente)

### 2.2 Si nada de eso funciona: Plan B (Google Apps Script)

No te preocupes. Google Sheets tiene una herramienta interna para ejecutar código sin instalar nada. Seguí estos pasos:

#### 2.2.1 Crear el script

1. Menú **Extensiones → Apps Script**
2. Se abre una pestaña nueva con un editor de código. Borrá TODO lo que aparezca (la función `myFunction` que viene por defecto).
3. Pegá el código completo de abajo (desde `function` hasta la última `}`):

```javascript
function ANALIZAR_SENTIMIENTO(texto) {
  if (!texto || texto === '') return 'Sin texto';

  var t = String(texto).toLowerCase();

  var positivas = ['excelente', 'genial', 'gracias', 'me encanta', 'mejor',
                   'util', 'ayuda', 'amo', 'wow', 'increible', 'recomiendo',
                   'buen', 'sorprendio', 'energia', 'aprendo', 'suscriptores'];
  var negativas = ['malo', 'no me gusto', 'decepcionado', 'pesimo', 'horrible',
                   'regular', 'basico', 'no entiendo', 'confundido', 'miedo',
                   'asustado', 'dificil', 'decepciona'];

  var puntaje = 0;

  for (var i = 0; i < positivas.length; i++) {
    if (t.indexOf(positivas[i]) !== -1) puntaje = puntaje + 1;
  }
  for (var j = 0; j < negativas.length; j++) {
    if (t.indexOf(negativas[j]) !== -1) puntaje = puntaje - 1;
  }

  if (puntaje > 0) return 'Positivo';
  if (puntaje < 0) return 'Negativo';
  return 'Neutral';
}
```

#### 2.2.2 Guardar BIEN (este paso es el que falla siempre)

1. Clic en el ícono del **diskette** (💾) en la barra superior, O menú **Archivo → Guardar**
2. En la ventana que aparece, poné como nombre: `AnalizadorSentimientos`
3. Clic en **Aceptar**
4. **IMPORTANTE:** Clic en el botón **"Ejecutar"** (▶️) una vez para autorizar los permisos:
   - Te va a pedir "Autorización necesaria"
   - Clic en **Revisar permisos**
   - Elegí tu cuenta de Google
   - Clic en **Avanzado → Ir a AnalizadorSentimientos (no seguro)**
   - Clic en **Permitir**

#### 2.2.3 ¡A probar!

1. Volvé a tu hoja de cálculo de Google Sheets
2. En la columna F1 escribí: `sentimiento_ia`
3. En la celda F2 escribí **exactamente**:
   ```
   =ANALIZAR_SENTIMIENTO(C2)
   ```
4. Presioná Enter. Deberías ver `Positivo`, `Negativo` o `Neutral`.
5. Arrastrá la esquinita inferior derecha de F2 hacia abajo hasta F16.

> **Acabás de programar tu primera función personalizada en Google Sheets.**

#### 2.2.4 ¿Te salió #NAME? o #¿NOMBRE? — Solución rápida

| Error | Causa | Solución |
|-------|-------|----------|
| `#NAME?` / `#¿NOMBRE?` | El script no se guardó o el nombre no coincide | Volvé a Apps Script, verificá que la función se llame `ANALIZAR_SENTIMIENTO` (todo en mayúsculas, con guiones bajos), guardá de nuevo y recargá la hoja (F5) |
| `#ERROR!` | La celda C2 está vacía o tiene algo raro | Verificá que la columna C tenga los tweets |
| Sale "Sin texto" | La celda está vacía | Normal, es para filas sin tweet |
| Pide permisos cada vez | No autorizaste bien | Volvé al editor de Apps Script, clic en ▶️ Ejecutar, y aceptá TODOS los permisos |

---

## Paso 3: Ejecutar el análisis con el complemento

El procedimiento exacto depende del complemento, pero la lógica es universal:

### Con Sentiment Analysis for Google Sheets:
1. Menú **Extensiones → Sentiment Analysis → Start**
2. Seleccioná la columna C (tweets) como texto a analizar
3. Elegí el idioma **Español**
4. Clic en **Analyze**
5. Los resultados aparecerán en una nueva columna

### Con GPT for Sheets:
1. Menú **Extensiones → GPT for Sheets → Launch**
2. En una celda nueva (F2), escribí:
   ```
   =GPT("Clasifica este tweet en Positivo, Negativo o Neutral. Responde SOLO con una palabra. Tweet: " & C2)
   ```
3. Arrastrá hacia abajo

---

## Paso 4: Compará resultados

Una vez que tengas los resultados de la IA, creá una tabla de comparación:

| Tweet | Sentimiento Original (columna E) | Sentimiento de la IA (columna F) | ¿Coinciden? |
|-------|----------------------------------|----------------------------------|-------------|
| 1 | positivo | | |
| 2 | positivo | | |
| ... | ... | ... | |

Para la columna "¿Coinciden?", usá esta fórmula en G2:
```
=SI(E2=F2;"SI";"NO")
```

### Preguntas para reflexionar:
- ¿Cuántos aciertos tuvo la IA? ¿Cuántos fallos?
- ¿Falló más en positivos, negativos o neutrales?
- ¿Por qué creés que falló donde falló?

---

## Paso 5: ¡A graficar! (Google Sheets)

Las bases de datos no solo guardan datos: **los muestran**.

### 5.1 Gráfico de pastel (distribución de sentimientos)

1. Seleccioná la columna F (resultados de la IA), incluyendo el encabezado
2. Menú **Insertar → Gráfico**
3. En el panel derecho, en "Tipo de gráfico", elegí **Gráfico circular** (pastel)
4. Personalizá: título "Distribución de Sentimientos — IA", etiquetas con porcentaje, colores

### 5.2 Gráfico de barras (conteo por sentimiento)

1. Primero, creá una tabla de conteo. En una zona libre de la hoja:

```
┌────────────┬────────┐
│ Sentimiento│ Conteo │
├────────────┼────────┤
│ Positivo   │   ?    │
│ Negativo   │   ?    │
│ Neutral    │   ?    │
└────────────┴────────┘
```

Usá la fórmula `=CONTAR.SI(F2:F16;"Positivo")` para cada fila.

2. Seleccioná esa mini-tabla
3. Menú **Insertar → Gráfico → Gráfico de columnas**

---

## Paso 6: Subí de nivel con Looker Studio

Looker Studio (antes Google Data Studio) es una herramienta gratuita de Google para crear dashboards profesionales. Es como los gráficos de Google Sheets, pero con esteroides.

### 6.1 Conectar los datos

1. Abrí [lookerstudio.google.com](https://lookerstudio.google.com)
2. Clic en **Crear → Informe**
3. Te va a pedir una fuente de datos. Elegí **Google Sheets**
4. Seleccioná tu hoja de cálculo y la hoja `dataset_original`
5. Clic en **Añadir**

### 6.2 Crear visualizaciones

Looker te muestra un lienzo en blanco. Arriba hay una barra de herramientas con tipos de gráficos:

```
┌──────────────────────────────────────────────────────────────┐
│  📊  📈  🥧  📉  🗺️  📋  🔢  ...   (barra de gráficos)     │
└──────────────────────────────────────────────────────────────┘
```

**Creá estos 3 gráficos:**

| # | Tipo | Qué mostrar | Dimensión | Métrica |
|---|------|-------------|-----------|---------|
| 1 | 🥧 Pastel | Distribución de sentimientos | `sentimiento` | Record count |
| 2 | 📊 Barras | Tweets por usuario | `usuario` | Record count |
| 3 | 📋 Tabla | Todos los tweets con su sentimiento | `tweet`, `sentimiento` | — |

### 6.3 Mini-dashboard final

Acomodá los 3 gráficos en el lienzo así:

```
┌─────────────────────────────────────────────────────┐
│     📊 DASHBOARD: ANÁLISIS DE SENTIMIENTOS          │
│                                                     │
│  ┌──────────────────┐  ┌──────────────────────────┐ │
│  │   🥧 PASTEL      │  │   📊 BARRAS              │ │
│  │   Distribución   │  │   Tweets por usuario     │ │
│  │   de sentimientos│  │                          │ │
│  │                  │  │   ████████  maria_luz    │ │
│  │   🔵 Positivo    │  │   ████████  carlos_dev   │ │
│  │   🔴 Negativo    │  │   ██████    ana_tech     │ │
│  │   ⚪ Neutral     │  │   ████      luis_gamer   │ │
│  └──────────────────┘  └──────────────────────────┘ │
│                                                     │
│  ┌──────────────────────────────────────────────────┐│
│  │  📋 TABLA: Todos los tweets                      ││
│  │  tweet                    │  sentimiento         ││
│  │  ¡NeoMax eres el mejor!...│  positivo            ││
│  │  No me gustó el último... │  negativo            ││
│  └──────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────┘
```

### 6.4 Compartí tu dashboard

1. Botón **Compartir** arriba a la derecha
2. Elegí **Cualquier persona con el enlace puede ver**
3. Copiá el link y compartilo con la clase

---

## Paso 7: Conexión con lo aprendido en clase

Respondé en una hoja nueva de Google Sheets llamada `reflexion`:

| Pregunta | Tu respuesta |
|----------|-------------|
| ¿Por qué Google Sheets es una base de datos? | |
| ¿Qué tipo de base de datos es? (Relacional / NoSQL / Clave-Valor / Vectorial) | |
| ¿Qué hace el complemento de Sentiment Analysis que una base de datos normal no puede hacer? | |
| Si tuvieras 1 millón de tweets en lugar de 15, ¿seguirías usando Google Sheets? ¿Qué usarías? | |
| ¿Para qué otro proyecto usarías Looker Studio? | |

---

## El Ing. de IA en esta práctica

Esta práctica te pone en 3 roles distintos, todos parte del día a día de un Ingeniero de IA:

| Rol | Lo que hiciste |
|-----|---------------|
| **Arquitecto de Datos** | Elegiste Google Sheets como base de datos para un volumen pequeño de datos |
| **Ingeniero de Integración** | Conectaste una base de datos (Sheets) con una herramienta de IA (complemento) |
| **Ingeniero de Visualización** | Creaste dashboards en Looker para comunicar resultados a personas no técnicas |

> **Reflexión final:** Un Ingeniero de IA no es el que escribe el código del complemento de sentimientos. Es el que sabe QUE existe, DÓNDE encontrarlo, y CÓMO conectarlo con la base de datos correcta para resolver un problema real. Google Sheets + Complemento de IA + Looker = sistema profesional sin una línea de código.

---

## Resumen visual

```
┌──────────────────────────────────────────────────────────────────┐
│  FLUJO COMPLETO DE LA PRÁCTICA                                    │
│                                                                   │
│  tweets_espanol.csv                                               │
│        │                                                          │
│        ▼                                                          │
│  ┌─────────────┐     ┌──────────────────┐     ┌───────────────┐  │
│  │   GOOGLE    │ ──► │  COMPLEMENTO DE  │ ──► │    LOOKER     │  │
│  │   SHEETS    │     │  SENTIMIENTOS    │     │    STUDIO     │  │
│  │  "La base"  │     │  "La IA"         │     │  "El dashboard"│ │
│  └─────────────┘     └──────────────────┘     └───────────────┘  │
│                                                                   │
│  ⬆ Base de Datos     ⬆ Análisis de IA     ⬆ Visualización       │
│  Relacional          Sin código           Profesional             │
└──────────────────────────────────────────────────────────────────┘
```

---

## 🏆 Criterios de Éxito

Completaste la práctica exitosamente si:
- [ ] Subiste el CSV a Google Sheets y se ve en filas y columnas
- [ ] Instalaste y ejecutaste el complemento de sentimientos (o usaste Apps Script)
- [ ] Comparaste los resultados de la IA con los sentimientos originales
- [ ] Creaste al menos 1 gráfico en Google Sheets (pastel o barras)
- [ ] Conectaste los datos a Looker Studio y generaste al menos 2 visualizaciones
- [ ] Tu dashboard de Looker es público y compartible
- [ ] Respondiste las preguntas de reflexión
- [ ] Podés explicarle a alguien por qué Google Sheets ES una base de datos

---

## 💡 Bonus: ¿Y si quiero hacerlo con 1 millón de tweets?

Esta práctica usa 15 tweets. Pero, ¿y si tuvieras 1 millón?

| Escala | Base de Datos | Herramienta de IA | Visualización |
|--------|--------------|-------------------|---------------|
| 15 tweets | Google Sheets | Complemento | Looker / Sheets |
| 1,000 tweets | Google Sheets | Complemento | Looker |
| 100,000 tweets | PostgreSQL | Python + API de IA | Looker conectado a PostgreSQL |
| 1,000,000 tweets | PostgreSQL + Redis (caché) | Python + API con caché | Looker + Grafana |

> **Moraleja:** La arquitectura cambia según la escala. Pero el concepto es el mismo. Aprendiste el concepto con 15 tweets; con 1 millón solo cambiás las herramientas, no la lógica.
