# Clase 7: Ingeniería de Prompts Profesional — Del texto a la respuesta

> Material de apoyo para el estudiante. Léelo directo en GitHub o en la vista web.

---

## Objetivo de la clase

Dejar de “hablarle” a la IA como si fuera un buscador de internet y empezar a darle instrucciones quirúrgicas. Vamos a entender cómo procesa el modelo tu texto, por qué una misma palabra puede cambiar de significado según sus vecinas y cómo usar parámetros avanzados para controlar la creatividad y la precisión de la respuesta.

La meta es simple: que cada prompt sea una instrucción con contexto, intención, límites y formato. No buscamos que la IA “se dé cuenta” de lo que queremos. Se lo vamos a decir con precisión.

---

## Filosofía de la clase

> **Un Ingeniero de IA no le “habla” a la IA como le hablaría a un amigo. Le escribe instrucciones quirúrgicas que aumentan la probabilidad de obtener el resultado que necesita. Eso es ingeniería de prompts.**

En las clases anteriores vimos costos, modelos y errores de la IA. Hoy empezamos a **usar** la IA de forma profesional: no como usuario casual, sino como ingeniero que diseña cada interacción para obtener un resultado más útil y verificable.

Si te llevás una sola cosa de esta clase, que sea esta:

> **La diferencia entre un prompt vago y uno quirúrgico es la diferencia entre un resultado genérico y uno que resuelve tu problema.**

---

## 1. Las 5 realidades de la IA

Antes de escribir un prompt, entendé con quién estás trabajando:

| # | Realidad | Implicación práctica |
|---|----------|---------------------|
| 1 | **“No comprende, predice”** | La IA no comprende tu intención como una persona. Calcula probabilidades y selecciona el siguiente token según la estrategia de decodificación. Sé explícito. |
| 2 | **“La memoria no está garantizada”** | Cada conversación nueva no conserva por sí sola lo que dijiste antes. No asumas que “recuerda” algo. |
| 3 | **“Espejo de datos”** | La IA refleja los sesgos y límites de sus datos de entrenamiento. Verificá los datos importantes. |
| 4 | **“La ambigüedad es un riesgo”** | Cuanto más vago sea el pedido, más formas puede tener la respuesta. La especificidad es tu herramienta. |
| 5 | **“Somos un equipo”** | Vos sos el estratega; la IA es la herramienta. No delegues la responsabilidad sin revisar. |

### Ejemplo: la realidad 1 en acción

```text
❌ VOS: “¿Qué opinás de la inteligencia artificial?”
   → La IA genera 500 palabras genéricas que no te sirven.

✅ VOS: “¿Qué ventajas tiene la IA para una pyme de 10 personas que vende ropa online?
   Quiero 3 puntos concretos, no textos largos.”
   → La IA te da 3 ventajas específicas y aplicables.
```

> **¿Por qué funciona mejor?** No le pediste “una opinión”. Le pediste algo específico: 3 ventajas, para un contexto concreto y con una restricción clara.

### Ejemplo: la realidad 4 en acción

```text
❌ VAGA: “Resumime esto”
   → ¿Qué es “esto”? ¿Cuántos puntos querés? ¿Para quién es el resumen?

✅ ESPECÍFICA: “Resumí este email en 3 puntos clave. Máximo 50 palabras.
   El resumen es para enviarlo a mi jefe, que tiene 2 minutos para leerlo.”
   → El modelo recibe instrucciones para producir 3 puntos, con un máximo de 50 palabras, para un lector ocupado.
```

---

## 2. Los 10 principios del ingeniero de prompts

| # | Principio | En una frase | Ejemplo rápido |
|---|-----------|-------------|----------------|
| 1 | La especificidad es poder | Lo vago produce respuestas vagas; lo específico produce resultados más útiles | “Escribe algo” → “Escribe un email de 100 palabras para confirmar una reunión mañana a las 3 p. m.” |
| 2 | El contexto es rey | Indicá quién, qué, por qué y en qué situación | “Soy vendedor de una inmobiliaria. Necesito un email para un cliente que vio 3 departamentos, pero no decidió.” |
| 3 | La experimentación es sagrada | Cada prompt es una hipótesis | Si el primer intento no sirve, cambiá una sola cosa y probá de nuevo. |
| 4 | El rol orienta el resultado | Una perspectiva puede orientar el estilo y el enfoque | “Eres un abogado” orienta la respuesta hacia lenguaje legal; “eres un diseñador”, hacia una respuesta visual. |
| 5 | La estructura libera la creatividad | Organizar el pedido mejora la calidad | Usá viñetas, numeración, separadores (`---`) y títulos. |
| 6 | Los ejemplos son espejos | Mostrás un patrón para que el modelo lo replique | “Escribí algo como este ejemplo y hacé uno similar para este tema.” |
| 7 | La iteración es el camino | Tu primer prompt rara vez es el mejor | Versión 1 → resultado → ajuste → versión 2. |
| 8 | Conocer el modelo mejora la calidad | Conocé las fortalezas y límites de cada modelo | Usá el modelo que mejor se adapte a la tarea y verificá sus resultados. |
| 9 | La revisión explícita de supuestos puede mejorar el prompt | Pedile a la IA que identifique qué le falta y verificá sus afirmaciones | “Antes de responder, indicá qué información adicional necesitás.” |
| 10 | El prompt es un producto | Diseñalo, probalo, versionalo y mejoralo | Guardá tus mejores prompts en un archivo para reutilizarlos. |

