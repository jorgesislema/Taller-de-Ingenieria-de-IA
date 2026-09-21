# Clase — Auditoría de Procesos: Qué Automatizar, Cómo Preguntarlo, y Cuándo Usar IA (y Cuándo No)

> Material de apoyo para el estudiante. Leelo directo en GitHub o en la vista web.


---

## Filosofía de la clase

> **El error más caro de un Ingeniero de IA no es programar mal. Es automatizar el proceso equivocado, con la herramienta equivocada, porque nunca hizo las preguntas correctas antes de abrir VSCode.**

Hasta ahora en el curso aprendimos a construir con IA: prompts, agentes, RAG, memoria. Hoy vamos a un paso **anterior** a todo eso, que casi ningún curso técnico enseña: **cómo averiguar qué automatizar antes de escribir una sola línea de código o un solo prompt.**

Un Ingeniero de IA que no sabe auditar procesos termina construyendo soluciones técnicamente impecables para problemas que nadie tenía, mientras el problema real —el que le costaba plata y horas a la empresa— sigue sin resolverse porque nadie preguntó bien.

> **La IA no es la primera pregunta. La primera pregunta es: ¿qué proceso duele, y por qué?**

---

## 1. Antes de Hablar con Nadie: Prepará el Terreno

### 1.1 Conseguí el mapa antes de entrar

Antes de la primera entrevista, conseguí el organigrama y el mapa de procesos de alto nivel con dirección o gerencia. Preguntales:

- ¿Cuáles son los 3-5 procesos que más dolor de cabeza dan hoy?
- ¿Dónde se pierden más horas-persona o dinero?
- ¿Qué expectativa tienen de la automatización?

> **Esta última pregunta es una trampa que tenés que detectar vos, no ellos.** Te dice si la dirección espera "reemplazar gente" — y si es así, tenés que saberlo antes de entrar a entrevistar a nadie (ver sección 4).

### 1.2 Comunicá el propósito ANTES de las entrevistas

Un correo o reunión de la dirección explicando **"vamos a mapear procesos para reducir trabajo repetitivo, no para recortar personal"** reduce muchísimo la resistencia.

> **Si esto no se dice explícitamente, la gente asume lo peor y te va a mentir u ocultar información en las entrevistas.** No es paranoia de tu parte — es una reacción humana completamente razonable ante alguien de afuera preguntando "¿cómo hacés tu trabajo?" sin contexto.

#### 📄 Plantilla: correo que envía la Gerencia (no vos)

> **Asunto:** Proyecto de mejora de procesos — próximas semanas
>
> Equipo,
>
> En las próximas semanas vamos a trabajar con [Tu Nombre / Tu Empresa] en un proyecto para revisar cómo funcionan nuestros procesos internos, especialmente en las áreas administrativa y contable.
>
> El objetivo es identificar tareas repetitivas o manuales que nos están quitando tiempo, para poder automatizarlas y que el equipo se enfoque en trabajo de mayor valor (análisis, atención a clientes, revisión de excepciones), en lugar de digitar o transcribir datos.
>
> **Esto no es un proyecto de reducción de personal. Es una inversión para que el equipo trabaje mejor, no para reemplazar a nadie.**
>
> Durante las próximas dos semanas, [Tu Nombre] va a agendar entrevistas individuales de 30-40 minutos con cada persona del área. Les pido que sean abiertos y honestos sobre cómo hacen su trabajo realmente — incluyendo esos "trucos" o formas alternativas que usan cuando el sistema oficial no alcanza. Esa información es exactamente lo que necesitamos para hacer un buen diagnóstico.
>
> Cualquier duda, estoy disponible.
>
> Saludos, [Nombre del gerente/dueño]

**Por qué funciona:** nombra explícitamente el miedo ("no es para reemplazar a nadie"), da un marco positivo (enfocarse en trabajo de valor), y legitima ante el equipo que hablar de sus atajos informales es seguro y deseado.

---

