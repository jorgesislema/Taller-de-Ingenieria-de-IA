# Clase 7: El Almacén del Futuro — Bases de Datos para IA

## Resumen

En las clases anteriores aprendimos a construir el motor (arquitectura de carpetas), a escribir el manual de instrucciones (archivos `.md`) y a decidir dónde estacionar el camión (Local, API, VPS). Pero nos falta lo más importante: **¿dónde ponemos la gasolina?**

La IA por sí sola es un motor vacío. Sin información, no hace nada. Si querés que tu IA te responda sobre las políticas de tu empresa, necesitás que esa información esté guardada en algún lado. Un simple archivo de Word o PDF no sirve cuando tenés 10,000 clientes o millones de registros. Ahí es donde entran las **Bases de Datos**.

Hoy dejamos de ver las bases de datos como ese tema aburrido de los contadores y las entendemos como lo que realmente son para la IA moderna: **el cerebro de la memoria a largo plazo**.

## Objetivos de Aprendizaje

Al finalizar esta clase, los alumnos podrán:

1. **Definir** qué es una base de datos con la analogía del almacén automatizado.
2. **Clasificar** los 4 tipos de bases de datos (Relacional, Documentos, Clave-Valor, Vectorial).
3. **Identificar** qué tipo de base de datos usar para cada caso de uso específico.
4. **Aplicar** la matriz de decisión para elegir la base de datos correcta.
5. **Diseñar** una arquitectura poliglota de bases de datos para un proyecto real.

## Agenda (70 min + 20 min)

### Fase 1: Introducción — El Combustible de la IA (5 min)
- La metáfora del motor vacío
- ¿Por qué las bases de datos son el cerebro de la memoria a largo plazo?

### Fase 2: ¿Qué es realmente una Base de Datos? (10 min)
- La analogía del almacén automatizado de Amazon
- Cómo cambia la definición según quién la use (contador vs. ingeniero de IA)

### Fase 3: La Gran Clasificación — Los 4 Reinos (25 min)
- **Reino 1:** Bases de Datos Relacionales (SQL) — El Archivo de Acero
- **Reino 2:** Bases de Datos NoSQL / Documentos — El Cajón de Sastre Inteligente
- **Reino 3:** Bases de Datos Clave-Valor — El Diccionario Ultra Rápido
- **Reino 4:** Bases de Datos Vectoriales — El Cerebro de la IA

### Fase 4: Arquitectura Poliglota — Caso de Estudio (15 min)
- Veterinaria inteligente: PostgreSQL + ChromaDB + Redis
- Por qué un buen sistema usa múltiples bases de datos

### Fase 5: La Matriz de Decisión (10 min)
- Tabla de criterios: cuándo usar cada familia
- Pensamiento crítico: rompiendo mitos ("MongoDB para todo")

### Fase 6: Integración con la Arquitectura (5 min)
- Conexiones a bases de datos desde `.env`
- Actualizando nuestro `ARCHITECTURE.md`

### Ejercicio Práctico: El Arquitecto de Datos (20 min — parte de consulta)
- Caso del banco digital con 3 módulos
- Decisión individual/grupal y discusión

### Consulta y Conversación (20 min)
- Dudas sobre los 4 tipos de bases de datos
- Discusión de casos reales de arquitectura poliglota

## Contenido de la Clase

- **Teoría completa:** Ver [apuntes.md](apuntes.md)
- **Glosario de términos:** Ver [glosario.md](glosario.md)
- **Práctica guiada:** Ver [practica.md](practica.md)
- **Recursos complementarios:** Ver [recursos.md](recursos.md)

## El Ingeniero de IA en esta Clase

El rol del Ingeniero de IA es **diseñar el almacén de datos**. No es el que construye las estanterías (eso lo hace el DBA o el desarrollador), pero sí es el que decide:

- **Qué tipo de mercancía** va a entrar (datos estructurados, documentos, vectores)
- **Cómo se va a mover** esa mercancía (arquitectura poliglota)
- **Qué almacén elegir** para cada necesidad (SQL para seguridad, Vectorial para RAG, Clave-Valor para caché)

Un Ingeniero de IA que no entiende de bases de datos es como un arquitecto que no sabe calcular pesos: el edificio se cae.
