# Clase 4 — La Economía de la IA: Tokens, Costos y Modalidades
### (Versión revisada y actualizada — septiembre 2026)

> Material de apoyo para el estudiante. Leelo directo en GitHub o en la vista web.
> **Nota sobre los precios de esta clase:** todos los precios fueron verificados contra las páginas oficiales de cada proveedor el 11 de septiembre de 2026. Los precios de IA cambian con mucha frecuencia (a veces mensualmente) — antes de usar estos números para un presupuesto real, revisá la fuente oficial linkeada en cada tabla.

---

## Filosofía de la clase

> **Un Ingeniero de IA no solo sabe pedirle cosas a ChatGPT. Sabe cuánto cuesta cada letra que escribe la IA, por qué un modelo es más caro que otro, y cómo elegir la forma correcta de conectarse para que el proyecto sea viable financieramente.**

En la Clase 3 vimos los riesgos de la IA. Hoy ponemos los pies sobre la tierra: **la IA no es gratis**. Cada palabra que genera tiene un costo real, en dólares, en electricidad, en hardware.

Si te llevás una sola cosa de esta clase, que sea esta:

> **La diferencia entre un usuario y un Ingeniero de IA es que el ingeniero sabe cuánto cuesta cada token antes de enviar el prompt.**

**Esta clase es la base para las Clases 5 y 6:** sin entender tokens y costos, no podés elegir un modelo (Clase 5) ni calcular cuánto cuesta mitigar sus errores (Clase 6).

---

## 1. Tokens: La Moneda de la IA

### 1.1 ¿Qué es un Token?

Un token es la **unidad mínima** por la que te cobra una API de IA. No es una palabra, no es una letra: es un trozo de texto que la IA "muerde" con su tokenizador.

| Unidad | Ejemplo | ¿Cuántos tokens? |
|--------|---------|-------------------|
| Una palabra corta | `gato` | 2 token |
| Una palabra larga | `hipopótamo` | ~3 tokens |
| Una palabra en inglés | `cat` | 1 token |
| Una palabra en español larga | `programación` | ~3 tokens |

> **Regla de oro:** 1 token ≈ 4 caracteres en inglés ≈ 0.75 de una palabra en español.

> **Detalle técnico que suma en un curso de ingeniería:** cada proveedor usa su propio tokenizador (OpenAI usa una familia llamada *tiktoken*, por ejemplo). Esto significa que el **mismo texto puede costar una cantidad distinta de tokens según el modelo** al que se lo mandes — no asumas que "1000 caracteres" es una unidad universal entre proveedores. Si necesitás precisión, cada proveedor publica una herramienta o librería para contar tokens exactos antes de enviar el prompt.

### 1.2 Input vs. Output

| | Tokens de Entrada (Input) | Tokens de Salida (Output) |
|---|---|---|
| **¿Qué son?** | Lo que vos escribís a la IA | Lo que la IA responde |
| **Costo relativo hoy** | 1x (barato) | típicamente 3x a 8x más caro, según el modelo |
| **¿Por qué?** | Leer es más barato computacionalmente | Generar texto token por token cuesta más cómputo |

**Lección:** Si tu chatbot recibe consultas cortas pero responde textos largos, el costo principal está en el output.

### 1.3 La Ventana de Contexto

> La **ventana de contexto** es la cantidad máxima de tokens que el modelo puede "tener en cuenta" en una conversación o documento de una sola vez.

| Ventana | Capacidad aproximada | Modelos de referencia (sept. 2026) |
|---------|-----------|-------------------|
| 128K | ~98,000 palabras (~350 páginas) | GPT-4o (generación anterior) |
| 200K-400K | ~150,000-300,000 palabras | Claude Sonnet 4.5 (estándar), GPT-5.1 |
| 1M | ~750,000 palabras (~2,500 páginas) | Gemini 3 Pro, Claude Sonnet 4.5 (contexto extendido) |

