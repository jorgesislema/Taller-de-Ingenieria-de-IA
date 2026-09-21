# Práctica — Clase 5: El Arquitecto de Mitigación

> Ejercicio práctico: Diseñar estrategias de mitigación de alucinaciones para proyectos reales.

---

## 🎯 El Reto: Proteger el Negocio de las Alucinaciones

### Contexto

Te contratan como **Arquitecto de Mitigación** para 3 empresas que quieren implementar IA. Tu trabajo es:
1. Identificar el nivel de riesgo de cada proyecto
2. Diseñar la estrategia de mitigación correcta
3. Calcular el "Impuesto de Verificación" para cada caso

No necesitás programar. Necesitás **pensar en riesgos y diseñar soluciones**.

---

## 📋 Los 3 Proyectos

### Proyecto 1: Chatbot de Atención al Cliente para un Banco

> *"El chatbot responde preguntas sobre saldos, transferencias y productos. Si el chatbot inventa una tasa de interés o una comisión que no existe, el banco puede recibir demandas de clientes. Necesitamos que el chatbot solo diga información verificada."*

**Preguntas para pensar:**
- ¿Qué pasa si el chatbot inventa una comisión?
- ¿Qué estrategia de mitigación usarías?
- ¿Necesitás supervisión humana para cada respuesta?

---

### Proyecto 2: Asistente de Investigación para un Estudio Jurídico

> *"Los abogados usan un asistente de IA para encontrar jurisprudencia y artículos de ley relevantes para sus casos. Si el asistente inventa un artículo que no existe, el abogado puede perder un juicio basándose en información falsa."*

**Preguntas para pensar:**
- ¿Qué es más peligroso: no encontrar jurisprudencia o inventar una?
- ¿Qué benchmark te importa más: Vectara o AA-Omniscience?
- ¿Cómo diseñarías el sistema para que el abogado siempre verifique?

---

### Proyecto 3: Asistente de Recursos Humanos para una Empresa de 500 Empleados

> *"El asistente responde preguntas de los empleados sobre políticas de la empresa: vacaciones, permisos, seguros, horarios. Usa un chatbot interno. Si el asistente inventa una política que no existe, los empleados pueden quejarse o demandar."*

**Preguntas para pensar:**
- ¿Dónde están guardadas las políticas reales?
- ¿Qué técnica usarías para que el asistente solo use información real?
- ¿Cuánto costaría verificar las respuestas humana?

---

## ✍️ Tu Tarea (Individual o en Parejas)

Para cada proyecto, completá esta tabla:

| Proyecto | Nivel de Riesgo | Estrategia de Mitigación | ¿Por qué? |
|----------|----------------|------------------------|-----------|
| **1. Banco** | | | |
| **2. Estudio Jurídico** | | | |
| **3. Recursos Humanos** | | | |

### Niveles de Riesgo:
- 🔴 **Alto:** Error puede causar demandas, pérdidas financieras o daño a la salud
- 🟡 **Medio:** Error puede causar inconvenientes pero no catástrofes
- 🟢 **Bajo:** Error es molesto pero no destructivo

### Estrategias de Mitigación:
- [ ] RAG (base de datos vectorial con documentos verificados)
- [ ] Prompting restrictivo (obligar a citar fuentes)
- [ ] Circuit breakers (aislar fallos)
- [ ] Ensamblaje multi-modelo (jurado de modelos)
- [ ] HITL (supervisión humana obligatoria)
- [ ] Modelo conservador (Command A+ o similar)

---

## 🧠 Preguntas de Reflexión

1. **Si el Proyecto 1 usa HITL (revisión humana para cada respuesta), ¿cuánto tiempo humano adicional necesitaría por día?** Con 500 consultas/día y 2 minutos por revisión.

2. **En el Proyecto 2, ¿usarías RAG o solo prompting restrictivo?** ¿Por qué la combinación es mejor que solo uno?

3. **Si el Proyecto 3 tiene presupuesto de $0 para herramientas adicionales, ¿qué mitigation podrías implementar gratis?**

4. **¿En qué situación el "Impuesto de Verificación" es mayor que el beneficio de usar IA?**

5. **Si pudieras elegir UNA sola estrategia de mitigación para todos los proyectos, ¿cuál sería? ¿Por qué?**

---

## 🎯 Las Respuestas Correctas (para discutir al final)

> **⚠️ NO LEAS ESTO hasta haber completado tu tabla.**

---

