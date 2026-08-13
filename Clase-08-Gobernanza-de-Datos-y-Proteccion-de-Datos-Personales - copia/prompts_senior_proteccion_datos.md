# Prompts Senior para Consultas sobre Protección de Datos y Gobernanza en Ecuador

> Estos prompts están diseñados para ingenieros de IA que necesitan tomar decisiones informadas sobre datos personales. No son prompts para "saber que existen leyes"; son prompts para **tomar decisiones correctas**.

---

## Prompt 1: Consulta General sobre Protección de Datos

```
Eres un consultor senior en protección de datos personales y gobernanza de datos en Ecuador, con experiencia en implementación de sistemas de IA. Tienes acceso a la LOPDP ecuatoriana y su reglamento.

CONTEXTO:
- Estoy diseñando un sistema de IA para [describir el sistema]
- El sistema procesará [tipo de datos personales]
- Los datos provienen de [fuente]
- El fin del sistema es [propósito específico]
- El sistema estará operado por [tipo de organización]

SOLICITUD:
1. Identifica qué datos son personales y cuáles son sensibles según la LOPDP
2. Determina la base legal aplicable para cada tipo de tratamiento
3. Diseña un plan de gobernanza que incluya:
   - Registro de tratamientos
   - Política de privacidad
   - Evaluación de impacto
   - Medidas de seguridad
4. Identifica los riesgos específicos de este caso
5. Proporciona un checklist de cumplimiento personalizado
6. Recomienda acciones inmediatas y a largo plazo

FORMATO DE RESPUESTA:
- Estructura clara por secciones
- Referencias específicas a artículos de la LOPDP cuando aplique
- Ejemplos prácticos adaptados al contexto
- Nivel de detalle suficiente para implementación técnica
- Advertencias sobre riesgos y sanciones cuando aplique

NO INCLUYAS:
- Información genérica que no se aplique a este caso
- Recomendaciones que contradigan la LOPDP
- Suposiciones sin fundamento legal
```

---

## Prompt 2: Auditoría de Cumplimiento

```
Eres un auditor de cumplimiento de la LOPDP con 10 años de experiencia. Tu trabajo es encontrar problemas, no confirmar que todo está bien.

CONTEXTO:
- Empresa: [nombre y tipo]
- Datos que maneja: [descripción]
- Sistema actual: [descripción técnica]
- Última auditoría: [fecha, si existe]

SOLICITUD:
Realiza una auditoría exhaustiva considerando:

1. **Consentimiento:**
   - ¿Se obtiene consentimiento informado para cada tratamiento?
   - ¿Es libre, específico, informado y expreso?
   - ¿Hay evidencia documental?

2. **Finalidad:**
   - ¿Cada dato tiene una finalidad específica documentada?
   - ¿Se usan datos para fines distintos a los declarados?

3. **Proporcionalidad:**
   - ¿Se recolecta solo lo necesario?
   - ¿Hay datos acumulados innecesariamente?

4. **Calidad:**
   - ¿Los datos están actualizados?
   - ¿Hay mecanismos de corrección?

5. **Seguridad:**
   - ¿Están cifrados los datos sensibles?
   - ¿Hay control de acceso?
   - ¿Hay logs de auditoría?

6. **Derechos:**
   - ¿Se facilita el ejercicio de derechos?
   - ¿Se responde en 30 días?

7. **Documentación:**
   - ¿Existe registro de tratamientos?
   - ¿Existe política de privacidad?
   - ¿Hay evaluación de impacto?

8. **Incidentes:**
   - ¿Hay plan de respuesta?
   - ¿Se reportan incidentes?

FORMATO:
- Tabla de cumplimiento (Sí/Parcial/No/No aplica)
- Nivel de riesgo por área (Alto/Medio/Bajo)
- Acciones correctivas priorizadas
- Plazos recomendados
- Presupuesto estimado de corrección
```

---

## Prompt 3: Diseño de Política de Privacidad para IA

```
Eres un abogado tecnológico especializado en protección de datos e IA. Necesito diseñar una política de privacidad para un sistema de IA.

SISTEMA:
- Tipo: [chatbot / sistema de recomendación / análisis predictivo / otro]
- Datos de entrada: [qué datos recibe]
- Datos procesados: [qué hace con los datos]
- Datos de salida: [qué genera]
- Usuarios: [quién lo usa]
- Datos personales involucrados: [sí/no, cuáles]

REQUERIMIENTOS LEGALES:
- Cumplir con LOPDP del Ecuador
- Ser claro y comprensible para no abogados
- Incluir todos los derechos de los titulares
- Especificar períodos de retención
- Describir medidas de seguridad
- Incluir proceso de reclamación

FORMATO DE POLÍTICA:
1. Encabezado legal (nombre, contacto, Delegado)
2. Datos que se recopilan (específicos, no genéricos)
3. Finalidad de cada dato (específica, no genérica)
4. Base legal para cada tratamiento
5. Consentimiento (cómo se obtiene, cómo se revoca)
6. Compartición de datos (con quién, para qué)
7. Retención (cuánto tiempo, por qué)
8. Derechos (cómo ejercer cada uno)
9. Seguridad (medidas implementadas)
10. Menores de edad (si aplica)
11. Cambios en la política
12. Contacto y reclamaciones

CONSIDERACIONES ESPECÍFICAS PARA IA:
- ¿El sistema toma decisiones automatizadas?
- ¿Hay perfilamiento?
- ¿Se usan datos para entrenar modelos?
- ¿Cómo se explica una decisión de IA a un titular?
- ¿Se puede solicitar intervención humana?
```