---

# Parte 1: el motor de la IA

Para escribir prompts profesionales, primero necesitamos una imagen mental sencilla de lo que ocurre con nuestro texto. No hace falta que memorices todas las fórmulas; sí necesitás entender qué significan y por qué influyen en la respuesta.

## 3. La pregunta clave: ¿cómo distingue la IA “gato” de “gato”?

Imaginá estas dos frases:

- “El gato duerme.”
- “El gato hidráulico está en el taller.”

En las dos aparece la palabra “gato”, pero una habla de un animal y la otra puede hablar de una herramienta.

### Respuesta directa

Durante la inferencia, el modelo usa los mismos pesos aprendidos. Si el token tiene el mismo identificador en el mismo modelo, su **embedding inicial** también es el mismo. Sin embargo, el modelo genera una **representación contextual diferente** para cada aparición de “gato” porque las palabras vecinas cambian la forma en que se interpreta ese token.

La diferencia está en el contexto de entrada y en cómo se propaga esa información por las capas del modelo, no en que el modelo tenga un interruptor secreto para animales y otro para herramientas.

### 3.1 Tokenización: la IA divide el texto en trozos

Un **token** no siempre es una palabra completa. Puede ser una palabra, una parte de una palabra, un signo de puntuación o varios caracteres.

Un ejemplo simplificado:

```text
Texto:  “El gato duerme”
Tokens: [“El”, “ gato”, “ duerme”]
```

En muchos tokenizadores, el espacio inicial forma parte del token. Por eso, `" gato"` y `"gato"` pueden ser entradas diferentes. No todos los modelos tokenizan de la misma manera, así que estos ejemplos sirven para entender la idea, no para adivinar qué tokens producirá cada plataforma.

La tokenización tiene tres efectos importantes:

1. El modelo procesa la entrada en unidades, no en conceptos perfectos.
2. La cantidad de tokens influye en el costo y en el límite de contexto.
3. Cambiar espacios, mayúsculas o puntuación puede cambiar la forma de tokenizar el texto.

### 3.2 Embedding inicial (estático): el vector por sí solo no representa todo el significado

Un **embedding** es una lista de números que representa una unidad de texto. Cada dimensión no tiene, por sí sola, un significado humano evidente. El modelo aprende la relación entre esas dimensiones durante el entrenamiento.

Por ejemplo, una entrada aproximada podría verse así:

```text
Embedding inicial de “gato” = [0.33, -0.21, 0.08, ...]
```

Si el token tiene el mismo identificador en el mismo modelo, el valor inicial de esa fila de la matriz de embeddings no cambia durante una misma ejecución. Pero ese vector inicial **no contiene por sí solo todo el significado de la frase**. Todavía falta incorporar el contexto.

> **Importante:** “estático” no significa “definitivo”. El embedding de entrada es fijo para ese token; su representación contextual cambia cuando pasa por las capas del modelo.

### 3.3 La clave: la atención es dinámica

En muchos modelos de lenguaje, la arquitectura **Transformer** utiliza autoatención (self-attention).

En una explicación sencilla, cada token produce tres representaciones vectoriales:

- **Query (Q):** una proyección que indica qué información busca el token para comparar.
- **Key (K):** una proyección que indica qué información ofrece para ser comparada.
- **Value (V):** una proyección que aporta información al resultado.

Las preguntas son una analogía: Q, K y V no son personas ni piezas que “piensen”. La atención permite que cada query asigne pesos a las keys permitidas y luego combine esa información para producir una representación contextualizada. En un modelo causal, una máscara impide que un token use tokens futuros.

#### Fórmula de la atención

```text
Atención(Q, K, V) = softmax((Q × Kᵀ) / √dₖ) × V
```

En notación matemática:

```text
Attention(Q, K, V) = softmax(QKᵀ / √dₖ)V
```

