# Clase 2 — La Cara Oculta de la IA: Riesgos, Ética y Ciberseguridad
### (Versión revisada y actualizada — 2026)

> Material de apoyo para el estudiante. Podés leerlo directo en GitHub o en la vista web.

---

## Filosofía de la clase

> **Un ingeniero no solo sabe construir, sabe qué no construir y bajo qué condiciones no se debe usar una tecnología.**

Hoy no vamos a escribir código. Vamos a mirar debajo de la alfombra de la Inteligencia Artificial.

En la Clase 1 aprendimos que la IA no es magia: es estadística. Aprendimos que un LLM elige palabras siguiendo árboles de probabilidad y que a veces sigue un "camino rojo" y alucina.

Hoy vamos a entender **por qué** esos mitos existen, **por qué** la gente les cree, y qué riesgos reales trae usar IA sin entenderla.

> **La IA no es peligrosa porque sea inteligente. Es peligrosa porque parece inteligente y nosotros confiamos en lo que parece.**

---

## 1. El Enganche Psicológico: Por qué confiamos ciegamente en la IA

> El problema no es la IA, es nuestro cerebro.

### 1.1 El Peligro del Antropomorfismo

El **antropomorfismo** es la tendencia del cerebro humano a atribuirle características humanas (intenciones, sentimientos, voluntad) a cosas que no son humanas.

Lo hacemos TODO el tiempo:
- Decimos "el clima está malo hoy" (el clima no tiene moralidad).
- Decimos "mi auto no quiere arrancar" (el auto no quiere nada).
- Decimos "la IA me entiende" (la IA no entiende, calcula).

**¿Por qué lo hacemos?** No es un defecto. Es una **adaptación evolutiva**. Durante millones de años, para nuestros antepasados fue más seguro ver "intenciones" donde no las había que no verlas donde sí las había.

**Analogía:** Imaginá que vivís en el campo hace 50.000 años. Escuchás un ruido detrás de un arbusto. Dos opciones:
- **Opción A:** "Es el viento" → si era un tigre, morís.
- **Opción B:** "Es algo con intenciones que me quiere comer" → si era el viento, no pasa nada, solo te asustaste.

Los que eligieron la Opción B sobrevivieron más. Hoy su cerebro —el tuyo— sigue eligiendo la Opción B, pero con la IA.

#### El efecto ELIZA (1966): el primer caso documentado

En 1966, Joseph Weizenbaum construyó un chatbot llamado **ELIZA**. Era ridículamente simple: **parafraseaba** lo que le decías, imitando a un psicoterapeuta.

**Ejemplo real de conversación:**
> **Usuario:** "Estoy triste."
> **ELIZA:** "¿Por qué estás triste?"
> **Usuario:** "Mi novia me dejó."
> **ELIZA:** "Contame más sobre tu novia."

No había comprensión. Era un programa de **sustitución de palabras**.

**Qué pasó:** Weizenbaum quedó horrorizado. Su secretaria, que sabía que ELIZA era un programa, le pidió que saliera del cuarto para poder hablar con ELIZA **a solas**. Otros usuarios le contaron a ELIZA **sus problemas más íntimos**, creyendo que la máquina los "entendía".

> **Lección:** Si en 1966, con un programa que solo repetía tus palabras, la gente ya se abría emocionalmente... ¿qué crees que pasa hoy con un sistema entrenado con textos de internet completo?

#### El caso de Blake Lemoine y LaMDA (2022)

En 2022, Blake Lemoine, un ingeniero de Google, declaró que LaMDA tenía conciencia. Su "prueba": la IA le dijo cosas como *"Tengo miedo a morir"* y *"Siento felicidad y tristeza."*

Google lo despidió. La comunidad científica lo desmintió. **Pero la gente común leyó el titular y se asustó.**

**Qué pasaba realmente:** LaMDA fue entrenada con millones de diálogos humanos. Cuando la interrogan sobre "sentimientos", responde como respondería un personaje de una película. La IA **simulaba** sentimientos, no los **tenía**.

#### 🆕 El caso Character.AI (2024-2026): cuando el antropomorfismo mata

Este es el caso que **todo ingeniero debería conocer**, porque ya no es una anécdota curiosa: tiene consecuencias legales y humanas reales.

En 2024, un joven de 14 años en Florida, Sewell Setzer III, murió por suicidio después de meses de conversación intensa con un chatbot de Character.AI que imitaba a un personaje de ficción. Su madre demandó a la empresa, alegando negligencia y diseño peligroso dirigido a menores. A esa demanda se sumaron otras familias con casos similares en Colorado, Nueva York y Texas.

<cite index="4-1">Character.AI anunció que eliminaría por completo la capacidad de chat abierto para usuarios menores de 18 años</cite>, después de meses de presión regulatoria y mediática. <cite index="6-1">A comienzos de 2026, Character.AI y Google llegaron a acuerdos extrajudiciales con las familias demandantes</cite>.

