# Glosario — Clase 4: Tokens, Costos y Modalidades

> Cada término con su definición en lenguaje simple y una analogía cotidiana.

---

## A

### API (Application Programming Interface)
**Qué es:** Ventanilla de pedidos. Tu programa se conecta directamente al modelo de IA sin pasar por un navegador. Es la única forma profesional de construir productos con IA.

**Analogía:** Pedir por delivery en vez de ir a comer al salón del restaurante. No ves el local, pero recibís la comida en tu casa. Y pagás por cada plato.

---

## C

### Context Window (Ventana de Contexto)
**Qué es:** La cantidad máxima de tokens que un modelo puede "recordar" en una sola conversación. Cuando se llena, lo más viejo se borra sin avisar.

**Analogía:** Un pizarrón. Todo lo que se dice se escribe. Cuando se llena, borras lo más viejo para hacer espacio. Si una decisión importante estaba al principio, se perdió.

---

## I

### Input (Tokens de Entrada)
**Qué es:** Lo que vos le escribís a la IA. Son los tokens que consumís al enviar un prompt. Son más baratos que el output.

**Analogía:** La materia prima que le llega a una fábrica. Rápida y barata de procesar.

---

## L

### Latencia
**Qué es:** El tiempo que tarda la IA en responder. Varía según el modelo: desde 0.5 segundos (Haiku) hasta 7 segundos (DeepSeek).

**Analogía:** El tiempo que esperás en una fila. Si es corto, no pasa nada. Si es largo, el cliente se va.

---

## M

### Modalidad
**Qué es:** La forma en que te conectás a la IA. Son 3: Chat (navegador), API (programa), Local (tu computadora). Cada una tiene ventajas y costos distintos.

**Analogía:** Cómo comprás un producto: en tienda (Chat), por internet (API) o lo fabricás en casa (Local).

---

## O

### Output (Tokens de Salida)
**Qué es:** Lo que la IA te responde. Son los tokens que genera el modelo. Cuestan 3-5x más que el input porque generar texto es más caro que leerlo.

**Analogía:** El producto terminado de una fábrica. Requiere más tiempo, energía y maquinaria que recibir la materia prima.

---

## P

### Parámetros
**Qué es:** Los números ajustables del modelo que se calibraron durante el entrenamiento. Más parámetros = más capacidad pero más costo.

**Analogía:** Las conexiones entre neuronas del cerebro. Un modelo de 8B parámetros tiene 8 mil millones de conexiones.

---

## R

### Rate Limits (Límites de tasa)
**Qué es:** La cantidad máxima de pedidos que podés hacer a la API por minuto. Si los excedes, tu aplicación recibe un error y se cae.

**Analogía:** Las cabinas de peaje de una autopista. Si llegan más autos de los que pueden pasar, se forma una cola.

---

## T

### Token
**Qué es:** La unidad mínima por la que te cobra una IA. No es una palabra ni una letra: es un trozo de texto al que se le asigna un número. 1 token ≈ 0.75 palabras en español.

**Analogía:** El gramo en una carnicería. No pagás por "plato" (palabra), pagás por "gramo" (token). Algunas palabras son livianas (1 token), otras pesadas (3 tokens).

### Tokenización
**Qué es:** El proceso de partir un texto en tokens. Un tokenizador (programa dentro del modelo) divide el texto en pedazos que ya conoce.

**Analogía:** Un carnicero que corta la carne. No corta vaca por vaca: corta en trozos que ya conoce de su catálogo.
