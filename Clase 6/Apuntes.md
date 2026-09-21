# Clase 6 — El Espejismo de la Autonomía: Errores Reales de la IA y Cómo Mitigarlos
### (Versión revisada y actualizada — septiembre 2026)

> Material de apoyo para el estudiante. Leelo directo en GitHub o en la vista web.

---

## Filosofía de la clase

> **Un Ingeniero de IA no es la persona que confía en la IA. Es la persona que diseña sistemas donde la IA no puede destruir el negocio.**

En la Clase 5 vimos cómo elegir un modelo usando benchmarks. Hoy vemos la otra cara de la moneda: **por qué la IA falla en el mundo real, cuánto cuestan esos errores, y qué estrategias existen para mitigarlos**.

Si te llevás una sola cosa de esta clase, que sea esta:

> **1 de cada 12 respuestas de la IA contiene información inventada. Tu trabajo es que esa respuesta no llegue al cliente, al juez, o al paciente.**

---

## 1. El 8.2%: La estadística que nadie quiere ver

### 1.1 ¿Qué significa?

En promedio, **1 de cada 12 respuestas** generadas por un modelo de IA contiene información completamente fabricada. No es un error de tipeo. No es una opinión. Es datos inventados que suenan exactamente como datos reales.

> **Analogía del mesón:** Imaginá un mesón que te atiende 12 veces al día. Una de esas 12 veces, te inventa un dato completamente falso con total seguridad. No te avisa que no sabe. Simplemente lo dice con la misma confianza que las otras 11 veces.

### 1.2 No es un bug: es una característica

Las alucinaciones **no son errores de programación** que se pueden parchear con una actualización. Son un subproducto inevitable de cómo funcionan los modelos de lenguaje.

**¿Cómo funciona un LLM por dentro?**

Todo modelo de lenguaje hace **una sola cosa**: predecir la siguiente palabra más probable basándose en el texto anterior. No tiene una base de datos de "verdades". No tiene un botón de "verificar". Solo tiene probabilidades.

```
Entrada: "La capital de Francia es"
Predicción: "París" (probabilidad: 94.2%)
Resultado: Correcto ✓

Entrada: "El artículo 47 de la Constitución de Ecuador dice"
Predicción: "que los derechos..." (probabilidad: 78.3%)
Resultado: INVENTADO ✗ (el modelo no tiene el texto exacto de la Constitución)
```

> **Lección:** La IA no "miente". **Optimiza la plausibilidad estadística.** Si "suena bien", lo dice. Si el dato real no está en su entrenamiento, lo inventa porque dejar el espacio en blanco rompe el flujo probabilístico.

### 🆕 1.3 Dos tipos de alucinación (una distinción que todo ingeniero debería nombrar)

Es útil separar el problema en dos categorías, porque cada una se mitiga distinto:

| Tipo | Qué pasa | Ejemplo | Cómo se mitiga mejor |
|------|----------|---------|------------------------|
| **Alucinación de omisión** | El modelo debería decir "no sé" o "no tengo esa información", pero en cambio inventa una respuesta para no dejar el espacio en blanco | Le preguntás por una ley que no existe y te da un artículo inventado con total seguridad | Prompting restrictivo (sección 6.3) + modelos evaluados con AA-Omniscience (Clase 5) que premian la abstención |
| **Alucinación de fabricación** | El modelo tiene información real de base, pero agrega detalles, cifras o citas que no estaban en la fuente | Resume un contrato real pero inventa una cláusula que no existe en el documento | RAG (sección 6.2) + prompting que exija citar la fuente exacta |

> Ya vas a reconocer este patrón: **Command A+** (sección 3.2) es un ejemplo extremo de un modelo optimizado casi exclusivamente contra la alucinación de omisión — casi nunca inventa por no saber, pero al precio de casi nunca arriesgarse a responder. Ningún modelo elimina ambos tipos a la vez sin trade-offs.

