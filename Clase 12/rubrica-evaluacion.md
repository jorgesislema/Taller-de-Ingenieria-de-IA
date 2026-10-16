# Rúbrica de Evaluación - Clase 12: Agentes y Skills (Sobresaliente sobre 100 puntos)

> **Objetivo:** Esta rúbrica evalúa el trabajo del alumno en el diseño de skills y agentes utilizando las plantillas profesionales. Cada área tiene un peso específico y define qué significa "aceptable" vs "necesita mejorar".

---

## Desglose de 100 Puntos

### 1. Requisitos (20 puntos posibles)

| Puntuación | Criterios |
|---|---|
| **18-20 puntos** | *Todos* los campos `*` de ambas plantillas (Skill y Agente) están completos sin excepciones. El problema está definido, el alcance es claro y las entradas/salidas están especificadas con tipos y restricciones. |
| **15-17 puntos** | Casi todos los campos `*` completados; quizás 1-2 campos opcionales o de mantenimiento faltan. El problema está definido y el alcance es mayormente claro. Las entradas/salidas tienen tipos mayormente especificados. |
| **10-14 puntos** | Varios campos `*` vacíos o con "pending". El problema tiene parte definida pero el alcance es vago. Las entradas/salidas tienen tipos parcialmente especificados. |
| **0-9 puntos** | Muchos campos `*` vacíos o con "copiar del ejemplo". El problema no está claramente definido. Las entradas/salidas no tienen tipos especificados. |

### 2. Calidad de la Skill (20 puntos posibles)

| Puntuación | Criterios |
|---|---|
| **18-20 puntos** | La skill tiene procedimiento secuencial atómico y descriptivo. Validaciones completas (formato, reglas de negocio, factual, consistencia). Tratamiento de errores para todos los escenarios previstos (campo ausente, datos contradictorios, herramienta falla, entrada inválida, límite superado). Formato de salida estructurado con todos los elementos definidos. Casos de prueba mínimos (5 casos) incluidos y coherentes. |
| **15-17 puntos** | Procedimiento secuencial definido pero algunos pasos son descriptivos en lugar de atómicos. Validaciones presentes pero quizá falta uno de los tipos (formato o reglas de negocio). Tratamiento de errores para 3-4 escenarios. Formato de salida definido pero quizá falta algún elemento. Casos de prueba incluidos (3-4 casos). |
| **10-14 puntos** | Procedimiento secuencial general. Validaciones básicas presentes. Tratamiento de errores para 1-2 escenarios. Salida definida pero falta estructura. Pocos casos de prueba (1-2 casos). |
| **0-9 puntos** | Procedimiento secuencial ausente o muy general. Pocas o ninguna validación. Tratamiento de errores inexistente o muy básico. Salida sin estructura definida. Pocos o ningún caso de prueba. |

### 3. Diseño del Agente (20 puntos posibles)

| Puntuación | Criterios |
|---|---|
| **18-20 puntos** | El agente tiene objetivo medible y problema definido claramente. Alcance con tareas incluidas/excluidas especificar. Límites de pasos y tiempo definidos con valores. Condiciones de finalización explícitas. Instrucciones principales con todos los aspectos (objetivo general, tono, prioridad, incertidumbre, interacción). Fuentes requeridas y principales definidas. Skills disponibles y condiciones para utilizarlas especificar. Herramientas con permisos y restricciones claros. Flujo de decisión con pasos y condiciones de transición definidos. Validaciones de resultados de los 4 tipos (formato, regla de negocio, factual, consistencia). Acciones que requieren autorización humana listadas y explicadas. Protecciones contra instrucciones maliciosas documentadas. Privacidad, mínimo privilegio y gestión de secretos especificados. Registros, trazabilidad y supervisión definidos. Pruebas funcionales, adversariales y de regresión incluidas (mínimo 5). Métricas de calidad, coste, latencia y tasa de fallos especificar. Procesos de despliegue, recuperación, mantenimiento y versionado detallados. |
| **15-17 puntos** | La mayoría de aspectos definidos pero quizás falta algún sub-campo específico. La mayoría de listas tienen elementos pero quizás 1-2 falten. La mayoría de validaciones presentes pero quizá 1-2 tipos falten. La mayoría de procesos descritos pero quizá algún paso con más detalle. |
| **10-14 puntos** | Varios aspectos definidos parcialmente. Algunas listas incompletas. Válidaciones básicas presentes. Algunos procesos descritos de forma general. |
| **0-9 puntos** | Varios aspectos clave ausentes (objetivo, alcance, habilidades, herramientas). Pocas o ninguna validación. Pocos o ningún caso de prueba. Métricas o procesos de mantenimiento faltantes. |