En un modelo causal, la fórmula se modifica conceptualmente con una máscara `M` que bloquea las posiciones futuras:

```text
Attention(Q, K, V) = softmax((QKᵀ / √dₖ) + M)V
```

El cálculo tiene cuatro movimientos:

1. **Q × Kᵀ:** compara cada query con cada key.
2. **División por √dₖ:** evita que las puntuaciones crezcan demasiado.
3. **Softmax:** convierte las puntuaciones en pesos que suman aproximadamente 1.
4. **Multiplicación por V:** combina los valores usando esos pesos.

### 3.4 T: la transpuesta no es una dimensión

La letra `T` no es una dimensión. Es una operación: **transponer** una matriz, es decir, intercambiar sus filas y columnas.

```text
K = [1  2  3]        Kᵀ = [1  4]
    [4  5  6]              [2  5]
                           [3  6]
```

- `K` tiene 2 filas × 3 columnas.
- `Kᵀ` tiene 3 filas × 2 columnas.

#### ¿Por qué se transpone K?

Porque para multiplicar `Q × Kᵀ`, las dimensiones internas deben coincidir:

```text
Q (n × dₖ)  ×  Kᵀ (dₖ × n)  =  matriz (n × n)
      ↑                ↑
  columnas dₖ      filas dₖ
  coinciden
```

La matriz final tiene una fila por cada token que actúa como query y una columna por cada token que actúa como key. Por eso tiene dimensiones `n × n`: cada token termina teniendo una puntuación de relevancia para cada token de la secuencia.

### 3.5 d: el tamaño de los vectores

La letra `d` indica una dimensión, es decir, el tamaño del vector. En un modelo de lenguaje pueden aparecer varias:

| Símbolo | Significado | Valor típico orientativo |
|---------|-------------|---------------------------|
| `d_model` | Dimensión del modelo y de los embeddings iniciales | 4096, 8192 |
| `d_q` | Dimensión de las queries | 64, 128 |
| `d_k` | Dimensión de las keys | 64, 128 |
| `d_v` | Dimensión de los values | 64, 128 |
| `n` | Número de tokens de la secuencia | Variable |

En una cabeza de atención simple, `d_q` y `d_k` suelen tener el mismo tamaño, pero eso no es una obligación universal. En este ejemplo didáctico usaremos `d_q = d_k = d_v = 4`. Por eso, Q se puede representar como `n × dₖ`. En modelos reales pueden existir muchas cabezas de atención y otras dimensiones, por lo que estos valores son solo ejemplos.

### 3.6 La fórmula paso a paso con un ejemplo numérico

Supongamos una frase muy corta:

```text
n = 3 tokens: [“El”, “ gato”, “ duerme”]
```

Para que el ejemplo sea manejable, suponemos que `d_q = d_k = d_v = 4` y omitimos la máscara causal. Un modelo real puede utilizar dimensiones mucho mayores.

#### Paso 1: calcular Q, K y V

Cada token tiene una representación. En una primera capa, `X` suele combinar el embedding del token con información posicional; en capas posteriores representa el estado oculto contextual. Luego, el modelo lo multiplica por matrices de pesos entrenados:

```text
Q = X × W_Q
K = X × W_K
V = X × W_V
```

En este ejemplo:

```text
Q = [0.1  0.2  0.3  0.4]     ← Query de “El”
    [0.5  0.6  0.7  0.8]     ← Query de “ gato”
    [0.9  1.0  1.1  1.2]     ← Query de “ duerme”

K = [0.2  0.1  0.4  0.3]     ← Key de “El”
    [0.6  0.5  0.8  0.7]     ← Key de “ gato”
    [1.0  0.9  1.2  1.1]     ← Key de “ duerme”

V = [0.3  0.1  0.2  0.4]     ← Value de “El”
    [0.7  0.5  0.6  0.8]     ← Value de “ gato”
    [1.1  0.9  1.0  1.2]     ← Value de “ duerme”
```

`W_Q`, `W_K` y `W_V` son matrices de pesos entrenados. `X` contiene las representaciones que entran a esta capa; en la primera capa pueden incluir el embedding del token y la información de su posición.

#### Paso 2: calcular Q × Kᵀ

Primero transponemos K:

```text
Kᵀ = [0.2  0.6  1.0]     ← transpuesta de K (4 × 3)
     [0.1  0.5  0.9]
     [0.4  0.8  1.2]
     [0.3  0.7  1.1]
```

Después calculamos el producto punto entre cada query y cada key:

```text
Q × Kᵀ = [0.28  0.68  1.08]
         [0.68  1.72  2.76]
         [1.08  2.76  4.44]
```