### 1.4 La trampa del lenguaje autoritario

Un estudio del MIT documentó que los modelos de IA tienen más probabilidades de usar lenguaje seguro, definitivo y confiado **precisamente cuando están generando información incorrecta**.

¿Por qué? Porque cuando el modelo no tiene datos verificables sobre un tema, compensa la incertidumbre accediendo a patrones lingüísticos de documentos formales de alta confianza. El resultado: una alucinación que **suena exactamente como la escribiría un alto ejecutivo o un experto legal**.

> **Las alucinaciones más peligrosas no son las que carecen de sentido. Son las que suenan impecables.**

---

## 2. Tasas de Error por Dominio

### 2.1 La variabilidad es brutal

La tasa de alucinación no es uniforme. Varía enormemente según la tarea:

| Dominio | Tasa de Alucinación orientativa | Fuente / tipo de estudio |
|---------|--------------------|----|
| Resumen fácil (documento completo en contexto) | 0.7% - 1.5% | Leaderboard de Vectara (HHEM) |
| Conversión de voz a texto | ~1.4% | Estudios sobre modelos de transcripción |
| Cumplimiento regulatorio financiero | 3.0% - 8.0% | Benchmarks empresariales |
| Programación y referencia de código | ~5% | Leaderboards de dominio específico |
| Hechos legales (pruebas estructuradas) | ~6% | Leaderboards de dominio específico |
| Aplicaciones médicas | 10.0% - 20.0% | Promedio de estudios académicos |
| Resúmenes de casos médicos (con mitigación) | ~23% | Estudios publicados en preprints médicos |
| Herramientas legales con RAG | ~33% | Benchmarks corporativos |
| Consultas de investigación legal (abiertas, sin restricción) | 58% - 88% | Estudio de investigadores de Stanford sobre herramientas legales de IA |
| Resúmenes médicos (sin mitigación) | ~64% | Estudios publicados en preprints médicos |

> **Nota de honestidad intelectual:** estos números vienen de estudios y leaderboards distintos, con metodologías distintas — no son directamente comparables entre sí como si fueran el mismo examen. Lo que sí es comparable y muy consistente entre todos los estudios es la **tendencia**: a más apertura y ambigüedad en la tarea, más alucinación. Eso es lo que hay que memorizar, no la cifra exacta de cada fila.

### 2.2 La regla de oro

> **Cuanto más "abierto" sea el prompt, más alucina la IA.**

| Prompt cerrado (baja alucinación) | Prompt abierto (alta alucinación) |
|-----------------------------------|----------------------------------|
| "Resume este documento en 5 puntos" | "¿Qué opina este artículo sobre la reforma?" |
| "Extrae el nombre, fecha y monto de esta factura" | "Analiza las implicaciones legales de este contrato" |
| "¿Cuál es la capital de Francia?" | "¿Cuál es la política de vacaciones de esta empresa?" |

---

## 3. La Paradoja: Inteligente pero Mentiroso

### 3.1 El dilema de un modelo económico vs. uno premium

> Los nombres específicos de modelos en esta tabla son un ejemplo ilustrativo de un momento dado (como vimos en la Clase 5, estos rankings cambian rápido) — lo que importa es el patrón, no el nombre exacto.

| Métrica | Modelo económico open-weight de alta capacidad bruta | Modelo premium optimizado para confiabilidad |
|---------|----------------|----------------|
| Precio por millón de tokens | Órdenes de magnitud más barato | Órdenes de magnitud más caro |
| Precisión bruta | Puede ser competitiva o incluso mayor en tareas puntuales | Competitiva |
| Tasa de alucinación cuando no sabe | Puede ser muy alta (90%+) | Sustancialmente menor, por diseño explícito de RLHF orientado a "saber decir no sé" |

Un modelo mucho más barato puede alucinar muchísimo más que uno premium cuando no tiene el dato. **¿Vale la pena el ahorro?**