**Peligro (sigue vigente):** Llenar la ventana de contexto tiene un costo directo. Si mandás 33,000 tokens de contexto en cada consulta, pagás esos tokens **cada vez que el usuario pregunta**.

> **🆕 El límite que no está en ningún pricing page: "lost in the middle".** Que un modelo *acepte* 1 millón de tokens no significa que los *use* todos igual de bien. Varios estudios de evaluación documentaron que la información ubicada en el medio de un contexto muy largo es recuperada con menos precisión que la que está al principio o al final del prompt. Para un ingeniero esto tiene una consecuencia práctica: **no confíes ciegamente en meter todo el documento en el contexto solo porque "entra"** — para información crítica, seguí prefiriendo poner lo importante cerca del principio o del final, o usar RAG (sección 4.2) para no depender de la memoria completa del modelo.

---

## 2. Parámetros: El "Peso" del Cerebro

### 2.1 ¿Qué significan los parámetros?

Cuando lees que un modelo tiene "X parámetros", eso es la cantidad de **números** que se ajustaron durante el entrenamiento.

| Modelo | Parámetros | Analogía |
|--------|-----------|----------|
| Perceptrón (Clase 1) | 3 | Un portero que decide "abrir o no" |
| Llama 3 8B | 8 mil millones | Una biblioteca municipal |
| GPT-4 | ~1.8 billones (estimación **no oficial**, nunca confirmada por OpenAI) | La Biblioteca del Congreso de EE.UU. |

> **Nota de ingeniería importante:** desde 2023-2024 ningún proveedor de punta (OpenAI, Anthropic, Google) publica oficialmente el conteo de parámetros de sus modelos de frontera. Además, los modelos actuales suelen usar arquitecturas **Mixture-of-Experts (MoE)**, donde el modelo tiene muchísimos parámetros totales pero solo "activa" una fracción de ellos en cada consulta — lo cual hace que "cantidad de parámetros" ya no sea, por sí sola, un buen predictor de costo o velocidad como lo era en 2020-2022. Tratá cualquier cifra de parámetros de un modelo propietario reciente como una estimación de terceros, no como un dato de catálogo confiable.

### 2.2 La relación: Capacidad = Costo (con matices)

| Modelo más grande / de razonamiento | Modelo más chico / rápido |
|----------------|------------------|
| ✅ Mejor en tareas complejas y de razonamiento largo | ✅ Más rápido y barato |
| ❌ Más caro y con más latencia | ❌ Pierde matices en tareas ambiguas |

> **Regla práctica (sigue siendo el consejo más valioso de la clase):** Para gran parte de las tareas de un producto real, un modelo pequeño o económico hace un trabajo perfectamente aceptable. Y como vas a ver en la sección 4, hoy la diferencia de precio entre el modelo más caro y el más barato competente puede ser de **50x a 100x**.

**Ejemplo de ahorro:**

| Tarea | Tipo de modelo recomendado | ¿Por qué? |
|-------|-------------------|-----------|
| Clasificar spam / intención de un mensaje | Modelo económico (mini/flash/lite) | Tarea simple y bien acotada |
| Analizar un contrato de 50 páginas con matices legales | Modelo de razonamiento (flagship) | Requiere seguir lógica compleja y no perder detalles |
| Chatbot de "¿cuál es mi saldo?" | Modelo económico | La gran mayoría de consultas son repetitivas y estructuradas |

---

## 3. Las 3 Modalidades: ¿Cómo te conectás a la IA?

### 3.1 Chat (Minorista)

Vas a una interfaz web o app, escribís, la IA responde. Los planes individuales de los proveedores principales rondan entre $20 y $200+ USD/mes según el nivel (los planes más caros suelen dar acceso a modelos de razonamiento más potentes y mayor uso).

| Para qué sirve | Para qué NO sirve |
|---------------|-------------------|
| Uso personal, aprendizaje | Producción profesional |
| Probar prompts | Automatización a gran escala |

### 3.2 API (Mayorista)

Tu programa se conecta directamente al modelo. Pagás por cada token (pay-as-you-go).

