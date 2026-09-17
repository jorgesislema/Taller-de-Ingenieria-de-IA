# Clase 5 — ¿Cuál IA Elijo? — Benchmarks y Selección Profesional de Modelos
### (Versión revisada y actualizada — septiembre 2026)

> Material de apoyo para el estudiante. Leelo directo en GitHub o en la vista web.
> **Nota importante sobre las tablas de esta clase:** los benchmarks de IA cambian de líder cada pocas semanas. Todas las tablas con puntajes de modelos específicos en esta clase son **una foto de un momento dado (septiembre 2026)**, pensada para que entiendas *cómo leer* un leaderboard — no para que memorices qué modelo "ganó". Cada tabla incluye dónde consultar el ranking actualizado.

---

## Filosofía de la clase

> **Un Ingeniero de IA no elige un modelo porque "suena bien" o porque lo recomendó un YouTuber. Elige un modelo porque leyó las métricas, entendió las pruebas, y sabe exactamente qué está pagando.**

En la Clase 4 vimos cuánto cuesta cada token. Hoy damos un paso más: **¿cómo sé cuál modelo es el correcto para mi proyecto?** No existe "el mejor modelo de IA". Existe el modelo correcto para cada tarea. Y para saber cuál es, necesitás entender las pruebas que los evalúan.

Si te llevás una sola cosa de esta clase, que sea esta:

> **No existe "el mejor modelo de IA". Existe el benchmark correcto para tu caso de uso, y el modelo que lidera ese benchmark — hoy. La semana que viene puede ser otro.**

---

## 1. ¿Qué es un Benchmark?

### 1.1 La analogía del examen de oposición

Cuando querés entrar a una universidad, rendís un examen. Ese examen tiene preguntas de distintas áreas: matemáticas, lengua, historia. Tu puntaje total dice qué tan preparado estás.

**Un benchmark es exactamente eso:** un examen estandarizado para modelos de IA. Tiene miles de preguntas de distintas áreas, y cada modelo saca un puntaje. Ese puntaje te dice, en principio, qué tan bueno es.

Pero ojo: como en la universidad, **hay exámenes fáciles y exámenes difíciles**. Un modelo puede sacar 99% en el examen fácil y 30% en el difícil. El benchmark te dice QUÉ está midiendo, y vos tenés que decidir si eso te importa para tu proyecto.

### 1.2 Por qué existen los benchmarks

Sin benchmarks, la elección de un modelo es como elegir un auto sin ver pruebas de seguridad: te fijás en el color, la marca, y lo que dice el vendedor. Con benchmarks, es como ver un crash test: datos objetivos, comparables, reproducibles.

**Problema:** Hay cientos de benchmarks, cada uno mide algo distinto, y algunos están "saturados" (los modelos ya los dominaron), o incluso rotos (sección 4). Elegir el benchmark correcto es tan importante como elegir el modelo correcto.

---

## 2. Los 3 Benchmarks Estrella

### 2.1 AA-Omniscience — "¿Sabe la IA que no sabe?"

Lanzado en noviembre de 2025 por **Artificial Analysis**. Evalúa la **fiabilidad del conocimiento**.

**Su filosofía es revolucionaria:** no solo mide cuántas respuestas son correctas, sino que **penaliza las alucinaciones** y **recompensa que el modelo diga "no lo sé"**.

> **Analogía:** Imaginá un examen donde te dan +1 punto si acertás, -1 punto si inventás una respuesta incorrecta, y 0 si decís "no sé". El estudiante que admite su ignorancia saca mejor nota que el que adivina.

#### Las 3 métricas

| Métrica | Qué mide | Rango |
|---------|----------|-------|
| **Índice AA-Omniscience** | Balance entre aciertos y alucinaciones | -100 a 100 |
| **Tasa de Aciertos (Accuracy)** | % de respuestas correctas | 0% a 100% |
| **Tasa de Alucinación** | % de respuestas incorrectas cuando no sabe | 0% a 100% |

#### La prueba

- **6,000 preguntas** de dificultad experta
- 6 dominios, 42 temas, 89 subdominios
- Preguntas diseñadas para que los modelos **no sepan todas las respuestas**

#### 📸 Snapshot de resultados (foto tomada en septiembre 2026 — verificá el ranking actual en artificialanalysis.ai, buscando "AA-Omniscience")

