# Clase 13 — De Prompts Artesanales a Sistemas: Salidas, Módulos, Plantillas y Cadenas
### (Septiembre 2026)

> Material de apoyo para el estudiante. Leelo directo en GitHub o en la vista web.
> **Nota de ubicación:** esta clase es el puente entre todo lo que aprendiste de prompting (Clases 7-12) y lo que viene después en el taller (Function Calling, Agentes, RAG). Acá dejamos de escribir prompts "a mano, uno por vez" y empezamos a pensarlos como **piezas de un sistema** — exactamente lo que necesitás para que tu asistente de la Clase 11 deje de ser un experimento y se vuelva una herramienta de verdad confiable.

---

## Filosofía de la clase

> **Hasta ahora escribiste prompts como quien escribe una carta: de principio a fin, de una sola vez. Un Ingeniero de IA los escribe como quien construye software: en piezas, reutilizables, versionadas, con un formato de salida predecible.**

Si tu asistente de cotizaciones (Clase 11) alguna vez le da una respuesta distinta a dos clientes que preguntaron exactamente lo mismo, o si no podés conectar su respuesta a tu sistema de facturación porque viene en texto libre e impredecible, esta clase resuelve ese problema.

Si te llevás una sola cosa de esta clase, que sea esta:

> **Un prompt que un humano puede leer no es lo mismo que un prompt que un programa puede usar. Diseñar para ambos es la diferencia entre un experimento y un sistema.**

---

## 1. Salidas: No Solo Importa Qué se Pide, Importa Cómo se Entrega

### 1.1 El problema de no especificar la salida

Pedirle a la IA "Analizá este documento" deja demasiadas preguntas sin responder: ¿qué información devuelve? ¿en qué orden? ¿cuánto escribe? ¿cómo representa un dato que no encontró?

```
QUÉ HACER        → Instrucción
CON QUÉ INFO      → Contexto
BAJO QUÉ COND.    → Restricciones
CÓMO ENTREGARLO   → Salida
```

**La salida no es un detalle estético. Es parte del diseño del sistema.**

### 1.2 Salida para humanos vs. salida para máquinas

| | Salida para humanos | Salida para máquinas |
|---|---|---|
| **Busca** | Comprensión, legibilidad, explicación | Estructura predecible, validable |
| **Ejemplo** | "El análisis detectó tres anomalías importantes: 1. Registros duplicados..." | `{"total_hallazgos": 3, "riesgo": "alto", "hallazgos": [...]}` |
| **La usa** | Una persona leyendo | Un programa que hace `respuesta["riesgo"]` |

> **Pensalo con el asistente de cotizaciones de la Clase 11:** si le pedís "dame la cotización" y te devuelve un párrafo lindo pero distinto cada vez, no podés conectarlo automáticamente a tu sistema de facturación. Si le pedís que devuelva `{"cliente": "...", "total": 1500.50, "items": [...]}`, cualquier programa (incluso una hoja de cálculo con una fórmula simple) puede leerlo.

### 1.3 Formatos de salida más comunes

| Formato | Uso frecuente |
|---|---|
| Texto | Conversación directa con una persona |
| Markdown | Documentación, informes para leer |
| Lista / Tabla | Comparaciones, elementos simples |
| **JSON** | Aplicaciones, APIs, conectar con otros sistemas |
| CSV | Datos tabulares, para abrir en Excel |
| YAML | Configuración |

No existe un formato "mejor" en abstracto — depende de quién o qué va a consumir esa respuesta.

### 1.4 JSON: el idioma universal entre sistemas

**JSON** (JavaScript Object Notation) es el formato más usado para que un sistema le "hable" a otro. Representa información con una estructura fija y predecible:

```json
{
  "cliente": "Empresa ABC",
  "total": 1500.50,
  "moneda": "USD",
  "aprobado": true,
  "items": ["silla", "mesa", "lámpara"]
}
```

### 1.5 ⚠️ Estructura no significa corrección

**Este es el punto más importante de toda la sección.** Que una respuesta venga en JSON perfecto **no significa que sea correcta**.

```json
{
  "riesgo": "bajo"
}
```

Puede estar perfectamente formateado y, al mismo tiempo, **completamente equivocado** en su contenido. Necesitás pensar en tres capas de validación distintas:

```
VALIDACIÓN SINTÁCTICA   → ¿Es JSON válido, sin errores de formato?
VALIDACIÓN SEMÁNTICA    → ¿Los valores tienen sentido? (¿"total" es un número, no texto?)
VALIDACIÓN DE NEGOCIO   → ¿El resultado es correcto para TU caso? (¿el monto realmente es ese?)
```

