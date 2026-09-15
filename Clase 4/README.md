# Clase 4: La Economía de la IA — Tokens, Costos y Modalidades

## Resumen

En la Clase 3 vimos los riesgos de la IA. Hoy vemos la otra cara: **la IA no es gratis**. Cada palabra que genera tiene un costo real en dólares. Esta clase enseña al alumno a entender los tokens, calcular presupuestos y elegir la modalidad correcta (Chat, API o Local) para cada proyecto.

Esta clase es la **base** para las Clases 5 (Benchmarks) y 6 (Errores y Mitigación): sin entender tokens y costos, no se puede elegir un modelo ni calcular cuánto cuesta mitigar sus errores.

## Objetivos de Aprendizaje

Al finalizar esta clase, los alumnos podrán:

1. **Definir** qué es un token y cuánto cuesta por modelo.
2. **Calcular** el costo mensual de un proyecto de IA usando tokens de input y output.
3. **Comparar** las 3 modalidades de conexión (Chat, API, Local) y elegir la correcta.
4. **Identificar** los costos ocultos (rate limits, latencia, VRAM) que pueden arruinar un proyecto.
5. **Argumentar** por qué un modelo barato puede ser mejor que uno caro para tareas simples.

## Agenda (70 min + 20 min)

### Fase 1: Introducción — La IA no es gratis (3 min)
- "Cada letra que escribe la IA tiene un costo real"

### Fase 2: Tokens y Tokenización (12 min)
- Qué es un token, input vs. output, la regla de oro
- La ventana de contexto y su costo

### Fase 3: Parámetros (8 min)
- Qué significan los números (8B, 70B, 1.8T)
- La relación parámetros = capacidad = costo
- Para el 80% de tareas, un modelo pequeño alcanza

### Fase 4: Las 3 Modalidades (15 min)
- Chat (personal, no profesional)
- API (la única forma profesional)
- Local (privacidad, sin costos por token)
- ¿Cuánta VRAM necesito?

### Fase 5: La Matemática de los Costos (15 min)
- Cómo leer una tabla de precios
- Ejemplo: resumir un libro de 200 páginas
- El costo del contexto (el peligro real)

### Fase 6: Costos Ocultos (7 min)
- Rate limits, latencia, hardware local

### Fase 7: El Ing. de IA y Conexión (5 min)
- "Sabe cuánto cuesta antes de preguntar cómo se hace"
- Conexión con Clase 5 (benchmarks) y Clase 6 (errores)

### Ejercicio Práctico: El Economista de la IA (20 min)
- Calcular presupuesto de un chatbot con 4 modelos
- Justificar la elección

### Consulta y Conversación (20 min)

## Contenido de la Clase

- **Teoría completa:** Ver [apuntes.md](apuntes.md)
- **Glosario de términos:** Ver [glosario.md](glosario.md)
- **Práctica guiada:** Ver [practica.md](practica.md)
- **Recursos complementarios:** Ver [recursos.md](recursos.md)

## El Ingeniero de IA en esta Clase

El rol del Ingeniero de IA es **calcular y optimizar costos**. No es el que paga la factura (eso lo hace el cliente), pero sí es el que:

- **Sabe cuánto cuesta** cada token antes de enviar un prompt
- **Elige la modalidad correcta** (API para producción, local para privacidad)
- **Optimiza el contexto** (no manda 50 correos de contexto cuando solo necesita 1)
- **Piensa en el costo total**, no en el costo por consulta

Un Ingeniero de IA que no sabe calcular costos es como un arquitecto que no sabe calcular materiales: construye edificios que quiebran.
