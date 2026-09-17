# Práctica — Clase 4: El Evaluador de Modelos

> Ejercicio práctico: Usar benchmarks reales para elegir el modelo de IA correcto para un proyecto concreto.

---

## 🎯 El Reto: Elegir el Modelo para tu Proyecto

### Contexto

Te contratan como **Evaluador de Modelos** para 3 proyectos distintos. Para cada uno, tenés que:
1. Identificar qué benchmark es relevante
2. Investigar qué modelo lidera ese benchmark
3. Justificar tu elección considerando costo, velocidad y precisión

No necesitás programar. Necesitás **leer, comparar y argumentar**.

---

## 📋 Los 3 Proyectos

### Proyecto 1: Asistente Legal para un Estudio de Abogados

> *"Necesitamos un asistente que resuma contratos de 50 páginas y responda preguntas sobre cláusulas específicas. Si el asistente inventa una cláusula que no existe en el contrato, podemos perder un juicio. La fiabilidad es prioridad #1."*

**Preguntas para pensar:**
- ¿Qué es más peligroso: que el asistente no sepa algo o que invente algo?
- ¿Qué benchmark mide la capacidad de un modelo para decir "no sé"?
- ¿Qué modelo tiene la tasa de alucinación más baja?

---

### Proyecto 2: Chatbot de Atención al Cliente para una Tienda Online

> *"El chatbot debe responder preguntas frecuentes sobre envíos, devoluciones y productos. Recibe 2,000 consultas por día. El presupuesto para la API es de $50 USD/mes. Si responde mal, el cliente se va a la competencia."*

**Preguntas para pensar:**
- ¿Necesito un modelo premium o uno barato alcanza?
- ¿Qué benchmark mide la capacidad conversacional?
- ¿Cuánto cuesta cada consulta con los distintos modelos?

---

### Proyecto 3: Investigador de Laboratorio con Datos Científicos

> *"Somos un equipo de investigación biomédica. Necesitamos un asistente que analice artículos científicos, extraiga datos de estudios clínicos y genere reportes. Los datos deben ser 100% fieles al artículo original. Error tolerance: 0%."*

**Preguntas para pensar:**
- ¿Qué benchmark mide la fidelidad al documento original?
- ¿Qué modelo tiene la tasa de alucinación más baja en Vectara?
- ¿Qué pasa si el modelo alucina un dato clínico?

---

## ✍️ Tu Tarea (Individual o en Parejas)

Para cada proyecto, completá esta tabla:

| Proyecto | Benchmark relevante | Modelo elegido | ¿Por qué? (al menos 2 razones) |
|----------|-------------------|----------------|-------------------------------|
| **1. Asistente Legal** | | | |
| **2. Chatbot Tienda** | | | |
| **3. Investigador** | | | |

### Opciones de Benchmarks:
- [ ] AA-Omniscience (fiabilidad del conocimiento)
- [ ] FACTS (veracidad factual)
- [ ] Vectara (alucinaciones en resúmenes)
- [ ] SWE-bench (programación)
- [ ] MMLU-Pro (conocimiento general)
- [ ] MT-Bench (conversación)

### Opciones de Modelos (agregar otros si encontrás):
- [ ] Claude Fable 5 (Anthropic)
- [ ] GPT-5.6 Sol (OpenAI)
- [ ] Gemini 3.1 Pro (Google)
- [ ] DeepSeek V4 Pro (DeepSeek)
- [ ] Qwen3.7 Max (Alibaba)
- [ ] Command A+ (Cohere)
- [ ] Mistral Small 4 (Mistral)

---

## 🧠 Preguntas de Reflexión (para discutir en grupo)

1. **¿Qué pasaría si usáramos el mismo modelo para los 3 proyectos?** ¿Funcionaría? ¿Cuáles serían los problemas?

2. **En el Proyecto 1, ¿por qué NO usarías DeepSeek V4 Pro aunque es baratísimo?**

3. **En el Proyecto 2, ¿por qué NO usarías Claude Fable 5 aunque es el más inteligente?**

4. **¿Qué factores que NO aparecen en los benchmarks podrían cambiar tu elección?**