## 2. La Entrevista por Área: Estructura de Preguntas

> **No preguntes "¿qué hacés?"** — la gente generaliza y omite lo tedioso. Una pregunta abierta genérica produce una respuesta abstracta e inútil. Necesitás una secuencia diseñada.

### 2.1 Bloque A — Mapeo del proceso real (no el oficial)

- "Caminame paso a paso por lo que hiciste ayer/esta semana en esta tarea"
- "¿Qué herramientas o sistemas usás para esto?" (Excel, correo, WhatsApp, ERP...)
- "¿Qué información necesitás antes de poder hacer este paso, y de dónde la sacás?"
- "¿A quién le entregás el resultado, y en qué formato?"

### 2.2 Bloque B — Detectar los cuellos de botella

- "¿Qué parte de tu trabajo es la más repetitiva o la que más tiempo consume sin aportar valor real?"
- **"¿Qué tarea harías con gusto que un sistema te quitara de encima?"** — esta pregunta es oro: revela lo tedioso sin amenazar a nadie.
- "¿Cuándo fue la última vez que algo se atrasó o salió mal en este proceso? ¿Por qué?"
- "¿Qué hacés cuando el sistema/proceso falla? ¿Tenés un 'truco' o workaround?" — acá aparecen los procesos informales que nadie documentó: minas de oro para automatizar.
- "Si te vas de vacaciones una semana, ¿quién hace esto y qué necesita saber?" / "¿Te pasó volver de vacaciones y encontrar desastres, o que a tu reemplazo le costó seguir el ritmo?" — detecta dependencia de una sola persona: riesgo y oportunidad a la vez.

### 2.3 Bloque C — Cuantificar (para priorizar después)

- "¿Cuántas veces al día/semana hacés esto?"
- "¿Cuánto tiempo te toma cada vez?"
- "¿Qué tan seguido hay errores humanos acá, y qué pasa cuando ocurren?"

> **Por qué este orden importa:** vas de lo cualitativo (Bloque A: cómo es el proceso) a lo emocional/tedioso (Bloque B: dónde duele) y recién al final a los números (Bloque C). Si empezás pidiendo números, la persona se pone a la defensiva o inventa cifras redondas. Si primero generás confianza contándole la historia de su día, los números salen más honestos.

---

## 3. Cómo Detectar Embudos Sin Que Te Los Digan Directamente

La gente rara vez dice "este paso es un embudo". Lo ves en señales indirectas:

| Señal que escuchás | Lo que realmente significa |
|---------------------|------------------------------|
| Palabras como "siempre", "toca esperar", "depende de" | Dependencias y cuellos de botella |
| Herramientas paralelas no oficiales (un Excel personal, notas en el celular) | El sistema oficial no cubre algo real |
| Tareas que se hacen "por si acaso" o "para tener respaldo" | Falta de confianza en el sistema, duplicación de esfuerzo |
| Silencio o risa nerviosa cuando preguntás "¿y si falla?" | Ahí hay un proceso frágil que nadie quiere admitir |
| Discrepancia entre lo que dice el jefe de área y lo que dice quien ejecuta la tarea | Casi siempre hay una verdad operativa distinta a la oficial — y ahí está |

---

## 4. El Miedo a Ser Reemplazado

> Esto es real, y si lo ignorás, la gente te sabotea — consciente o inconscientemente — dándote información incompleta.

### Tácticas para manejarlo con honestidad

1. **Nunca preguntes "¿qué de tu trabajo se puede automatizar?"** — suena a "¿qué parte de vos sobra?". En cambio: "¿qué te quita tiempo de hacer lo que realmente importa de tu rol?"
2. **Enmarcá la automatización como quitar lo tedioso, no la persona.** La mayoría de la gente odia el trabajo repetitivo — si les mostrás que van a poder enfocarse en algo con más criterio, cooperan.
3. **Sé honesto si sí va a haber reducción de personal.** No prometas lo que no podés garantizar. Si la empresa SÍ planea reducir headcount, es mejor que lo sepas de entrada (preguntáselo directamente a quien te contrató) para no generar falsas expectativas que después se te van a devolver como resentimiento.
4. **Entrevistá individualmente, no en grupo**, al menos la primera ronda. En grupo, la gente se cuida de decir lo que realmente pasa.

