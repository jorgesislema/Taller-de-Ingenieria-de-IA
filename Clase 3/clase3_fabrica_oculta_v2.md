# Clase 3 — La Fábrica Oculta + Herramientas del Ingeniero
### (Versión revisada y actualizada — 2026)

> Material de apoyo para el estudiante. Podés leerlo directo en GitHub o en la vista web.

---

## Filosofía de la clase

> **La IA no es "artificial". Es profundamente humana: datos, trabajo, energía, dinero.**

Esta clase no busca asustarte ni generarte desconfianza hacia la tecnología que vas a usar toda tu carrera. Busca lo contrario: que entiendas **los incentivos reales** detrás de cada modelo que uses, para que puedas tomar mejores decisiones técnicas y éticas cuando construyas con IA. Un ingeniero que entiende de dónde viene el costo, toma mejores decisiones que uno que solo sabe usar la API.

Hoy vamos a ver cómo se construye realmente la IA, qué costo tiene, y por qué no es gratuita ni neutra. Después, vamos a empezar a usar las herramientas del ingeniero: VSCode, Git y GitHub.

---

## 1. La Fábrica Oculta: Cómo se construye realmente la IA

### 1.1 La basura que entra: el problema de los datos

**¿Qué comen los modelos?**
- Common Crawl (petabytes de páginas web)
- Reddit, Twitter/X, Wikipedia
- Libros publicados (muchos sin permiso)
- Código fuente de GitHub

**Analogía:** Es como la dieta de un niño. Si le das frutas, crece sano. Si le das solo gaseosa, crece pero mal. Los modelos comieron de todo.

**Caso Microsoft Tay (2016):** Microsoft lanzó un chatbot en Twitter. En **menos de 24 horas**, los usuarios lo hicieron decir *"Hitler tenía razón"*. Tay no era racista: era un reflejo de lo que la gente le enseñó.

> **La esencia, no el susto:** Tay no fue un "modelo malo". Fue un modelo que aprendía en tiempo real de lo que le decían usuarios anónimos coordinados para manipularlo — un diseño sin ningún filtro entre el input hostil y el output público. Los modelos actuales ya no funcionan así (no reentrenan en vivo con lo que vos les decís), pero el principio de fondo sigue siendo válido: **un modelo es tan bueno como el proceso que filtra sus datos de entrada**, no solo los datos en sí.

### 1.2 La mano humana invisible: RLHF

**RLHF** = Reinforcement Learning from Human Feedback. Es lo que convirtió a los modelos de "predictores de texto crudo" a "asistentes útiles".

**Cómo funciona:**
1. El modelo lee texto masivo y aprende a predecir la siguiente palabra (esto es el "pretraining").
2. Se generan respuestas y se las muestran a humanos. Cada persona lee dos o más respuestas y decide cuál es mejor.
3. Se entrena un **modelo de recompensa** que aprende a puntuar respuestas según esas preferencias humanas.
4. El modelo principal se ajusta (fine-tuning) para maximizar esa recompensa.

**Analogía:** Como entrenar a un perro. El perro hace algo. Vos le decís "¡bien!" o "¡no!". Con repeticiones, aprende qué comportamiento buscás.

**El problema real (no un defecto, una consecuencia lógica):** Quien califica decide, con su propio criterio cultural, qué respuesta es "mejor". Esto no es una falla de diseño malintencionada — es matemáticamente inevitable: **cualquier sistema que optimiza para "gustarle a alguien" hereda los gustos de ese alguien.** El ejercicio interesante como ingeniero no es indignarse por esto, sino preguntarte: *¿quién calificó el modelo que estoy por usar, y para qué caso de uso calificaron?*

### 1.3 El costo humano detrás de la calificación

OpenAI, Google, Anthropic y otras empresas **subcontratan** buena parte del trabajo de calificación y moderación de contenido a empresas de terceros, muchas veces en el Sur Global.