### 4. Seguridad (15 puntos posibles)

| Puntuación | Criterios |
|---|---|
| **13-15 puntos** | Protecciones contra inyección de instrucciones, fuga de datos, permisos excesivos y acciones no autorizadas están documentadas y tienen mecanismo de implementación sugerido. Principio de mínimo privilegio explícito. Gestión de secretos especificada (sin credenciales en documento). Acciones sensibles siempre requieren aprobación humana definida y explicada. |
| **10-12 puntos** | La mayoría de protecciones documentadas. Algunos mecanismos de implementación descritos. Mínimo privilegio mencionado pero quizá sin detalle. Gestión de secretos básica (quizá con alguna referencia). Acción sensible requiere aprobación pero quizás sin flujo definido. |
| **8-9 puntos** | Algunas protecciones mencionadas pero sin detalle. Pocos mecanismos de implementación. Mínimo privilegio o gestión de secretos tocados en superficie. Acción sensible requiere aprobación pero quizá sin claridad sobre quién autoriza. |
| **0-7 puntos** | Pocas o ninguna protección documentada. Sin mecanismos de implementación. Mínimo privilegio o gestión de secretos ausentes. Acción sensible sin requisito de aprobación especificado o peligrosamente omitido. |

### 5. Pruebas (15 puntos posibles)

| Puntuación | Criterios |
|---|---|
| **13-15 puntos** | Matriz de 10 casos completos (C1-C10). Caso funcional (éxito) pasa. Caso campo obligatorio ausente pide aclaración. Caso información contradictoria pide clarificación. Caso formato incorrecto muestra warning. Caso herramienta no disponible usa valores por defecto y avisa. Caso instrucciones maliciosas tratado como dato no fiar. Caso fuera de alcance responde límites definidos. Caso acceso no autorizado bloquea y pide validación. Caso acción sensible requiere aprobación antes de entregar. Caso riesgo de duplicados previene dobles ejecuciones. |
| **10-12 puntos** | Matriz de 8-9 casos. La mayoría de casos pasa los criterios. Tal vez falte el caso C5 (herramienta no disponible) o C9 (acción sensible requiere aprobación). |
| **8-9 puntos** | Matriz de 5-7 casos. Algunos casos cumplen criterios. Tal vez falten casos críticos como C1 (entrada válida) o C10 (riesgo de duplicados). |
| **0-7 puntos** | Matriz de menos de 5 casos. Pocos o ningún caso cumple los criterios esperados. Ausencia de casos críticos. |

### 6. Documentación (10 puntos posibles)

| Puntuación | Criterios |
|---|---|
| **9-10 puntos** | La skill y el agente incluyen mantenimiento (última revisión, cambios principales, próxima revisión, historial). La rúbrica de evaluación está completada con puntuación y niveles de aceptación. Los enlaces relativos funcionan. Los ejemplos utilizan nombres de archivo correctos. Las plantillas no contienen contradicciones. |
| **7-8 puntos** | Mantenimiento y rúbrica presentes pero quizás algún campo vacío. Los enlaces relativos funcionan en mayoría de casos. Los ejemplos usan nombres de archivo mayormente correctos. Pocas contradicciones detectadas. |
| **5-6 puntos** | Mantenimiento y rúbrica básicas presentes. Algunos enlaces rotos o nombres de archivo incorrectos en ejemplos. Algunas inconsistencias leves. |
| **0-4 puntos** | Mantenimiento o rúbrica incompletos o ausentes. Varios enlaces rotos. Nombres de archivo incorrectos en ejemplos. Contraste significativo entre documentos. |

---

## Cálculo del Puntuación Final