> **Nota ética para el Ingeniero de IA:** esta sección no es "técnica de manipulación", es honestidad estructurada. La diferencia entre generar confianza genuina y manipular es que vos, como consultor, tenés que saber la verdad primero (¿va a haber despidos o no?) y comunicarla con esa misma honestidad hacia el equipo — nunca prometer algo que no controlás.

---

## 5. El Otro Extremo: Que Quieran Automatizarlo "Todo"

Esto pasa mucho con dueños o gerentes entusiasmados. Señales de abuso de alcance:

- Piden automatizar procesos que cambian constantemente (alto costo de mantenimiento, bajo retorno).
- Quieren automatizar decisiones que requieren juicio humano o criterio legal/ético.
- No tienen el proceso ni siquiera estandarizado ("automaticemos el caos").

### Cómo poner límites profesionalmente

- **Priorizá con una matriz simple:** Volumen × Frecuencia × Estabilidad del proceso × Impacto económico. Lo que no está estandarizado, no se automatiza bien — primero se ordena, después se automatiza.
- Si un proceso cambia cada semana según el criterio de una persona, decíselo claro: "esto no está listo para automatizar, primero necesitamos definir reglas claras".
- **Cobrá o presupuestá por fases.** Esto naturalmente frena el "hacelo todo" porque cada fase tiene costo y tiempo visibles.
- **No automatices lo que no entendés al 100%.** Si el dueño del proceso no puede explicarte las excepciones, vos tampoco podés automatizarlas bien — vas a construir algo que se rompe con el primer caso raro.

---

## 6. El Entregable de la Auditoría

Al final necesitás, por cada proceso relevante:

1. Diagrama de flujo actual (*as-is*)
2. Tiempo y costo estimado actual
3. Puntos de fricción / errores frecuentes
4. Nivel de estandarización (¿hay reglas claras o depende del criterio de una persona?)
5. Priorización (impacto vs. esfuerzo de automatizar)
6. Riesgos (dependencia de una persona, resistencia detectada, excepciones no documentadas)

---

## 7. Caso Completo: Carlos, el Contador que Digitaba Facturas

> Esta transcripción es un ejemplo de cómo se ve, en la práctica, aplicar todo lo anterior en una entrevista real de 15-20 minutos.

**Contexto:** Carlos recibe facturas de proveedores por correo y WhatsApp, las imprime o las tiene en PDF, y pasa manualmente los datos (proveedor, monto, fecha, número de factura, conceptos) al sistema contable.