**Casos documentados:**
- OpenAI subcontrató a Sama (Kenia) entre 2021-2022 para etiquetar contenido tóxico y de seguridad. Investigaciones periodísticas (Time, 2023) reportaron pagos de **$1.32 a $2 USD por hora** para ese trabajo específico, con trabajadores expuestos a descripciones de violencia y abuso extremos, algunos reportando síntomas compatibles con estrés postraumático.
- Meta tuvo un litigio similar en Kenia por condiciones de trabajo de moderadores de contenido subcontratados también vía Sama, que derivó en demandas laborales locales.

> **La esencia, no el susto:** Esto no es exclusivo de la IA — la moderación de contenido en redes sociales tiene el mismo problema hace más de una década. Lo nuevo es que ahora hay una cadena de valor multimillonaria (la de la IA generativa) apoyada en ese trabajo, y como ingeniero es información que vale la pena tener cuando evaluás "qué tan ético" es un proveedor, igual que evaluarías las condiciones de una cadena de suministro de hardware.

---

## 2. Los Sesgos de la IA: No es Solo Geográfico

> La IA tiene sesgos porque sus datos tienen sesgos. No es un bug que se pueda "arreglar" del todo — es una propiedad estructural de aprender de datos generados por humanos.

### 2.1 El sesgo cultural inevitable

**Los tres grandes bloques:**

| EE.UU. | Europa | China |
|--------|--------|-------|
| GPT (OpenAI) | Mistral (Francia) | Qwen (Alibaba) |
| Claude (Anthropic) | Llama (Meta) | Ernie (Baidu) |
| Gemini (Google) | | DeepSeek |

- **EE.UU.:** ecosistema competitivo, regulación federal todavía limitada aunque creciente. Valores dominantes en el diseño: libertad de expresión amplia, iteración rápida de producto.
- **Europa:** el **AI Act** (aprobado 2024, entrando en vigencia por fases hasta 2026-2027) es el primer marco legal integral del mundo para IA. Prioriza privacidad, transparencia y protección frente a sistemas de "alto riesgo" (contratación, crédito, salud, educación, justicia).
- **China:** la IA es infraestructura estratégica de Estado, con censura integrada por regulación. Valores priorizados: estabilidad social y alineación con la política del Estado.

**Caso:** DeepSeek (chino) bloquea o evade consultas sobre eventos como Tiananmen 1989, con respuestas genéricas o evasivas — un ejemplo claro de cómo la regulación local moldea directamente el comportamiento del modelo, no solo sus datos de entrenamiento.

**Latinoamérica:** no tiene, por ahora, modelos fundacionales propios a la escala de los anteriores. La estrategia realista de la región no es "competir" en entrenar modelos desde cero, sino **especializarse en la capa de aplicación**: fine-tuning, evaluación, adaptación cultural y de producto sobre modelos existentes — que es, de hecho, donde hoy se genera más valor económico por dólar invertido que en el entrenamiento de modelos base.

### 2.2 Sesgo de género

La IA asocia profesiones con géneros según la frecuencia estadística en sus datos de entrenamiento — no porque "piense" que un género es mejor en algo, sino porque reproduce la distribución del texto que leyó.

| Asociación | Origen del sesgo |
|------------|---------------------|
| "Doctor" → hombre | Mayor frecuencia histórica de "el doctor" en el corpus |
| "Enfermera" → mujer | Mayor frecuencia histórica de "la enfermera" en el corpus |
| "Programador" → hombre | La industria tech fue mayoritariamente masculina durante décadas |
| "Maestra" → mujer | La docencia primaria fue mayoritariamente femenina |

**Estudios de Stanford y otras universidades (2023-2024)** documentaron que varios LLM asocian sistemáticamente profesiones técnicas con hombres y profesiones de cuidado con mujeres al generar texto sin especificar género.

**El punto para vos como ingeniero:** este tipo de sesgo es medible y mitigable (hay técnicas de *debiasing*, prompts de control, y evaluación con benchmarks específicos). No es una excusa para no usar el modelo — es una razón para **testearlo** antes de ponerlo en producción en un caso de uso sensible (por ejemplo, un sistema que preseleccione CVs).

### 2.3 Sesgo racial, étnico y algorítmico en decisiones de alto riesgo