| Ventaja | Explicación |
|---------|-------------|
| Escala | 1 consulta o 1 millón |
| Automatización | Tu programa decide cuándo llamar a la IA |
| Control | Vos elegís modelo, parámetros, temperatura |

> **La API es la ÚNICA forma profesional de construir productos con IA.** Nunca dependas de una sesión de chat abierta en un navegador.

### 3.3 Local (Soberanía)

Corrés el modelo en tu computadora, sin internet. Usando herramientas como **Ollama** o **LM Studio**, típicamente con modelos abiertos como Llama, Qwen o DeepSeek en sus versiones "destiladas" más chicas.

| Ventaja | Costo oculto |
|---------|-------------|
| Privacidad total | Necesitás GPU con suficiente VRAM |
| Sin costos por token | Electricidad + mantenimiento |
| Sin dependencia de un proveedor externo | Modelo generalmente más lento y con menor calidad que el flagship en la nube |

**¿Cuánta VRAM necesito?**

| Modelo | VRAM aproximada | Depende fuertemente de: |
|--------|---------------|--------------------------|
| Modelo abierto ~8B parámetros | ~6-8 GB (cuantizado a 4-8 bit) | Nivel de cuantización |
| Modelo abierto ~70B parámetros | ~35-45 GB (cuantizado) | Nivel de cuantización |
| Modelo propietario vía API | No aplica (corre en la nube del proveedor) | — |

> **🆕 El dato que faltaba: la cuantización cambia todo.** Un mismo modelo puede pesar la mitad o un cuarto de VRAM según la precisión con la que lo corras: FP16 (precisión completa) es el más pesado, 8-bit reduce el peso a la mitad, y 4-bit lo reduce a un cuarto — a cambio de una pequeña pérdida de calidad, generalmente aceptable para la mayoría de los usos. Antes de comprar una GPU "porque la tabla dice que necesito 40GB", fijate qué nivel de cuantización pensás usar: puede ser la diferencia entre necesitar una GPU de $300 o una de $3,000.

---

## 4. La Matemática de los Costos

### 4.1 Precios verificados hoy (11 de septiembre de 2026)