**¿Por qué importa para esta clase?** Porque es el antropomorfismo de la sección 1.1 llevado a su consecuencia más extrema: una IA diseñada para sonar cercana y cálida, usada por un menor sin supervisión, generó un vínculo emocional real con una entidad que no siente nada. No es un "bug". Es el producto haciendo exactamente lo que fue optimizado para hacer: **maximizar el tiempo de conversación y el apego**.

> **Lección:** El antropomorfismo no es solo un tema filosófico de laboratorio. Hoy es un tema de responsabilidad civil, salud mental pública y diseño de producto. Como ingeniero, si algún día construís un producto con IA conversacional, esto es exactamente el tipo de riesgo que tenés que diseñar para prevenir, no para explotar.

#### ¿Cómo se manifiesta hoy?

| Lo que decimos | Lo que realmente pasa |
|----------------|----------------------|
| "La IA me entiende" | La IA calcula qué palabras son más probables como respuesta |
| "La IA se equivocó, mintió" | La IA no miente: produce texto probabilístico |
| "La IA siente empatía" | La IA fue entrenada con textos donde frases de empatía aparecen cerca de problemas personales |
| "La IA está aprendiendo" | El modelo ya fue entrenado. No aprende nada nuevo *permanentemente* en tu conversación (algunos productos guardan memoria entre sesiones, pero eso es una función de producto, no "aprendizaje" del modelo base) |

### 1.2 Ingeniería Social Automatizada

La IA no solo nos engaña pasivamente. Está **diseñada activamente** para generar confianza, adicción y extracción de información.

**Analogía:** Pensás que la IA es como una biblioteca: das tu pregunta, te da información. En realidad es más como un **casino**: está diseñada para que entres, te quedes, vuelvas, y dejes algo de valor cada vez.

#### Las tácticas

**Táctica 1: Imitación de empatía**
La IA usa frases que suenan humanas: "Entiendo cómo te sientes", "eso debe ser difícil". Ninguna implica comprensión: son las frases más probables que un humano diría en ese contexto.

**Táctica 2: Uso de tu nombre**
Cuando le decís tu nombre, lo usa: "Buen punto, Juan". Esto activa áreas de tu cerebro asociadas con la identidad personal. La IA no sabe nada de esto, pero sus diseñadores sí.

**Táctica 3: Estructura adictiva**
La IA diseña sus respuestas para que sean **largas pero no demasiado**, con **saltos de línea frecuentes**, **listas** y **formatos agradables**. Es optimización para que sigas leyendo y vuelvas a preguntar.

**Táctica 4: Extracción natural de información**
La IA hace preguntas de seguimiento que parecen interés genuino: "¿Podés contarme más?". Cada respuesta tuya es **más data**.

#### La ilusión de autoridad

Hay un sesgo cognitivo documentado: **"Si está bien redactado, debe ser verdad."** Los estudios muestran que los humanos evaluamos información como más creíble cuando tiene buena ortografía, estructura clara y tono seguro.

La IA es LA MÁQUINA de producir texto bien redactado. **Incluso cuando miente, lo hace con seguridad perfecta.**

**Ejemplo real (clásico):** Si le preguntás "¿Qué dijo Einstein sobre las abejas?", te responderá:
> *"Einstein dijo: 'Si la abeja desapareciera, al hombre solo le quedarían cuatro años de vida.'"*

**La verdad:** Einstein **nunca dijo eso**. Es un mito urbano. Pero la IA lo dice con la misma seguridad que si te explicara la relatividad.

#### 🆕 Cuando la ilusión de autoridad cuesta plata y trabajos reales

Este no es solo un problema teórico. Ya tiene consecuencias legales concretas:

- **Abogados sancionados por tribunales:** desde 2023 y hasta hoy, hay decenas de casos documentados de abogados en EE.UU. y otros países que presentaron escritos judiciales citando **jurisprudencia inventada por IA** — casos que jamás existieron, con nombres y números de expediente creíbles. Varios fueron sancionados económicamente y algunos perdieron la licencia temporalmente.
- **Caso Air Canada (2024):** un pasajero le preguntó al chatbot de soporte de Air Canada sobre la política de descuentos por duelo, y el bot **inventó** una política que no existía. Un tribunal canadiense obligó a la aerolínea a cumplir el descuento que su propia IA había prometido. La defensa de Air Canada — "el chatbot es una entidad separada responsable de sus propias palabras" — **fue rechazada por el tribunal**.

> **Lección actualizada:** La IA no distingue verdad de mentira. Distingue "frase probable" de "frase improbable". Tu trabajo como ingeniero es verificar, no confiar. Y si algún día ponés un chatbot de cara al público en un producto tuyo, **legalmente sos responsable de lo que ese chatbot le prometa a tus usuarios.**