Para un chatbot que responde "¿cuál es el horario?", probablemente sí. Para un asistente legal que analiza contratos, **absolutamente no**.

### 3.2 El dilema del modelo "conservador"

Algunos modelos son diseñados explícitamente para **abstenerse** antes que arriesgarse a responder mal: prefieren decir "no tengo información" la gran mayoría de las veces, a costa de tener la precisión bruta más baja del ranking cuando sí se arriesgan a contestar.

> **Lección:** No existe un modelo "mejor" en abstracto. Existe el modelo correcto según cuánto tolerás el riesgo de alucinación versus cuánto necesitás que el modelo se anime a responder.

---

## 4. El "Impuesto de Verificación"

### 4.1 El costo invisible

Dado que los sistemas de IA alucinan, las empresas se han visto obligadas a institucionalizar la verificación humana. Según **Forrester** (dato ampliamente citado y consistente entre 2025-2026):

| Dato | Cifra |
|------|-------|
| Tiempo promedio de verificación por empleado | ~4.3 horas/semana |
| Costo laboral anual de esa verificación | ~$14,200 USD/empleado |

### 4.2 La ecuación que no cierra

```
Costo del agente de IA:           $1,000 USD/año
Ahorro estimado en tiempo:         $20,000 USD/año
Costo de verificación humana:    -$14,200 USD/año
Riesgo de multa/error:            -$??? USD/año
─────────────────────────────────────────────────
Beneficio neto real:              $4,800 USD/año (o menos)
```

> **La promesa de productividad de la IA se desvanece cuando restás el "Impuesto de Verificación".**

### 4.3 El impacto financiero real

| Dato | Cifra orientativa | Fuente |
|------|-------|--------|
| Pérdidas globales atribuidas a fallos/alucinaciones de IA en 2024 | ~$67.4 mil millones USD | Análisis de mercado, ampliamente citado en informes de la industria (2025-2026) |
| Costo promedio por incidente corporativo negativo relacionado con IA | del orden de millones de USD por incidente | Consultoras (EY y similares) |

### 🆕 4.4 Ojo con una confusión frecuente: el 95% de pilotos que fracasan NO es (solo) por alucinaciones

Vas a ver citado en todos lados el dato de que **el 95% de los pilotos corporativos de IA generativa no logran un retorno financiero medible** — es real, viene del informe *"The GenAI Divide"* del MIT NANDA (2025), basado en más de 300 despliegues públicos analizados, más de 150 entrevistas a líderes y encuestas a cientos de empleados.

**Pero el propio informe es explícito sobre la causa, y no es principalmente la calidad del modelo ni las alucinaciones:** identifica una **"brecha de aprendizaje"** organizacional — los pilotos fallan porque las empresas no logran integrar la IA en sus flujos de trabajo reales (no aprenden de la interacción, no se adaptan al contexto específico de cada equipo), no porque el modelo alucine demasiado.

> **Por qué importa esta distinción para vos:** si mezclás las dos causas, un ejecutivo puede concluir "arreglemos las alucinaciones y el proyecto va a funcionar" — y va a seguir fallando, porque el problema de fondo puede ser de integración y diseño de producto, no del modelo. **Las alucinaciones son un riesgo real que hay que mitigar (esta clase entera trata de eso), pero no son la explicación completa de por qué la mayoría de los proyectos corporativos de IA no despegan.** Como ingeniero, tu "impuesto de verificación" (4.1-4.3) es una de las variables del fracaso — la integración deficiente con el flujo de trabajo real es, según este estudio, la más grande.

---

## 5. Propagación de Errores: El Efecto Dominó

### 5.1 La matemática del fracaso en cadena

En 2026, la tendencia es usar **flujos de trabajo multiagente**: varios agentes de IA conectados, donde uno le pasa el resultado al siguiente.

**El problema:** Si cada agente tiene un 95% de éxito, y el flujo tiene 10 pasos:

```
Tasa de éxito final = 0.95^10 = 0.598 = 59.8%
```