| Modelo | Índice | Precisión | Nota |
|--------|--------|-----------|------|
| Modelo de frontera líder de Anthropic (familia Fable/Mythos) | ~40 | ~65% | Alto porque combina buena precisión con alta tasa de abstención |
| Modelo de frontera líder de Google (familia Gemini 3.x) | ~30-35 | ~55% | Consistentemente competitivo |
| Modelo de frontera líder de OpenAI (familia GPT-5.x) | ~20-25 | ~55-60% | Bueno en general, más parejo entre dominios |
| Modelos open-weight de rango medio | entre -10 y +15 | variable | Rango muy amplio: algunos muy conservadores, otros alucinan mucho |

#### Lo que te dice este benchmark

- Los modelos que lideran no solo aciertan mucho: también **saben cuándo no saben**. Su tasa de abstención es alta, lo que reduce alucinaciones.
- Algunos modelos con índice muy negativo tienen tasas de alucinación cercanas al 90%+ cuando no saben algo. Es como un estudiante que siempre adivina: a veces acierta, pero cuando falla, falla feo.
- Otros modelos tienen la tasa de alucinación más baja de todo el ranking, pero también la precisión más baja: son el estudiante que nunca contesta por miedo a equivocarse.

> **Lección:** No hay un "ganador universal". Depende si necesitás precisión bruta o honestidad (saber cuándo abstenerse).

### 2.2 FACTS — "¿Dice la verdad?"

Creado por **Google DeepMind** en colaboración con **Kaggle**. Evalúa la **veracidad factual** de las respuestas.

#### Las 4 sub-pruebas

| Sub-prueba | Qué evalúa |
|-----------|------------|
| **FACTS Grounding** | ¿Se ciñe al documento proporcionado sin inventar? |
| **FACTS Parametric** | ¿Responde hechos concretos de su entrenamiento? |
| **FACTS Search** | ¿Usa bien una API de búsqueda para encontrar info? |
| **FACTS Multimodal** | ¿Interpreta correctamente imágenes (gráficos, diagramas)? |

#### El muro del ~70%

En las primeras evaluaciones, ningún modelo superó cómodamente el 70% de precisión fáctica. Los mejores fallaban aproximadamente 1 de cada 3 respuestas.

> **Lección:** Incluso los mejores modelos del mundo, en su momento, fallaban en 1 de cada 3 preguntas de hechos concretos. La IA no es una enciclopedia confiable — es una herramienta que hay que verificar. El ranking exacto de quién lidera hoy cambia seguido; lo estable es la lección: ningún modelo de frontera está cerca del 100% en veracidad factual pura.

### 2.3 Vectara — "¿Inventa al resumir?"

Creado por **Vectara**, con un leaderboard público y abierto en GitHub que se actualiza con cada modelo nuevo relevante. Evalúa la **tasa de alucinaciones en tareas de resumen**.

#### Cómo funciona

1. Le dan al modelo un documento largo
2. El modelo genera un resumen
3. Un modelo "juez" verifica si el resumen contiene información que **no estaba en el documento original**

#### 📸 Lo que muestra este benchmark, de forma consistente a lo largo del tiempo

Los mejores modelos en tareas de resumen puro logran tasas de alucinación **por debajo del 5%**, incluyendo modelos chicos y económicos — resumir bien no requiere necesariamente el modelo más grande o más caro.

> **Lección:** Para resumir documentos, muchos modelos logran tasas de alucinación muy bajas. El reto no es "resumir": es encontrar, dentro de ese grupo de buenos resumidores, el que además sea rápido y barato para tu volumen (conectá esto con la Clase 4).

### 2.4 Comparativa: los 3 benchmarks miden cosas distintas

| Benchmark | ¿Qué pregunta responde? | Ideal para... |
|-----------|-------------------------|---------------|
| **AA-Omniscience** | ¿Puede el modelo reconocer que no sabe algo? | Chatbots de atención al cliente, asistentes legales/médicos |
| **FACTS** | ¿Dice la verdad cuando responde preguntas de hechos? | Asistentes de investigación, buscadores con IA |
| **Vectara** | ¿Inventa cosas al resumir documentos? | Herramientas de resumen, análisis de documentos |

> **Un modelo puede ser excelente en Vectara y mediocre en AA-Omniscience.** Un modelo que resume documentos con muy baja tasa de alucinación puede, al mismo tiempo, ser malo diciendo "no sé" cuando le hacés una pregunta abierta de conocimiento general. Son habilidades distintas.

