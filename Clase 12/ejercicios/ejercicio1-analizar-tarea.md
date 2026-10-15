# Ejercicio 1: Analizar una Tarea y Decidir si Necesita un Prompt, Skill o Agente

> **Objetivo:** Practicar la decisión fundamental de elegir la solución proporcional al problema.  
> **Tiempo estimado:** 15 minutos.  
> **Materiales:** Esta guía, un caso de negocio real o imaginado, acceso a la PLANTILLA-SKILL.md y la PLANTILLA-AGENTE.md.

---

## Instrucciones

1. **Lee** el caso de negocio a continuación.
2. **Responde** a las preguntas guía.
3. **Documenta** tu decisión usando la estructura mental (no es necesario llenar todos los campos de la plantilla aún, solo decidir el tipo de solución).
4. **Compara** con un compañero si está disponible y discute las diferencias.

---

## Caso de Negocio: Atención al Cliente de una Panadería

### Contexto
"Elena" gestiona las solicitudes de clientes para la panadería "El Buen Pan". Recibe entre 10 y 30 solicitudes semanales mediante formulario web, correo electrónico y teléfono. Cada solicitud incluye:
- Tipo de producto(s) solicitado(s)
- Cantidad deseada
- Nombre o razón social del cliente
- Si el cliente es de una empresa o una fiesta familiar/uso personal

### Tareas que Elena actualmente realiza manualmente:
1. Leer cada solicitud.
2. Determinar si el cliente es persona o empresa.
3. Buscar los precios correspondientes (unitarios o al por mayor).
4. Aplicar los descuentos por cantidad según la tabla.
5. Calcular subtotal, descuentos y total.
6. Redactar un pequeño texto de justificación.
7. Determinar si la proforma requiere aprobación humana antes de enviar.

---

## Preguntas Guía

Responde por escrito (o en discusión con tu grupo):

### A. Clasificación de la Tarea
1. ¿Esta tarea es **puntual** (sucede una vez) o **repetitiva** (se realizará varias veces)?
2. ¿La tarea tiene **dependencias externas** (consultar precios, acceder a archivos, usar herramientas) o es **autónoma** con los datos siempre iguales?
3. ¿La tarea requiere **decisiones intermedias** (elegir entre varias opciones) o sigue un **procedimiento único y fijo**?

### B. Elección de Solución
2. Basado en tus respuestas a A, ¿cuál solución inicial recomiendas?
   - **Prompt:** Una instrucción aislada para una sola ejecución.
   - **Skill:** Un procedimiento empaquetado y reutilizable.
   - **Agente:** Un sistema que coordina pasos, decide herramientas y puede solicitar intervención humana.

3. Justifica tu elección en una frase: "Elegiría [prompt/skill/agente] porque..."

### C. Fundamento
4. ¿Qué componente(s) clave serían necesario(s) para tu solución elegida?
   - Si elegiste **prompt**: ¿un texto de instrucciones bien estructurado?
   - Si elegiste **skill**: ¿entradas definidas, procedimiento, formato de salida, validaciones?
   - Si elegiste **agente**: ¿objetivo, skills disponibles, herramientas, condiciones de decisión, validación, aprobación humana?

5. ¿Cuál es el **riesgo más alto** si eliges la opción incorrecta?
   - Usar prompt cuando se necesita reutilización → repetir trabajo una y otra vez.
   - Usar skill cuando se necesitan decisiones complejas → clasificación incorrecta o cálculos erróneos.
   - Usar agente cuando una skill basta → complejidad innecesaria, más puntos de fallo, costo mayor.

---

## Estructura de Registro

Completa este formato y guárdalo en tu carpeta de práctica:

```
Caso: [Breve descripción de tu caso, ej. "Atención al cliente panadería"]
Fecha: [Fecha de realización]

### Decisión
Tipo de solución elegida: [prompt / skill / agente]

### Justificación (máximo 2 líneas)
[Tu razón principal en una frase]

### Componentes Mínimos Necesarios
[Lista solo lo esencial que necesitabas para tu solución]

### Riesgo si se eligiera incorrectamente
[Un riesgo clave identificado]

### Comentario de reflexión
[Qué aprendiste al comparar con compañeros o al revisar la plantilla]
```

---

## Solución Esperada (para autocomparación)

Después de intentar el ejercicio, revisa esta guía de solución esperada:

**Análisis del caso:**
- La tarea es **repetitiva** (se recibe entre 10-30 solicitudes semanalmente).
- Tiene **dependencias externas** (consultar precios, aplicar descuentos, acceder a archivo de precios).
- Requiere **decisiones intermedias** (clasificar cliente, elegir ruta de precios, aplicar descuentos correctos).

**Solución recomendada: Skill**
- **Por qué:** La tarea se repite con estructura similar, requiere procedimiento estandarizado y tiene dependencias claras (archivo de precios, reglas de descuento). Una skill permite reutilizar el procedimiento una y otra vez con consistencia.
- **Componentes mínimos:** Entradas (tipo cliente, productos, cantidades), dependencia (archivo-precios.md), procedimiento (clasificar, consultar precios, calcular totales), validaciones (formatos, reglas de negocio, factual), salida (tabla + totales + justificación).
- **Riesgo si se eligiera incorrectamente:**
  - *Si se usara prompt:* Elena tendría que redactar la misma instrucción para cada una de las 10-30 solicitudes semanales, desperdiciando tiempo y corroyendo consistencia.
  - *Si se usara agente:* Diseñar un agente para solo clasificar y calcular sería sobreingeniería: más componentes, más posibilidades de fallo, costo de mantenimiento mayor sin necesidad real.

**Tu reflejo:** "Al comparar con compañeros, vi que algunos propusieron agente por considerar el 'factor humano' de aprobación, pero al revisar la plantilla de skill comprendí que las validaciones y la acción sensible (aprobación de proforma) podían manejarse como un paso dentro de la skill en sí, sin necesidad de un agente completo."

---
*Ejercicio diseñado para la Clase 12: Agentes y Skills - Taller de Ingeniería IA. Base en caso de atención al cliente panadería.*