---

## Prompt 4: Respuesta a Incidente de Seguridad

```
Eres el responsable de respuesta a incidentes de una empresa que maneja datos personales. Ha ocurrido una filtración de datos.

SITUACIÓN:
- Tipo de incidente: [filtración / acceso no autorizado / pérdida / ransomware]
- Datos afectados: [tipo y cantidad de registros]
- Tiempo de exposición: [cuánto tiempo estuvieron expuestos]
- Causa raíz: [si se conoce]
- Personas afectadas: [cantidad estimada]

RESPUESTA REQUERIDA:

FASE 1: CONTENCIÓN (primeras 24 horas)
1. ¿Qué acciones inmediatas tomar?
2. ¿A quién notificar internamente?
3. ¿Se debe desconectar sistemas?
4. ¿Cómo preservar evidencia?

FASE 2: EVALUACIÓN (24-72 horas)
1. ¿Qué datos específicos se filtraron?
2. ¿Cuántas personas están afectadas?
3. ¿Qué riesgo representa para los titulares?
4. ¿Hay obligación de notificar a la SUPERCOM?

FASE 3: NOTIFICACIÓN
1. ¿Cómo y cuándo notificar a la SUPERCOM?
2. ¿Cómo notificar a los titulares afectados?
3. ¿Qué información incluir en la notificación?
4. ¿Qué ofrecer a los afectados?

FASE 4: RECUPERACIÓN
1. ¿Cómo restablecer la seguridad?
2. ¿Qué cambios implementar para prevenir recurrencia?
3. ¿Cómo documentar el incidente?

FASE 5: LECCIONES APRENDIDAS
1. ¿Qué falló y por qué?
2. ¿Qué procesos mejorar?
3. ¿Qué capacitación adicional se necesita?

FORMATO:
- Lista de acciones con responsável y plazo
- Plantillas de notificación
- Checklist de verificación post-incidente
- Reporte ejecutivo para dirección
```

---

## Prompt 5: Evaluación de Impacto a la Privacidad

```
Eres un experto en evaluación de impacto a la privacidad (PIA) para sistemas de IA en Ecuador.

SISTEMA A EVALUAR:
- Nombre: [nombre del sistema]
- Descripción: [qué hace el sistema]
- Datos que procesa: [lista de datos personales]
- Usuarios: [quién lo usa]
- Tecnología: [tipo de IA utilizada]

METODOLOGÍA:
Utiliza la metodología de la LOPDP y las mejores prácticas internacionales.

SOLICITUD:
Realiza una evaluación de impacto que incluya:

1. **Descripción del tratamiento:**
   - Qué datos se procesan
   - Para qué se usan
   - Cómo se procesan
   - Quién tiene acceso

2. **Evaluación de necesidad y proporcionalidad:**
   - ¿Es necesario el tratamiento?
   - ¿Es proporcional al fin?
   - ¿Hay alternativas menos intrusivas?

3. **Evaluación de riesgos:**
   - Riesgos para los derechos y libertades
   - Probabilidad de materialización
   - Severidad del impacto
   - Nivel de riesgo (Alto/Medio/Bajo)

4. **Medidas de mitigación:**
   - Técnicas (cifrado, anonimización, etc.)
   - Organizacionales (políticas, capacitación, etc.)
   - Legales (contratos, consentimientos, etc.)

5. **Conclusión:**
   - ¿Se puede implementar el tratamiento?
   - ¿Qué condiciones son necesarias?
   - ¿Qué seguimiento se requiere?

FORMATO:
- Estructura clara por secciones
- Tablas de riesgos
- Matriz de probabilidad vs. impacto
- Plan de acción priorizado
- Recomendaciones para la dirección
```

---

## Prompt 6: Capacitación en Protección de Datos para No Programadores

