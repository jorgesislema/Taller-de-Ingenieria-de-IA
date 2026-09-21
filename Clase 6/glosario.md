# Glosario — Clase 5: Tasa de Errores y Mitigación

> Cada término con su definición en lenguaje simple y una analogía cotidiana.

---

## A

### Alucinación (en IA)
**Qué es:** Cuando un modelo de lenguaje genera información completamente inventada pero la presenta como si fuera un hecho real, con total seguridad y coherencia lingüística.

**Analogía:** Un empleado que, cuando no sabe la respuesta, la inventa con la misma confianza que si la supiera. No te avisa que no sabe. Simplemente la dice.

### Abstención
**Qué es:** Capacidad de un modelo para negarse a responder cuando no tiene información suficiente. Modelos como Command A+ fueron diseñados para priorizar la abstención sobre la alucinación.

**Analogía:** Un empleado que dice "déjeme consultarlo y le respondo" en vez de inventar una respuesta.

---

## C

### Circuit Breaker (Cortacircuito)
**Qué es:** Mecanismo de seguridad que detecta cuando un agente de IA ha fallado y detiene la cadena de procesamiento antes de que el error se propague. Usa tipado estricto (JSON, boolean flags) para aislar fallos.

**Analogía:** El interruptor eléctrico de tu casa. Si hay un cortocircuito, se baja automáticamente antes de que se queme la instalación.

### Compound Error Rate (Tasa de Error Compuesto)
**Qué es:** La acumulación de pequeños errores a lo largo de múltiples pasos en un sistema de IA. Si cada paso tiene un 95% de éxito, 10 pasos dan un 60% de éxito total.

**Analogía:** El telephone game. 10 personas se pasan un mensaje. Cada una lo entiende al 95%. Al final, el mensaje se distorsionó irreconociblemente.

---

## E

### Ensamblaje multi-modelo
**Qué es:** Estrategia que usa varios modelos más pequeños para "vigilar" y validar las respuestas de un modelo grande. Si los modelos discrepan, se activa revisión humana.

**Analogía:** Un jurado de 3 personas en vez de un solo juez. Si 2 dicen lo mismo, es confiable. Si uno discrepa, se revisa.

---

## H

### HITL (Human-in-the-Loop)
**Qué es:** Arquitectura donde una persona humana supervisa y valida las decisiones de la IA antes de que se ejecuten. Es obligatorio en sectores de alto riesgo (legal, médico, financiero).

**Analogía:** Un piloto automático en un avión. Puede volar solo, pero el piloto humano siempre está vigilando y puede tomar el control.

### Hallucination (Alucinación)
**Qué es:** Ver Alucinación.

---

## I

### Impuesto de Verificación
**Qué es:** Costo oculto que las empresas pagan cuando dedican tiempo humano a revisar y validar la información generada por IA. Según Forrester, son 4.3 horas/semana por empleado, ~$14,200 USD/año.

**Analogía:** Como tener un empleado que trabaja gratis pero que necesita un supervisor leyendo todo lo que escribe para asegurarse de que no inventó datos.

---

## P

### Predicción del siguiente token
**Qué es:** El mecanismo fundamental de los LLMs. No "entienden" el texto: predice estadísticamente cuál es la siguiente palabra más probable. Las alucinaciones ocurren cuando la palabra más probable no es la correcta.

**Analogía:** Un predictor de texto del celular. Cuando escribís "Buenos", sugiere "días" porque es lo más probable. Pero quizás querías escribir "Buenos Aires". La IA funciona igual: siempre elige lo más probable, no lo correcto.

### Prompt restrictivo
**Qué es:** Instrucciones que obligan al modelo a citar fuentes, admitir incertidumbre o abstenerse de responder cuando no tiene evidencia. Reduce alucinaciones entre 20% y 40%.

**Analogía:** Como ponerle reglas a un empleado: "Si no sabés, decí 'no sé'. No inventes. Cita la fuente."

---

## R

### RAG (Retrieval Augmented Generation)
**Qué es:** Técnica que combina una base de datos vectorial con un modelo de lenguaje. En vez de depender de la memoria del modelo, recupera documentos verificados de una base de datos y se los pasa como contexto.

**Analogía:** Un bibliotecario que busca el libro correcto antes de que el experto responda. El experto no necesita recordar todo: solo leer lo que el bibliotecario le trajo.

### Reasoning Extendido (Razonamiento Extendido)
**Qué es:** Modo de algunos modelos que "piensan más tiempo" antes de responder, usando cadenas de razonamiento largo. Reduce alucinaciones en preguntas abiertas pero puede aumentarlas en resúmenes.

**Analogía:** Un estudiante que se toma 10 minutos para pensar antes de responder vs. uno que responde al instante.

---

## T

### Tasa de Alucinación
**Qué es:** El porcentaje de respuestas incorrectas que un modelo genera cuando no tiene la información correcta. Es la métrica más peligrosa para aplicaciones reales.

**Analogía:** Si le preguntás 100 cosas que no sabe, ¿cuántas inventa? Si dice 94, es DeepSeek V4 Pro. Si dice 14, es Command A+.