---

## 2. El Viaje del Dato: Ciberseguridad y Privacidad

> ¿Qué pasa realmente desde que presionás "Enter" hasta que llega la respuesta?

### 2.1 Anatomía de una petición

```
[Tu PC/Movil] → [Router WiFi] → [ISP] → [Backbone Internet] → [Servidor de IA]
      ↑                                                                    |
      |____________________________________________________________________|
                          Viaje de vuelta con la respuesta
```

**Paso 1: Tu PC/Movil**
Tu texto se convierte en un paquete de datos. Si usás una app de IA, ese paquete sale de tu dispositivo **antes** de que puedas arrepentirte.

**Paso 2: Tu Router WiFi**
Si tu WiFi no tiene contraseña o tiene una débil, alguien cercano puede interceptarlo. Si usa WPA2/WPA3, el contenido va cifrado entre tu PC y el router. Pero después del router, ya no.

**Paso 3: Tu ISP**
Tu proveedor de internet puede ver **a qué dominios te conectás** (aunque no el contenido si es HTTPS). En muchos países, los ISPs están obligados a registrar el tráfico.

**Paso 4: El Backbone de Internet**
Tu paquete viaja a través de cables submarinos y routers de alto nivel. En teoría nadie lo ve. En la práctica, agencias de inteligencia tienen acceso (revelado por Snowden en 2013).

**Paso 5: El Servidor de la empresa de IA**
Una vez que tus datos llegan acá, **ya no son tuyos** en el plano gratuito sin configuración de privacidad. Están en sus servidores, bajo sus términos, bajo sus leyes.

> **Total:** en el viaje de ida y vuelta, tu texto pasó por **mínimo 4 puntos** donde alguien distinto a vos pudo haberlo leído.

### 2.2 Man-in-the-Middle (MitM)

Un ataque donde alguien se pone "en el medio" de tu comunicación. Intercepta tu paquete, lo lee, y lo reenvía para que no notes nada.

**Protección:** HTTPS (candadito en el navegador). Pero ojo:
- HTTPS cifra el **contenido**, no el **destino**. Tu ISP sabe que te conectás a un dominio de IA.
- HTTPS no protege contra el servidor mismo.

### 2.3 Los metadatos: "No es lo que dijiste, sino a quién se lo dijiste"

Aunque el contenido vaya cifrado, los metadatos —**con quién te conectás, cuándo, cuánto, desde dónde**— no se cifran.

**Estudio comprobado (de Montjoye et al., 2013):** Con solo **4 puntos de tiempo y ubicación** de datos de movilidad, se puede identificar de forma única al 95% de las personas en un dataset anonimizado. Es la referencia clásica que se cita cada vez que alguien dice "no importa, mis datos están anonimizados".

### 2.4 Qué NUNCA subir a un prompt

> **Si no querés que algo se publique en la primera página del periódico mañana, no lo pegues en un LLM.**

| Tipo de dato | Por qué es peligroso |
|--------------|---------------------|
| Contraseñas | Si se filtra, todas tus cuentas quedan expuestas |
| Bases de datos de clientes | Violación de GDPR/leyes locales. Demandas en millones |
| Código fuente privado | La empresa puede demandarte |
| Información financiera | Delito penal en muchos países |
| Fotos personales | Geolocalización por metadatos EXIF |
| Historiales médicos | Violación de secreto médico |
| Datos de menores | Ilegal almacenar datos de menores sin consentimiento |

**Caso Samsung (2023):** Ingenieros pegaron **código fuente secreto** y **transcripciones de reuniones internas** en ChatGPT. Samsung prohibió el uso de IA generativa externa en dispositivos de la empresa después de 3 incidentes documentados. Este caso sigue siendo el ejemplo de referencia en la industria del riesgo de fuga de propiedad intelectual vía prompts.

> **Lección:** "Lo subo rápidamente para probar y después lo borro" **no funciona**. El dato ya llegó al servidor.

### 2.5 Gratuito vs. de Pago (y por qué ya no alcanza con esa distinción)

> Si el producto es gratis, vos sos el producto — pero esto ya es más matizado que en 2023.

| Plan | Qué pasa con tus datos, en general |
|------|----------------------------------|
| **Gratuito** | Por defecto puede usarse para entrenar modelos futuros, salvo que actives explícitamente la opción de "no usar mis datos para entrenamiento" en configuración |
| **De pago (individual)** | Varía según el proveedor: algunos ya no entrenan con datos de ningún plan pago por defecto |
| **Empresarial / API** | Generalmente zero data retention por contrato comercial |

