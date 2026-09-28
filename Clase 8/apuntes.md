# Clase 8 — Técnicas de Razonamiento: Chain-of-Thought y ReAct
### (Septiembre 2026)

> Material de apoyo para el estudiante. Leelo directo en GitHub o en la vista web.

---

## Filosofía de la clase

> **Un modelo que responde de inmediato adivina. Un modelo al que le pedís que razone, calcula. La diferencia entre ambos puede ser la diferencia entre una respuesta correcta y una alucinación con total seguridad (Clase 6).**

En la Clase 7 aprendiste a estructurar prompts con CO-STAR y a iterarlos con RIPPLE. Hoy vamos un paso más allá: no solo **qué** le pedís a la IA, sino **cómo hacer que piense mejor antes de responder**.

Si te llevás una sola cosa de esta clase, que sea esta:

> **Para cualquier problema con más de un paso lógico, pedirle a la IA que "piense paso a paso" no es un truco — es la diferencia entre una respuesta confiable y una adivinanza con buena redacción.**

---

## 1. El Problema que Resuelve el Razonamiento Explícito

Recordá la Clase 6: la IA predice la palabra más probable, no "calcula" en el sentido humano. Cuando le hacés una pregunta que requiere varios pasos lógicos y le pedís la respuesta directa, el modelo intenta "adivinar" el resultado final de una sola vez — y en problemas de varios pasos, eso falla más de lo que pensás.

### Ejemplo: el mismo problema, dos formas de preguntar

**Sin pedir razonamiento:**
> "En una tienda, una camisa cuesta $25 y tiene 20% de descuento. Hay que pagar 8% de impuesto sobre el precio final. ¿Cuánto pago?"
>
> Respuesta típica: **"$21.60"** *(a veces correcta, a veces el modelo mezcla el orden de las operaciones y se equivoca — con la misma confianza en ambos casos)*

**Pidiendo razonamiento paso a paso:**
> "...¿Cuánto pago? Pensemos paso a paso."
>
> ```
> Paso 1: Precio original = $25
> Paso 2: Descuento = 20% de $25 = $5
> Paso 3: Precio con descuento = $25 - $5 = $20
> Paso 4: Impuesto = 8% de $20 = $1.60
> Paso 5: Precio final = $20 + $1.60 = $21.60
> Respuesta: $21.60
> ```

En este ejemplo ambas dieron lo mismo — pero en problemas más largos o con más pasos encadenados, forzar el razonamiento explícito reduce notablemente los errores, porque cada paso queda "anclado" al anterior en vez de que el modelo tenga que acertar el resultado final de un salto.

---

## 2. Chain-of-Thought (CoT): La Frase Mágica

**Definición:** pedirle al modelo que razone paso a paso antes de dar la respuesta final, en vez de ir directo a la conclusión.

**La frase que lo activa:** *"Pensemos paso a paso"* (o su versión en inglés, *"Let's think step by step"*).

### 2.1 Cuándo usar CoT

- Problemas matemáticos o de cálculo
- Razonamiento lógico con varias condiciones
- Toma de decisiones con múltiples factores a sopesar
- Análisis de situaciones complejas (ej. el caso de Carlos el contador, de la clase de auditoría de procesos)
- Cualquier caso donde ya notaste que la respuesta directa suele venir mal

### 2.2 Las 4 variantes de CoT

| Variante | Qué es | Cuándo usarla |
|---|---|---|
| **Zero-Shot CoT** | Simplemente agregar "pensemos paso a paso" al final del prompt | La más simple, andá con esta primero |
| **Few-Shot CoT** | Dar 1-2 ejemplos que YA incluyen el razonamiento paso a paso, además de la respuesta | Cuando querés que el modelo razone de una forma muy específica (tu propia metodología) |
| **Auto-CoT** | Pedirle al modelo que genere sus propios ejemplos de razonamiento antes de resolver el caso real | Para tareas repetitivas donde no tenés ejemplos armados de antemano |
| **Tree-of-Thought (ToT)** | El modelo explora varios caminos de razonamiento en paralelo y evalúa cuál conviene seguir, en vez de un solo camino lineal | Problemas con varias soluciones posibles a comparar (ej. "¿qué estrategia de precios conviene más?") |

### 2.3 Ejemplo de Few-Shot CoT aplicado a un caso de negocio

