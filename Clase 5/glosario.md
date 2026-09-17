# Glosario — Clase 4: Benchmarks y Selección de Modelos

> Cada término con su definición en lenguaje simple y una analogía cotidiana.

---

## A

### Accuracy (Tasa de Aciertos)
**Qué es:** El porcentaje de respuestas correctas de un modelo sobre el total de preguntas. Es la métrica más tradicional y simple.

**Analogía:** Si un estudiante responde 80 preguntas bien de 100, su accuracy es 80%. No dice nada sobre si las 20 que falló las inventó o si simplemente no sabía.

### AA-Omniscience
**Qué es:** Benchmark que evalúa la fiabilidad del conocimiento de un modelo. Otorga +1 por acierto, -1 por alucinación, 0 si el modelo dice "no sé". Su índice va de -100 a 100.

**Analogía:** Un examen donde te castigan por adivinar. Si no sabés, es mejor quedarte callado que inventar una respuesta.

---

## B

### Benchmark
**Qué es:** Prueba estandarizada diseñada para evaluar una capacidad específica de un modelo de IA. Contiene miles de preguntas con respuestas conocidas.

**Analogía:** Un examen de oposición. Todos rinden la misma prueba, y los puntajes permiten comparar objetivamente quién sabe más de qué.

---

## C

### Contaminación de datos
**Qué es:** Cuando un modelo fue entrenado con las mismas preguntas que aparecen en un benchmark, inflando artificialmente su puntaje. Es como dar el examen con las respuestas en la mesa.

**Analogía:** Un alumno que robó el examen antes de la fecha. Sacó 10, pero no sabe nada.

---

## F

### FACTS
**Qué es:** Benchmark creado por Google DeepMind que evalúa la veracidad factual de los modelos a través de 4 sub-pruebas: fundamentación, conocimiento paramétrico, búsqueda y multimodal.

**Analogía:** Un examen de(option) culto general donde te preguntan datos concretos: "¿En qué año fue la batalla de X?" Si inventás la fecha, perdés puntos.

---

## H

### Hallucination Rate (Tasa de Alucinación)
**Qué es:** El porcentaje de veces que un modelo genera información incorrecta cuando no está seguro de la respuesta. Es la métrica más peligrosa para aplicaciones reales.

**Analogía:** Un empleado que, cuando no sabe la respuesta, se la inventa con total seguridad en vez de decir "déjeme consultarlo".

### HLE (Humanity's Last Exam)
**Qué es:** Benchmark diseñado con preguntas de dificultad experta, deliberadamente difícil de saturar. Mide el rendimiento en el límite de la capacidad del modelo.

**Analogía:** Un examen de doctorado tan difícil que ningún estudiante ha sacado más de 65%.

---

## I

### Índice AA-Omniscience
**Qué es:** La métrica principal de AA-Omniscience. Suma +1 por acierto, resta -1 por alucinación, y da 0 si el modelo se abstiene. Rango: -100 a 100. Un índice positivo significa que el modelo acierta más de lo que alucina.

**Analogía:** Un puntaje donde ser honesto ("no sé") es mejor que arriesgarse y equivocarse.

---

## M

### MMLU (Massive Multitask Language Understanding)
**Qué es:** Benchmark que evalúa conocimiento general en 57 materias: ciencias, humanidades, matemáticas, derecho, etc. Es el benchmark de "cultura general" más conocido.

**Analogía:** Un examen de ingreso a la universidad que cubre todas las materias del colegio secundario.

### Multimodal
**Qué es:** Capacidad de un modelo para procesar y generar no solo texto, sino también imágenes, audio y video. Un benchmark multimodal evalúa esta capacidad.

**Analogía:** Un empleado que solo sabe leer (texto) vs. uno que también sabe interpretar gráficos, fotos y diagrams (multimodal).

---

## P

### Precisión (Accuracy)
**Qué es:** Ver Accuracy.

---

## R

### Razonamiento extendido (Extended Reasoning)
**Qué es:** Modo de algunos modelos (como GPT-5.5 Pro) que "piensan más tiempo" antes de responder, usando cadenas de razonamiento largo. Reduce alucinaciones en preguntas abiertas pero puede aumentarlas en resúmenes.

**Analogía:** Un estudiante que se toma 10 minutos para pensar antes de responder vs. uno que responde al instante. El primero acierta más en problemas difíciles, pero a veces se complic la respuesta en tareas simples.

---

## S

### Saturación de benchmarks
**Qué es:** Cuando los modelos alcanzan puntajes tan altos (>95%) en un benchmark que ese benchmark deja de ser útil para diferenciarlos. Los datos de entrenamiento de los modelos pueden haber incluido las preguntas del benchmark.

**Analogía:** Un examen donde todos sacan 10. No sirve para elegir al mejor, porque todos parecen iguales.

### SWE-bench
**Qué es:** Benchmark que evalúa la capacidad de un modelo para resolver problemas reales de ingeniería de software extraídos de repositorios de GitHub. Es el estándar para medir capacidades de programación en el mundo real.

**Analogía:** En vez de preguntar "¿qué es un bucle for?", te dan un programa con un error real y te piden que lo arreglés. Es la diferencia entre un examen teórico y un examen práctico.

---

## V

### Vectara
**Qué es:** Benchmark especializado en medir la tasa de alucinaciones de modelos al resumir documentos. Usa su propio modelo juez (HHEM) para verificar si el resumen es fiel al texto original.

**Analogía:** Un editor que compara tu resumen con el artículo original y señala cada cosa que inventaste.

### Ventana de contexto
**Qué es:** La cantidad máxima de tokens que un modelo puede "recordar" en una sola conversación. Desde 4K hasta 1M tokens. Affects directamente el costo y la calidad de las respuestas.

**Analogía:** El tamaño de la pizarra donde escribís todo lo que dice el cliente. Si la pizarra se llena, lo que estaba al principio se borra.