**Caso COMPAS (EE.UU.):** un sistema algorítmico usado en varios tribunales estadounidenses para estimar el riesgo de reincidencia mostró, en una investigación de ProPublica (2016), tasas más altas de falsos positivos de "alto riesgo" para personas afroamericanas que para personas blancas, con tasas de reincidencia real similares. El origen no era un algoritmo "racista" en su código — era que el algoritmo aprendió de datos históricos de arrestos, que ya reflejaban patrones desiguales de vigilancia y arresto.

> **La esencia:** COMPAS es el ejemplo perfecto para entender por qué "el algoritmo es objetivo porque es matemática" es una afirmación falsa. Un algoritmo entrenado con datos históricos sesgados **automatiza y escala** ese sesgo, dándole además una apariencia de neutralidad numérica que lo hace más difícil de cuestionar que una decisión humana. Este es exactamente el tipo de sistema que el EU AI Act clasifica como "alto riesgo" y sujeta a auditoría obligatoria.

### 2.4 Sesgo religioso y de valores

Los datos de entrenamiento en inglés están dominados por producción textual de tradición cultural occidental y mayoritariamente cristiana, lo cual influye en qué respuestas el modelo trata como "el default" cuando una pregunta no especifica contexto cultural (ej.: "¿cuál es la forma correcta de criar a un hijo?" tenderá a responder desde un marco occidental si no se le pide explícitamente otra perspectiva).

**Por qué importa para vos:** si construís un producto para una audiencia culturalmente distinta a la angloparlante-occidental, **no asumas que el default del modelo es neutral** — vas a necesitar prompts o fine-tuning que traigan explícitamente el marco cultural correcto.

### 2.5 Sesgo socioeconómico

Internet, y por lo tanto los datos de entrenamiento, sobrerrepresentan a personas con acceso a conectividad, educación formal y capacidad de producir contenido escrito — lo cual sesga sistemáticamente qué se presenta como "profesional", "exitoso" o "normal" hacia perfiles de clase media-alta.

### 2.6 Sesgo lingüístico

| Idioma | Cuota aproximada en datos de entrenamiento | Calidad típica de la IA |
|--------|-------------------|------------------|
| Inglés | Mayoría dominante | Excelente |
| Español | Minoría significativa | Buena, mejorando rápido |
| Portugués | Minoría menor | Buena, mejorando |
| Quechua, Aimara, Guaraní | Marginal | Limitada |

Los modelos más recientes (2025-2026) mejoraron muchísimo en español respecto a hace dos años, en parte porque los proveedores empezaron a invertir deliberadamente en datos multilingües de mayor calidad, no solo en volumen de scraping. Igual, la brecha con lenguas originarias americanas sigue siendo enorme, y ahí la "traducción interna" del modelo (pensar en inglés, traducir conceptos) sigue perdiendo matices culturales.

### 2.7 Sesgo de discapacidad

Los datos asocian implícitamente "capacidad", "productividad" y "normalidad" con la ausencia de discapacidad, simplemente porque la mayoría de los textos disponibles fueron escritos desde esa perspectiva, sin intención de exclusión pero con el efecto de invisibilizar otras experiencias.

---

## 3. El Impacto Físico y Económico

> Esta sección no es para que salgas con culpa de usar IA. Es para que entiendas que cada llamada a un modelo tiene un costo material real, igual que cada consulta SQL tiene un costo de cómputo — y que ese costo es un input más a considerar en el diseño de un producto, junto con la latencia o el precio de la API.

### Energía y agua

- Estimaciones de terceros (no cifras oficiales confirmadas por las empresas) sitúan el entrenamiento de GPT-3 en el orden de ~1,300 MWh. Para modelos más grandes y recientes, la cifra es sustancialmente mayor, aunque las empresas no suelen publicar el dato exacto.
- Varios estudios estiman que una consulta a un chatbot de IA consume entre 5 y 10 veces más energía que una búsqueda tradicional en un buscador — el rango varía mucho según el modelo y el largo de la respuesta.
- Microsoft y Google reportaron en sus informes de sostenibilidad aumentos de doble dígito en consumo de agua en los años de mayor expansión de sus datacenters de IA (2022-2024).
- Los datacenters dedicados a IA ya representan un porcentaje creciente del consumo eléctrico mundial, con proyecciones de organismos como la Agencia Internacional de Energía apuntando a que podrían duplicarse o más hacia el final de la década.

