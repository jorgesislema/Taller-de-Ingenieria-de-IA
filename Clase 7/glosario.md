# Glosario — Clase 7: Ingeniería de Prompts Profesional

> Cada término con una definición en lenguaje sencillo y una analogía cotidiana.

---

## A

### Alucinación
**Qué es:** Una respuesta que parece segura, pero contiene información inventada o incorrecta. Puede ocurrir cuando el modelo no tiene suficiente información o intenta completar un patrón estadístico.

**Analogía:** Una persona que, cuando no sabe la respuesta, completa el espacio con una suposición y la dice con seguridad.

---

### Autoatención (self-attention)
**Qué es:** Mecanismo de un modelo Transformer que permite comparar tokens entre sí para calcular qué información es relevante para cada uno. En una versión causal, cada token puede usar los tokens anteriores, pero no los futuros.

**Analogía:** En una conversación, cada persona escucha lo que dijeron los demás y ajusta su interpretación usando ese contexto.

---

## C

### CO-STAR
**Qué es:** Plantilla de seis elementos para organizar un prompt: **C**ontexto, **O**bjetivo, **S**tilo, **T**ono, **A**udiencia y **R**espuesta. Es una ayuda para no olvidar partes importantes; no es un estándar universal.

**Analogía:** Como una lista de apartados de una receta: si falta un ingrediente, el resultado puede quedar incompleto.

### Contexto
**Qué es:** La información que rodea a una palabra o a una instrucción: situación, antecedentes, público, objetivo y restricciones. El modelo usa esa información para ajustar su representación y su respuesta.

**Analogía:** “Gato” puede describir un animal o una herramienta. Las palabras que lo rodean funcionan como el contexto de una fotografía.

### Criterio de éxito
**Qué es:** Una condición observable que permite decidir si una respuesta cumple lo que pediste. Puede ser una cantidad, un formato, un tono, un límite de palabras o un dato verificable.

**Analogía:** Es la regla con la que revisás una cocina: no alcanza con decir “se ve bien”; verificás si está caliente, completo y servido en el recipiente correcto.

---

## D

### Dimensión
**Qué es:** El tamaño de un vector. Por ejemplo, `dₖ = 64` indica que cada vector de clave (key) tiene 64 números. Una dimensión no es una palabra ni una idea: es una coordenada dentro de una representación matemática.

**Analogía:** Es como una ficha con varias casillas. Cuantas más casillas tiene la ficha, más detalles numéricos puede guardar, aunque no siempre sean útiles para cada tarea.

---

## E

### Embedding
**Qué es:** Representación de un token o de un texto mediante una lista de números. El embedding inicial de un token es fijo dentro de un mismo modelo, pero su representación contextual cambia según el texto que lo rodea.

**Analogía:** Es una ficha de identidad matemática. La misma persona puede tener una ficha inicial y una ficha diferente en cada situación porque sus compañeros cambian.

### Estado oculto contextual
**Qué es:** Representación interna de un token después de combinar su información inicial con señales de los tokens relevantes. No es una traducción directa de su significado, sino una representación matemática que ayuda a predecir lo siguiente.

**Analogía:** Es como comprender una palabra en una oración: “gato” no queda aislado; se relaciona con “duerme”, “hidráulico” o “taller”.

---

## H

### Harness
**Qué es:** Estructura que conecta a un agente con sus herramientas, instrucciones, estado y ciclo de ejecución. En la Clase 8 veremos cómo se organiza.

**Analogía:** Es el tablero de control que coordina a una persona y sus herramientas para completar un trabajo.

---

## K

### Key (clave)
**Qué es:** Proyección vectorial que describe qué información ofrece un token para ser comparada con las queries de otros tokens. En la fórmula de atención se representa con `K`.

**Analogía:** Es la etiqueta de un libro: le permite al catálogo compararlo con la pregunta del lector.

---

## M

### Máscara causal
**Qué es:** Regla que impide que un token use información de tokens que aparecen después en la secuencia. Se usa para impedir que el modelo use tokens futuros al predecir el siguiente token.

**Analogía:** Como leer una frase sin mirar todavía las palabras que vienen después.

### Mezcla de expertos (MoE)
**Qué es:** Arquitectura en la que un enrutador puede activar solo algunos módulos especializados, llamados expertos, para una parte de la entrada. Una instrucción como “actúa como” no garantiza que se active un experto específico.

**Analogía:** Es como un director que envía cada trabajo al especialista más adecuado, pero no siempre elige al mismo especialista para todas las tareas.

---

## P

### Parámetro de muestreo
**Qué es:** Valor que modifica cómo el modelo elige el siguiente token a partir de su distribución de probabilidades. No agrega conocimiento al modelo ni cambia sus pesos; cambia el margen para explorar alternativas.

**Analogía:** Es el dial de volumen de una radio: no cambia la canción, pero sí cuánto se escucha una opción frente a otra.