Cada celda `(i, j)` es la puntuación entre la query del token `i` y la key del token `j`.

Por ejemplo, la primera celda es:

```text
0.1×0.2 + 0.2×0.1 + 0.3×0.4 + 0.4×0.3 = 0.28
```

#### Paso 3: dividir por √dₖ

```text
dₖ = 4
√dₖ = 2

(Q × Kᵀ) / 2 = [0.14  0.34  0.54]
               [0.34  0.86  1.38]
               [0.54  1.38  2.22]
```

¿Por qué dividir por la raíz de `dₖ`?

Cuando `dₖ` es grande, los productos punto pueden producir puntuaciones muy altas. El factor `√dₖ` reduce el efecto de esa escala, ayuda a mantener el softmax en un rango manejable y estabiliza el aprendizaje durante el entrenamiento.

#### Paso 4: aplicar softmax

El softmax convierte cada fila en pesos aproximados que suman 1:

```text
Fila “El”:      [0.269, 0.329, 0.402]
Fila “ gato”:   [0.181, 0.305, 0.513]
Fila “ duerme”: [0.115, 0.267, 0.618]
```

Estos son los **pesos de atención** del ejemplo. No son porcentajes de certeza sobre el significado; son coeficientes que indican cuánta información de cada token se incorpora en cada representación contextual.

#### Paso 5: multiplicar por V

```text
Atención = pesos × V
```

El resultado aproximado es:

```text
[0.753  0.553  0.653  0.853]
[0.832  0.632  0.732  0.932]
[0.901  0.701  0.801  1.001]
```

Cada fila corresponde a un token, pero ahora incorpora información del contexto. En una arquitectura real, también intervienen la codificación posicional, las conexiones residuales, la normalización y la atención de múltiples cabezas.

### 3.7 Resumen visual de las dimensiones

```text
Q       (n × dₖ)      n = 3 tokens, dₖ = 4
K       (n × dₖ)      n = 3 tokens, dₖ = 4
Kᵀ      (dₖ × n)      4 × 3
V       (n × dᵥ)      n = 3 tokens, dᵥ = 4

Q × Kᵀ        → (n × n)   → 3 × 3
/ √dₖ         → (n × n)   → 3 × 3
softmax        → (n × n)   → 3 × 3, pesos
× V            → (n × dᵥ) → 3 × 4, resultado
```

### 3.8 Qué significa cada símbolo

| Símbolo | Nombre | Qué representa | Dimensión o valor |
|---------|--------|----------------|-------------------|
| `Q` | Query | ¿Qué busca este token? | `n × dₖ` |
| `K` | Key | ¿Qué ofrece este token para ser comparado? | `n × dₖ` |
| `V` | Value | ¿Qué información puede aportar este token? | `n × dᵥ` |
| `Kᵀ` | Key transpuesta | K con filas y columnas intercambiadas | `dₖ × n` |
| `dₖ` | Dimensión de las keys | Tamaño de cada vector de key | 64, 128 o más |
| `dᵥ` | Dimensión de los values | Tamaño de cada vector de value | 64, 128 o más |
| `n` | Número de tokens | Cantidad de tokens de la secuencia | Variable |
| `√dₖ` | Raíz de `dₖ` | Factor de escala | 8 para `dₖ = 64`; 11,3 para `dₖ = 128` |
| `T` | Transpuesta | Operación, no dimensión | — |

### 3.9 Analogía de la biblioteca

Imagá una biblioteca:

- **Q (Query):** lo que preguntás: “¿Tenés libros sobre gatos?”
- **K (Key):** el título o la etiqueta de cada libro: “Historia de los gatos”, “Matemáticas”, “Gatos en el arte”.
- **V (Value):** el contenido de cada libro.
- **Q × Kᵀ:** compará tu pregunta con cada título y obtenés una puntuación de relevancia.
- **Softmax:** convertís las puntuaciones en pesos: por ejemplo, el libro sobre gatos recibe más peso.
- **× V:** mezclás el contenido de los libros según esa relevancia para construir una respuesta contextualizada.
- **dₖ:** la cantidad de características que el catálogo usa para comparar títulos; no es literalmente la cantidad de palabras.
- **T:** girar la lista de títulos para que sus dimensiones coincidan con las de la pregunta.

La biblioteca no comprende el significado como una persona. Compara señales, encuentra coincidencias y construye una representación útil a partir de ellas.

### 3.10 Frase clave

> **T es la transpuesta, es decir, una operación. dₖ es la dimensión de las keys, es decir, el tamaño del vector. n es el número de tokens. La atención convierte comparaciones entre queries y keys en pesos y luego usa esos pesos para combinar los values.**