> Conectá esto con la Clase 6: que la salida "se vea prolija" no reemplaza verificar que el contenido sea verdadero. Un JSON bien formado puede alucinar con la misma tranquilidad que un párrafo de texto libre.

### 1.6 Ejemplo aplicado — el asistente de cotizaciones de Carlos

**Sin especificar salida:**
> "Dame una cotización para 3 sillas y 1 mesa"
>
> *Resultado: un párrafo distinto cada vez, a veces con el total, a veces sin el IVA desglosado.*

**Con salida estructurada:**
```
Devolvé la cotización ÚNICAMENTE en este formato JSON:

{
  "cliente": "string",
  "items": [{"producto": "string", "cantidad": number, "precio_unitario": number}],
  "subtotal": number,
  "iva": number,
  "total": number
}

Si falta algún dato del cliente, usá null en ese campo, nunca inventes un valor.
```

---

## 2. Prompts Modulares: Dejar de Escribir Todo en un Solo Bloque

### 2.1 El problema del prompt monolítico

Hasta ahora, probablemente escribiste cada prompt como **un bloque único**: rol, objetivo, contexto, reglas, ejemplos y formato, todo mezclado en un solo texto. Funciona para tareas simples. Pero cuando tu asistente crece, aparecen problemas:

- Prompts cada vez más largos
- Instrucciones repetidas en varios lugares
- Si cambiás una regla, tenés que buscarla dentro de un texto enorme
- No podés reutilizar partes en otro asistente

### 2.2 La solución: pensar el prompt como piezas

```
PROMPT
   │
   ├── Rol
   ├── Objetivo
   ├── Contexto
   ├── Restricciones
   ├── Ejemplos
   └── Salida
```

Cada pieza se puede escribir, revisar y mejorar **por separado**, y después se ensamblan.

### 2.3 Ejemplo aplicado: tu asistente del negocio, modularizado

En vez de un único texto gigante, organizás tu asistente en piezas reutilizables:

```
mi_asistente/
├── rol.md              → "Sos el asistente de cotizaciones de [Negocio]..."
├── politica_precios.md → reglas de precios, descuentos, formas de pago
├── politica_no_inventar.md → "si no tenés el dato, decí 'no tengo esa información'"
├── ejemplos.md          → 2-3 cotizaciones reales como ejemplo (Few-Shot, Clase 7)
└── formato_salida.md    → el JSON exacto que debe devolver
```

> **Conexión directa con la Clase 8 (Skills del bloque técnico):** esto es, literalmente, la misma idea de "empaquetar instrucciones reutilizables" que vas a formalizar con código más adelante. Acá la estás aprendiendo primero con texto simple.

### 2.4 Por qué modularizar — 2 ventajas que vas a sentir enseguida

| Ventaja | Qué significa en la práctica |
|---|---|
| **Reutilización** | La "política de no inventar" que armaste para tu asistente de cotizaciones sirve también para un asistente de atención al cliente — no la reescribís de cero |
| **Mantenimiento** | Si cambian tus precios, editás solo `politica_precios.md`, sin tocar el resto del asistente |

### 2.5 Dos conceptos de software que te van a servir toda la vida

- **Cohesión:** cada módulo tiene UNA responsabilidad clara. El módulo de "política de precios" no debería tener mezclado el estilo de redacción.
- **Acoplamiento:** cuánto depende un módulo de otro. Si cambiar tu ejemplo de cotización obliga a reescribir también la política de precios, están demasiado enredados entre sí — eso es alto acoplamiento, y es justo lo que querés evitar.

---

## 3. Plantillas: La Estructura que se Repite, los Datos que Cambian

### 3.1 ¿Qué es una plantilla?

Una **plantilla** separa lo que siempre es igual de lo que cambia cada vez:

```
T = E + V

E = elementos estáticos (siempre iguales)
V = variables (cambian en cada uso)
```

### 3.2 Plantilla vs. prompt — la diferencia clave

| | Prompt concreto | Plantilla |
|---|---|---|
| Ejemplo | "Analizá este informe financiero y encontrá inconsistencias" | "Analizá este {TIPO_DOCUMENTO} y encontrá {TIPO_PROBLEMA}" |
| Sirve para | Una ejecución específica | Muchas ejecuciones distintas, reusando la misma estructura |

### 3.3 Plantilla aplicada al negocio de Carlos

```
Eres el asistente de {NEGOCIO}.

Analizá la siguiente {TIPO_DOCUMENTO}: {DOCUMENTO}

Extraé: proveedor, fecha, monto, conceptos.

Si falta algún dato, indicá "no encontrado" — nunca lo inventes.

Devolvé el resultado en formato JSON.
```