> **Vos:** Carlos, gracias por el tiempo. Esto no es una evaluación de desempeño, es para entender cómo funciona realmente tu día a día con las facturas, para ver dónde te podemos quitar carga de encima. ¿Te parece si empezamos por lo que hiciste ayer?
>
> **Carlos:** Sí, claro. Ayer me llegaron como 18 facturas. Algunas por correo, otras me las manda un proveedor por WhatsApp porque no tiene bien montado su sistema de facturación.
>
> **Vos:** Ok, contame el paso a paso desde que te llega esa factura hasta que queda registrada.
>
> **Carlos:** Primero las voy guardando en una carpeta en mi computador, las que llegan por WhatsApp las paso al PC. Luego, una por una, abro el sistema contable y voy digitando: nombre del proveedor, NIT, número de factura, fecha, cada uno de los ítems con su valor, el IVA... Si la factura tiene muchos ítems, eso me puede tomar quince, veinte minutos por factura.
>
> **Vos:** ¿Cuántas facturas manejás en promedio a la semana?
>
> **Carlos:** Uy, en temporada alta pueden ser 150, 200. En temporada baja unas 80.
>
> **Vos:** ¿Y qué pasa cuando te equivocás digitando algo?
>
> **Carlos:** *(risa nerviosa)* Pasa más de lo que quisiera, la verdad. Sobre todo con los números de factura o cuando hay muchos decimales. A veces no me doy cuenta hasta que el proveedor llama a reclamar porque no le cuadra el pago, o hasta el cierre de mes cuando no cuadran los libros.
>
> **Vos:** Cuando eso pasa, ¿qué hacés?
>
> **Carlos:** Toca revisar factura por factura contra el sistema, comparando a mano. Eso me puede tomar un día entero, dependiendo de qué tan grande sea el error.
>
> **Vos:** Interesante. Y de todo esto que me contás, si pudieras quitarte una sola tarea de encima, ¿cuál sería?
>
> **Carlos:** Sin duda la digitación. No es que no sepa hacerlo, es que es lo mismo todos los días y es donde más me equivoco, porque después de la factura quince ya uno no está tan atento.
>
> **Vos:** ¿Usás algún archivo o sistema aparte del oficial para llevar control de esto? ¿Un Excel, notas...?
>
> **Carlos:** Sí, tengo un Excel donde anoto qué facturas ya procesé y cuáles me faltan, porque el sistema contable no tiene una forma fácil de ver eso. También ahí anoto las que tienen algún problema, para no perder el hilo.
>
> **Vos:** Eso es justo el tipo de cosa que buscamos. Última pregunta: si te vas de vacaciones una semana, ¿quién hace esto y qué necesita saber?
>
> **Carlos:** Normalmente nadie más lo hace, se acumula hasta que vuelvo. Una vez lo intentó hacer alguien de otra área y se demoró el triple porque no conocía los proveedores ni sus formatos raros de factura.
>
> **Vos:** Última pregunta general: ¿hay algo que no te haya preguntado que debería saber sobre este proceso?
>
> **Carlos:** Sí — hay tres proveedores que mandan las facturas en un formato distinto cada vez, casi que a mano. Esas son las que más tiempo me quitan y las que más errores tienen.

### 7.1 Lo que se detecta en esta entrevista (así se anota en la ficha)

| Señal detectada | Lectura |
|-------------------|---------|
| 15-20 min por factura, hasta 200/semana | Alto volumen, tarea claramente automatizable (OCR + extracción de datos) |
| Errores por fatiga, descubiertos tarde | Riesgo financiero y de relación con proveedores — automatizar reduce el error humano |
| Excel paralelo no oficial | El sistema contable no cubre el seguimiento — hay que integrar esa función al nuevo flujo, no ignorarla |
| Nadie más puede hacer la tarea | Dependencia de una sola persona = riesgo operativo, y argumento fuerte para justificar el proyecto ante dirección |
| 3 proveedores con formato irregular | Excepción a resolver aparte — probablemente necesiten revisión manual asistida, no automatización 100% |
| Reacción positiva a "quitarte la digitación" | Sin resistencia — el miedo no está en perder el trabajo sino en seguir cometiendo errores. Buena entrada para presentar la solución |

---

## 8. El Punto Ciego: Cuando el Proceso a Auditar Es el Tuyo Propio

> Todo lo anterior asume que auditás a otra persona. Pero como Ingeniero de IA freelance o dueño de tu propio proceso, muchas veces el "cliente" sos vos mismo — y ahí aparece un problema distinto.

### 8.1 Por qué auditarte a vos mismo es más difícil, no más fácil

- **No te interrogás a vos mismo.** No hay nadie que te repregunte "¿y por qué hacés eso así?" — tu cerebro da la respuesta obvia y sigue de largo.
- **Normalizás tus propios atajos.** Lo que para un auditor externo sería "señal de alerta" (un Excel paralelo, un truco raro), para vos es simplemente "así lo hago yo", invisible por costumbre.
- **Subestimás el tiempo.** La memoria miente. Si te preguntás "¿cuánto me toma esto?" tendés a responder con la versión optimista, no con la real.
- **Ego y sesgo de confirmación.** Es más fácil ver el problema en el proceso de otro que admitir que el tuyo es ineficiente — sobre todo si llevás años haciéndolo así y te sentís "bueno" en eso.
- **No hay distancia temporal.** Vivís el proceso todos los días, así que no notás el patrón — como no notás el ruido de fondo constante.