### 3.11 Comparativa en acción: el contexto lo es todo

| Elemento | “El gato duerme” | “El gato hidráulico está en el taller” | ¿Cambia? |
|----------|------------------|----------------------|----------|
| Pesos del modelo | Los mismos | Los mismos | No |
| Embedding inicial de “gato” | `[0.33, -0.21, ...]` | `[0.33, -0.21, ...]` | No |
| Tokens vecinos | “duerme” | “hidráulico” | Sí |
| Atención | Integra señales de “duerme” | Integra señales de “hidráulico” | Sí |
| Estado oculto contextual | Puede asociarse con un animal | Puede asociarse con una herramienta | Sí |
| Asociación contextual más probable | Animal que descansa | Herramienta mecánica | Sí |

#### Analogía de la calculadora

Imagá una calculadora con la tecla `×`. La función es siempre la misma, pero `3 × 4 = 12` y `5 × 6 = 30`. Misma función, distinta entrada, distinto resultado.

En la IA ocurre algo parecido: mismos pesos aprendidos, distinto contexto y distinta representación contextual.

### 3.12 Caso práctico: “El gato está bajo el carro”

La entrada podría tokenizarse así:

```text
[“El”, “ gato”, “ está”, “ bajo”, “ el”, “ carro”]
```

La palabra “gato” recibe información de tokens como “está”, “bajo” y “carro”. Como no aparecen palabras como “taller”, “mecánico” o “hidráulico”, la interpretación más probable en muchos contextos se orienta hacia un animal.

Si añadimos “hidráulico”:

```text
“El gato hidráulico está en el taller.”
```

El contexto cambia, la atención se recalcula y la representación contextual de “gato” cambia. El modelo tiene entonces más señales para relacionarlo con una herramienta.

La conclusión es importante:

> **La IA no tiene un interruptor de “animal” o “herramienta”. Tiene un proceso gradual de contextualización. Por eso, las palabras que rodean a tu concepto clave son tan importantes como el concepto mismo.**

---

# Parte 2: el panel de control

## 4. Parámetros avanzados de generación

Después de procesar la entrada completa —incluidos el mensaje de sistema, el historial y el mensaje actual—, el modelo produce una distribución de probabilidades para el siguiente token. Los parámetros de muestreo modifican **cómo se hace la elección**. No cambian los pesos entrenados del modelo ni le dan conocimiento nuevo; modifican cuánto margen tiene para explorar alternativas.

No todas las interfaces exponen los tres parámetros. Sus nombres, rangos, valores por defecto y comportamiento pueden variar según el modelo y el proveedor. Revisá las opciones disponibles en la herramienta que estés usando.

| Parámetro | ¿Qué es? | Valor bajo | Valor alto | Uso orientativo |
|-----------|----------|------------|------------|-----------------|
| **Temperature** | El “dial de creatividad”. Controla cuánto se arriesga el modelo al elegir el siguiente token. | Concentración: favorece la opción más probable y reduce la variedad. | Exploración: considera con más peso opciones menos probables y puede aumentar la variedad. | Valores bajos suelen servir para código, contratos, resúmenes y datos financieros. Valores altos pueden ayudar con lluvia de ideas, nombres y poesía. La temperatura no garantiza precisión factual. |
| **Top-P (nucleus sampling o muestreo por núcleo)** | Limita los candidatos según la probabilidad acumulada. Se ordenan las probabilidades y se conserva el conjunto mínimo que alcanza el valor indicado. | Considera menos candidatos. | Considera más candidatos, con mayor variedad relativa. | Puede combinarse con `temperature` si la interfaz lo permite. `0.9` puede ser un punto de partida, pero no existe un valor universal. |
| **Top-K** | Limita los candidatos a los `K` tokens más probables. | `K = 1`: una sola opción; muy rígido. | Valores como `40` o `50` pueden abrir más opciones, según el modelo. | Reduce el conjunto de candidatos, pero no garantiza que sean “mejores” ni que no sean incoherentes. |

### Temperature

Con una temperatura baja, la distribución de candidatos se concentra más alrededor de las opciones más probables. Con una temperatura alta, las opciones menos probables reciben relativamente más peso. El resultado exacto depende de la implementación.

Por eso, una tarea de cobranza no debería depender de una temperatura alta: la creatividad puede ser útil, pero la precisión y el tono profesional son más importantes. Una temperatura baja tampoco garantiza que una afirmación sea verdadera.

### Top-P

Top-P se llama también **nucleus sampling** o muestreo por núcleo. En lugar de fijar una cantidad de opciones, ordena las probabilidades y conserva el conjunto mínimo que alcanza la masa de probabilidad acumulada indicada.