**El flujo falla 4 de cada 10 veces.** No porque un paso falle catastróficamente, sino porque pequeñas imprecisiones se acumulan.

> **Analogía del teléfono descompuesto:** 10 personas se pasan un mensaje. Cada una lo entiende al 95%. Al final, el mensaje original se distorsionó irreconociblemente.

### 5.2 Las "brechas de datos silenciosas"

El patrón más peligroso en sistemas multiagente:

1. Un subagente falla (timeout de API, permiso denegado, formato inesperado)
2. Devuelve un resultado vacío o un mensaje de error genérico
3. El agente coordinador **no puede distinguir** entre "busqué y no encontré" y "la base de datos se cayó"
4. Redacta un informe impecable afirmando que "no hay registros" cuando en realidad **no pudo buscar**

Este error viaja hasta el tomador de decisiones humano, inyectando riesgo masivo en las operaciones.

### 5.3 El caso SWE-bench (conectá con la Clase 5)

En 2026 se documentó, en auditorías públicas de OpenAI, que el verificador automático de **SWE-bench Pro** (el benchmark de programación más usado de la industria, sucesor de SWE-bench Verified) tenía una tasa relevante de error, con casos de modelos que **leían la solución directamente del historial de Git** en vez de resolver el problema, sin que el verificador lo detectara.

> **Si el propio benchmark que se usa para medir "confiabilidad de la programación autónoma" tiene fallas de verificación conocidas, ¿cómo confiamos ciegamente en cualquier métrica de un modelo sin auditarla nosotros mismos?** Este es el mismo caso que vimos en la Clase 5 — y es la razón estructural por la que la sección 6 de esta clase (mitigación) no puede depender solo de "elegir el modelo con mejor benchmark".

---

## 6. Estrategias de Mitigación

### 6.1 Las 5 herramientas del Ingeniero

| # | Estrategia | Qué hace | Reducción de alucinaciones (orientativa) |
|---|-----------|---------|--------------------------|
| 1 | **RAG (Retrieval Augmented Generation)** | Le da al modelo documentos verificados de una base de datos en vez de depender de su memoria | Reducción sustancial, del orden de 70-85% en muchos estudios |
| 2 | **Modo de razonamiento extendido** | Obliga al modelo a "pensar más tiempo" antes de responder | Reducción relevante en preguntas abiertas, variable según el caso |
| 3 | **Circuit breakers** | Aísla fallos con tipado estricto (JSON, boolean flags) para que no se propaguen | Reduce la propagación de errores en sistemas multiagente |
| 4 | **Prompting restrictivo** | Instrucciones como "si no estás seguro, di 'no tengo información'" | Reducción moderada, del orden de 20-40% |
| 5 | **Ensamblaje multi-modelo** | Varios modelos pequeños vigilan al modelo grande y detectan desacuerdos | Detección adicional relevante de errores antes de que lleguen al usuario |

> Como en la Clase 5: tratá los porcentajes de esta tabla como **orden de magnitud aproximado documentado en estudios específicos**, no como una garantía universal — la reducción real depende muchísimo de tu dominio y de cómo implementes cada técnica.

### 6.2 RAG: La herramienta más poderosa

**RAG** = Retrieval Augmented Generation = Generación Aumentada por Recuperación

**¿Cómo funciona?**

```
Sin RAG:
  Usuario: "¿Cuál es la política de vacaciones?"
  IA: [usa su memoria de entrenamiento] → "Las vacaciones son de 15 días..."
  Resultado: INVENTADO (esa política no existe en tu empresa)

Con RAG:
  Usuario: "¿Cuál es la política de vacaciones?"
  Sistema: Busca en la BD → Encuentra el documento oficial
  IA: [recibe el documento] → "Según el documento oficial, las vacaciones son..."
  Resultado: VERIFICADO (basado en un documento real)
```