5. **Si el presupuesto del Proyecto 3 fuera $20 USD/mes en vez de $50, ¿cómo cambiaría tu elección?**

---

## 🎯 Las Respuestas Correctas (para discutir al final)

> **⚠️ NO LEAS ESTO hasta haber completado tu tabla.**

---

### Respuesta: Proyecto 1 — Asistente Legal

**Benchmark:** AA-Omniscience (fiabilidad del conocimiento) + Vectara (fidelidad al documento)

**Modelo recomendado:** Claude Fable 5

**Razones:**
1. **Índice AA-Omniscience más alto (40):** Cuando no sabe algo, admite su ignorancia en vez de inventar. Para un asistente legal, un dato inventado puede costar un juicio.
2. **Baja tasa de alucinación:** Claude está diseñado para abstenerse cuando no está seguro. Command A+ tiene alucinación más baja (14.2%) pero su precisión (9%) es demasiado baja para ser útil.
3. **Ventana de contexto amplia:** Puede procesar contratos de 50 páginas sin perder información.

**¿Por qué NO DeepSeek V4 Pro?** Aunque cuesta 1/10 del precio, su tasa de alucinación es 94%. En un contexto legal, eso es inaceptable.

---

### Respuesta: Proyecto 2 — Chatbot Tienda Online

**Benchmark:** MT-Bench (conversación) + costo por token

**Modelo recomendado:** GPT-5.4-nano o Claude 3 Haiku

**Razones:**
1. **Costo ultra-bajo:** GPT-5.4-nano cuesta fracciones de centavo por consulta. Con 2,000 consultas/día, el costo mensual es mínimo.
2. **Velocidad:** Los modelos pequeños responden en <1 segundo. Los clientes no esperan.
3. **Suficiente para tareas simples:** Las preguntas sobre envíos y devoluciones son repetitivas y predecibles. No necesitás razonamiento profundo.

**¿Por qué NO Claude Fable 5?** Sería como usar un Ferrari para ir al supermercado. Es brillante, pero cuesta 50x más y es más lento para tareas simples.

---

### Respuesta: Proyecto 3 — Investigador Biomédico

**Benchmark:** Vectara (fidelidad al documento) + FACTS (veracidad factual)

**Modelo recomendado:** finix_s1_32b (AntGroup) o Gemini 3 Pro

**Razones:**
1. **Vectara:** finix_s1_32b tiene la tasa de alucinación más baja (1.8%). Para datos clínicos, cada dato debe ser fiel al artículo original.
2. **FACTS Grounding:** Gemini 3 Pro lidera (~69%) en fundamentación estricta. Se ciñe al documento sin inventar.
3. **Trade-off:** Si el presupuesto es ajustado, DeepSeek-V3.2-Exp (5.3% de alucinación) es una alternativa viable.

**¿Por qué NO un modelo genérico?** Los datos biomédicos son de alta criticidad. Un dato inventado puede llevar a conclusiones erróneas en un estudio.

---

## 🏆 Criterios de Éxito

Completaste la práctica exitosamente si:
- [ ] Identificaste el benchmark correcto para cada proyecto
- [ ] Elegiste un modelo con justificación basada en métricas reales
- [ ] Explicaste por qué NO elegiste otros modelos (incluidos los "mejores" en rankings)
- [ ] Consideraste factores que los benchmarks NO miden (costo, velocidad, contexto)
- [ ] Podés explicarle a un compañero por qué "el modelo más caro" no siempre es "el mejor"

---

## 💡 Bonus: Elige tu propio proyecto

**Si mañana creás tu propio proyecto de IA, ¿qué modelo elegirías?**

Pensá en:
1. ¿Qué tipo de tareas haría? (resumir, chatear, generar código, analizar imágenes)
2. ¿Qué benchmark es más relevante para esas tareas?
3. ¿Cuál es tu presupuesto mensual?
4. ¿Necesitás que el modelo corra en local (privacidad) o en la nube (conveniencia)?

Completá esta tabla:

| Tu proyecto | Benchmark elegido | Modelo elegido | Costo estimado/mes |
|------------|-------------------|----------------|-------------------|
| | | | |