- Con `Top-P = 0.5`, puede quedar un conjunto de candidatos más pequeño.
- Con `Top-P = 0.9`, se pueden considerar más candidatos hasta alcanzar el 90 % de probabilidad acumulada.

El tamaño exacto del conjunto depende de cómo se distribuyen las probabilidades en cada paso.

### Top-K

Top-K utiliza una regla sencilla: si `K = 20`, el modelo solo considera los 20 tokens más probables. No es lo mismo que Top-P: uno limita por cantidad y el otro por probabilidad acumulada. Si se usan juntos, ambos filtros pueden limitar el conjunto de candidatos; la interacción depende de la implementación.

### Ejemplo práctico

**Prompt:** “Escribe un asunto para un correo de cobranza a un cliente moroso.”

**Con `temperature = 0.2`:**

```text
Recordatorio de pago pendiente — factura n.º 123
```

**Con `temperature = 0.9`:**

```text
¡Hola! ¿Te llegó nuestra factura? Te agradecería revisar el pago pendiente.
```

La segunda versión puede ser más expresiva, pero no necesariamente más adecuada para una cobranza. El parámetro no decide qué es correcto: vos debés elegirlo según el riesgo de la tarea. Para comparar efectos, mantené los demás parámetros constantes y repetí la prueba varias veces.

---

# Parte 3: la anatomía de un prompt profesional

Ahora que entendimos que el contexto cambia el significado, tenemos que darle a la IA el mejor contexto posible. No alcanza con decir “escribe algo”. Necesitamos indicar quién debe responder, qué debe lograr y cómo querés recibir el resultado.

## 5. La estructura esencial

### 5.1 Los tres bloques mínimos

```text
┌─────────────────────────────────────────┐
│ 1. PERSONA                             │
│ ¿Quién debe ser la IA?                │
│ “Eres un experto en...”                │
├─────────────────────────────────────────┤
│ 2. CONTEXTO                            │
│ ¿Cuál es la situación?                 │
│ “Trabajo en una empresa que...”        │
├─────────────────────────────────────────┤
│ 3. INSTRUCCIÓN                         │
│ ¿Qué exactamente querés?              │
│ “Genera un informe que...”             │
└─────────────────────────────────────────┘
```

### 5.2 La fórmula completa

```text
PERSONA + CONTEXTO + OBJETIVO + RESTRICCIONES + FORMATO = PROMPT ESPECÍFICO
```

### 5.3 La escala de calidad

| Nivel | Prompt | Calidad |
|-------|--------|---------|
| 1 (Vago) | “Escribe algo” | 1/5 |
| 2 (Básico) | “Escribe un email” | 2/5 |
| 3 (Dirigido) | “Escribe un email profesional de seguimiento” | 3/5 |
| 4 (Detallado) | “Escribe un email de seguimiento para un cliente que asistió a nuestra demo” | 4/5 |
| 5 (Quirúrgico) | “Eres el director de ventas de una empresa SaaS B2B. Escribe un email de seguimiento de máximo 150 palabras para María González, CTO de TechCorp, que asistió a nuestra demo el martes. Menciona integración con su CRM, reducción de costos del 30 % y un piloto gratuito de 30 días. Tono profesional, pero cálido.” | 5/5 |

La fórmula completa amplía esos tres bloques con objetivo, restricciones y criterios de calidad. Un prompt no se vuelve mejor por estar más largo, sino cuando cada parte aporta información que el modelo puede utilizar. Los datos como una reducción de costos deben estar verificados; si son hipotéticos, indicálo en el prompt.

## 6. La fórmula del rol de élite

Evitá decirle solamente “actúa como un contador”. Esa frase orienta la respuesta de manera general. Para pedir mayor precisión, agregá nivel, especialización y un marco de trabajo.

```text
[Nivel jerárquico] + [Profesión base] + [Hiperespecialización] + [Marco de trabajo o contexto]
```

### Comparación

```text
❌ No profesional: “Actúa como un vendedor.”

✅ Profesional: “Actúa como un director de ventas B2B, especializado en negociación
de alto valor y con experiencia en clientes del sector agroindustrial ecuatoriano.
Usá el método de venta consultiva SPIN.”
```

La segunda versión no activa mágicamente a un “experto n.º 87”. Es una metáfora: orienta la respuesta hacia los patrones que el modelo aprendió para textos de ventas consultiva, negociación B2B y el sector indicado.

Aunque algunos modelos utilizan arquitecturas de mezcla de expertos (MoE), una frase con “actúa como” no selecciona de manera garantizada un subconjunto concreto de expertos. El resultado depende de la representación interna, del contexto completo y de los patrones aprendidos.