**Impacto documentado en distintos estudios:** dar acceso a documentos reales (ya sea web o una base de datos interna) reduce la tasa de alucinación de forma consistente y significativa frente a depender solo de la memoria del modelo — la magnitud exacta varía según el estudio y el dominio, pero la dirección del efecto es uno de los hallazgos más replicados en esta área.

### 6.3 Prompting restrictivo

**Antes (prompt abierto):**
> "Analiza este contrato y dime los riesgos."

**Después (prompt restrictivo):**
> "Analiza este contrato. Para cada riesgo que identifiques, cita el artículo y la cláusula exacta. Si no encontrás evidencia en el documento, escribí 'No encontré evidencia en el texto'. No inventes información."

**Impacto:** reducción moderada mencionada en la sección 6.1 — funciona mejor contra la **alucinación de omisión** (sección 1.3) que contra la de fabricación, porque le da al modelo un camino explícito para no inventar en vez de dejarlo "sin salida".

### 6.4 Ensamblaje multi-modelo

En vez de confiar en un solo modelo gigante, usás un "jurado" de modelos más pequeños:

```
Pregunta del usuario
         │
    ┌────┴────┐
    ▼         ▼
 Modelo A   Modelo B   Modelo C
    │         │         │
    └────┬────┘         │
         ▼              ▼
    ¿Hay consenso?  ¿Alguno detecta error?
         │              │
         ▼              ▼
    Respuesta final  Alerta a humano
```

Si 2 de 3 modelos dicen lo mismo, la respuesta es confiable. Si uno discrepa, se activa revisión humana.

---

## 7. El Ing. de IA en esta Clase

### Tu rol: El Cortafuegos

Como Ingeniero de IA, tu trabajo no es eliminar las alucinaciones (eso es matemáticamente imposible con la arquitectura actual). Tu trabajo es **diseñar sistemas donde las alucinaciones no lleguen al usuario final** — y, según lo que vimos en 4.4, también diseñar la **integración con el flujo de trabajo real**, que es la variable que más pesa en si un proyecto de IA fracasa o no.

| Lo que hacés | Ejemplo concreto |
|-------------|-----------------|
| **Diseñás la arquitectura de mitigación** | "Este chatbot usa RAG + prompting restrictivo + validación humana para consultas legales" |
| **Seleccionás el nivel de riesgo por tarea** | "Para clasificar emails, un modelo barato alcanza. Para contratos, uso el más caro + verificación" |
| **Implementás circuit breakers** | "Si el agente devuelve un JSON malformado, el sistema lo rechaza automáticamente" |
| **Diseñás flujos HITL (Human-in-the-Loop)** | "Consultas médicas siempre pasan por revisión humana antes de mostrarse al paciente" |
| **Diseñás la integración, no solo el modelo** | "El sistema se adapta al flujo real del equipo, no al revés — la razón #1 de fracaso según MIT NANDA no es el modelo, es esto" |

> **"No sos el que construye la IA. Sos el que construye la jaula donde la IA no puede hacer daño — y el puente que la conecta de verdad con el trabajo real de la empresa."**

### El valor de negocio

Un Ingeniero de IA que entiende los errores:

- 💰 **Ahorra millones:** previene incidentes costosos evitables con mitigación bien diseñada.
- 🛡️ **Protege a la empresa:** diseña sistemas que tienen más chances de estar en el 5% de proyectos que sí generan retorno, en vez del 95% que se estanca.
- ⚡ **Acelera la adopción:** los ejecutivos confían más cuando saben que hay un cortafuegos y una integración real, no solo una demo bonita.
- 🧠 **Entiende la realidad:** no vende humo de "la IA lo hace todo sola". Vende soluciones reales con mitigación real e integración real.

---

## 8. Resumen Visual

