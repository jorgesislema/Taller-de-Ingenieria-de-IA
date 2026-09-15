# Práctica — Clase 4: El Economista de la IA

> Ejercicio práctico: Calcular el costo real de un proyecto de IA y elegir la modalidad correcta.

---

## 🎯 El Reto: Presupuestar un Chatbot de Atención al Cliente

### Contexto

Una empresa de e-commerce te contrata para construir un **chatbot de atención al cliente**. Debes calcular el costo mensual y elegir la modalidad correcta.

---

## 📋 Datos del Proyecto

- **500 consultas por día** (30 días = 15,000 consultas/mes)
- Cada consulta del cliente: **200 palabras** (~267 tokens)
- Cada respuesta de la IA: **100 palabras** (~133 tokens)
- Contexto histórico: **últimas 3 interacciones** (~300 palabras = ~400 tokens)
- **Presupuesto máximo:** $100 USD/mes

---

## ✍️ Tu Tarea

### Paso 1: Calcular tokens por consulta

| Concepto | Palabras | Tokens (aprox.) |
|----------|----------|-----------------|
| Consulta del cliente | 200 | ? |
| Contexto histórico | 300 | ? |
| **Total input** | **500** | **?** |
| Respuesta de la IA | 100 | **?** |

### Paso 2: Calcular tokens mensuales

| Concepto | Tokens por consulta | × 15,000 consultas | = Tokens mensuales |
|----------|--------------------|--------------------|-------------------|
| Input | ? | × 15,000 | **?** |
| Output | ? | × 15,000 | **?** |

### Paso 3: Calcular costo con cada modelo

| Modelo | Costo Input (1M tokens) | Costo Output (1M tokens) | Costo Input mensual | Costo Output mensual | **Total mensual** | ¿Cabe en $100? |
|--------|------------------------|-------------------------|--------------------|--------------------|-------------------|----------------|
| GPT-4o | $2.50 | $10.00 | ? | ? | **?** | ? |
| GPT-4o-mini | $0.15 | $0.60 | ? | ? | **?** | ? |
| Claude 3 Haiku | $0.25 | $1.25 | ? | ? | **?** | ? |
| DeepSeek-V3 | $0.27 | $1.10 | ? | ? | **?** | ? |

### Paso 4: Justificar tu elección

Escribí por qué elegiste un modelo u otro:

| Modelo elegido | ¿Por qué? |
|---------------|-----------|
| | |

---

## 🧠 Preguntas de Reflexión

1. **Si GPT-4o cuesta $45/mes y DeepSeek-V3 cuesta $4.90/mes, ¿qué justificaría elegir GPT-4o?**

2. **¿Qué pasaría con el costo si el 10% de las consultas requieren respuestas de 500 palabras en vez de 100?**

3. **Si la empresa crece a 5,000 consultas/día, ¿cómo cambia el costo mensual?**

4. **¿Conviene mandar siempre las últimas 3 interacciones como contexto o solo cuando la consulta lo requiere?**

5. **¿En qué situación usarías un modelo local (Ollama) para este proyecto?**

---

## 🎯 Respuesta Esperada

| Modelo | Input mensual | Output mensual | **Total** | ¿Cabe en $100? |
|--------|--------------|----------------|-----------|----------------|
| GPT-4o | $10.00 | $20.00 | **$30.00** | ✅ Sí |
| GPT-4o-mini | $0.60 | $1.20 | **$1.80** | ✅ Sobrado |
| Claude 3 Haiku | $1.00 | $2.50 | **$3.50** | ✅ Sobrado |
| DeepSeek-V3 | $1.08 | $2.20 | **$3.28** | ✅ Sobrado |

> **Lección:** GPT-4o-mini cuesta **16x menos** que GPT-4o para esta tarea. Y la calidad de las respuestas probablemente sea igual de buena para preguntas simples sobre envíos y devoluciones.

---

## 🏆 Criterios de Éxito

Completaste la práctica exitosamente si:
- [ ] Calculaste correctamente los tokens de input y output
- [ ] Calculaste el costo mensual con al menos 2 modelos
- [ ] Elegiste un modelo con justificación basada en costo y calidad
- [ ] Entendés que "el más caro" no siempre es "el mejor"
- [ ] Podés explicar por qué el contexto histórico es costoso