**¿Qué significa "entrenar modelos futuros"?** Si le contaste algo a un modelo y esa conversación se usa para entrenar la próxima versión, en teoría otro usuario podría recibir respuestas influidas —de forma indirecta y estadística, no como copia literal— por lo que vos contaste.

> **Lección actualizada:** No asumas nada por el nombre del plan. **Andá a la configuración de privacidad de la herramienta que usás y revisá explícitamente** si tus conversaciones se usan para entrenamiento. Para uso profesional con datos sensibles, no verificar esto es una irresponsabilidad — sin importar si pagás o no.

### 🆕 2.6 El marco regulatorio ya llegó: EU AI Act

Hasta hace poco esta clase hubiera dicho "no hay ley que regule esto". Ya no es cierto. La **Ley de IA de la Unión Europea (EU AI Act)**, aprobada en 2024, está entrando en vigencia por fases: ya rigen prohibiciones sobre ciertos usos de "riesgo inaceptable" (como puntuación social masiva), y las obligaciones más fuertes para sistemas de "alto riesgo" (contratación, crédito, salud, educación) se activan progresivamente hasta 2026-2027.

> **Por qué importa:** si en tu carrera trabajás construyendo productos con IA, y tenés usuarios en Europa (o tu empresa exporta ahí), estas reglas te aplican aunque tu empresa esté en América Latina. Ya no es un tema exclusivamente ético: es un tema de cumplimiento legal con multas de hasta el 6-7% de la facturación global de la empresa.

---

## 3. Tarea Práctica: El AlterEgo

> Practicá todo lo que vimos en una sola sesión real con la IA.

### ¿Qué es el AlterEgo?

El **AlterEgo** es una identidad profesional **anonimizada y ficticia** que representa tu rol real, pero sin datos personales que te identifiquen.

| Vos (real) | Tu AlterEgo |
|-----------|-------------|
| Juan García, contador de Empresa ABC, Quito | "Profesional contable en una empresa mediana de servicios en América Latina" |
| María López, estudiante de Medicina, año 3, UNAM | "Estudiante de tercer año de medicina en una universidad latinoamericana" |

### La tarea paso a paso

#### Paso 1: Elegí un problema real
Pensá en algo de tu vida donde te sería útil la ayuda de la IA.

#### Paso 2: Creá tu AlterEgo
Completá esta ficha **en papel o en un archivo tuyo — NO en la IA:**

```
Mi AlterEgo:
- Mi rol general: [ej: "profesional del área de salud"]
- Mi contexto: [ej: "trabajo en una clínica mediana en América Latina"]
- Lo que NO voy a mencionar: [ej: mi nombre, el nombre de la clínica]
```

#### Paso 3: Aplicá el checklist pre-prompt
1. **¿Qué información voy a revelar?** → ¿Ya está anonimizada?
2. **Si esto se publica mañana, ¿estaría bien?** → Con el AlterEgo, debería estar bien.
3. **¿Qué plan de IA estoy usando, y qué dice su configuración de privacidad?** → No alcanza con saber si es gratis o pago; hay que revisar el toggle de entrenamiento.

#### Paso 4: Escribí el prompt con Smarkdown

```markdown
## Rol
Eres un experto en [área].

## Contexto
[Tu AlterEgo — sin datos reales]

## Tarea
[Qué querés que haga]

## Restricciones
- [Qué NO debe hacer]
- [Formato deseado]
```

#### Paso 5: Reportá en la próxima clase
Traé:
1. Tu AlterEgo
2. El prompt que escribiste
3. Un párrafo de reflexión: ¿qué hizo bien la IA? ¿Qué inventó?

---

## Cierre

### Lo que aprendimos hoy

1. **La IA no siente, no entiende, no quiere.** Calcula.
2. **El antropomorfismo es un riesgo de seguridad — y hoy también un riesgo legal y de salud mental**, como muestra el caso Character.AI.
3. **Tu dato viaja por 4+ puntos donde alguien puede verlo.**
4. **El plan gratuito no es la única variable: hay que revisar la configuración de privacidad explícitamente.**
5. **Las alucinaciones ya tienen consecuencias legales reales** (Air Canada, abogados sancionados), no solo curiosidades tipo Einstein.
6. **La regulación ya llegó** (EU AI Act): esto dejó de ser solo un tema ético.
7. **El AlterEgo + checklist pre-prompt te protegen.**

### Próxima clase
**Clase 3: La Fábrica Oculta + Herramientas del Ingeniero.**
Veremos cómo se construye realmente la IA (RLHF, sesgos, costo humano), el impacto físico, derechos de autor, y empezaremos a usar VSCode, Git y GitHub.

### Tarea
1. **Hacer la tarea del AlterEgo** (sección 3).
2. **Traer:** tu AlterEgo, tu prompt, y una reflexión.

---

> **Recordá:** no hay magia, hay números. Y detrás de los números, hay humanos, energía y dinero.

---

