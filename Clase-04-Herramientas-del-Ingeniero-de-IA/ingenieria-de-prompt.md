# Ingenieria de Prompt — Resumen del Taller

> Resumen extraido del [repositorio completo de ingenieria de prompt](https://github.com/jorgesislema/apuntes_de_ingenieria_de_prompt).
> Si queres profundizar, ahi estan los 16 modulos completos. Esto es lo esencial para arrancar.

---

## 1. Que es un prompt (en serio)

Un **prompt** es la instruccion que le das a la IA. Todo lo que escribis antes de presionar Enter.

La IA no "entiende" tu prompt como lo haria una persona. Lo que hace es buscar, en su enorme arbol de probabilidades, cual es la secuencia de palabras mas probable para responder.

**Analogia:** Es como hablarle a alguien que habla tu idioma pero recien llego al pais. Entiende las palabras, pero no el contexto cultural, no el tono implicito, no "lo que no dijiste". Cuanto mas explicito seas, mejor resultado obtenes.

> **Regla de oro:** La calidad de la respuesta es proporcional a la calidad del prompt. Prompt vago = respuesta vaga. Prompt preciso = respuesta precisa.

---

## 2. Los 5 elementos de un buen prompt

Todo prompt efectivo puede tener hasta 5 componentes. No todos son obligatorios siempre.

| Elemento | Que es | Obligatorio | Ejemplo |
|----------|--------|-------------|---------|
| **Rol** | Que personaje o experto queres que sea la IA | Recomendado | "Eres un diseniador senior con 15 anios de experiencia" |
| **Contexto** | La situacion, quien sos vos | Muy recomendado | "Soy estudiante del taller de IA, armando mi portfolio" |
| **Tarea** | Que queres que haga, con verbo concreto | **SI, siempre** | "Redacta / Genera / Explica / Analiza / Lista" |
| **Restricciones** | Limites: formato, tono, longitud | Recomendado | "Maximo 200 palabras, tono profesional, en espaniol" |
| **Ejemplo** | Muestra del output esperado | Opcional pero muy util | "Aca hay un ejemplo de como quiero que se vea..." |

### Verbos de tarea mas utiles

| Si queres... | Usa este verbo |
|-------------|----------------|
| Un texto nuevo | **Redacta / Escribi / Crea** |
| Explicar algo complejo | **Explica como si tuviera 12 anios** |
| Un listado | **Lista / Enumera / Dame 5 opciones** |
| Analizar | **Analiza / Evalua / Identifica puntos clave** |
| Resumir | **Resumi en X parrafos** |
| Mejorar algo escrito | **Mejora / Revisa / Reescribi** |
| Traducir | **Traduci al [idioma] manteniendo el tono** |
| Comparar | **Compara A vs B en una tabla** |
| Dar pasos | **Explica paso a paso como...** |

---

## 3. Los 4 tipos de prompting

| Tipo | Como funciona | Cuando usarlo |
|------|---------------|---------------|
| **Zero-shot** | Le pedis sin ejemplos previos | Tareas simples y directas |
| **One-shot** | Un ejemplo, despues tu consulta | Queres un formato especifico |
| **Few-shot** | Varios ejemplos (3+), despues tu consulta | Clasificacion, formatos fijos |
| **Chain of Thought** | Le pedis que muestre su razonamiento paso a paso | Matematicas, logica, decisiones |

### Ejemplo de Zero-shot
```
Resumi en 3 puntos el concepto de inteligencia artificial.
```

### Ejemplo de One-shot
```
Clasifica comentarios como POSITIVO, NEGATIVO o NEUTRO.

Ejemplo:
Comentario: "El producto llego roto"
Clasificacion: NEGATIVO

Ahora clasifica:
Comentario: "El servicio fue rapido pero el empaque daniado"
Clasificacion:
```

### Ejemplo de Chain of Thought
```
Resolve este problema paso a paso, mostrando cada razonamiento:
Si tengo 24 manzanas y reparto 1/3 entre 4 amigos,
cuantas manzanas le toca a cada uno?
```

**Analogia de los 4 tipos:**
- Zero-shot: "Cantame una cancion triste" (sin mostrarte ninguna)
- One-shot: Te muestro UNA foto de como doblar remeras → "todas igual"
- Few-shot: Te muestro 5 empanadas → "asi las quiero"
- Chain of Thought: "Explicame la receta mientras cocinas"

---

## 4. La plantilla Smarkdown

Smarkdown = Structured Markdown. Es escribir prompts usando sintaxis Markdown.

Copiala, edita lo que necesites, borra lo que no uses:

```markdown
## Rol
Eres [profesion/personaje] con [X anios] de experiencia en [area].

## Contexto
[Situacion. Quien sos vos. Que problema estas resolviendo.]

## Tarea
[Verbo concreto + que + para que/para quien]

## Restricciones
- Formato: [parrafo / lista / tabla / codigo]
- Tono: [formal / informal / simple / tecnico]
- Longitud: [maximo X palabras / X parrafos]
- No incluir: [X, Y, Z]
- Idioma: [espaniol]

## Ejemplo de output esperado
[Opcional: muestra del formato que queres]
```

> **Por que Markdown funciona mejor:** La IA fue entrenada con millones de documentos en Markdown (GitHub, documentacion tecnica, tutorials). Cuando estructuras tu prompt con `##`, `-`, `|`, la IA reconoce el patron y responde con mas precision.

---

## 5. Agentes: la IA con personalidad definida

Un **agente** es una IA a la que le asignas un rol fijo y una serie de instrucciones que sigue siempre. No es magia: es un system prompt que se mantiene "pegado" a cada conversacion.

### Componentes de un agente

```
┌─────────────────────────────────────────────┐
│                  AGENTE                      │
├─────────────────────────────────────────────┤
│  1. ROL FIJO — siempre el mismo personaje    │
│  2. INSTRUCCIONES — que debe hacer siempre   │
│  3. PERSONALIDAD — tono, estilo, voz         │
│  4. LIMITES — que NO debe hacer nunca         │
│  5. SKILLS — herramientas/capacidades extra  │
│  6. KNOWLEDGE — archivos o datos que "sabe"  │
└─────────────────────────────────────────────┘
```

**Analogia:** Un agente es como un empleado con un manual de procedimientos. No importa quien le hable: responde segun el manual.

### La estructura universal de un agente

```markdown
## Rol
Eres [profesion/personaje] con [X anios] de experiencia en [area].

## Contexto
Tus usuarios son [descripcion]. El objetivo es [objetivo].

## Tarea principal
- [Tarea 1]
- [Tarea 2]

## Reglas y restricciones
- [Regla 1]
- [Lo que NUNCA debe hacer]

## Formato de respuesta
[Tono, estructura, longitud esperada]

## Skills / Herramientas
- [Herramienta 1]
- [Herramienta 2]
```

> **Tip del ingeniero:** El system prompt de un agente es el 80% de su utilidad. Dedicale tiempo. Un agente con malas instrucciones es peor que ningun agente.

---

## 6. Skills: las herramientas del agente

Las **skills** son capacidades extra que le das a un agente para que haga cosas que normalmente no haria:

| Skill | Que le permite hacer | Ejemplo de uso |
|-------|---------------------|----------------|
| Busqueda web | Acceder a informacion actualizada | "Busca el precio del dolar hoy" |
| Leer archivos | Analizar PDFs, Excels, imagenes | "Resumi este PDF de 50 paginas" |
| Ejecutar codigo | Correr Python, calculos complejos | "Analiza este dataset y grafica los resultados" |
| APIs | Consultar servicios externos | "Busca vuelos a Mendoza para el finde" |
| Generar imagenes | Crear ilustraciones, diagramas | "Dibuja un diagrama de flujo de este proceso" |

**Analogia:** Las skills son las herramientas del cinturon de Batman. El agente es Batman. Las skills son el batarang, la pistola de garfio, la capa. Sin skills, es solo un tipo disfrazado.

---

## 7. Loops: cuando el agente trabaja en ciclos

Un **loop** (bucle) es el ciclo de: pensar → actuar → observar → pensar otra vez... hasta completar la tarea.

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│  PENSAR  │ ──→ │  ACTUAR  │ ──→ │ OBSERVAR │
│ (que     │     │ (ejecutar│     │ (leer el  │
│  hago?)  │ ←── │  accion) │ ←── │ resultado)│
└──────────┘     └──────────┘     └──────────┘
      ↑                                  │
      └────────── REPETIR ──────────────┘
```

### Ejemplo concreto

Le pedis a un agente: "busca vuelos baratos a Mendoza para el finde largo".

1. **Piensa:** "Necesito buscar en 3 aerolineas, comparar precios"
2. **Actua:** Llama a la API de Aerolineas Argentinas
3. **Observa:** $15,000, sale 18:30
4. **Piensa:** "Falta consultar FlyBondi y JetSmart"
5. **Actua:** Llama a las otras APIs
6. **Observa:** Ya tiene los 3 precios
7. **Piensa:** "La mas barata es JetSmart a $12,000"
8. **Accion final:** Te entrega el resultado con comparativa

### Por que importan los loops

| Sin loop | Con loop |
|----------|----------|
| 1 solo paso (A → B) | Varios pasos (A → B → C → D) |
| Bueno para tareas simples | Necesario para tareas complejas |
| Menos tokens, mas barato | Mas tokens, mas caro, mejor resultado |
| ChatGPT gratuito | Agentes con herramientas |

**Analogia:** Es como armar un rompecabezas. Sin loop, miras la caja una vez y tiras todas las piezas juntas. Con loop, probas una pieza, ves si encaja, ajustas, probas otra. Es mas lento pero el resultado es mejor.

> **Dato clave de la Clase 3:** Los loops consumen mas tokens. Cada vuelta del ciclo suma tokens a tu factura. Por eso los agentes con loops suelen estar en planes de pago.

---

## 8. Errores comunes al hacer prompts

### Error 1: El prompt vago
```
MAL:  "Explicame la IA"
BIEN: "Explica en 3 parrafos que es un LLM para alguien sin
       conocimientos tecnicos, usando una analogia cotidiana"
```

### Error 2: Pedir todo de una
```
MAL:  "Haceme un plan de negocio completo con FODA, finanzas,
       marketing y operaciones" → todo superficial

BIEN: Prompt 1: "Genera el FODA"
      Prompt 2: "Basado en el FODA, genera estrategia de marketing"
      Prompt 3: "Para la estrategia 2, desarrolla el plan operativo"
```

### Error 3: No dar contexto
```
MAL:  "Revisa este email y mejoralo" (sin contexto)

BIEN: "Revisa este email de solicitud de trabajo para el puesto X
       en una empresa del sector Y. Tono profesional pero no robotico.
       El destinatario es el jefe de RRHH."
```

### Error 4: No iterar
```
El 90% de la gente: Prompt → No le gusta → Abandona.

El ingeniero: Prompt → Resultado → "Mejora X" → Resultado 2 →
"Ajusta Y" → Resultado 3 → LISTO.
```

### Error 5: Creer que "mas largo = mejor"
Un prompt de 500 palabras sin estructura es peor que uno de 100 palabras con Smarkdown. La clave es **precision**, no extension.

---

## 9. Checklist antes y despues de cada prompt

### ANTES de enviar
- [ ] Tiene al menos Tarea + Restricciones?
- [ ] Use mi AlterEgo? (sin datos personales reales)
- [ ] Si esto se publica maniana en un diario, estaria bien?

### DESPUES de recibir
- [ ] Lei la respuesta completa (no solo el primer parrafo)?
- [ ] Verifique numeros, fechas y citas clave?
- [ ] Edite y personalice antes de usar?
- [ ] Podria defender este contenido si alguien me pregunta de donde salio?

---

## 10. Queres profundizar?

Este archivo es un resumen. El [repositorio completo](https://github.com/jorgesislema/apuntes_de_ingenieria_de_prompt) tiene 16 modulos:

- 01 — Conceptos Fundamentales (anatomia del prompt)
- 02 — Tecnicas de Prompting (zero-shot, few-shot, CoT, ReAct)
- 03 — Secretos del Maestro (tecnicas avanzadas)
- 04 — Prompting a Escala Empresarial (Salesforce, Spotify, Morgan Stanley)
- 05 — Adaptacion por Modelo (GPT, Claude, Gemini, DeepSeek, Llama)
- 06 — Preparacion para Entrevistas (+300 preguntas reales)
- 07 — Laboratorio y Ejemplos (casos practicos)
- 08 — Errores Comunes y Soluciones
- 12 — Seguridad y Defensa de Prompts
- 16 — Agentes, Skills y Loops (arquitectura de IA autonoma)

Y muchos mas. Recomendado para despues del taller.
