# Clase 5: ¿Cuál IA Elijo? — Benchmarks y Selección Profesional de Modelos

## Resumen

En las clases anteriores aprendimos qué es la IA, sus riesgos, sus costos y sus herramientas. Pero falta una pregunta fundamental: **¿cómo sé cuál modelo es el correcto para mi proyecto?**

La respuesta no está en el marketing, ni en un video de YouTube, ni en lo que diga el vendedor. Está en los **benchmarks**: pruebas estandarizadas que evalúan capacidades específicas de cada modelo.

Hoy aprendemos a leer esas pruebas, a elegir el benchmark correcto según nuestro caso de uso, y a tomar decisiones de selección de modelos basadas en datos, no en intuición.

## Objetivos de Aprendizaje

Al finalizar esta clase, los alumnos podrán:

1. **Definir** qué es un benchmark y por qué existen.
2. **Explicar** las 3 métricas fundamentales de AA-Omniscience (índice, precisión, alucinación).
3. **Comparar** los 3 benchmarks estrella (AA-Omniscience, FACTS, Vectara) y entender qué mide cada uno.
4. **Identificar** las 4 trampas de los benchmarks (contaminación, optimización, verificador defectuoso, saturación).
5. **Aplicar** el framework de 4 pasos para elegir un modelo según el caso de uso.
6. **Reconocer** los factores que los benchmarks NO miden (costo, velocidad, contexto, idioma).

## Agenda (70 min + 20 min)

### Fase 1: Introducción — El Examen de la IA (5 min)
- La analogía del examen de oposición
- Por qué no podemos confiar en el marketing

### Fase 2: ¿Qué es un Benchmark? (7 min)
- Definición y tipos
- El problema de la saturación

### Fase 3: Los 3 Benchmarks Estrella (20 min)
- **AA-Omniscience:** ¿Sabe la IA que no sabe?
- **FACTS:** ¿Dice la verdad?
- **Vectara:** ¿Inventa al resumir?

### Fase 4: Tabla Resumen de Benchmarks (8 min)
- Conocimiento general, programación, matemáticas, veracidad
- Cuáles están saturados y cuáles no

### Fase 5: ⚠️ Los Benchmarks Mienten (10 min)
- El caso SWE-bench Pro (32% de error en el verificador)
- Las 4 trampas: contaminación, optimización directa, verificador defectuoso, benchmark fácil
- Cómo ser escéptico sin perder la utilidad

### Fase 6: Framework de 4 Pasos (10 min)
- Paso 1: Define tu caso de uso
- Paso 2: Asigna el benchmark correcto
- Paso 3: Factores que los benchmarks NO miden
- Paso 4: Prueba con TUS datos

### Fase 6: El Ing. de IA en esta Clase (5 min)
- Tu rol: El Evaluador
- El valor de negocio

### Ejercicio Práctico: El Evaluador de Modelos (20 min — parte de consulta)
- 3 proyectos con restricciones distintas
- Elegir benchmark y modelo para cada uno

### Consulta y Conversación (20 min)

## Contenido de la Clase

- **Teoría completa:** Ver [apuntes.md](apuntes.md)
- **Glosario de términos:** Ver [glosario.md](glosario.md)
- **Práctica guiada:** Ver [practica.md](practica.md)
- **Recursos complementarios:** Ver [recursos.md](recursos.md)

## El Ingeniero de IA en esta Clase

El rol del Ingeniero de IA es **evaluar y seleccionar modelos**. No es el que crea benchmarks (eso lo hacen laboratorios como Google DeepMind), pero sí es el que:

- **Sabe QUÉ benchmark mirar** para cada caso de uso
- **Lee las tablas de resultados** sin impresionarse por números altos en pruebas saturadas
- **Aplica el framework de 4 pasos** para decisiones informadas
- **Prueba con datos reales** antes de confiar en cualquier métrica

Un Ingeniero de IA que no sabe evaluar modelos es como un médico que receta medicinas sin leer los resultados de los ensayos clínicos.
