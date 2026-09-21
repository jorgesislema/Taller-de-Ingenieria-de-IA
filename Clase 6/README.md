# Clase 6: El Espejismo de la Autonomía — Errores Reales de la IA y Cómo Mitigarlos

## Resumen

En la Clase 4 vimos cómo elegir un modelo usando benchmarks. Pero los benchmarks muestran el mejor caso. En el mundo real, **la IA falla常失**. Esta clase desmitifica la promesa de autonomía total y enseña al alumno a diseñar sistemas donde las alucinaciones no destruyan el negocio.

El dato central: **1 de cada 12 respuestas de la IA contiene información inventada**. Y el 95% de los pilotos empresariales de IA fracasan en generar impacto real. La solución no es abandonar la IA: es diseñar sistemas con mitigación.

## Objetivos de Aprendizaje

Al finalizar esta clase, los alumnos podrán:

1. **Explicar** por qué la IA alucina (mecanismo de predicción del siguiente token).
2. **Comparar** tasas de alucinación por dominio (desde 0.7% hasta 88%).
3. **Calcular** el "Impuesto de Verificación" para un proyecto real.
4. **Diseñar** una estrategia de mitigación usando RAG, prompting restrictivo, circuit breakers, multi-modelo y HITL.
5. **Argumentar** por qué "la IA sola" nunca es suficiente para proyectos críticos.

## Agenda (70 min + 20 min)

### Fase 1: Introducción — El 8.2% (3 min)
- "1 de cada 12 respuestas tiene info inventada"

### Fase 2: ¿Por qué la IA alucina? (10 min)
- Predicción del siguiente token
- La trampa del lenguaje autoritario

### Fase 3: Tasas de Error por Dominio (12 min)
- Tabla de alucinaciones por sector
- La regla: prompt abierto = más alucinación

### Fase 4: La Paradoja — Inteligente pero Mentiroso (8 min)
- DeepSeek V4 Pro: 94% de alucinación
- Command A+: 9% de precisión pero 14% de alucinación
- No existe "el mejor": depende del riesgo

### Fase 5: El Impuesto de Verificación (10 min)
- 4.3 horas/semana por empleado
- $14,200 USD anuales
- El 95% de pilotos fracasan

### Fase 6: Propagación de Errores (10 min)
- Efecto dominó en sistemas multiagente
- Brechas de datos silenciosas
- El caso SWE-bench Pro (32% de error)

### Fase 7: Estrategias de Mitigación (10 min)
- Las 5 herramientas: RAG, razonamiento, circuit breakers, prompting, multi-modelo
- RAG: reducción del 73-86%
- Prompting restrictivo: reducción del 20-40%

### Fase 8: El Ing. de IA y Cierre (7 min)
- Tu rol: El Cortafuegos
- "Diseñás la jaula donde la IA no puede hacer daño"

### Ejercicio Práctico: El Arquitecto de Mitigación (20 min)
- 3 proyectos con distintos niveles de riesgo
- Diseñar estrategia de mitigación para cada uno

### Consulta y Conversación (20 min)

## Contenido de la Clase

- **Teoría completa:** Ver [apuntes.md](apuntes.md)
- **Glosario de términos:** Ver [glosario.md](glosario.md)
- **Práctica guiada:** Ver [practica.md](practica.md)
- **Recursos complementarios:** Ver [recursos.md](recursos.md)

## El Ingeniero de IA en esta Clase

El rol del Ingeniero de IA es **diseñar sistemas resilientes**. No es el que elimina las alucinaciones (eso es matemáticamente imposible), pero sí es el que:

- ** Diseña la arquitectura de mitigación** adecuada para cada nivel de riesgo
- **Calcula el "Impuesto de Verificación"** antes de prometer ahorros
- **Implementa RAG** como base de cualquier sistema de IA en producción
- **Diseña flujos HITL** para tareas críticas (legal, médico, financiero)

Un Ingeniero de IA que no entiende los errores es como un ingeniero civil que no conoce los terremotos: construye edificios que se caen.