### Respuesta: Proyecto 1 — Banco

**Nivel de Riesgo:** 🔴 ALTO

**Estrategia recomendada:** RAG + Prompting restrictivo + HITL para consultas financieras

**Razones:**
1. **RAG obligatorio:** El chatbot debe acceder a las políticas reales del banco desde una base de datos, no de su memoria de entrenamiento. Reduce alucinaciones 73-86%.
2. **Prompting restrictivo:** "Para cada respuesta, cita la sección y página de la política. Si no encontrás evidencia, decí 'Consulte con su asesor'."
3. **HITL para montos:** Cualquier consulta que involucre montos, tasas o comisiones debe pasar por revisión humana antes de mostrarse al cliente.
4. **Costo de verificación:** 500 consultas × 2 min = 1,000 min = ~17 horas/día de revisión humana. Si el 30% son consultas financieras, son ~5 horas/día.

---

### Respuesta: Proyecto 2 — Estudio Jurídico

**Nivel de Riesgo:** 🔴 ALTO

**Estrategia recomendada:** RAG + Ensamblaje multi-modelo + HITL obligatorio

**Razones:**
1. **RAG con base de datos de jurisprudencia:** El asistente debe buscar en una base de datos de leyes y jurisprudencia reales, no inventar artículos.
2. **Ensamblaje multi-modelo:** Usar 2-3 modelos para validar cada respuesta. Si uno inventa un artículo, los otros lo detectan.
3. **HITL obligatorio:** El abogado SIEMPRE debe verificar la jurisprudencia citada antes de usarla en un caso. La IA solo es un punto de partida.
4. **Benchmark relevante:** Vectara (fidelidad al documento) + AA-Omniscience (decir "no sé").

---

### Respuesta: Proyecto 3 — Recursos Humanos

**Nivel de Riesgo:** 🟡 MEDIO

**Estrategia recomendada:** RAG + Prompting restrictivo

**Razones:**
1. **RAG con handbook de empleados:** Cargar las políticas reales de la empresa en una base de datos vectorial. El asistente solo responde con información del handbook.
2. **Prompting restrictivo:** "Responde SOLO con información del handbook de empleados. Si la pregunta no está en el handbook, decí 'Para esta consulta, contacte a Recursos Humanos'."
3. **Sin HITL:** Dado que el riesgo es medio (no hay demandas inmediatas), se puede confiar en RAG + prompting. Si la tasa de alucinación sube del 5%, activar HITL.
4. **Costo de verificación:** $0 si el RAG funciona bien. Si se necesita HITL: 100 consultas/día × 2 min = ~3 horas/día.

---

## 📊 Ejercicio de Cálculo: El Impuesto de Verificación

Para cada proyecto, calculá cuánto cuesta verificar las respuestas de la IA:

| Proyecto | Consultas/día | Tiempo de verificación | Horas/día | Costo mensual ($8/hr) |
|----------|--------------|----------------------|-----------|---------------------|
| **1. Banco** | 500 | 2 min/consulta | ? | ? |
| **2. Jurídico** | 50 | 5 min/consulta (más complejo) | ? | ? |
| **3. RRHH** | 100 | 1 min/consulta (más simple) | ? | ? |

---

## 🏆 Criterios de Éxito

Completaste la práctica exitosamente si:
- [ ] Identificaste correctamente el nivel de riesgo de cada proyecto
- [ ] Elegiste al menos 2 estrategias de mitigación por proyecto
- [ ] Calculaste el "Impuesto de Verificación" para cada caso
- [ ] Entendés por qué HITL es obligatorio en sectores de alto riesgo
- [ ] Podés explicarle a un compañero por qué "la IA sola" nunca es suficiente para proyectos críticos

---

## 💡 Bonus: Diseñá tu propio sistema de mitigación

**Si mañana creás un proyecto de IA, ¿qué sistema de mitigación diseñarías?**

Pensá en:
1. ¿Qué tan crítico es el error en tu proyecto? (alto/medio/bajo)
2. ¿Qué estrategia usarías como base? (RAG es casi siempre la respuesta)
3. ¿Necesitás supervisión humana? ¿Para todas las respuestas o solo para las críticas?
4. ¿Cuánto cuesta la mitigación vs. cuánto cuesta un error?

Completá esta tabla:

| Tu proyecto | Nivel de riesgo | Estrategias | Costo estimado de mitigación |
|------------|----------------|-------------|------------------------------|
| | | | |