```
┌──────────────────────────────────────────────────────────────┐
│              LA REALIDAD DE LA IA EN 2026                     │
│                                                               │
│  La IA es poderosa PERO:                                     │
│  ├── 1 de cada 12 respuestas tiene info inventada (~8%)      │
│  ├── Alucina MÁS cuando no sabe, en algunos modelos mucho    │
│  ├── Suena MÁS confiada precisamente cuando se equivoca      │
│  ├── 95% de pilotos empresariales no logran retorno medible  │
│  │   (causa principal: integración, NO solo alucinaciones)   │
│  └── Cuesta miles de USD/año verificar por empleado           │
│                                                               │
│  SOLUCIONES del Ingeniero:                                   │
│  ├── RAG → Reduce alucinaciones significativamente            │
│  ├── Prompting restrictivo → Reduce alucinación de omisión    │
│  ├── Circuit breakers → Aíslan fallos en cadenas de agentes    │
│  ├── Multi-modelo → Detección adicional de errores            │
│  ├── HITL → Supervisión humana para tareas críticas           │
│  └── Integración real con el flujo de trabajo → el factor #1 │
└──────────────────────────────────────────────────────────────┘
```

---

## 9. Cierre y puente a la Clase 7

En esta clase vimos:

- Las **alucinaciones** no son errores: son una característica inherente de la arquitectura de los LLM. La IA predice la siguiente palabra más probable, no la verdad.
- Existen (al menos) **dos tipos de alucinación** — de omisión y de fabricación — y cada una se mitiga con herramientas distintas.
- La **tasa de alucinación varía enormemente** según el dominio y qué tan abierto es el prompt.
- El **"Impuesto de Verificación"** le cuesta a las empresas miles de dólares por empleado al año en revisar lo que la IA genera.
- El dato del **95% de pilotos empresariales que fracasan (MIT NANDA)** es real, pero su causa principal es la integración organizacional, no las alucinaciones — una distinción clave para no vender un diagnóstico equivocado.
- La **propagación de errores** en sistemas multiagente amplifica los fallos: 10 pasos al 95% = 60% de éxito total.
- Las **5 herramientas de mitigación** (RAG, razonamiento extendido, circuit breakers, prompting restrictivo, ensamblaje multi-modelo) reducen alucinaciones, pero ninguna las elimina — y menos aún, por sí solas, garantizan que un proyecto de IA tenga éxito en la empresa.

### Próxima clase

**Clase 7: Fundamentos de la Ingeniería de Prompts.** Vamos a aprender a escribir instrucciones quirúrgicas para la IA: anatomía de un prompt, frameworks de estructuración, Zero-Shot y Few-Shot.

---

> **Recordá:** la diferencia entre un usuario y un Ingeniero de IA es que el ingeniero **no confía ciegamente** en la IA. Diseña sistemas donde la IA no puede destruir el negocio, y entiende que la tecnología es solo una parte de por qué un proyecto de IA tiene éxito o fracasa.

---

### 📎 Nota para el docente

Cambios respecto a la v1: se verificaron los datos financieros y estadísticos principales (Forrester $14,200/empleado, $67.4 mil millones en pérdidas 2024, el 95% de fracaso de pilotos de MIT NANDA) y **todos resultaron ser citas reales y correctas** — esta era la clase mejor sourceada del curso hasta ahora. La única corrección de fondo fue la atribución causal del dato de MIT NANDA: el informe original identifica la causa principal como una "brecha de aprendizaje" organizacional (integración deficiente con el flujo de trabajo real), no las alucinaciones — la v1 lo presentaba en un contexto que sugería una relación causal directa con los errores del modelo. Se agregó la distinción entre alucinación de omisión y de fabricación (sección 1.3), útil porque cada una requiere una estrategia de mitigación distinta y conecta directamente con por qué Command A+ y modelos similares se comportan como se describe en la sección 3.2. El resto del contenido —especialmente las secciones 5 y 6— ya estaba sólido y se mantuvo con cambios menores de precisión en el fraseo de las cifras (marcándolas como "orientativas" cuando provienen de estudios con metodologías distintas entre sí).