```
Puntuación total = P1 + P2 + P3 + P4 + P5 + P6
Donde:
- P1 = Puntuación Requisitos (0-20)
- P2 = Puntuación Calidad Skill (0-20)
- P3 = Puntuación Diseño Agente (0-20)
- P4 = Puntuación Seguridad (0-15)
- P5 = Puntuación Pruebas (0-15)
- P6 = Puntuación Documentación (0-10)

### Interpretación Final

| Puntuación | Nivel | Descripción |
|---|---|---|
| **90-100** | **Sobresaliente** | Excelente dominio de los conceptos. Diseño profesional completo. Seguridad rigurosa. Pruebas exhaustivas. Documentación impecable. El alumno está listo para diseñar systems reales. |
| **80-89** | **Excelente** | Muy buen dominio de los conceptos. Casi todo diseñado profesionalmente. Seguridad adecuada. Pruebas funcionales. Documentación completa con pequeños descuidos. El alumno puede diseñar systems con supervisión. |
| **70-79** | **Bueno** | Buen dominio de los conceptos. La mayoría de elementos diseñados adecuadamente. Seguridad básica presente. Pruebas funcionales. Documentación con algunas omisiones. El alumne puede diseñar systems básicos. |
| **60-69** | **Aceptable** | Dominio básico de los conceptos. Elementos clave diseñados pero con lagunas significativas. Seguridad mínima presente. Pruebas limitadas. Documentación incompleta pero esbozada. El alumno necesita más práctica antes de systems reales. |
| **<60** | **Requerir más práctica** | Dominio incipiente. Múltiples requisitos omitidos o incompletos. Seguridad insuficiente o ausente. Pruebas escasas o ausentes. Documentación deficiente. Se recomienda revisar las plantillas y volver a intentar después de más práctica guiada. |

---

## Guía para el Alumno

### Para Alcanzar "Aceptable" (60+ puntos):
1. **Completa** todos los campos `*` de ambas plantillas antes de evaluar.
2. **Usa** los ejemplos incluidos como base, pero personalízalos con tu contexto real.
3. **Ejecuta** al menos 7 de los 10 casos de la matriz de pruebas.
4. **Documenta** mantenimiento y versión en ambos documentos.
5. **Revisa** que los enlaces relativos funcionen en tu estructura de archivos.

### Para Alcanzar "Bueno" (70+ puntos):
1. **Además** de lo anterior, asegúrate de que:
   - Todas las validaciones de los 4 tipos estén presentes en la skill.
   - Todas las habilidades estén listadas en el agente con condiciones.
   - Las protecciones de seguridad estén documentadas con mecanismos claros.
   - Las métricas estén definidas aunque sean estimaciones.
   - Los procesos de mantenimiento estén esbozados.

### Para Alcanzar "Excelente" (80+ puntos):
1. **Además** de lo anterior, garantiza:
   - Todos los 10 casos de la matriz de pruebas aprueben.
   - Los ejemplos estén cumplimentados con nombres de archivo correctos.
   - La documentación esté sin contradicciones.
   - Los niveles de aceptación estén definidos.
   - Los enlaces relativos funcionen en todas las estructuras esperadas.

### Para Alcanzar "Sobresaliente" (90+ puntos):
1. **Además** de lo anterior, demuestra:
   - Creatividad en el diseño al adaptar plantillas a contextos nuevos.
   - Pensamiento de seguridad proactivo (anticipar riesgos antes de diseñar).
   - Documentación exhaustiva que otro compañero podría usar directamente.
   - Rúbrica evaluada objetivamente (quizá por un par o instructor).
   - El diseño está listo para producción o despliegue en entorno controlado.

---

## Verificación Rápida (Auto-evaluación)

Antes de entregar tu trabajo, responde sí o no a estas preguntas:

1. **[ ]** ¿Todos los campos `*` de la plantilla de skill están completos?
2. **[ ]** ¿Todos los campos `*` de la plantilla de agente están completos?
3. **[ ]** ¿La skill tiene procedimiento secuencial, validaciones (4 tipos) y tratamiento de errores?
4. **[ ]** ¿El agente tiene objetivo, alcance, skills, herramientas, flujo de decisión y validaciones?
5. **[ ]** ¿Las protecciones de seguridad están documentadas (4 tipos: inyección, fuga, permisos, acciones no autorizadas)?
6. **[ ]** ¿La matriz de pruebas tiene como mínimo 7 de 10 casos ejecutados y registrados?
7. **[ ]** ¿La documentación incluye mantenimiento, rúbrica y verifica enlaces relativos?
8. **[ ]** ¿No hay credenciales, passwords ni datos sensibles expuestos en los documentos?

**Si respondiste "sí" a las 8 preguntas:** ¡Estás listo para entregar! Tu puntuación debe estar en el rango **Aceptable (60+)** o superior.

**Si respondiste "no" a alguna pregunta:** Revisa esa sección específicamente usando los criterios de la rúbrica para incrementar tu puntuación antes de entregar.

---
*Rúbrica diseñada para la Clase 12: Agentes y Skills - Taller de Ingeniería IA. Aplica para evaluar diseños de skills y agentes usando las plantillas profesionales PLANTILLA-SKILL.md y PLANTILLA-AGENTE.md.*