## 7. Complementos opcionales de un prompt avanzado

| # | Componente | Pregunta guía | Ejemplo |
|---|-----------|---------------|---------|
| 1 | **Rol o persona** | ¿Quién es la IA? | “Eres un consultor con experiencia en marketing digital.” |
| 2 | **Contexto** | ¿Cuál es la situación? | “Trabajo en una startup de fintech con 50 empleados.” |
| 3 | **Objetivo** | ¿Qué querés lograr? | “Crear una estrategia de contenido para LinkedIn.” |
| 4 | **Restricciones** | ¿Qué límites hay? | “Presupuesto de 500 dólares por mes, sin herramientas de pago.” |
| 5 | **Formato** | ¿Cómo debe verse la salida? | “Plan mensual en formato de tabla.” |
| 6 | **Audiencia** | ¿Para quién es? | “Emprendedores de 25 a 40 años.” |
| 7 | **Ejemplos** | ¿Qué patrón debe seguir? | “Este es un ejemplo de publicación que me gusta.” |
| 8 | **Criterios de calidad** | ¿Cómo evaluás el resultado? | “Debe tener una llamada a la acción clara y datos concretos.” |

Estos ocho componentes no son todos obligatorios. Son una lista de ampliación para completar la fórmula según la complejidad de la tarea.

## 8. Marco CO-STAR: una plantilla para organizar el prompt

CO-STAR es una plantilla útil para revisar si tu prompt cubre seis elementos de la comunicación. No es un estándar universal y no reemplaza la fórmula completa: el rol, las restricciones y los criterios de calidad pueden añadirse según la tarea.

| Letra | Significado | Pregunta guía | Ejemplo: emprendimiento |
|-------|-------------|---------------|------------------------|
| **C** | Contexto | ¿Cuál es la situación y cuáles son los antecedentes? | “Tengo una tienda de ropa en Quito y las ventas bajaron 15 % este mes.” |
| **O** | Objetivo | ¿Qué tarea principal debo lograr? | “Crear un plan de 3 acciones de bajo costo para reactivar las ventas.” |
| **S** | Estilo | ¿Cómo debe estar escrito? | “Profesional, empático y orientado a la solución.” |
| **T** | Tono | ¿Qué actitud o emoción debe transmitir la respuesta? | “Urgente, pero esperanzador.” |
| **A** | Audiencia | ¿Quién leerá el resultado? | “Mis clientes actuales, mujeres de 30 a 50 años.” |
| **R** | Respuesta | ¿Qué contenido, formato y extensión debe tener la salida? | “Una tabla con Acción, Canal (WhatsApp o Instagram) y Guion de mensaje, de máximo 150 palabras.” |

### Ejemplo completo con CO-STAR

```text
C: Tengo una tienda de ropa en Quito. Este mes las ventas bajaron 15 %.
O: Crear un plan de 3 acciones de bajo costo para reactivar las ventas.
S: Profesional, empático y orientado a la solución.
T: Urgente, pero esperanzador.
A: Mis clientes actuales, mujeres de 30 a 50 años.
R: Una tabla con las columnas Acción, Canal (WhatsApp o Instagram) y Guion de mensaje.
```

---

# Parte 4: el método de iteración RIPPLE

## 9. La regla de oro

> **Como regla de diagnóstico, intentá no cambiar varias partes del prompt al mismo tiempo. Si modificás el rol, el contexto y el formato en una sola iteración, será más difícil descubrir qué cambio ayudó o perjudicó la respuesta.**

Un prompt es una hipótesis. Antes de probarlo, escribí una lista breve de criterios de éxito. Después, modificá **un solo elemento**, observá el resultado y repetí la prueba.

### 9.1 Los seis pasos de RIPPLE

| Letra | Paso | Acción |
|--------|------|--------|
| **R** | Redactá | Escribí tu primer prompt usando CO-STAR. |
| **I** | Inspeccioná | Leé la respuesta completa y observá qué cambió. |
| **P** | Preguntate | ¿Qué faltó? ¿Qué sobró? ¿Dónde falló? |
| **P** | Perfeccioná | Ajustá un solo componente: rol, contexto, temperatura o formato. |
| **L** | Lanzá | Ejecutá nuevamente el prompt mejorado. |
| **E** | Evaluá | Compará el resultado con los criterios que definiste. Si no se cumplen, volvé a **Perfeccioná**; si se cumplen, cerrá la iteración. |

### Ejemplo de una iteración