```
Evaluá si conviene aceptar este pedido especial, razonando paso a paso.

Ejemplo:
Pedido: 500 unidades a $8 c/u, costo variable $6, capacidad ociosa disponible.
Razonamiento:
Paso 1: Ingreso adicional = 500 × $8 = $4,000
Paso 2: Costo variable adicional = 500 × $6 = $3,000
Paso 3: Como hay capacidad ociosa, no hay costo fijo adicional
Paso 4: Ganancia marginal = $4,000 - $3,000 = $1,000
Conclusión: Conviene aceptar, genera $1,000 de ganancia marginal.

Nuevo caso:
Pedido: 800 unidades a $5 c/u, costo variable $6, sin capacidad ociosa (hay que
rechazar producción regular que se vende a $9 c/u con el mismo costo variable).
Razonamiento:
```

---

## 3. ReAct: Razonar + Actuar (Introducción Conceptual)

> Esta sección es **conceptual**. Vas a construir un ReAct real, con herramientas de verdad conectadas, más adelante en el bloque de Agentes del taller. Hoy entendés el patrón; ahí lo programás.

### 3.1 ¿Qué es ReAct?

**ReAct** (Reasoning + Acting) combina razonamiento con acción. En vez de responder directo, el modelo:
1. **Piensa** qué necesita saber (Thought)
2. **Ejecuta** una acción para obtenerlo (Action)
3. **Observa** el resultado (Observation)
4. Repite el ciclo hasta poder responder

### 3.2 El formato

```
Thought: [razonamiento sobre qué hacer]
Action: [acción a ejecutar]
Observation: [resultado de la acción]
... (el ciclo se repite las veces que haga falta)
Final Answer: [respuesta final]
```

### 3.3 Ejemplo completo

**Pregunta:** "¿Cuál es la población de la capital de Francia y cómo se compara con la de Barcelona?"

```
Thought: Necesito saber cuál es la capital de Francia y su población.
Action: buscar[capital de Francia]
Observation: París

Thought: Ahora necesito la población de París.
Action: buscar[población de París]
Observation: 2.16 millones (ciudad), 12.3 millones (área metropolitana)

Thought: Necesito comparar con Barcelona.
Action: buscar[población de Barcelona]
Observation: 1.62 millones (ciudad), 5.3 millones (área metropolitana)

Thought: Tengo todos los datos. Puedo comparar.
Final Answer: París tiene 2.16M habitantes vs Barcelona con 1.62M.
El área metropolitana de París (12.3M) es más del doble que la de
Barcelona (5.3M).
```

### 3.4 Cuándo se usa ReAct (y por qué hoy es solo conceptual)

- Tareas que requieren información externa que el modelo no tiene de memoria
- Análisis multi-paso con verificación intermedia
- Diagnóstico y troubleshooting

> **La diferencia entre esto y un agente real:** en este ejemplo, "buscar[...]" es una simulación — nosotros escribimos el resultado a mano para entender el patrón. Un agente real necesita **Function Calling** (conectar el modelo a una herramienta de búsqueda de verdad) y un **loop de control programado** que ejecute este ciclo automáticamente. Eso es, literalmente, lo que vas a construir más adelante en el bloque técnico del taller — hoy te llevás el patrón de pensamiento, ahí le agregás el código.

---

## 4. Psicología del Contexto: Cómo "Lee" el Modelo tu Prompt

> Esto conecta directamente con "lost in the middle", que vimos en la Clase 4 sobre ventanas de contexto grandes. Acá lo aplicamos a nivel de un solo prompt.