### 8.2 Cómo resolverlo: reemplazá la introspección por evidencia

La clave es no confiar en tu memoria ni en tu opinión sobre vos mismo — usá registros externos y reglas mecánicas, igual que harías con otra persona.

1. **Llevá un log real por 5-7 días, no un resumen mental.** Cada vez que hagas una tarea repetitiva, anotá: hora de inicio, hora de fin, qué hiciste. No lo hagas "de memoria" al final del día — anotalo en el momento o usá un time-tracker (Toggl, o hasta un Excel abierto todo el día). Al final de la semana, los patrones saltan solos porque son datos, no percepción.
2. **Usá evidencia digital, no tu recuerdo.** Revisá tu historial: carpetas de descargas, historial del navegador, mensajes enviados, archivos modificados. Ahí está la verdad de lo que realmente hacés, no lo que creés que hacés.
3. **Aplicá la prueba del extraño.** Preguntate: "si alguien nuevo entrara a mi puesto mañana, ¿qué le parecería absurdo de cómo hago esto?"
4. **Pedí que alguien más te "entreviste" a vos.** Usá exactamente el mismo checklist de la sección 2, pero que otra persona te haga las preguntas en voz alta. Verbalizarlo ante alguien que no sabe nada saca cosas que jamás notarías escribiéndolas vos mismo.
5. **Reformulá las preguntas de forma incómoda.** En vez de "¿qué tarea harías con gusto que un sistema te quitara de encima?" (fácil de responder en automático), preguntate: "¿qué hice esta semana que sabía perfectamente que era una pérdida de tiempo mientras lo hacía?"
6. **Contá, no sientas.** Nunca uses "mucho / poco / rápido / lento" con vos mismo — son juicios que tu ego filtra. Usá solo números: cuántas veces, cuántos minutos, cuántos clics.
7. **Desconfiá de tu primera respuesta a "¿por qué lo hago así?"** Si tu respuesta es "porque siempre lo he hecho así" o "porque es más seguro", preguntate una segunda vez: "¿de verdad es más seguro, o simplemente es lo que conozco?"

---

## 9. Cómo Decidir: ¿IA o Código Puro?

> Esta es, probablemente, la decisión de ingeniería más importante de toda la clase — y la que más separa a un profesional de alguien que "usa IA porque está de moda".

### 9.1 La regla de oro

Antes de cualquier decisión, hacete esta pregunta única para **cada paso del proceso** (no para el proceso completo):

> **¿Esta tarea tiene reglas fijas y determinísticas, o requiere interpretar algo variable/ambiguo?**

| Tipo de tarea | Solución |
|----------------|----------|
| Reglas fijas ("si el monto > $500, requiere aprobación") | Código puro |
| Interpretación de algo variable (texto libre, imágenes, lenguaje natural, criterio) | Ahí sí entra la IA |

> La mayoría de los procesos administrativos tienen partes de ambos tipos — por eso lo más común y correcto es el **modelo combinado**, no "todo IA" ni "todo código".

### 9.2 Marco de decisión práctico

| Característica del proceso | Solución |
|-------------------------------|----------|
| Reglas claras, inputs estructurados (Excel, formularios, campos fijos) | Código / RPA puro (scripts, Zapier, Make, macros) |
| Datos numéricos, cálculos, validaciones matemáticas | Código puro — nunca uses IA para sumar o validar montos, es más lento, más caro y menos confiable que una fórmula |
| Texto libre, correos, documentos no estructurados, clasificación de intención | IA (extracción, clasificación, resumen) |
| Decisión que requiere "leer entre líneas" o contexto humano | IA, con supervisión humana en casos límite |
| Todo lo anterior en un mismo flujo (ej: llega una factura en PDF, se extraen datos, se valida contra reglas, se registra) | Combinado: IA para extraer/interpretar → código para validar/ejecutar |