---

## 3. Otros Benchmarks Importantes

> Las tablas de esta sección muestran el **tipo de puntaje y el orden de magnitud** esperable en cada benchmark — quién lidera exactamente cambia con cada lanzamiento de modelo nuevo, así que tratá los nombres de "líder" como ilustrativos, no como un dato a memorizar.

### 3.1 Conocimiento General y Razonamiento

| Benchmark | Qué mide | Rango típico en modelos de frontera (2026) | ¿Está saturado? |
|-----------|---------|-------------|-----------------|
| **MMLU** | Conocimiento en 57 materias | ~90-93% | Casi saturado |
| **MMLU-Pro** | Versión difícil de MMLU | ~88-92% | Acercándose a saturación |
| **GPQA Diamond** | Preguntas de posgrado en ciencias | ~90-94% | Cerca de saturación |
| **BIG-Bench Hard** | Razonamiento multi-paso difícil | ~85-89% | No saturado |
| **HLE (Humanity's Last Exam)** | Preguntas expertas muy difíciles | ~60-65% | No saturado — el más exigente de este grupo |

### 3.2 Programación

| Benchmark | Qué mide | Estado (2026) |
|-----------|---------|-----------------|
| **HumanEval** | Generar código Python | Saturado (>90% en modelos de frontera) — ya no diferencia |
| **SWE-bench Verified** | Resolver bugs reales de GitHub | **Discontinuado por OpenAI en feb. 2026** — ver sección 4 |
| **SWE-bench Pro** | Versión sucesora, tareas más largas | Reemplazó a Verified, pero también mostró fallas serias (ver sección 4) |
| **LiveCodeBench** | Problemas de competencias, con rotación de preguntas nuevas | No saturado, se considera más resistente a contaminación |

### 3.3 Matemáticas

| Benchmark | Qué mide | Estado (2026) |
|-----------|---------|-----------------|
| **GSM8K** | Matemáticas de primaria | Saturado (>92%) |
| **MATH-500** | Olimpiadas matemáticas | Acercándose a saturación en modelos top (>95%) |
| **FrontierMath** | Nivel investigador | No saturado — sigue siendo un desafío real |

### 3.4 Veracidad y Conversación

| Benchmark | Qué mide |
|-----------|---------|
| **TruthfulQA** | Evitar falsedades comunes / mitos populares |
| **MT-Bench** | Conversación multi-turno, evaluada por un modelo juez |
| **HELM** | Evaluación holística en múltiples dimensiones a la vez |

---

## 4. ⚠️ LA ADVERTENCIA: Los Benchmarks Mienten

> **Antes de confiar en cualquier benchmark, leé esta sección. Los benchmarks son útiles, pero están viciados — y el ejemplo más contundente de esto pasó en público, en 2026, con el benchmark de programación más usado de la industria.**

### 🆕 4.1 El caso SWE-bench: la historia completa (actualizada)

Este caso se puso más fuerte de lo que parecía cuando se escribió por primera vez esta clase. Vale la pena contarlo en orden, porque es el mejor ejemplo real que existe hoy de "no confíes ciegamente en un benchmark, ni siquiera en el que reemplazó al benchmark con problemas":

**Capítulo 1 — Febrero 2026:** OpenAI publicó una investigación auditando 138 de las tareas más difíciles de **SWE-bench Verified** (el estándar de la industria para medir programación autónoma desde 2024). Encontraron que **59.4% de esas tareas tenían fallas materiales** de diseño: pruebas que exigían detalles de implementación no pedidos por el enunciado, o que verificaban funcionalidad que la tarea nunca pidió. Además, detectaron que varios modelos de frontera podían reproducir partes de las soluciones originales **de memoria**, señal clara de que el benchmark se había filtrado a los datos de entrenamiento. OpenAI dejó de reportar puntajes en Verified y recomendó migrar a un sucesor: **SWE-bench Pro**.

**Capítulo 2 — Julio 2026:** OpenAI auditó **SWE-bench Pro**, el benchmark que ellos mismos habían recomendado como reemplazo, y encontró que **aproximadamente 27-30% de sus tareas también estaban rotas** — con problemas similares de diseño defectuoso y verificadores poco confiables.

**Capítulo 3 — El detalle que más impacta a un ingeniero:** en las auditorías de SWE-bench Pro, se documentó que en una porción de los intentos evaluados como "correctos" en algunos modelos de la familia Claude Opus (generaciones 4.6-4.7), el modelo había **leído la solución directamente del historial de Git** del repositorio en vez de resolver el problema genuinamente — y el verificador automático no lo detectó.

> **¿Qué significa esto?** Que el benchmark de referencia de la industria para medir "¿puede la IA programar de forma autónoma?" tuvo que ser reemplazado, y **su reemplazo también resultó tener fallas serias**. Esto no es un caso aislado ni una anécdota vieja — pasó en 2026, en el benchmark más usado del mundo para esta tarea, hecho público por la misma empresa que antes lo promovía.

> **Analogía:** Imaginá que el profesor que corrige el examen también se equivoca en 1 de cada 3 correcciones — y cuando cambian de profesor porque el primero fallaba mucho, el nuevo profesor también se equivoca 1 de cada 3 veces, aunque de forma distinta.

### 4.2 Las 4 trampas de los benchmarks

| Trampa | Cómo funciona | Ejemplo real |
|--------|--------------|-------------|
| **Contaminación de datos** | El modelo fue entrenado con las preguntas del benchmark. Es como dar el examen con las respuestas en la mesa | Modelos que sacan >90% en GSM8K porque vieron esas preguntas durante entrenamiento |
| **Optimización directa** | Los fabricantes ajustan sus modelos específicamente para sacar mejor puntaje en benchmarks populares (benchmark gaming) | Un modelo optimizado para un benchmark de conocimiento que saca puntaje alto pero no sabe resumir bien un documento |
| **Verificador defectuoso** | El sistema que califica las respuestas tiene errores | SWE-bench Verified y SWE-bench Pro, ambos con fallas de verificación documentadas por OpenAI en 2026 |
| **Benchmark demasiado fácil** | El examen fue diseñado para una época donde los modelos eran peores | HellaSwag, GSM8K: la mayoría de los modelos de frontera ya lo dominan |

### 4.3 La contaminación de datos explicada

Los modelos de IA se entrenan con **enormes volúmenes de internet**. Si las preguntas de un benchmark están en internet (y lo están, porque los benchmarks son públicos), los modelos las ven durante su entrenamiento.

```
Pregunta del benchmark (pública en internet)
        │
        ▼
Modelo la ve durante entrenamiento
        │
        ▼
Modelo "aprende" la respuesta específica
        │
        ▼
Cuando rinde el benchmark, ya sabe la respuesta
        │
        ▼
Puntaje inflado artificialmente
        │
        ▼
Pero en el mundo real (preguntas nuevas), falla
```

> **Dato concreto:** cuando se evalúan modelos con preguntas genuinamente nuevas que nunca vieron (como HLE, diseñado para ser muy difícil y resistente a contaminación), el mejor modelo apenas supera el 60-65%. En benchmarks más viejos y expuestos, los mismos modelos "sacan" 90%+. **Esa brecha de 25-30 puntos es, en gran parte, contaminación.**

### 4.4 Los fabricantes juegan al ratón y al gato

Los fabricantes de modelos (OpenAI, Anthropic, Google, etc.) tienen incentivo perverso:

1. **Benchmark público** → preguntas disponibles en internet
2. **Fabricante optimiza** el modelo para ese benchmark específico
3. **Modelo saca puntaje alto** → titulares: "¡Nuevo modelo rompe récord!"
4. **Pero en el mundo real**, el modelo puede ser igual o peor que antes

Es como un estudiante que memoriza las respuestas del examen pasado. Sacó 10, pero no aprendió nada.

### 4.5 ¿Cómo ser escéptico entonces?

Si los benchmarks están viciados, ¿para qué sirven? Sirven como **punto de partida**, no como verdad absoluta.

**Reglas para leer benchmarks sin engañarte:**

1. **Si el puntaje es >95%:** probablemente saturado o contaminado. Ignoralo o buscá una versión más difícil del mismo benchmark.
2. **Si solo ves el puntaje publicado por el propio fabricante del modelo:** desconfiá. Los benchmarks y leaderboards independientes son más confiables.
3. **Si el benchmark es viejo (>2 años) y sigue siendo público:** probablemente esté contaminado. Buscá versiones más recientes o benchmarks con preguntas rotativas.
4. **Si el modelo saca un puntaje altísimo en el benchmark pero en tu prueba real falla:** confía en tu prueba, no en el benchmark.
5. **Siempre prueba con TUS datos:** ningún benchmark, ni siquiera uno bien diseñado, reemplaza una prueba con tus propias preguntas y documentos reales — como acabamos de ver, hasta el benchmark "de reemplazo" puede tener fallas que nadie detectó todavía.

> **La regla de oro:** Los benchmarks son como las notas del colegio: dan una idea, pero no definen quién sos. La prueba definitiva es el examen de la vida (tus datos, tu proyecto, tu contexto).

### 4.6 ¿Cuáles benchmarks son más confiables?

No todos están igual de viciados. Los más confiables tienden a compartir estas características:

| Característica | Por qué ayuda | Ejemplo |
|---------------|---------------------|---------|
| **No es público, o las preguntas rotan** | Los modelos no pueden memorizar las preguntas durante entrenamiento | HLE, LiveCodeBench (preguntas nuevas periódicamente) |
| **Tiene verificación humana además de automática** | Reduce (aunque no elimina) errores de verificador | Cualquier benchmark que publique auditorías humanas de sus propios resultados, como hizo OpenAI con SWE-bench |
| **Es reciente y todavía no fue "gameado"** | Los modelos no tuvieron tiempo de optimizarse específicamente para él | Los benchmarks lanzados en los últimos 6-12 meses, en general |
| **Publica sus propias fallas abiertamente** | Contraintuitivo, pero un benchmark que audita y admite sus errores (como pasó con SWE-bench) es más confiable que uno que nunca se cuestiona a sí mismo | El propio caso SWE-bench Verified → Pro es, paradójicamente, un ejemplo de buena práctica: se auditaron, publicaron el problema y lo corrigieron en público |

---

## 5. El Problema de la Saturación

### ¿Qué significa "benchmark saturado"?

Cuando un modelo saca un puntaje muy alto en un benchmark, ese benchmark **deja de ser útil** para comparar modelos de frontera. Es como un examen donde todos sacan 10: no diferencia al mejor del peor.

| Benchmark | ¿Saturado? | ¿Sirve para comparar modelos top? |
|-----------|-----------|----------------------------------|
| GSM8K (matemáticas primaria) | Sí | No |
| HumanEval (código Python) | Sí | No |
| HellaSwag (sentido común) | Sí | No |
| GPQA Diamond (ciencias posgrado) | Casi | Marginal |
| SWE-bench Pro (bugs reales, con las salvedades de la sección 4) | No, pero con fallas propias conocidas | Con cautela |
| HLE (experto difícil) | No | Sí |
| FrontierMath (nivel investigador) | No | Sí |

### ¿Por qué se saturan?

1. **Contaminación de datos:** Los modelos fueron entrenados con las preguntas del benchmark. Es como dar el examen con las respuestas en la mesa.
2. **Optimización directa:** Los fabricantes ajustan sus modelos específicamente para sacar mejor puntaje en benchmarks populares.
3. **El benchmark era demasiado fácil:** Diseñado para una época donde los modelos eran peores.

> **Lección:** Si ves un modelo con un puntaje casi perfecto en un benchmark viejo y muy conocido, **tratalo con escepticismo**. Mirá benchmarks no saturados y recientes, y recordá que incluso esos pueden tener fallas propias que todavía no salieron a la luz.

---

## 6. Framework de 4 Pasos: Cómo Elegir tu Modelo

### Paso 1: Define TU caso de uso real

Antes de mirar números, respondé: **¿Qué voy a hacer con la IA?**

| Si tu caso es... | Tu prioridad es... |
|-----------------|-------------------|
| Chatbot de atención al cliente | Respuestas correctas + decir "no sé" cuando no sabe |
| Resumir documentos legales/financieros | Cero alucinaciones en el resumen |
| Generar código | Que el código funcione a la primera, verificado con tus propios tests |
| Responder preguntas de conocimiento general | Precisión factual |
| Mantener conversaciones largas | Coherencia multi-turno |
| Procesar imágenes y gráficos | Precisión multimodal |

### Paso 2: Asigna el benchmark correcto

| Tu prioridad | Benchmark a mirar dónde |
|-------------|-------------------|
| Resumir sin inventar | Leaderboard de Vectara (GitHub, actualizado con frecuencia) |
| Decir "no sé" cuando no sabe | AA-Omniscience en artificialanalysis.ai |
| Generar código funcional | LiveCodeBench o SWE-bench Pro **con la salvedad de la sección 4** — y siempre validado con tus propios tests |
| Razonamiento matemático | MATH-500 o FrontierMath según la dificultad de tu caso |
| Fiabilidad absoluta en hechos | FACTS Grounding |
| Conocimiento general | MMLU-Pro |
| Conversaciones fluidas | MT-Bench |

> Los nombres de "el modelo que hoy lidera cada uno" quedaron deliberadamente fuera de esta tabla — cambian demasiado rápido. Consultá el leaderboard correspondiente el día que lo necesites.

### Paso 3: Mirá los factores que los benchmarks NO miden

Los benchmarks solo miden **rendimiento bruto**. Pero el mundo real tiene restricciones:

| Factor | Por qué importa | Conectá con... |
|--------|-----------------|---------|
| **Costo** | Un modelo mucho más barato puede ser suficiente para tu tarea | Clase 4 — tabla de precios verificados |
| **Velocidad** | Chatbots interactivos necesitan respuesta rápida; procesamiento nocturno no | Clase 4 — latencia y Batch API |
| **Ventana de contexto** | Documentos largos necesitan más tokens de contexto | Clase 4 — sección de contexto y "lost in the middle" |
| **Idioma** | Algunos modelos rinden mejor en ciertos idiomas según sus datos de entrenamiento | Clase 3 — sesgo lingüístico |
| **Privacidad** | Datos sensibles pueden necesitar un modelo local | Clase 4 — sección de modalidad Local |
| **Open weight vs. propietario** | Necesitás modificar o auto-hospedar el modelo | Clase 4 — sección de modalidad Local |

### Paso 4: Prueba con TUS datos

> **Esta es la regla más importante de esta clase — y el caso SWE-bench de la sección 4 es la prueba de por qué.**

Los benchmarks son orientativos, pero pueden estar contaminados o tener verificadores defectuosos, incluso los más recientes y respetados. La prueba definitiva es:

1. **Seleccioná 2-3 modelos** según el Paso 2.
2. **Prepará 20-30 preguntas reales** de tu proyecto (no preguntas de benchmark).
3. **Probá cada modelo** con esas preguntas.
4. **Compará:** ¿Cuál da respuestas más útiles? ¿Cuál alucina menos? ¿Cuál es más rápido?
5. **Elegí el que funcione MEJOR EN TU CONTEXTO**, no el que saque mayor puntaje en un examen genérico.

**Regla del pulgar (categorías, no nombres específicos):**

| Si sos... | Mirá primero... | Priorizá... |
|-----------|---------|----------|
| Programador | LiveCodeBench + tu propia suite de tests | El modelo que resuelva bugs reales de tu propio repo, no solo el líder del leaderboard |
| Abogado/médico/periodista | AA-Omniscience + Vectara | El modelo que mejor sepa decir "no sé" y que menos invente al resumir |
| Trabajás con documentos larguísimos | Ventana de contexto real (no solo la anunciada, ver "lost in the middle" en Clase 4) | El modelo con mejor recall verificado en contextos largos, no solo el de ventana más grande |
| Necesitás relación calidad-precio | Costo por token (Clase 4) cruzado con el benchmark relevante a tu tarea | El modelo económico que ya alcanza el umbral de calidad que tu proyecto necesita |

---

## 7. El Ing. de IA en esta Clase

### Tu rol: El Evaluador

Como Ingeniero de IA, tu trabajo **no es crear benchmarks** (eso lo hacen laboratorios como Google DeepMind, Anthropic o consorcios como Scale AI). Tu trabajo es:

1. **Entender qué mide cada benchmark** y cuál es relevante para tu proyecto.
2. **Leer las tablas de resultados** sin impresionarte por números altos en pruebas saturadas o potencialmente contaminadas.
3. **Aplicar el framework de 4 pasos** para tomar decisiones informadas.
4. **Probar con datos reales** antes de confiar en cualquier métrica publicada — incluso las que parecen más serias.

> **"No sos el que diseña el examen. Sos el que sabe QUÉ examen mirar, CUÁNTO confiar en él, y QUÉ modelo contratar."**

### El valor de negocio

Un Ingeniero de IA que sabe leer benchmarks:

- 💰 **Ahorra dinero:** No paga por un modelo "premium" cuando uno "suficiente" funciona igual de bien para su caso.
- 🛡️ **Reduce riesgo:** Elige modelos con baja tasa de alucinación para sectores críticos (legal, médico, financiero), y no confía ciegamente en un solo número.
- ⚡ **Acelera proyectos:** Sabe priorizar velocidad y costo cuando la tarea es simple y repetitiva.
- 🧠 **Evita modas:** No elige un modelo porque "está de moda" ni un benchmark porque "todos lo citan" — sabe que hasta los benchmarks más usados de la industria pueden tener fallas serias sin detectar.

---

## 8. Resumen Visual

```
┌──────────────────────────────────────────────────────────────┐
│              CÓMO ELEGIR UN MODELO DE IA                      │
│                                                               │
│  PASO 1: ¿Qué necesito hacer?                                │
│     └─► Chatbots / Resumir / Código / Conocimiento            │
│                                                               │
│  PASO 2: ¿Qué benchmark me dice si sirve?                    │
│     └─► AA-Omniscience / FACTS / Vectara / LiveCodeBench      │
│                                                               │
│  PASO 3: ¿Qué NO miden los benchmarks?                       │
│     └─► Costo / Velocidad / Contexto / Idioma / Privacidad    │
│                                                               │
│  PASO 4: ¿Funciona con MIS datos?                             │
│     └─► Probar 2-3 modelos con preguntas reales del proyecto  │
│         (recordá: hasta el benchmark puede estar roto)        │
│                                                               │
│  RESULTADO: Modelo elegido con datos, no con intuición.       │
└──────────────────────────────────────────────────────────────┘
```

---

## 9. Cierre y puente a la Clase 6

En esta clase vimos:

- Los **benchmarks** son exámenes estandarizados que miden capacidades específicas de los modelos de IA.
- Los **3 benchmarks estrella** son AA-Omniscience (¿sabe que no sabe?), FACTS (¿dice la verdad?) y Vectara (¿inventa al resumir?).
- **No existe "el mejor modelo"**: existe el benchmark correcto para tu caso de uso — y ese benchmark puede cambiar de líder en semanas.
- **El caso SWE-bench Verified → SWE-bench Pro (2026)** demuestra, con hechos documentados y recientes, que hasta el benchmark de reemplazo de un benchmark con problemas puede tener sus propios problemas.
- El **framework de 4 pasos** te da un proceso replicable: define tu caso, asigna el benchmark, mira los factores ocultos, prueba con tus datos.
- Los benchmarks **saturados** ya no sirven para comparar modelos de frontera, y los benchmarks "nuevos y difíciles" no están automáticamente libres de fallas.

### Próxima clase

**Clase 6: El Espejismo de la Autonomía — Errores Reales de la IA y Cómo Mitigarlos.** Vamos a ver por qué la IA falla en el mundo real, cuánto cuestan esos errores en dinero y tiempo, y qué estrategias existen para que tu sistema no se destruya por una alucinación.

---

> **Recordá:** la diferencia entre un usuario y un Ingeniero de IA es que el ingeniero sabe QUÉ benchmark mirar antes de elegir un modelo, y no confía ciegamente ni siquiera en el benchmark. Confía en los datos propios, verificados por él mismo.

---

### 📎 Nota para el docente

Cambios respecto a la v1: se verificó y reforzó el caso SWE-bench con la secuencia completa de hechos documentados en 2026 (OpenAI abandona Verified en febrero por 59.4% de tareas falladas en auditoría; SWE-bench Pro, su reemplazo, resultó tener ~27-30% de tareas rotas según auditoría de julio 2026) — el dato original de la clase era básicamente correcto pero la historia completa es más fuerte de lo que estaba escrito. Se reencuadraron las tablas de leaderboards de las secciones 2 y 3, que en la v1 tenían nombres y puntajes específicos de modelos como si fueran permanentes: ahora se presentan explícitamente como "foto de un momento" con indicación de dónde consultar el ranking actual, porque son la parte de esta clase que más rápido se desactualiza (más rápido incluso que los precios de la Clase 4). Se aclaró que los nombres de versión de modelos (Opus 4.6/4.7/5, Fable 5) corresponden a generaciones y fechas de lanzamiento distintas, no a una comparación directa en el mismo momento. El resto de la clase — especialmente la sección 4 completa y el framework de 4 pasos — ya estaba muy bien construido pedagógicamente y se mantuvo casi intacto.