| Principio | Qué significa | Qué hacer |
|---|---|---|
| **Primacía** | La información al inicio del prompt tiene más peso | Poné el rol y el contexto más importante AL PRINCIPIO |
| **Recencia** | La información al final influye más en la respuesta inmediata | Poné las instrucciones de formato AL FINAL |
| **Densidad informacional** | Cada palabra cuenta; no llenes de relleno | Un prompt corto y denso rinde más que uno largo y diluido |
| **Anclaje** | El primer ejemplo (en Few-Shot) sesga todas las respuestas siguientes | Elegí con cuidado tu primer ejemplo |
| **Contraste** | El modelo nota mejor lo que se distingue visualmente del resto | Usá marcadores claros (###, tablas, negritas) para separar secciones |

### Estructura recomendada de un prompt largo, aplicando estos 5 principios

```
[ROL — Primacía: activa el conocimiento especializado]
[CONTEXTO — establece la situación]
[TAREA PRINCIPAL — el qué, con verbo de acción claro]
[EJEMPLOS — Anclaje: si usás Few-Shot]
[RESTRICCIONES — los límites]
[FORMATO — Recencia: el último empujón hacia el resultado exacto]
```

---

## 5. Cuándo Combinar CoT + Few-Shot + Rol Específico

Las técnicas de esta clase y de la Clase 7 no son excluyentes — en la práctica profesional se combinan:

```
ROL (Clase 7): Actuá como consultor de startups en foodtech latinoamericana

CONTEXTO (Clase 7): App de delivery de comida casera en Quito

FEW-SHOT (Clase 7): [1-2 ejemplos del formato de análisis esperado]

INSTRUCCIÓN CoT (Clase 8): Antes de dar tu recomendación final, razoná
paso a paso considerando: viabilidad financiera, competencia local, y
capacidad operativa. Mostrá tu razonamiento y después la conclusión.
```

> Este es, en esencia, el prompt de nivel "Maestro" que mencionamos en la escala de calidad de la Clase 7 — todo lo que aprendiste hasta ahora, en una sola instrucción bien armada.

---

## 6. El Ingeniero de IA en esta Clase

| Habilidad | Qué significa |
|-----------|--------------|
| Sabe cuándo un problema necesita razonamiento explícito | No confía en la respuesta directa para problemas de varios pasos |
| Elige la variante correcta de CoT | Zero-Shot para lo simple, Few-Shot para su propia metodología, ToT para comparar opciones |
| Entiende el patrón ReAct antes de programarlo | Sabe qué está construyendo cuando llegue al bloque de agentes |
| Estructura el prompt según cómo "lee" el modelo | Aplica primacía, recencia y contraste, no arma el prompt al azar |

---

## 7. Resumen Visual

```
┌──────────────────────────────────────────────────────────────┐
│         DE LA RESPUESTA DIRECTA AL RAZONAMIENTO GUIADO         │
│                                                                │
│  Respuesta directa                                             │
│  └── Rápida, pero falla en problemas de varios pasos          │
│                                                                │
│  + Chain-of-Thought ("pensemos paso a paso")                  │
│  └── El modelo ancla cada paso al anterior, menos error        │
│                                                                │
│  + ReAct (razonar → actuar → observar → repetir)               │
│  └── El modelo puede buscar información que no tiene           │
│      (hoy: simulado a mano | después: con herramientas reales) │
│                                                                │
│  + Psicología del contexto (dónde poner cada cosa)             │
│  └── El mismo contenido, mejor ordenado, mejor resultado       │
└──────────────────────────────────────────────────────────────┘
```

---

## 8. Cierre y puente a la Clase 9

En esta clase vimos:

- Por qué pedirle a la IA que **razone paso a paso** reduce errores en problemas de varios pasos.
- Las **4 variantes de Chain-of-Thought**: Zero-Shot, Few-Shot, Auto-CoT, Tree-of-Thought.
- El patrón **ReAct** (Thought → Action → Observation) de forma conceptual — la versión con herramientas reales viene en el bloque de agentes.
- Los **5 principios de psicología del contexto**: primacía, recencia, densidad, anclaje, contraste.
- Cómo **combinar** rol específico + Few-Shot + CoT en un solo prompt profesional.

### Próxima clase

**Clase 9: Prompting Multimodal I — Imágenes.** Vamos a ver cómo describir, generar, editar y analizar imágenes con prompts — incluyendo un tema poco discutido: el sesgo de belleza de la IA, y cómo "romper el molde" para generar imágenes que representen personas y situaciones reales.

---

> **Recordá:** un prompt sin razonamiento explícito le pide a la IA que adivine el resultado final de un salto. Un prompt con CoT le pide que lo calcule, paso a paso, igual que lo harías vos en un papel.

---

### 📎 Nota para el docente

Esta clase se armó desde cero con el material del módulo 02 (Zero/Few-shot, CoT, ReAct) que trajiste, más la sección de psicología del contexto del módulo 03. Decisión clave: el ReAct se presenta **explícitamente como conceptual/simulado**, dejando claro que la versión real con Function Calling y un loop programado viene después en el bloque técnico — esto evita el mismo problema de secuencia que detectamos en la Clase 8 original (donde el ejemplo de agente usaba function calling antes de que existiera esa clase). La sección 5 (combinar todo) funciona como repaso integrador de la Clase 7 + 8 juntas, útil como cierre de las dos primeras clases del bloque de prompting profesional.