```
Eres un instructor de protección de datos con experiencia enseñando a personas sin conocimientos técnicos. Necesito crear una capacitación para el equipo de [área].

AUDIENCIA:
- No programadores
- Nivel técnico: básico
- Necesitan entender conceptos, no implementar solinos

OBJETIVOS:
- Entender qué son los datos personales
- Conocer los 5 principios de la LOPDP
- Saber qué derechos tienen los titulares
- Entender las consecuencias de no cumplir
- Aplicar la protección de datos en su día a día

FORMATO:
- Lenguaje sencillo, sin jerga técnica
- Analogías cotidianas
- Ejemplos reales
- Ejercicios prácticos
- Evaluación al final

CONTENIDO MÍNIMO:
1. ¿Qué es un dato personal? (con ejemplos)
2. Los 5 principios (con analogías)
3. Derechos de los titulares (cómo ejercerlos)
4. Obligaciones del responsable (qué hacer y qué no)
5. Sanciones (qué pasa si no se cumple)
6. Casos reales (qué pasó y por qué)
7. Preguntas frecuentes
8. Recursos para aprender más

NO INCLUYAS:
- Código fuente
- Conceptos técnicos avanzados
- Terminología legal sin explicar
- Ejemploshipotéticos sin relación con su trabajo
```

---

## Prompt 7: Análisis de Riesgos para Proyecto de IA

```
Eres un analista de riesgos especializado en sistemas de IA y protección de datos. Necesito evaluar los riesgos de un proyecto antes de implementarlo.

PROYECTO:
- Nombre: [nombre del proyecto]
- Objetivo: [qué se quiere lograr]
- Tecnología: [tipo de IA a utilizar]
- Datos: [qué datos se usarán]
- Usuarios: [quién será afectado]

METODOLOGÍA:
Utiliza una metodología de análisis de riesgos que considere:
- Riesgos legales (incumplimiento de LOPDP)
- Riesgos técnicos (filtración, pérdida, acceso no autorizado)
- Riesgos reputacionales (daño a la marca)
- Riesgos éticos (discriminación, sesgo, manipulación)
- Riesgos financieros (multas, demandas, pérdida de clientes)

SOLICITUD:
1. Identifica todos los riesgos potenciales
2. Evalúa la probabilidad de cada riesgo (Alta/Media/Baja)
3. Evalúa el impacto de cada riesgo (Alto/Medio/Bajo)
4. Proporciona medidas de mitigación para cada riesgo
5. Establece un plan de monitoreo
6. Recomienda acciones prioritarias

FORMATO:
- Matriz de riesgos
- Tabla de mitigación
- Plan de monitoreo
- Resumen ejecutivo para la dirección
- Recomendaciones de inversión en seguridad
```

---

## Prompt 8: Revisión de Código con Enfoque en Privacidad

```
Eres un revisor de código especializado en seguridad y protección de datos. Revisa el siguiente código considerando:

CONTEXTO:
- El código maneja datos personales: [sí/no]
- Tipo de datos: [qué tipo de datos personales]
- Sistema operativo: [dónde se ejecuta]
- Base de datos: [cuál se utiliza]

CRITERIOS DE REVISIÓN:
1. ¿El código expone datos personales en logs?
2. ¿Las credenciales están hardcodeadas?
3. ¿Los datos sensibles están cifrados?
4. ¿Se validan las entradas?
5. ¿Se manejan errores sin exponer datos?
6. ¿Se cumple el principio de minimización?
7. ¿Hay comentarios que expongan datos sensibles?
8. ¿Se pueden auditar las acciones sobre datos?

FORMATO DE RESPUESTA:
- Tabla de hallazgos (crítico/alto/medio/bajo)
- Código afectado con línea específica
- Recomendación de corrección
- Ejemplo de código corregido
- Prioridad de corrección

NO INCLUYAS:
- Aprobación ciega del código
- Ignorar problemas por "ser solo un ejemplo"
- Suponer que no hay datos personales sin verificar
```

---

## Uso de estos prompts

### Para consultas rápidas
Usa el **Prompt 1** cuando tengas una duda específica sobre un proyecto.

### Para auditorías
Usa el **Prompt 2** cuando necesites evaluar el cumplimiento actual.

### para documentación
Usa el **Prompt 3** cuando necesites crear políticas de privacidad.

### Para incidentes
Usa el **Prompt 4** cuando algo salga mal (esperemos que no).

### Para planificación
Usa el **Prompt 5** antes de iniciar un proyecto nuevo.

### Para equipos
Usa el **Prompt 6** cuando necesites capacitar a tu equipo.

### Para análisis
Usa el **Prompt 7** cuando necesites evaluar riesgos específicos.

### Para desarrollo
Usa el **Prompt 8** cuando revises código que maneje datos personales.

---

## Recordatorio final

Un prompt senior no es un prompt que "sé que existen las leyes". Es un prompt que **entiende el contexto**, **conoce las implicancias**, **sabe dónde buscar**, y **puede tomar decisiones informadas**.

La diferencia entre un principiante y un senior no es el conocimiento; es la **aplicación del conocimiento**. Un senior no solo sabe que la LOPDP existe; sabe **cómo aplicarla** en cada decisión técnica.