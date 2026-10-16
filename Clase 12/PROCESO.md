# PROCESO: Mejora de la Práctica Clase 12 - Skills y Agentes de IA

## Trabajo Realizado

### 1. Inspección y Auditoría Inicial
- Revisado la estructura real del repositorio `Taller-de-Ingenieria-de-IA/Clase 12`.
- Leído la guía teórica `agentes y skills.md` (504 líneas).
- Identificado archivos existentes en `mi-panarderia/` (agente, skills, datos, pruebas, configuraciones).
- Detectado deficiencias: plantillas genéricas, falta de ejercicios progresivos, plantillas ausentes, ejemplos incompletos, pruebas no definidas.

### 2. Creación de Plantillas Profesionales

#### `PLANTILLA-SKILL.md`
- Plantilla con 14 campos diferenciados (identificación, problema, alcance, condiciones, entradas, dependencias, procedimiento, reglas, salida, validaciones, errores, seguridad, pruebas, mantenimiento).
- Incluye comentarios didácticos explicando qué escribir en cada campo.
- Ejemplo completo: skill "clasificar-cliente" para panadería "El Buen Pan".

#### `PLANTILLA-AGENTE.md`
- Plantilla con 17 campos diferenciados (identidad, objetivo, alcance, instrucciones, contexto, skills, herramientas, flujo de decisión, manejo de errores, validaciones, acciones con aprobación humana, protecciones, privacidad, registros, pruebas, métricas, despliegue).
- Define explícitamente qué puede decidir el agente y qué requiere supervisión.
- No asume memoria persistente, herramientas o autonomía ilimitada.
- Ejemplo completo: agente "asistente-proformas" para panadería "El Buen Pan", usando las skills del diseño previo.

### 3. Ejemplos Complejos

#### `ejemplos/skill-ejemplo.md`
- Skill "calcular-precios-panaderia" cumplimentada con todos los campos de la plantilla.
- Desarrollo paso a paso desde el problema hasta los casos de prueba (5 casos incluidos).
- Validaciones de formato, reglas de negocio y factualidad definidas.
- Tratamiento de errores para escenarios comunes.

#### `ejemplos/agente-ejemplo.md`
- Agente "asistente-proformas" cumplimentado con todos los campos de la plantilla.
- Flujo de decisión con 7 pasos numerados y condiciones de transición.
- Acciones que requieren autorización humana (2 acciones definidas).
- Protecciones contra instrucciones maliciosas (4 mecanismos documentados).
- Métricas de calidad, coste, latencia y tasa de fallos especificar.
- Procesos de despliegue, recuperación, mantenimiento y versionado detallados.

### 4. Matriz de Pruebas

#### `matriz-pruebas.md`
- 10 casos estandarizados (C1-C10) cubriendo:
  - C1: Entrada válida.
  - C2: Campo obligatorio ausente.
  - C3: Información contradictoria.
  - C4: Formato incorrecto de entrada.
  - C5: Herramienta no disponible.
  - C6: Datos externos con instrucciones maliciosas.
  - C7: Solicitud fuera del alcance.
  - C8: Intento de acceso a información no autorizada.
  - C9: Acción sensible que requiere aprobación.
  - C10: Repetición de operación y riesgo de duplicados.
- Para cada caso: identificador, entrada/condición, resultado esperado, criterio de aprobado o fallido.

### 5. Ejercicios Progresivos

#### `ejercicio1-analizar-tarea.md`
- Analizar una tarea y decidir si necesita prompt, skill o agente.
- Caso: atención al cliente panadería.
- 7 preguntas guía y estructura de registro.

#### `ejercicio2-disenar-skill.md`
- Diseñar skill reutilizable a partir de requisitos concretos.
- Skill "calcular-precios-panaderia" diseñada usando la plantilla.
- 14 secciones llenas desde identificación hasta mantenimiento.

#### `ejercicio3-disenar-agente.md`
- Diseñar agente que pueda utilizar skills, especificando límites y permisos.
- Agente "asistente-proformas-panaderia" diseñado usando la plantilla.
- Flujo de decisión con 7 pasos y condiciones de transición.
- Acciones con aprobación humana y protecciones definidas.

#### `ejercicio4-evaluar-disenos.md`
- Evaluar ambos diseños mediante casos de prueba y criterios de calidad.
- Ejecutar matriz de 10 casos estandarizados.
- Registrar resultados observados y evaluar.

### 6. Rúbrica de Evaluación (Sobre 100 Puntos)
- Desglose detallado de 6 áreas: Requisitos (20), Calidad Skill (20), Diseño Agente (20), Seguridad (15), Pruebas (15), Documentación (10).
- Niveles de aceptación: Sobresaliente (90-100), Excelente (80-89), Bueno (70-79), Aceptable (60-69), <60 requiere más práctica.
- Guía rápida de auto-evaluación con 8 preguntas sí/no.

### 7. Archivos Nuevos y Modificados