### 9.3 Cinco preguntas por cada paso del proceso

No decidas "todo el proceso es de IA" o "todo es código" de una sola vez. Desglosá el proceso en pasos y decidí paso por paso:

1. **¿El input es estructurado o no estructurado?** Un campo de formulario = estructurado = código. Un PDF escaneado a mano o un correo redactado libremente = no estructurado = ahí puede entrar IA (OCR + extracción).
2. **¿La lógica se puede escribir como un "si esto, entonces esto"?** Si podés dibujar un diagrama de flujo con condiciones claras, es código. Si la respuesta depende de "depende del contexto", es candidato a IA.
3. **¿Qué tan tolerante es el proceso al error probabilístico?** La IA generativa se equivoca (alucina, interpreta mal — Clase 6). En procesos financieros, legales o de cumplimiento, la IA puede hacer el trabajo pesado de interpretación, pero **el código debe validar el resultado antes de ejecutar** — nunca dejes que la IA escriba directo a un sistema crítico sin una capa de verificación determinística.
4. **¿Necesitás explicabilidad y auditoría?** Si un regulador o auditor va a preguntar "¿por qué el sistema tomó esta decisión?", el código puro es más defendible. La IA es una caja más opaca — usala donde el costo de una explicación imperfecta es bajo.
5. **¿El volumen y el costo lo justifican?** Llamar a un modelo de IA cuesta dinero y latencia por cada ejecución (Clase 4). Si tenés 10,000 registros con formato idéntico, un script que parsea ese formato fijo es mil veces más barato y rápido que mandarlos uno por uno a un LLM.

### 9.4 El caso de Carlos, resuelto con la matriz

| Paso del proceso | Tipo de solución | Por qué |
|--------------------|---------------------|---------|
| Recibir factura por correo/WhatsApp | Código (automatización de captura) | Es solo mover un archivo de un lugar a otro |
| Leer la factura y extraer proveedor, monto, fecha, ítems | IA (OCR + modelo de extracción) | Los formatos varían entre proveedores, no hay estructura fija |
| Validar que el monto coincide con la orden de compra | Código | Es una comparación numérica determinística |
| Detectar si la factura es "rara" (formato inusual, proveedor nuevo) | IA (clasificación) | Requiere criterio, no una regla fija |
| Registrar en el sistema contable | Código (vía API/RPA) | Es una escritura estructurada a un sistema con reglas fijas |
| Alertar si algo no cuadra | Código (regla de negocio) | Umbral definido, no necesita "interpretación" |

> **El patrón a memorizar:** IA en los bordes, donde hay variabilidad (leer, clasificar, interpretar). Código en el núcleo, donde hay que ser exacto y auditable (calcular, validar, ejecutar).

### 9.5 Señales de que estás usando IA por moda, no por necesidad

- Usás un LLM para tareas que un `VLOOKUP` o un `if` resolvería igual de bien y más rápido.
- No podés explicar qué pasaría si la IA se equivoca en ese paso específico.
- El costo por ejecución de IA es mayor que el valor que ahorra.
- Elegiste IA antes de mapear el proceso, no después.
- El cliente te pidió "algo con IA" sin que vos hayas evaluado si el proceso lo necesita — ahí tu trabajo es educarlo, no complacerlo.

### 9.6 Cómo comunicárselo al cliente sin que sienta que le estás vendiendo menos

Muchos clientes piden IA porque creen que es "más moderno" o "mejor". Podés decirles algo así:

> *"Vamos a usar la herramienta correcta para cada parte del proceso. Donde hay reglas claras, usamos automatización tradicional porque es más rápida, más barata y 100% predecible. Donde hay texto o documentos variables que hoy vos interpretás con criterio, ahí sí usamos IA, porque es lo único que puede hacer ese trabajo. Mezclar las dos de forma inteligente es lo que te da un sistema robusto, no usar IA en todo por moda."*

---

## 10. El Ingeniero de IA en esta Clase

| Habilidad | Qué significa |
|-----------|----------------|
| Sabe preparar el terreno antes de preguntar | No entra "a ciegas" a entrevistar — llega con contexto de dirección y un mensaje de confianza ya comunicado |
| Hace las preguntas correctas, en el orden correcto | Va de lo cualitativo a lo cuantitativo, no al revés |
| Detecta señales indirectas | No espera que le digan "esto es un embudo" — lo reconoce en el lenguaje y en los atajos informales |
| Maneja el miedo al reemplazo con honestidad, no con marketing | Sabe la verdad antes de prometer nada |
| Pone límites al alcance | No automatiza el caos — primero exige estandarización |
| Elige la herramienta correcta por cada paso, no por el proceso completo | IA para lo ambiguo, código para lo determinístico — nunca "todo IA" por defecto |

---

## 11. Resumen Visual

```
┌──────────────────────────────────────────────────────────────┐
│           AUDITORÍA DE PROCESOS EN 4 FASES                    │
│                                                                │
│  FASE 1: Preparar el terreno                                  │
│     └─► Mapa de procesos + comunicación honesta del propósito │
│                                                                │
│  FASE 2: Entrevistar                                          │
│     └─► Mapeo real → Cuellos de botella → Cuantificar          │
│         (nunca al revés)                                      │
│                                                                │
│  FASE 3: Detectar lo que no te dicen directamente             │
│     └─► Excel paralelos, "siempre", risas nerviosas            │
│                                                                │
│  FASE 4: Decidir la herramienta, paso por paso                │
│     └─► ¿Reglas fijas? → Código                                │
│         ¿Interpretación ambigua? → IA                          │
│         La mayoría de los procesos: COMBINADO                 │
└──────────────────────────────────────────────────────────────┘
```

---

## Cierre

### Lo que aprendimos hoy

1. **Antes de automatizar, hay que auditar** — y auditar bien requiere preparación, no solo buena intención.
2. **La forma de preguntar determina la calidad de lo que vas a descubrir.** Preguntas abiertas y genéricas producen respuestas inútiles.
3. **El miedo al reemplazo es real y hay que manejarlo con honestidad**, nunca con promesas vacías.
4. **Auditarte a vos mismo es más difícil que auditar a otro** — necesitás evidencia externa, no introspección.
5. **La IA no es la respuesta por defecto.** La pregunta correcta es "¿esto requiere interpretar algo ambiguo, o es una regla fija?" — y esa pregunta se responde paso por paso, no para el proceso completo.
6. **El patrón ganador es casi siempre combinado:** IA en los bordes (leer, clasificar, interpretar), código en el núcleo (calcular, validar, ejecutar).

### Próxima clase

Con el diagnóstico de qué automatizar y con qué herramienta ya en mano, volvemos al terreno técnico: empezamos a construir el agente que va a resolver el proceso que identificaste en esta auditoría — el Proyecto Ancla del taller parte, justamente, de un problema real bien diagnosticado, no de una idea abstracta.

### Tarea

1. Elegí un proceso real (tuyo, de tu trabajo, o de un negocio conocido) y aplicá el checklist de entrevista completo (secciones 2 y 3), aunque sea entrevistándote a vos mismo con las técnicas de la sección 8.
2. Completá la matriz de decisión IA-vs-código (sección 9) para al menos 5 pasos de ese proceso.
3. Traé a la próxima clase: el entregable de auditoría (sección 6) de ese proceso, completo.

---

> **Recordá:** el Ingeniero de IA más valioso no es el que sabe usar más herramientas de IA. Es el que sabe, para cada problema real, cuándo la respuesta correcta es *no* usar IA.