### Prompt
**Qué es:** Instrucción o pregunta que le escribís a un modelo para obtener una respuesta. Un prompt profesional incluye contexto, objetivo, restricciones y formato.

**Analogía:** Es una orden de trabajo: cuanto más clara es, menos tiene que adivinar la persona que la recibe.

### RIPPLE
**Qué es:** Método propio de esta clase para iterar un prompt: **R**edactá, **I**nspeccioná, **P**reguntate, **P**erfeccioná, **L**anzá y **E**valuá. Se usa para cambiar una variable por vez y comparar resultados.

**Analogía:** Es como ajustar una receta: cambiás un ingrediente, probás y observás si el plato mejora, en lugar de modificar todos los ingredientes sin medir nada.

### RTF
**Qué es:** Plantilla rápida de tres elementos: **R**ole o rol, **T**ask o tarea y **F**ormat o formato. Es útil para probar una solicitud sencilla.

**Analogía:** Como una orden breve: quién hace, qué hace y cómo entrega el resultado.

---

## Q

### Query (consulta)
**Qué es:** Proyección vectorial que indica qué información busca un token para compararse con las keys. En la fórmula de atención se representa con `Q`.

**Analogía:** Es la pregunta del lector que se compara con las etiquetas de los libros del catálogo.

---

## S

### Softmax
**Qué es:** Función que convierte un conjunto de puntuaciones en pesos aproximados que suman 1. En la atención, esos pesos indican cuánto se mezcla el valor de cada token en la representación contextual.

**Analogía:** Es como repartir 100 puntos entre varias opciones: si una opción recibe 70 puntos, pesa más que una que recibe 10.

---

## T

### Temperature
**Qué es:** Parámetro que modifica la distribución de candidatos al elegir el siguiente token. Una temperatura baja concentra más la distribución; una alta puede producir mayor variedad. No garantiza que la respuesta sea verdadera.
**Analogía:** Es un dial entre una respuesta segura y una más arriesgada, pero nunca convierte una suposición en un hecho.

### Token
**Qué es:** Unidad de texto que el modelo procesa. Puede ser una palabra, una parte de una palabra, un espacio o un signo de puntuación. El mismo texto puede dividirse de maneras distintas según el tokenizador.

**Analogía:** Es como cortar una frase en fichas pequeñas: una ficha puede contener una palabra completa o solamente una parte.

### Tokenización
**Qué es:** Proceso de dividir el texto en tokens. La cantidad y la forma de los tokens influyen en el costo, el límite de contexto y la representación de la entrada.

**Analogía:** Es como leer una factura y separarla en conceptos: nombre, fecha, importe y descripción.

### Top-K
**Qué es:** Método de muestreo que limita la elección a los `K` tokens más probables. `K` es una cantidad de tokens, no de palabras, y su efecto depende del modelo.

**Analogía:** Es como elegir solo las cinco opciones con mejor puntaje de una lista.

### Top-P
**Qué es:** Método de muestreo por núcleo que ordena las probabilidades y conserva el conjunto mínimo de candidatos que alcanza una masa de probabilidad acumulada. El conjunto exacto depende de cada paso y de cada modelo.

**Analogía:** Es como reunir opciones hasta cubrir el 90 % de las probabilidades disponibles, sin abrir el abanico a todas.

### Transformer
**Qué es:** Arquitectura de modelos de lenguaje que usa mecanismos como la autoatención para combinar información de los tokens y representar el contexto.

**Analogía:** Es una organización en la que cada palabra recibe un informe de las palabras relevantes y actualiza su representación.

### Transpuesta
**Qué es:** Operación que intercambia filas y columnas de una matriz. En la fórmula de atención, `Kᵀ` hace coincidir las dimensiones internas de `Q` y `Kᵀ`.

**Analogía:** Es como girar una tabla: las columnas pasan a ser filas.

---

## V

### Value (valor)
**Qué es:** Proyección vectorial que aporta la información que se combina usando los pesos de atención. En la fórmula de atención se representa con `V`.

**Analogía:** Es el contenido del libro: si el título resulta relevante, el catálogo puede usar ese contenido con mayor peso.

---

## Términos de apoyo

### B2B
**Qué es:** Sigla de “business to business”, es decir, ventas o soluciones para empresas.

### CTO
**Qué es:** Sigla de “chief technology officer”, en español, director o directora de tecnología.

### Fintech
**Qué es:** Empresa o solución que combina tecnología y servicios financieros.

### Startup
**Qué es:** Empresa emergente, generalmente creada para desarrollar una idea innovadora y escalar rápidamente.

### CRM
**Qué es:** Sigla de “customer relationship management”, un sistema para organizar relaciones con clientes.

### SaaS
**Qué es:** Sigla de “software as a service”, software que se usa mediante una suscripción o acceso en línea.

### SPIN
**Qué es:** Método de venta consultiva basado en preguntas sobre Situación, Problema, Implicación y Necesidad de compra.

---

> **La idea central:** una palabra puede conservar su embedding inicial y cambiar su representación cuando recibe información de las palabras que la rodean.