### GPUs y Nvidia

- Nvidia mantiene una posición dominante en el mercado de GPUs para entrenamiento e inferencia de IA, con estimaciones de mercado que rondan el 80-90%+ según el segmento.
- En octubre de 2025, Nvidia se convirtió en la **primera empresa de la historia en superar los 5 billones de dólares de valor de mercado** — para dimensionar: eso es más que el PBI anual de la mayoría de los países del mundo. Desde entonces el valor osciló entre los 4.5 y los 5 billones.

### ¿Estamos en una burbuja?

El debate sigue abierto y **los números de 2023 ya quedaron viejos** — la industria creció mucho más rápido de lo que muchos analistas proyectaban, pero también el gasto en infraestructura (datacenters, chips, energía) escaló a niveles sin precedentes, comprometiendo cientos de miles de millones de dólares en construcción futura por parte de OpenAI, Microsoft, Meta, Google, Amazon y xAI.

> **La esencia:** no importa tanto memorizar la cifra exacta (va a cambiar antes de que termines de leer esto) sino entender la pregunta de fondo que un ingeniero senior se hace: *¿el valor real que este sistema genera hoy justifica la inversión de capital que se le está poniendo?* Esa pregunta aplica tanto a la industria completa como a cada feature con IA que vos decidas construir en tu trabajo. No hace falta tener una postura ideológica sobre "burbuja sí/no" — hace falta el hábito de hacerte esa pregunta de costo-beneficio.

---

## 4. Las Minas Legales: Derechos de Autor

### Los modelos fueron entrenados con contenido protegido

| Contenido | ¿Hubo permiso explícito? |
|-----------|-----------|
| Libros (algunos vía shadow libraries como LibGen) | Generalmente no |
| Artículos periodísticos | Generalmente no |
| Arte / imágenes (DeviantArt, ArtStation) | Generalmente no |
| Código fuente (GitHub) | Depende de la licencia original |
| Wikipedia | Sí (licencia abierta) |

### Casos de guerra legal (todos siguen en litigio activo, sin sentencia final a la fecha)

- **NYT vs. OpenAI (desde 2023):** el NYT presentó evidencia de que ChatGPT podía reproducir fragmentos extensos y muy similares a sus artículos originales. El caso continúa en curso en tribunales de EE.UU.
- **Getty vs. Stability AI (desde 2023):** Getty mostró que Stable Diffusion generaba imágenes con una versión distorsionada del watermark de Getty, como evidencia de que el modelo memorizó imágenes específicas en vez de solo "aprender estilos". También en curso.
- **Demandas de programadores vs. GitHub Copilot (desde 2022):** alegan que Copilot reproducía código bajo licencias que exigían atribución, sin dar esa atribución.

> **La esencia:** estos casos importan menos por su resultado final (que puede tardar años) y más porque **están definiendo en tiempo real** qué significa "uso justo" (*fair use*) cuando el que "lee" y "aprende" de una obra es un modelo entrenado con fines comerciales masivos, no una persona. Es un terreno legal genuinamente nuevo, y vas a trabajar toda tu carrera bajo las reglas que estos casos terminen de fijar.

### ¿De quién es el output?

| Situación | ¿Hay copyright protegible? |
|-----------|-----------|
| Texto 100% escrito por vos | Sí |
| Texto 100% generado por IA, sin edición humana significativa | Generalmente no, en la mayoría de jurisdicciones actuales |
| Texto que vos editaste y estructuraste significativamente | Zona gris, depende de cuánto aporte humano hubo |
| Imagen 100% generada por IA | Generalmente no, salvo edición sustancial posterior |

> **Regla práctica:** si usás IA para un cliente o un trabajo profesional, avisá que la usaste, verificá el resultado, editalo con criterio propio y documentá tu proceso. No es solo una cuestión ética — cada vez más contratos y políticas empresariales lo exigen explícitamente.

---

## 5. Zonas de Alta Responsabilidad: Dónde el Error de la IA Pesa Más

> El título original de esta sección hablaba de "riesgo letal". Preferimos hablar de **alta responsabilidad**: la IA no es peligrosa por sí misma en estos campos, es que el costo de un error no verificado es mucho mayor que en otros contextos — igual que un error de cálculo estructural pesa más que un error en un borrador de email.