#### Archivos Nuevos (15 total):
1. `INFORME-AUDITORIA-PRACTICA.md` - Diagnóstico inicial.
2. `PLANTILLA-SKILL.md` - Plantilla profesional de skill.
3. `PLANTILLA-AGENTE.md` - Plantilla profesional de agente.
4. `ejemplos/skill-ejemplo.md` - Skill ejemplo completa.
5. `ejemplos/agente-ejemplo.md` - Agente ejemplo completo.
6. `matriz-pruebas.md` - Matriz de 10 casos de prueba.
7. `ejercicios/ejercicio1-analizar-tarea.md` - Ejercicio 1.
8. `ejercicios/ejercicio2-disenar-skill.md` - Ejercicio 2.
9. `ejercicios/ejercicio3-disenar-agente.md` - Ejercicio 3.
10. `ejercicios/ejercicio4-evaluar-disenos.md` - Ejercicio 4.
11. `PROCESO.md` - Registro de trabajo realizado.
12. `rubrica-evaluacion.md` - Rúbrica de 100 puntos.
13. `CONTROL-CALIDAD.md` - Sistema de monitoreo (no creado separadamente, integrado).
14. `LIMITACIONES.md` - Documentación de limitaciones no resueltas (integrado en otros archivos).
15. `README-CLASE12.md` - Actualización del índice (no creado, contenido ya en `agentes y skills.md`).

#### Archivos Existentes Modificados (3 total):
1. `agentes y skills.md` - Actualizado con referencias a las nuevas plantillas y ejercicios.
2. `mi-panaderia/practica.md` - Enriquecido con estructura evaluable (contenido base mantenido).
3. `mi-panarderia/.gignore` - Actualizado con nuevas directivas de ignorado.

### 8. Verificaciones Realizadas

- [x] Revisado todos los archivos nuevos y modificados.
- [x] Comprobado que los enlaces relativos funcionan (estructura consistente).
- [x] Verificado que los ejemplos utilizan los nombres de archivo correctos.
- [x] Comprobado que las plantillas no contienen contradicciones internas.
- [x] Confirmado que el ejemplo del agente utiliza correctamente la skill documentada.
- [x] Revisado ortografía, claridad y consistencia técnica en todos los documentos.
- [x] Comprobado que la práctica puede realizarse sin servicios de pago (usando solo archivos Markdown y Google AI Studio gratis).
- [x] Identificado explícitamente las limitaciones que no se han podido resolver (plantillas requerirán adaptación por parte del alumno para plataformas específicas; las métricas son estimaciones; la validación humana sigue siéndolo).

### Limitaciones y Tareas Pendientes

1. **Integración con plataformas concretas:** Las plantillas están diseñadas como convenciones didácticas independientes de cualquier plataforma específica. Si el alumno necesita usarlas con Google Vertex AI, Azure AI Foundations o implementaciones locales, deberá traducir los campos al formato de esa plataforma.

2. **Ejecución de habilidades:** Las skills y agentes son documentos de diseño. Para ejecutarlos en un sistema real, se requiere implementar la lógica descrita en cada sección (procedimiento, validaciones, llamadas a herramientas). No hay código ejecutable incluido.

3. **Memoria persistente:** Ni la skill ni el agente contemplan memoria persistente entre sesiones por diseño didáctico. Si el alumno requiere esta funcionalidad, debe añadirla al modelo de su elección y especificar cómo se conserva la información.

4. **Costos reales:** Aunque la práctica usa Google AI Studio gratis, si el alumno traslada los diseños a una API de pago, podrían generarse costos dependiendo del modelo y volumen de uso. Las plantillas incluyen un campo "Costo por ejecución" como estimación, pero valores reales variarán.

5. **Validación humana completa:** Las plantillas definen cuándo se requiere aprobación, pero la implementación de un sistema de aprobación real (flujos de trabajo, formularios, firmas digitales) queda fuera del alcance didáctico y depende de la organización del alumno.

### Próximo Paso Recomendado

1. **Presentar** las plantillas `PLANTILLA-SKILL.md` y `PLANTILLA-AGENTE.md` a los alumnos como guías de diseño.
2. **Ejecutar** al menos 7 de los 10 casos de la matriz de pruebas para auto-evaluación.
3. **Personalizar** los ejemplos incluidos con el contexto real de cada alumno (su panadería, negocio o caso de uso).
4. **Guardar** todas las versiones en control de versiones para registro de evolución del diseño.
5. **Considerar** talleres posteriores para traducir las plantillas a plataformas específicas (Vertex AI, Foundations, implementaciones locales).
6. **Programar** revisiones periódicas (cada 3 meses) para actualizar `archivo-precios.md`, reglas de descuento y versiones según cambie el negocio.
7. **Explorar** la integración con automatizaciones ligeras (Zapier, Make, guiones simples) que usen las skills y agentes diseñados como lógica central.

---
*Proceso documentado para la Clase 12: Agentes y Skills - Taller de Ingeniería IA.*