Con esta única plantilla, Carlos puede procesar facturas, recibos, o notas de crédito — solo cambia qué variable le pasa (`TIPO_DOCUMENTO` y `DOCUMENTO`), la estructura del prompt queda igual siempre.

### 3.4 Variables no son solo texto

Una variable puede ser un número, una lista, o hasta un documento entero (`{DOCUMENTO}`, `{IDIOMA}`, `{PRODUCTOS}`). Pensar en el **tipo de dato** de cada variable es lo que después te va a permitir conectar tu asistente con una hoja de cálculo o un sistema real, sin sorpresas.

---

## 4. Metaprompting: Usar la IA para Mejorar tus Propios Prompts

### 4.1 La idea central

**Metaprompting** es pedirle a la IA que trabaje, no sobre tu documento o tu pregunta, sino **sobre tu propio prompt** — que lo analice, lo mejore o genere uno nuevo.

```
PROMPTING NORMAL:        Usuario → Prompt → Modelo → Resultado
METAPROMPTING:           Usuario → Metaprompt → Modelo → Prompt MEJORADO → Modelo → Resultado
```

### 4.2 Ejemplo práctico: pedile a la IA que audite tu propio asistente

```
Analizá el siguiente prompt que uso para mi asistente de cotizaciones.

Evaluá:
- ¿Hay ambigüedades?
- ¿Hay instrucciones que se contradicen?
- ¿El formato de salida está bien definido?
- ¿Qué pasa si falta un dato — está contemplado?

<PROMPT>
[pegá acá tu prompt actual]
</PROMPT>

No lo modifiques todavía. Primero dame el diagnóstico.
```

### 4.3 La regla de oro del metaprompting: no cambiar el objetivo

Si le pedís "mejorá este prompt", el riesgo es que la IA termine **cambiando lo que el prompt hace**, no solo cómo lo hace. Por eso siempre agregá la restricción explícita:

```
Mejorá este prompt. NO CAMBIES SU OBJETIVO ORIGINAL.
Reducí ambigüedades. Eliminá redundancias.
```

> **Ejercicio sugerido:** tomá el prompt de tu propio asistente (Clase 11) y pedile a la IA, con el prompt de la sección 4.2, que lo audite. Es casi seguro que encuentre algo que no habías notado — especialmente en el manejo de "¿qué pasa si falta un dato?".

---

## 5. Prompt Chaining: Dividir una Tarea Grande en Pasos Conectados

### 5.1 El problema de pedir todo en un solo prompt

```
Analizá esta factura. Extraé los datos, comprobá los cálculos,
detectá anomalías, evaluá el riesgo, y generá un informe.
```

Todo en un solo paso. Si algo sale mal, **no sabés en qué parte falló**.

### 5.2 La solución: una cadena de prompts

```
Factura → [Extracción] → Datos → [Validación] → [Detección de anomalías] →
→ [Evaluación de riesgo] → [Informe final]
```

Cada etapa tiene **una sola responsabilidad**, y la salida de una es la entrada de la siguiente.

### 5.3 Por qué esto importa tanto: localizar el error

```
Extracción       ✓
Validación       ✓
Anomalías        ✗  ← acá está el problema
Riesgo           — (no llegó a ejecutarse)
Informe          —
```

Con un solo prompt gigante, nunca sabrías en qué parte del proceso se originó el error. Con una cadena, lo ves exacto.

### 5.4 Ejemplo aplicado: la cadena de facturas de Carlos (conectando con la Clase de Auditoría de Procesos)

¿Te acordás del caso de Carlos el contador, que digitaba facturas a mano? Esto es, literalmente, cómo se vería su proceso resuelto con Prompt Chaining:

```
Etapa 1 — Extracción:
"Extraé proveedor, fecha, monto y conceptos de esta factura.
No agregues información que no esté en el documento."
→ Salida: {"proveedor": "...", "fecha": "...", "monto": ...}

Etapa 2 — Validación:
"Verificá que el monto coincida con la suma de los conceptos."
→ Salida: {"valido": true/false, "diferencia": 0}

Etapa 3 — Clasificación de riesgo:
"Si el proveedor es nuevo o el monto es inusual, marcá riesgo alto."
→ Salida: {"riesgo": "bajo/medio/alto"}

Etapa 4 — Informe:
"Generá un resumen de una línea para el equipo contable."
→ Salida final para un humano
```

> Fijate el patrón: las **primeras 3 etapas producen JSON** (salida para máquina — Carlos no las lee, las procesa su sistema), y **recién la última etapa produce texto para humano**. Esto conecta todo lo que vimos en esta clase: salidas (sección 1), módulos reutilizables (sección 2), la plantilla de cada etapa (sección 3) — todo armado como una cadena (sección 5).