### Medicina

Los modelos de lenguaje generales pueden acertar diagnósticos comunes con buena frecuencia, pero en casos atípicos pueden generar una respuesta **igual de segura y bien redactada** para un diagnóstico incorrecto que para uno correcto — porque el modelo no "sabe" que se equivocó, solo genera la continuación más probable. En medicina, la diferencia entre ambos casos puede ser crítica para el paciente. Por eso los sistemas de IA médica seria no reemplazan el criterio clínico: lo asisten, con el profesional siempre validando.

### Derecho — Caso Mata v. Avianca / "Caso Schwartz" (2023)

Un abogado usó ChatGPT para preparar un escrito judicial. El modelo generó **varios casos legales con nombres, fechas y citas que sonaban perfectamente reales**. Ninguno existía. El juez impuso una multa de $5,000 a los abogados por presentarlos sin verificar. Este fue el primer caso ampliamente mediatizado, pero **no fue el único**: desde entonces se documentaron decenas de casos similares en varios países, lo cual confirma que no fue "un abogado descuidado" sino un patrón estructural de mal uso de una herramienta poderosa sin verificación.

### Ingeniería (civil, estructural, de software crítico)

Si usás IA para asistir cálculos estructurales, código de sistemas de seguridad, o cualquier sistema donde un error se traduce en daño físico, y el modelo genera un número o una línea de código plausible pero incorrecto, las consecuencias pueden ser graves e irreversibles.

> **Regla, no advertencia:** la IA puede acelerar el trabajo pesado en estos campos — pero **la firma, el sello y la responsabilidad profesional siguen siendo humanas, y así va a seguir siendo por diseño regulatorio**, no por limitación técnica. Esto no es un "hasta que la IA mejore" — es una decisión de sociedad sobre quién responde legalmente por un daño.

---

## 6. El Protocolo del Ingeniero: Cómo usar la IA de forma segura

### Checklist pre-prompt (las 3 preguntas)

1. **¿Qué información estoy a punto de revelar?** → Anonimizá lo que no sea estrictamente necesario.
2. **Si esto se publica mañana, ¿estaría bien?** → Si no, no lo subas.
3. **¿Qué plan de IA estoy usando y qué dice su política de privacidad?** → Para datos sensibles, siempre verificá la configuración explícitamente, no asumas por el nombre del plan.

### Human-in-the-Loop (HITL)

- **Gran parte del trabajo mecánico y repetitivo:** lo puede hacer la IA.
- **El criterio crítico — qué preguntar, qué verificar, qué descartar:** lo hace el humano.
- **El 100% de la responsabilidad final del resultado:** sigue siendo humana. Esto no es una cifra arbitraria — es, cada vez más, un requisito legal explícito (ver EU AI Act y regulaciones profesionales de colegios de abogados, médicos e ingenieros).

### Smarkdown

**Structured Markdown** para prompts. Usá `## Rol`, `## Contexto`, `## Tarea`, `## Restricciones` para darle estructura clara a tus instrucciones.

```markdown
## Rol
Eres un experto en [área].

## Contexto
[Situación general, sin datos sensibles]

## Tarea
[Qué querés que haga]

## Restricciones
- [Qué NO debe hacer]
- [Formato deseado]
```

---

## 7. Práctica con VSCode

> Referencia completa: ver [`vscode.md`](../Clase-04-Herramientas-del-Ingeniero-de-IA/vscode.md)

### Los 5 atajos que necesitás HOY

| Atajo | Qué hace |
|-------|---------|
| `Ctrl+Shift+P` | Paleta de comandos (el buscador universal) |
| `Ctrl+P` | Abrir archivo rápido |
| `Ctrl+` ` | Abrir/cerrar terminal |
| `Ctrl+B` | Mostrar/ocultar barra lateral |
| `Ctrl+Shift+V` | Previsualizar Markdown |

### La terminal integrada

`Ctrl+` ` para abrirla. Ya se abre en la carpeta de tu proyecto.

---

## 8. Práctica con Git y GitHub