```text
Versión 1: formato tabla, temperatura = 0.2
Problema: el mensaje es correcto, pero resulta difícil de enviar.
Versión 2: cambiar únicamente el formato a una lista breve.
Resultado esperado: la salida puede ser más fácil de aplicar, aunque el contenido también puede cambiar.
```

En otra iteración, si el problema es la falta de variedad, podés cambiar únicamente la temperatura de `0.2` a `0.7`. No cambies simultáneamente el rol, el contexto y el formato. Como la generación puede ser aleatoria, repetí varias ejecuciones y, si la interfaz lo permite, usá una semilla fija.

---

# Parte 5: resumen visual de la clase

```text
┌─────────────────────────────────────────────────────────────┐
│          EL CAMINO DEL INGENIERO DE PROMPTS                │
│                                                             │
│ 1. COMPRENDE: el embedding inicial puede ser el mismo,     │
│    pero el contexto y los patrones de atención cambian     │
│    su representación contextual.                            │
│                                                             │
│ 2. CONFIGURA: elegí Temperature, Top-P y Top-K para       │
│    equilibrar precisión, creatividad y coherencia.          │
│                                                             │
│ 3. ESTRUCTURA: combiná rol, contexto, objetivo,            │
│    restricciones y formato; revisá la plantilla CO-STAR.   │
│                                                             │
│ 4. ITERA: aplicá RIPPLE y cambiá un solo elemento          │
│    en cada prueba.                                          │
└─────────────────────────────────────────────────────────────┘
```

### La frase que resume toda la clase

> **El contexto es el entorno que le da sentido a tus palabras; el prompt es la instrucción que organiza ese contexto; y la iteración es el método que permite mejorarlo con evidencia.**

---

## El Ing. de IA en esta clase

### Tu rol: el arquitecto de instrucciones

| Habilidad | Qué significa |
|-----------|--------------|
| Diseñar prompts quirúrgicos | Cada palabra tiene un propósito y una función. |
| Usar marcos estructurados | Aplicá CO-STAR o RTF según la tarea. |
| Elegir la técnica correcta | Ajustá el prompt al nivel de detalle y al riesgo de la tarea. |
| Ajustar parámetros | Elegí Temperature, Top-P y Top-K según la creatividad que necesitás. |
| Iterar y versionar | Tu primer prompt es un experimento, no el resultado final. |
| Evaluar antes de confiar | Revisá hechos, supuestos, formato y límites. |

> **No sos el que le “habla” a la IA. Sos el que diseña las instrucciones que aumentan la probabilidad de obtener el resultado que necesitás.**

---

## Tarea práctica progresiva

### Nivel sencillo: RTF y temperatura baja

Escribí un prompt usando el marco RTF para organizar tu lista de compras semanal o las tareas de tu negocio. Si la interfaz te permite configurar la temperatura, usá `temperature = 0.2` para obtener una respuesta más directa.

### Nivel avanzado: CO-STAR y rol de élite

Elegí un problema real de tu trabajo, estudio o emprendimiento. Escribí un prompt completo usando CO-STAR y creá un rol de élite con la fórmula de cuatro partes:

```text
[Nivel jerárquico] + [Profesión base] + [Hiperespecialización] + [Marco de trabajo o contexto]
```

### Prueba RIPPLE

Si la primera respuesta no cumple tus criterios, cambiá un solo elemento:

- Subí la temperatura de `0.2` a `0.7`, o
- Cambiá únicamente el formato de tabla a una lista breve.

Guardá las dos versiones y anotá qué cambió. Repetí la prueba si la respuesta es aleatoria; no podés atribuir el cambio a una sola variable a partir de una sola ejecución.

---

## Cierre y puente a la Clase 8

En esta clase vimos:

- Las 5 realidades de la IA y por qué conviene escribir con precisión.
- Los 10 principios del ingeniero de prompts.
- Cómo la tokenización, los embeddings y la atención ayudan a contextualizar una palabra.
- Qué significan Q, K, V, `Kᵀ`, `dₖ` y `n` dentro de la atención.
- Cómo usar Temperature, Top-P y Top-K para controlar la generación.
- La anatomía de un prompt profesional, la fórmula del rol de élite y CO-STAR.
- El método RIPPLE para mejorar una respuesta cambiando un solo elemento por vez.

### Próxima clase

**Clase 8: habilidades, agentes, bucles y harness** —la estructura que conecta al agente con sus herramientas—. Vamos a pasar de escribir mejores instrucciones a construir sistemas que puedan usar herramientas, observar resultados, repetir acciones y cumplir objetivos más complejos.

---

> **Recordá:** la diferencia entre un usuario y un ingeniero de IA es que el ingeniero diseña cada prompt como un producto: con requisitos, especificaciones, parámetros y criterios de calidad.