### 5.5 El contrato entre etapas

No alcanza con decir "la salida de la Etapa 1 pasa a la Etapa 2" — hay que **definir exactamente qué estructura** tiene esa salida, para que la etapa siguiente sepa qué esperar. Ese acuerdo de formato es el "contrato" entre etapas.

### 5.6 Validación intermedia: no asumas que cada etapa salió bien

```
Prompt 1 → Salida → ¿Es válida?
                      ├── Sí → continúa a Prompt 2
                      └── No → se corrige o se reintenta, no sigue adelante con datos malos
```

> Esto es exactamente el mismo principio de los **circuit breakers** que vimos en la Clase 6 — no dejar que un error se propague en cadena sin que nadie lo note.

---

## 6. El Ingeniero de IA en esta Clase

| Habilidad | Qué significa |
|---|---|
| Diseña la salida, no solo la instrucción | Sabe si necesita texto para humano o JSON para sistema, y lo especifica |
| No confunde formato con corrección | Verifica el contenido aunque el JSON esté perfecto |
| Modulariza en vez de escribir todo junto | Sus prompts se mantienen y reutilizan sin reescribir de cero |
| Usa plantillas para no repetir trabajo | Una estructura, muchos casos de uso |
| Usa metaprompting para auditar sus propios prompts | No confía solo en su propio criterio — le pide a la IA que revise su trabajo |
| Divide tareas grandes en cadenas con contrato claro | Puede localizar exactamente dónde falló el proceso |

---

## 7. Resumen Visual

```
┌──────────────────────────────────────────────────────────────┐
│       DE PROMPT ARTESANAL A SISTEMA DE PROMPTS                │
│                                                                │
│  1. SALIDA: ¿para humano o para máquina? ¿qué formato?        │
│                                                                │
│  2. MÓDULOS: rol, reglas, ejemplos — piezas separadas,         │
│     no un bloque único                                        │
│                                                                │
│  3. PLANTILLAS: estructura fija + variables que cambian        │
│                                                                │
│  4. METAPROMPTING: usá la IA para auditar tus propios prompts  │
│                                                                │
│  5. PROMPT CHAINING: tareas grandes → etapas pequeñas,         │
│     cada una con su contrato de entrada/salida                │
└──────────────────────────────────────────────────────────────┘
```

---

## Cierre

### Lo que aprendimos hoy

1. La **salida** es parte del diseño, no un detalle — y especificarla (sobre todo en JSON) es lo que te permite conectar tu asistente con sistemas reales.
2. **Estructura no es lo mismo que corrección.** Un JSON perfecto puede tener datos falsos adentro.
3. Modularizar un prompt (rol, reglas, ejemplos, salida como piezas separadas) lo hace mantenible y reutilizable.
4. Una **plantilla** separa lo fijo de lo variable, para no reescribir la misma estructura cada vez.
5. **Metaprompting** es usar la IA para auditar y mejorar tus propios prompts — siempre cuidando no cambiarles el objetivo.
6. **Prompt Chaining** divide una tarea compleja en etapas con responsabilidad única, con contratos claros entre cada una, para poder localizar errores.

### Próxima clase

Con esto ya tenés todo lo necesario para dar el salto hacia **Function Calling**: un prompt que devuelve JSON estructurado (sección 1) es exactamente lo que un programa necesita para decidir qué función ejecutar. El bloque de Agentes empieza acá.

---

> **Recordá:** la diferencia entre un prompt que funciona una vez y un sistema que funciona siempre es el diseño de la salida, la modularidad, y saber dónde, exactamente, puede fallar cada paso.

---

### 📎 Nota para el docente

Esta clase sintetiza los 5 módulos técnicos que trajiste (Salidas, Prompt Modular, Plantillas, Metaprompting, Prompt Chaining), reorganizados en una sola sesión con un hilo conductor común: el asistente de cotizaciones de la Clase 11 y el caso de Carlos el contador de la clase de auditoría de procesos, para que el contenido técnico no se sienta desconectado del resto del taller. Se simplificó el lenguaje de ingeniería de software del material original (cohesión, acoplamiento, contratos) sin perder los conceptos, y se recortaron partes muy extensas del original (ej. toda la sección de "tipos de metaprompt" se condensó a lo esencial: generar, mejorar, auditar). Si el grupo tiene mucho interés técnico, esta clase se puede partir en dos (13a: Salidas + Modularidad + Plantillas: 13b: Metaprompting + Prompt Chaining) sin perder continuidad, siguiendo el mismo criterio de partición que usamos en clases anteriores.
