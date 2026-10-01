# Glosario — Clase 9: Function Calling / Tool Use

> Cada término con su definición en lenguaje simple y una analogía cotidiana.

---

## F

### Function Calling
**Qué es:** Capacidad de un LLM para llamar a funciones externas definidas por el desarrollador. El modelo decide qué función ejecutar según la solicitud del usuario.

**Analogía:** Como un chef que, según el pedido, decide si usa el horno, la sartén o la licuadora.

---

## J

### JSON Schema
**Qué es:** Formato para definir la estructura de datos de una función: nombre, descripción, parámetros y tipos. Es el "contrato" entre el LLM y la herramienta.

**Analogía:** Como una ficha técnica de un electrodoméstico: dice qué hace, qué botones tiene y qué pasa si los presionás.

---

## R

### Router
**Qué es:** Componente que decide qué herramienta ejecutar según la solicitud del usuario. Evalúa el prompt, selecciona la función correcta y extrae los parámetros.

**Analogía:** Como un centralista de emergencias: recibe la llamada, evalúa qué servicio necesitás (bomberos, ambulancia, policía) y despacha al correcto.

---

## T

### Tool
**Qué es:** Herramienta externa que un LLM puede ejecutar. Puede ser una función simple (calculadora), una API (clima) o un servicio complejo (base de datos).

**Analogía:** Como las herramientas de un taller: cada una tiene un uso específico (martillo, destornillador, llave inglesa).

### Tool Use
**Qué es:** El acto de usar una herramienta externa desde un LLM. Incluye: seleccionar la herramienta, pasar parámetros y recibir resultados.

**Analogía:** Como usar un GPS: le decís a dónde vas (prompt), él calcula la ruta (function calling) y te da instrucciones (respuesta).
