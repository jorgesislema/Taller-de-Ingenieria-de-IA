# Clase 5: Arquitectura, Estructura y Mentalidad de Ingeniería para IA

## Resumen

En esta clase damos un salto fundamental: dejamos de ser "usuarios que escriben prompts" para convertirnos en **Arquitectos de IA**. No aprenderemos a programar, sino a **diseñar el entorno** para que la IA (y los programadores) trabajen de forma segura, ordenada y eficiente.

Aprenderemos a pensar como ingenieros: ¿dónde vive nuestra IA? ¿Cómo organizamos los archivos? ¿Cómo le damos instrucciones a la IA sin escribir una sola línea de código? La respuesta está en **archivos de texto plano (.md)** y en una **estructura de carpetas inteligente**.

## Objetivos de Aprendizaje

Al finalizar esta clase, los alumnos podrán:

1. **Distinguir** entre las opciones de despliegue (Local, API, VPS) y elegir la más adecuada según su caso de uso.
2. **Diseñar** la estructura de carpetas de un proyecto de IA siguiendo principios de ingeniería.
3. **Crear** archivos `.md` (CONTEXT.md, RULES.md, SECURITY.md) para controlar el comportamiento de cualquier IA.
4. **Aplicar** convenciones de nombres (snake_case, extensiones) para evitar errores comunes.
5. **Comprender** los 4 principios fundamentales de ingeniería de software aplicados a IA.

## Agenda (70 min + 20 min)

### Fase 1: El Cambio de Mentalidad (10 min)
- De "usuarios" a "arquitectos"
- La pregunta fundamental: ¿Dónde vive mi IA?

### Fase 2: Arquitectura Física y Lógica (15 min)
- Opción A: Local (Cocinar en casa)
- Opción B: API (Uber Eats)
- Opción C: VPS/Cloud (Alquilar un local)
- Pensamiento crítico: ¿Cuál elijo?

### Fase 3: La Gramática del Software (10 min)
- La regla de oro: Cero espacios
- Extensiones de archivos (.py, .md, .json, .env)
- Convenciones de nombres (snake_case, camelCase)

### Fase 4: Los 4 Mandamientos del Arquitecto (10 min)
- Cada quien a su casa (Separación de Conceptos)
- Cero Adornos (KISS + YAGNI)
- No uses Super Pegamento (Bajo Acoplamiento)
- El Especialista, no el Hombre Orquesta

### Fase 5: El Plano Físico - Estructura de Carpetas (10 min)
- La estructura sagrada (data/, src/, models/, docs/, tests/)
- Los archivos invisibles (.venv, .gitignore)

### Fase 6: Programando a la IA sin Código (15 min)
- La revolución de los .md
- La tríada de poder: CONTEXT.md, RULES.md, SECURITY.md
- La biblioteca extendida (GLOSSARY.md, FAQ.md)

### Fase 7: Herramientas y Flujo de Trabajo (5 min)
- Estándar universal vs. atajos privativos
- El equipo rojo: Generar vs. Auditar

### Consulta y Conversación (20 min)
- Preguntas y respuestas
- Discusión de casos de uso reales

## Contenido de la Clase

- **Teoría completa:** Ver [apuntes.md](apuntes.md)
- **Glosario de términos:** Ver [glosario.md](glosario.md)
- **Práctica guiada:** Ver [practica.md](practica.md)
- **Recursos complementarios:** Ver [recursos.md](recursos.md)

## El Ingeniero de IA en esta Clase

El rol del Ingeniero de IA es **diseñar el entorno**. No escribimos el código, pero decidimos:
- Dónde vivirá la IA (local, API, nube)
- Cómo se organizarán los archivos (estructura de carpetas)
- Qué reglas seguirá la IA (archivos .md)
- Cómo se protegerán los datos (seguridad)

Un buen diseño de arquitectura vale más que mil líneas de código desordenado.