# Glosario — Clase 8: Skills, Agentes, Loops, Harness

> Cada término con su definición en lenguaje simple y una analogía cotidiana.

---

## A

### Agente
**Qué es:** Un sistema que piensa, actúa y observa en ciclos hasta resolver un problema. No es solo un chatbot: tiene autonomía para tomar decisiones y usar herramientas.

**Analogía:** Como un asistente personal que no solo responde preguntas, sino que busca información, ejecuta tareas y te informa los resultados.

---

## B

### Backoff Exponencial
**Qué es:** Estrategia de reintentos donde el tiempo de espera se duplica cada vez que falla. Intento 1: 2s, Intento 2: 4s, Intento 3: 8s.

**Analogía:** Como cuando llamás a un servicio técnico y si no te atienden, esperás más tiempo antes de volver a llamar.

---

## E

### Embedding
**Qué es:** Representación numérica de un texto como un vector (lista de números). Permite comparar similitud semántica entre documentos.

**Analogía:** Como una huella digital del texto: textos similares tienen huellas similares.

---

## F

### Function Calling
**Qué es:** Capacidad de un LLM para llamar a funciones externas definidas por el desarrollador. El modelo decide qué función ejecutar según la solicitud del usuario.

**Analogía:** Como un chef que, según el pedido, decide si usa el horno, la sartén o la licuadora.

---

## H

### Harness
**Qué es:** Capa de protección que envuelve a un agente para que funcione en producción. Incluye retry, límites de pasos y logging.

**Analogía:** Como el cinturón de seguridad de un auto: no cambia cómo maneja, pero te protege si algo sale mal.

---

## L

### Loop
**Qué es:** Ciclo repetitivo de ejecución. En agentes, el loop Think→Act→Observe se repite hasta resolver el problema o alcanzar un límite.

**Analogía:** Como una receta de cocina que se repite: mirar la receta, hacer un paso, verificar el resultado, repetir.

---

## R

### Retry
**Qué es:** Reintentar una operación que falló. Generalmente con un límite máximo de intentos y tiempo de espera entre ellos.

**Analogía:** Como cuando intentás abrir una puerta que está trabada: la forzás una vez, dos veces, y a la tercera buscás otra puerta.

---

## S

### Skill
**Qué es:** Un prompt empaquetado con metadata (nombre, versión), template (el prompt reutilizable) y examples (ejemplos few-shot). Es un componente versionado como código.

**Analogía:** Como una receta de cocina guardada en una libreta: tiene nombre, ingredientes, pasos y ejemplos de cómo debe quedar el plato.

---

## T

### Think→Act→Observe
**Qué es:** El ciclo fundamental de un agente. THINK: el modelo razona qué hacer. ACT: ejecuta una acción. OBSERVE: evalúa el resultado. Se repite hasta resolver.

**Analogía:** Como resolver un laberinto: mirar el mapa (think), dar un paso (act), verificar si es el camino correcto (observe), repetir.