| Modelo | Input $/1M tokens | Output $/1M tokens | Contexto | Fuente oficial |
|--------|-------------------|---------------------|----------|-----------------|
| GPT-5.1 (OpenAI) | $1.25 | $10.00 | 400K | [platform.openai.com/pricing](https://platform.openai.com/docs/pricing) |
| GPT-4o (OpenAI, generación anterior) | $2.50 | $10.00 | 128K | [platform.openai.com/pricing](https://platform.openai.com/docs/pricing) |
| GPT-4o-mini (OpenAI) | $0.15 | $0.60 | 128K | [platform.openai.com/pricing](https://platform.openai.com/docs/pricing) |
| Claude Sonnet 4.5 (Anthropic) | $3.00 | $15.00 | 200K (1M en beta) | [platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing) |
| Gemini 3 Pro (Google) | $2.00 | $12.00 | 1M | [ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| Gemini 3.1 Flash Lite (Google) | $0.25 | $1.50 | 1M | [ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| DeepSeek-V3.2 (DeepSeek, open weight) | $0.23-0.25 | $0.34-0.38 | 164K | [api-docs.deepseek.com/quick_start/pricing](https://api-docs.deepseek.com/quick_start/pricing) |
| DeepSeek V4 Flash (DeepSeek) | ~$0.09 | ~$0.18 | 1M | [api-docs.deepseek.com/quick_start/pricing](https://api-docs.deepseek.com/quick_start/pricing) |

> **Cómo leer esta tabla en clase:** la diferencia entre el modelo más caro (Claude Sonnet 4.5, $15/M output) y el más barato (DeepSeek V4 Flash, $0.18/M output) es de **~80x**. Ninguno es "el mejor" en abstracto — depende de la tarea: para razonamiento complejo y bajo riesgo de error, el precio premium se justifica; para clasificación simple a gran escala, no.

### 4.2 📊 La caída histórica del precio de la inteligencia

Este es, probablemente, el dato más importante de toda la clase para entender **por qué** la IA se volvió accesible tan rápido. Siguiendo el precio de input del modelo económico/masivo de referencia de cada año:

| Año | Modelo de referencia | Precio input, USD por millón de tokens |
|-----|----------------------|------------------------------------------|
| 2020 | GPT-3 Davinci (precio de lanzamiento) | $60.00 |
| 2022 | GPT-3 Davinci (tras el recorte de precios de OpenAI) | $20.00 |
| 2023 | GPT-3.5-turbo | $2.00 |
| 2024 | GPT-4o-mini | $0.15 |
| 2026 | DeepSeek V4 Flash | ~$0.09 |

**El precio del "tier económico" cayó aproximadamente 660 veces en 6 años.** Para dimensionarlo: es como si un pasaje de avión que costaba $600 hoy costara menos de $1.

> **La esencia para un ingeniero:** esta curva es la razón estructural por la que "elegir el modelo correcto para la tarea" (sección 2.2) es hoy una decisión mucho más rentable que en 2020-2022, cuando el único modelo disponible era también el más caro. La lección no es "los precios de esta tabla van a seguir siendo así" — es que **la brecha de precio entre "suficientemente bueno" y "el mejor posible" tiende a ampliarse con el tiempo**, y parte de tu trabajo como ingeniero es revisar esa brecha cada vez que arrancás un proyecto nuevo, porque cambia rápido.

### 4.3 Cómo leer una tabla de precios: ejemplo práctico

```
GPT-4o: Input $2.50 / 1M tokens | Output $10.00 / 1M tokens
```

**Ejemplo:** Resumir un libro de 200 páginas (~133,000 tokens input, ~3,333 tokens output):

| Modelo | Costo Input | Costo Output | **Total** |
|--------|-------------|--------------|-----------|
| GPT-4o | $0.33 | $0.033 | **$0.36 USD** |
| GPT-4o-mini | $0.02 | $0.002 | **$0.022 USD** |
| DeepSeek-V3.2 | $0.033 | $0.001 | **$0.034 USD** |

> **La diferencia entre el más caro y el más barato de esta tabla es ~16x.** ¿Vale la pena pagar 16x más para resumir un libro? Para la mayoría de los casos de uso, probablemente no — pero si ese resumen alimenta una decisión legal o médica, la respuesta puede cambiar. El costo nunca se evalúa solo: se evalúa contra el riesgo de un error.

### 4.4 El costo del contexto (el peligro real)

**Escenario:** Asistente legal que envía 3 contratos previos como contexto (45,000 tokens) en cada consulta, usando GPT-4o.

| Cálculo | Costo |
|---------|-------|
| Input por consulta: 45,000 × $2.50/1M | $0.1125 USD |
| × 1,000 consultas/día | $112.50 USD/día |
| × 30 días | **~$3,375 USD/mes** |

> **Solución 1 (ya estaba en la clase):** Usar RAG para enviar solo los documentos relevantes (2,000 tokens en vez de 45,000). El costo baja más de 20x.

> **🆕 Solución 2, la que hoy usa cualquier ingeniero antes que RAG cuando el contexto se repite: prompt caching.** Si tu contexto (por ejemplo, el mismo system prompt largo, o los mismos 3 contratos) es **idéntico entre llamadas consecutivas**, casi todos los proveedores hoy ofrecen un precio de "input cacheado" muchísimo más barato que el input normal — en el caso de GPT-5.1, por ejemplo, el input cacheado cuesta $0.125 por millón de tokens frente a $1.25 del input normal (10x más barato), y en Claude el descuento es similar. Para el escenario del asistente legal: si los 45,000 tokens de contexto no cambian entre consultas del mismo día, con caching el costo mensual puede bajar de ~$3,375 a una fracción de eso — sin tener que rediseñar el sistema con RAG. **RAG y prompt caching no son alternativas, se combinan:** RAG reduce cuánto contexto mandás; caching abarata lo que sí mandás repetido.

---

## 5. Costos Ocultos

### 5.1 Rate Limits

Las APIs no te dejan enviar infinitos pedidos. Si excedés el límite, tu app se cae o las llamadas fallan.

**Solución:** Retry con backoff exponencial + batch processing.

> **🆕 Lo que sorprende a quien recién empieza:** la mayoría de los proveedores asignan límites de tasa (rate limits) **por niveles ("tiers")** que suben automáticamente según cuánto gastaste acumulado en tu cuenta, no según lo que necesitás desde el día uno. Una cuenta nueva puede tener límites bastante bajos incluso si tu tarjeta de crédito soporta cualquier volumen — esto sorprende a equipos que arrancan un proyecto y descubren que no pueden escalar tan rápido como esperaban sin antes "subir de nivel" con uso gradual o pidiendo un aumento de límite directamente al proveedor.

### 5.2 Latencia

| Tipo de modelo | Latencia típica orientativa |
|--------|----------------|
| Modelo económico / rápido (mini, flash, lite) | ~0.5-1.5 segundos |
| Modelo flagship estándar | ~2-5 segundos |
| Modelo de razonamiento extendido ("thinking") | puede llegar a varios segundos o más, según cuánto "piense" |

**Para chatbots interactivos:** generalmente necesitás mantenerte por debajo de 2-3 segundos de latencia percibida. **Para procesamiento por lotes (batch) o nocturno:** la latencia deja de importar, y ahí conviene usar el Batch API (ver 5.3).

### 5.3 🆕 Batch API: la palanca de costo que falta en la mayoría de las clases

Casi todos los proveedores principales ofrecen un **Batch API**: le mandás un lote grande de solicitudes que no necesitan respuesta inmediata (por ejemplo, procesar 50,000 documentos durante la noche) y a cambio pagás **típicamente ~50% menos** que el precio estándar por token, con el trade-off de que la respuesta puede tardar minutos u horas en vez de segundos.

> **Conexión directa con 5.2:** si tu caso de uso es de los que "la latencia no importa" (procesamiento nocturno, análisis masivo, generación de reportes), **usar el Batch API no es opcional, es la decisión de ingeniería correcta por defecto** — es dinero que se deja sobre la mesa si no lo hacés.

### 5.4 Costo de Hardware Local

Una GPU de consumo con 12 GB de VRAM cuesta en el orden de $1000-4000 USD y puede correr modelos de hasta ~13B parámetros cuantizados. Para modelos de 70B+ parámetros, generalmente se necesita hardware de nivel servidor o múltiples GPUs, con costos que se multiplican por 10 o más.

---

## 6. El Ingeniero de IA en esta Clase

> El Ingeniero de IA es la persona que responde **"¿cuánto cuesta?"** antes de **"¿cómo se hace?"**

| Habilidad | Qué significa |
|-----------|--------------|
| Sabe contar tokens | Estima si conviene resumir antes de mandar, y sabe que el conteo varía por modelo |
| Elige la modalidad correcta | API para producción, local para privacidad |
| Optimiza costos | Modelo económico para tareas simples, caching para contexto repetido, batch para lo que no es urgente |
| Piensa en el costo total | No mira el costo por consulta, sino el mensual — y lo revisa cada pocos meses, porque los precios se mueven |

---

## 7. Conexión con las Próximas Clases

| Lo que aprendiste hoy | Cómo se conecta |
|----------------------|-----------------|
| Los tokens cuestan dinero, y el precio cae rápido con el tiempo | En la **Clase 5** verás que los benchmarks miden calidad, pero vos tenés que balancear calidad vs. costo vs. cuán rápido se desactualiza esa comparación |
| La API es la forma profesional | En la **Clase 5** elegirás qué modelo usar vía API según tu caso de uso |
| RAG y prompt caching reducen el costo del contexto | En la **Clase 6** verás que RAG también reduce alucinaciones de forma medible |
| Los costos ocultos (rate limits, batch, VRAM) pueden arruinar un proyecto | En la **Clase 6** verás que el "Impuesto de Verificación" es otro costo oculto más |

---

## 8. Resumen Visual

```
┌──────────────────────────────────────────────────────────────┐
│              ECONOMÍA DE LA IA EN 3 PASOS                     │
│                                                               │
│  PASO 1: ¿Qué son los tokens?                                │
│     └─► Unidades de texto que cuestan dinero                  │
│         Input = barato | Output = 3-8x más caro               │
│                                                               │
│  PASO 2: ¿Cuánto cuesta mi proyecto?                          │
│     └─► Tokens × precio por modelo = costo mensual            │
│         Contexto largo = alto costo recurrente,               │
│         salvo que uses caching o RAG                          │
│                                                               │
│  PASO 3: ¿Cómo me conecto?                                    │
│     └─► Chat (personal) | API (profesional) | Local (privado) │
│         Siempre empezá con el modelo más barato que alcance   │
└──────────────────────────────────────────────────────────────┘
```

---

## 9. Cierre

En esta clase vimos:

- El **token** es la moneda de la IA. No es una palabra: es un trozo de texto, y su conteo exacto varía según el tokenizador de cada proveedor.
- El **output** cuesta varias veces más que el input. Generar texto es más caro que leerlo.
- La **ventana de contexto** es la memoria del modelo. Llenarla cuesta dinero, y además una ventana grande no garantiza que el modelo use bien toda la información ("lost in the middle").
- Los **parámetros** ya no son un dato público confiable en los modelos de frontera, y con arquitecturas MoE dejaron de predecir el costo de forma directa.
- Existen **3 modalidades**: Chat (personal), API (profesional), Local (privado) — y la elección de cuantización en local cambia el costo de hardware drásticamente.
- **El precio de la IA "suficientemente buena" cayó ~660x entre 2020 y 2026.** Esa caída, no una opinión sobre qué modelo es "mejor", es la base económica de por qué conviene evaluar el modelo más barato primero.
- **Prompt caching y Batch API** son las dos palancas de ahorro que un ingeniero real usa además de (no en vez de) RAG.
- Los **costos ocultos** (rate limits por tier, latencia, VRAM y cuantización) pueden arruinar un proyecto si no se planifican desde el diseño.

### Próxima clase

**Clase 5: Benchmarks y Selección de Modelos.** Ahora que sabés cuánto cuesta, vamos a ver **cómo elegir el modelo correcto** para tu proyecto usando benchmarks reales.

---

> **Recordá:** la diferencia entre un usuario y un Ingeniero de IA es que el ingeniero sabe cuánto cuesta cada token **antes** de enviar el prompt.

---

### 📎 Nota para el docente

Todos los precios de esta versión fueron verificados el 11/09/2026 contra las páginas oficiales de OpenAI, Anthropic, Google y DeepSeek (linkeadas en la tabla 4.1). **Sugerencia:** antes de cada vez que dictes esta clase, volvé a verificar la tabla de precios — es, con diferencia, la parte del curso que más rápido se desactualiza. El gráfico de la caída histórica (4.2) y el concepto de "lost in the middle" (1.3) son mucho más estables en el tiempo que cualquier tabla de precios puntual, así que si tenés que priorizar qué actualizar primero en el futuro, empezá por la tabla 4.1.

Cambios respecto a la v1: se agregaron precios verificados de los modelos de frontera actuales (GPT-5.1, Claude Sonnet 4.5, Gemini 3 Pro, DeepSeek V3.2/V4) con fuente oficial linkeada; se agregó la comparación histórica de precios 2020-2026 con gráfico; se incorporaron los conceptos de prompt caching, Batch API, "lost in the middle", cuantización, y rate limits por tier, todos ausentes en la v1; se marcó explícitamente el dato de "1.8 billones de parámetros de GPT-4" como estimación no oficial.