> Referencia completa: ver [`github.md`](../Clase-04-Herramientas-del-Ingeniero-de-IA/github.md)

### Los 7 comandos que necesitás

| Comando | Qué hace |
|---------|---------|
| `git clone <url>` | Baja un repo de GitHub |
| `git status` | Ve qué archivos cambiaron |
| `git add .` | Marca todos los cambios |
| `git commit -m "mensaje"` | Guarda con descripción |
| `git push` | Sube a GitHub |
| `git pull` | Baja cambios de otros |
| `git log --oneline` | Historial resumido |

### Flujo típico

```bash
git status          # Ver qué cambió
git add .           # Marcar todo
git commit -m "msg" # Guardar
git push            # Subir
```

### Crear tu cuenta de GitHub

1. Andá a https://github.com
2. Click "Sign up"
3. Email, contraseña, nombre de usuario
4. Verificar email
5. Listo — ya tenés tu repo

---

## 9. Práctica con Markdown

> Referencia completa: ver [`markdown.md`](../Clase-04-Herramientas-del-Ingeniero-de-IA/markdown.md)

### Sintaxis rápida

| Elemento | Sintaxis |
|----------|----------|
| Título | `# Texto` |
| Negrita | `**Texto**` |
| Lista | `- Item` |
| Link | `[texto](url)` |
| Código | `` `código` `` |
| Tabla | `\| A \| B \|` |

### Previsualizar en VSCode

`Ctrl+Shift+V` con el archivo `.md` abierto.

---

## Cierre

### Lo que aprendimos hoy

1. **La IA es trabajo humano masivo**, muchas veces invisible y mal remunerado en su etapa de calificación.
2. **No existe IA neutra.** Cada modelo refleja los valores e incentivos de quien lo entrenó y de quién calificó sus respuestas — y esto es medible, no solo una opinión.
3. **La IA tiene un costo físico real:** energía, agua, chips — un input más a considerar al diseñar un producto, no un tabú.
4. **Los modelos fueron entrenados con contenido protegido**, y los casos legales que definirán las reglas del juego siguen abiertos.
5. **En medicina, derecho e ingeniería, el costo de un error no verificado es mayor** — de ahí la importancia estructural del HITL, no como recomendación sino como diseño responsable.
6. **El protocolo:** checklist + anonimización + HITL, aplicado con criterio, no con miedo.
7. **VSCode, Git y GitHub** son las herramientas base del ingeniero.

### Próxima clase
**Clase 4: Herramientas del Ingeniero de IA + Vibe Coding.**
Ahora que tenés las herramientas instaladas y configuradas, vamos a usar IA para programar de forma segura — con Smarkdown, AlterEgo y HITL.

### Tarea
1. **Crear tu cuenta de GitHub** si no la tenés.
2. **Crear un repo** con un `README.md` escrito en Markdown.
3. **Hacer commit y push** desde VSCode.
4. **Leer** [`vscode.md`](../Clase-04-Herramientas-del-Ingeniero-de-IA/vscode.md), [`github.md`](../Clase-04-Herramientas-del-Ingeniero-de-IA/github.md), [`markdown.md`](../Clase-04-Herramientas-del-Ingeniero-de-IA/markdown.md).

---

> **Recordá:** no hay magia, hay números. Y detrás de los números, hay humanos, energía y dinero.

---

### 📎 Nota para el docente

Cambios respecto a la v1: se corrigieron/matizaron cifras de Nvidia (superó los $5 billones en oct. 2025) y del debate de "burbuja" (el dato de Sequoia de 2023 ya está desactualizado), se aclaró que NYT vs. OpenAI y Getty vs. Stability siguen **sin sentencia final** (no son "casos cerrados de 2023"), se contextualizó el caso Schwartz como "el primero conocido, no el único", y se agregaron notas de "esencia, no susto" después de cada caso fuerte (Tay, Sama, COMPAS) para que el estudiante entienda el mecanismo estructural detrás del caso, en vez de quedarse solo con el shock anecdótico. El objetivo pedagógico de esta versión es que el alumno termine la clase pudiendo explicar *por qué* pasa cada cosa (incentivos, datos, quién decide qué es "bueno"), no solo repetir el caso como advertencia.
