# Apuntes de la Clase 8: Gobernanza de Datos y Protección de Datos Personales en Ecuador

## Introducción: Los Datos son Personas

Imaginá que entrás a un supermercado desordenado. No hay etiquetas en los estantes, los productos están mezclados, las fechas de vencimiento no se ven, y no sabés qué es fresco y qué está podrido. ¿Comprarías ahí? Probablemente no.

Eso es exactamente lo que pasa cuando una empresa maneja datos sin **gobernanza**. Los datos de clientes, empleados y pacientes están mezclados, sin orden, sin control, sin saber quién accede a qué, ni cuándo se vencen, ni si están correctos.

Y cuando esos datos son **personales** — el nombre de alguien, su cédula, su historial médico, sus fotos — la cosa se pone seria. No es solo desorden; es una violación de derechos fundamentales.

Hoy vamos a aprender a ser ese supermercado bien organizado. Pero no por capricho, sino porque es un **derecho humano** y una **obligación legal**.

---

## Parte 1: Gobernanza de Datos — El Supermercado Bien Organizado

### ¿Qué es la gobernanza de datos?

**Gobernanza de datos** es el conjunto de reglas, procesos y responsabilidades que definen **cómo se maneja la información** en una organización.

Pensalo así: la gobernanza es el **manual de instrucciones del supermercado**. Define:
- **Quién** es responsable de cada sección (¿quién revisa las frutas?)
- **Qué** información se guarda y cuál se descarta (¿guardamos las facturas viejas?)
- **Cómo** se organiza y clasifica (¿dónde van las verduras vs. los productos de limpieza?)
- **Cuándo** se revisa y actualiza (¿cada cuánto se revisan las fechas de vencimiento?)

### Los 4 pilares de la gobernanza de datos

| Pilar | Pregunta clave | Analogía del supermercado |
|-------|----------------|---------------------------|
| **Quién** | ¿Quién es dueño de los datos? ¿Quién puede acceder? | El gerente asigna quién trabaja en cada sección |
| **Qué** | ¿Qué datos tenemos? ¿Son personales? ¿Están clasificados? | Las etiquetas en los estantes dicen qué hay en cada lugar |
| **Cómo** | ¿Cómo se recolectan, almacenan y usan? | Las reglas de limpieza y almacenamiento |
| **Cuándo** | ¿Cuánto tiempo se guardan? ¿Cuándo se eliminan? | Las fechas de vencimiento y la rotación de stock |

### ¿Por qué importa para un ingeniero de IA?

Porque la IA **alimenta de datos**. Si los datos están mal gobernados:
- La IA toma decisiones basadas en información incorrecta o desactualizada
- Se filtran datos personales a quien no debe
- Se violan derechos de las personas
- La empresa enfrenta multas y demandas

Un ingeniero de IA que no entiende de gobernanza es como un cocinero que no revisa la fecha de vencimiento de los ingredientes: puede envenenar a alguien sin querer.

---

## Parte 2: Protección de Datos Personales — El Derecho a la Privacidad

### ¿Qué es un dato personal?

Un **dato personal** es cualquier información que permita **identificar a una persona**. No importa si está en papel, en una base de datos, en una foto o en un audio.

**Ejemplos de datos personales:**
- Nombre completo
- Cédula de identidad o pasaporte
- Dirección de domicilio
- Correo electrónico
- Número de teléfono
- Historial médico
- Historial laboral
- Datos bancarios
- Fotos donde se reconozca a la persona
- Ubicación geográfica (GPS)
- Dirección IP

**Lo que NO es dato personal:**
- El nombre de una empresa (si no se puede identificar a una persona concreta)
- Datos estadísticos agregados (ej: "el 30% de los ecuatorianos...")
- Información anónima donde es imposible reconstruir la identidad

### La LOPDP del Ecuador: La Ley que Protege a las Personas

La **Ley Orgánica de Protección de Datos Personales y de los Derechos de Acceso a la Información (LOPDP)** fue publicada en el Registro Oficial el 26 de mayo de 2021.

Esta ley establece:
- **Quiénes** son los actores (titulares, responsables, encargados)
- **Qué** derechos tienen las personas
- **Cómo** se deben manejar los datos personales
- **Cuándo** se puede usar la información y cuándo no
- **Qué** consecuencias hay por incumplir

### Los 5 principios fundamentales de la LOPDP

#### 1. Consentimiento informado
**Significado:** Nadie puede usar tus datos sin tu permiso claro y específico.

**Analogía:** Es como cuando alguien te pide prestado el auto. No le decís "sí, usalo para todo". Le decís: "Sí, podés ir al supermercado, pero no a la carrera y no lleves a nadie más".

**En la práctica:**
- El consentimiento debe ser **libre** (sin presión)
- debe ser **informado** (sabés para qué se usa)
- debe ser **específico** (para un fin concreto)
- debe ser **expreso** (no se asume por silencio)

**Ejemplo en IA:** Si una app de salud recopila tus datos médicos para "mejorar el servicio", necesita tu consentimiento explícito para cada uso. No puede vender esos datos a una aseguradora sin tu permiso separado.

#### 2. Finalidad específica
**Significado:** Los datos solo se pueden usar para el propósito para el cual fueron recolectados.

**Analogía:** Si le diste tu dirección para que te envíen un paquete, no pueden usarla para enviarte publicidad por correo, a menos que también te hayas dado cuenta para eso.

**En la práctica:**
- Cada recolección de datos debe tener un **propósito claro**
- No se pueden reutilizar para fines distintos sin nuevo consentimiento
- Se debe informar la finalidad **antes** de recolectar los datos

**Ejemplo en IA:** Una empresa de e-commerce que pide tu correo para enviar la factura no puede usarlo para entrenar un modelo de IA que prediga tus compras futuras, a menos que te lo haya comunicado y hayas aceptado.

#### 3. Proporcionalidad
**Significado:** Solo se recolecta la información **estrictamente necesaria** para el fin declarado.

**Analogía:** Si querés entrar al cine, no necesitás dar tu número de cédula, tu dirección y tu grupo sanguíneo. Solo necesitás la entrada.

**En la práctica:**
- Pedir solo lo indispensable
- No acumular "por si acaso"
- Evaluar si realmente se necesita esa pieza de información

**Ejemplo en IA:** Un chatbot de atención al cliente no necesita tu historial completo de compras de los últimos 5 años para resolver una duda sobre el envío de un paquete.

#### 4. Calidad de los datos
**Significado:** La información debe ser **correcta, actualizada y completa** según el fin para el que se usa.

**Analogía:** Si el supermercado tiene tu dirección vieja y te envían el pedido a tu casa anterior, el sistema falló.

**En la práctica:**
- Permitir a los titulares **corregir** sus datos
- **Actualizar** información desactualizada
- **Eliminar** datos innecesarios o inexactos
- Verificar la **exactitud** antes de tomar decisiones automatizadas

**Ejemplo en IA:** Si un algoritmo de IA decide otorgar un crédito basado en datos desactualizados de un buró de crédito, está tomando una decisión sobre información incorrecta, lo cual es injusto e ilegal.

#### 5. Seguridad y confidencialidad
**Significado:** Los datos deben estar **protegidos** contra acceso no autorizado, pérdida, destrucción o uso indebido.

**Analogía:** Es como tener una caja fuerte en casa. No solo la cerrás con llave, sino que la ponés en un lugar seguro, y solo vos tenés acceso.

**En la práctica:**
- Cifrado de datos sensibles
- Control de acceso (quién puede ver qué)
- Copias de seguridad
- Plan de respuesta ante incidentes
- Capacitación del personal

**Ejemplo en IA:** Si entrenás un modelo de IA con datos de pacientes y esos datos se filtran porque no estaban cifrados, no solo violás la ley; causás daño real a personas reales.

---

## Parte 3: Derechos y Obligaciones — El Contrato Social de los Datos

### Los derechos de los titulares (quién tiene mis datos)

La LOPDP reconoce que las personas tienen derechos sobre su información. Estos derechos son como los "botones de control" que cada persona tiene sobre sus propios datos:

| Derecho | Qué significa | Ejemplo práctico |
|---------|---------------|------------------|
| **Acceso** | Saber qué datos tiene una empresa sobre vos | Pedir una copia de todo lo que una app sabe de vos |
| **Rectificación** | Corregir datos incorrectos | Cambiar tu dirección en un registro |
| **Eliminación** | Pedir que borren tus datos | Borrar tu cuenta y todos tus datos |
| **Oposición** | Decir "no" a un uso específico de tus datos | No recibir publicidad personalizada |
| **Portabilidad** | Llevarte tus datos a otro servicio | Exportar tus contactos de una app a otra |
| **Limitación** | Pedir que solo guarden, pero no usen, tus datos | Congelar tu información mientras revisás algo |
| **No ser discriminado** | Que no te penalicen por ejercer tus derechos | No te pueden cancelar un servicio solo porque pediste borrar tus datos |

### Las obligaciones de los responsables (quién maneja mis datos)

Quien maneja datos personales (una empresa, una institución, un gobierno) tiene obligaciones claras:

1. **Informar:** Decir claramente qué datos recopila, para qué y con quién los comparte
2. **Obtener consentimiento:** Pedir permiso antes de usar los datos
3. **Proteger:** Implementar medidas de seguridad técnicas y organizativas
4. **Reportar:** Informar sobre incidentes de seguridad en un plazo razonable
5. **Facilitar derechos:** Hacer posible que las personas ejerzan sus derechos
6. **Documentar:** Mantener un registro de las actividades de tratamiento

### El Delegado de Protección de Datos

Es la persona o entidad encargada de **supervisar** que se cumplan las reglas. No es un simple "encargado de IT"; es un rol con autoridad independiente.

**Analogía:** Es como el árbitro en un partido de fútbol. No juega para ningún equipo; se asegura de que todos cumplan las reglas.

---

## Parte 4: Gobernanza de Datos para IA — El Caso Práctico

### Cómo aplicar la gobernanza a proyectos de IA

Cuando diseñás un sistema de IA que usa datos personales, necesitás:

1. **Mapa de datos:** ¿Qué datos voy a usar? ¿Son personales? ¿De dónde vienen?
2. **Evaluación de impacto:** ¿Qué riesgos tiene para las personas?
3. **Base legal:** ¿Bajo qué principio los uso? ¿Tengo consentimiento?
4. **Medidas técnicas:** ¿Cómo protejo los datos? ¿Están cifrados? ¿Quién tiene acceso?
5. **Documentación:** ¿Tengo todo por escrito? ¿Puedo demostrarlo si me preguntan?

### El checklist del ingeniero ético

Antes de empezar un proyecto de IA con datos personales, preguntate:

- [ ] ¿Tengo consentimiento informado para usar estos datos?
- [ ] ¿El uso es proporcional al fin declarado?
- [ ] ¿Los datos son correctos y están actualizados?
- [ ] ¿Están protegidos contra accesos no autorizados?
- [ ] ¿Puedo explicarle a una persona qué hago con sus datos en lenguaje sencillo?
- [ ] ¿Tengo documentado todo en un registro de tratamientos?
- [ ] ¿Sé qué hacer si hay un incidente de seguridad?

### Documentos mínimos

Todo proyecto serio de IA con datos personales debe tener:

1. **Política de privacidad:** Documento público que explica qué datos se recopilan y cómo se usan
2. **Registro de tratamientos:** Lista detallada de todas las actividades con datos personales
3. **Evaluación de impacto:** Análisis de riesgos para los derechos de las personas
4. **Contratos de confidencialidad:** Acuerdos con quienes acceden a los datos
5. **Plan de respuesta a incidentes:** Qué hacer si hay una filtración

---

## Parte 5: Integración con la Arquitectura del Proyecto

### Cómo documentar decisiones de gobernanza en el repo

En un proyecto de IA, la gobernanza no es solo un tema legal; es parte de la **arquitectura técnica**. Debemos documentar:

1. **En `ARCHITECTURE.md`:** Qué datos se usan, de dónde vienen, cómo se protegen
2. **En un archivo `POLITICA_PRIVACIDAD.md`:** La política de privacidad del proyecto
3. **En el `.env`:** Variables que contengan configuración de privacidad
4. **En los comentarios del código:** Decisiones de protección de datos

### El archivo `POLITICA_PRIVACIDAD.md`

Este archivo debe contener:
- Qué datos se recopilan
- Para qué se usan
- Con quién se comparten
- Cuánto tiempo se guardan
- Cómo se protegen
- Cómo ejercer derechos
- Contacto del responsable

---

## Parte 6: Sanciones y Consecuencias Legales — Cuando la Cosas se Ponen Serias

### El marco sancionatorio de la LOPDP

La LOPDP no es solo un documento de buenas intenciones. Tiene **dientes**. Esto significa que hay consecuencias reales, medibles y dolorosas por no cumplir.

**Analogía:** Es como el semáforo en una intersección. Si lo cruzás en rojo, no es solo "no recomendable"; es multa, puntos en la licencia, y si chocás, responsabilidad civil y penal.

### Tipos de sanciones

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Amonestación pública** | La SUPERCOM te "pega el nombre" en los periódicos | Tu empresa aparece en El Comercio por violar datos de clientes |
| **Multa económica** | Pago en dólares (no en días de trabajo) | Desde $500 hasta el 2% de los ingresos anuales |
| **Cierre temporal** | Suspensión de actividades | Tu app se baja de las tiendas mientras se investiga |
| **Cierre definitivo** | Liquidación de la empresa | Si la violación es gravísima y reincidente |
| **Responsabilidad civil** | Indemnización a los afectados | Pagar daños y perjuicios a cada persona afectada |
| **Responsabilidad penal** | Cárcel para los responsables | Hasta 3 años de prisión por delitos informáticos |

### Montos de las multas

Según la LOPDP y su reglamento:

- **Infracciones leves:** $200 - $1,000
- **Infracciones moderadas:** $1,000 - $5,000
- **Infracciones graves:** $5,000 - $20,000 o el 1% de los ingresos brutos anuales
- **Infracciones muy graves:** Hasta el 2% de los ingresos brutos anuales

**Dato real:** En 2023, la SUPERCOM impuso multas por más de $500,000 a empresas que violaron la LOPDP. Una empresa de telecomunicaciones pagó $150,000 por filtrar datos de 2 millones de clientes.

### ¿Qué constituye una infracción?

| Acción | Nivel | Consecuencia |
|--------|-------|--------------|
| No informar la finalidad del tratamiento | Leve | Amonestación + multa |
| No obtener consentimiento para datos sensibles | Grave | Multa + cierre temporal |
| Filtrar datos médicos por negligencia | Muy grave | Multa + responsabilidad civil + penal |
| Vender datos personales sin consentimiento | Muy grave | Cierre definitivo + cárcel |
| No atender derechos de titulares en 30 días | Moderada | Multa |
| No reportar incidentes de seguridad | Grave | Multa |
| No designar Delegado de Protección de Datos | Leve | Amonestación |

### Casos reales en Ecuador

#### Caso 1: Filtración del IESS (2019)
- **Qué pasó:** Se filtraron datos médicos de más de 1 millón de pacientes
- **Causa:** Vulnerabilidad en el sistema informático no parchada
- **Consecuencia:** Investigación de la Fiscalía, multas, demandas colectivas
- **Lección:** La seguridad no es opcional; es parte de la gobernanza

#### Caso 2: App de delivery que compartía ubicación
- **Qué pasó:** Una app de entrega de comida compartía la ubicación en tiempo real de los clientes con anunciantes
- **Causa:** Modelo de negocio basado en la venta de datos
- **Consecuencia:** Multa de $50,000, retiro de la app, demandas individuales
- **Lección:** La ubicación es dato personal; no se puede vender sin consentimiento

#### Caso 3: Banco que usaba datos para scoring social
- **Qué pasó:** Un banco usaba datos de redes sociales para evaluar la "reputación" de clientes
- **Causa:** Algoritmo de IA que discriminaba por actividad en redes
- **Consecuencia:** Cierre del programa, multa, investigación de la Defensoría del Pueblo
- **Lección:** La IA no puede discriminar; los datos tienen una finalidad específica

### Responsabilidad personal del ingeniero

**Punto crítico:** La responsabilidad no es solo de la empresa. El ingeniero de IA puede tener responsabilidad **personal**.

- **Responsabilidad civil:** Pagar daños si actuó con negligencia grave
- **Responsabilidad penal:** Cárcel si cometió un delito informático
- **Responsabilidad administrativa:** Multas personales por incumplimiento

**Analogía:** Es como un piloto de avión. Si el avión se cae por falla mecánica, responde la aerolínea. Si el avión se cae porque el piloto estaba borracho, responde el piloto personalmente.

### ¿Cómo protegerse?

1. **Documentar todo:** Cada decisión, cada consentimiento, cada medida de seguridad
2. **Seguir el principio de precaución:** Si no estás seguro, no lo hagas
3. **Consultar antes de actuar:** Cuando hay dudas, consulta con legal
4. **Capacitación continua:** Mantenerse actualizado sobre la ley
5. **Seguros de responsabilidad profesional:** Protección financiera ante errores

---

## Parte 7: Prompt Senior para Consultas sobre Protección de Datos y Gobernanza

### ¿Qué es un prompt senior?

Un prompt senior no es un prompt que "sé que existen las leyes". Es un prompt que **entiende el contexto**, **conoce las implicancias**, **sabe dónde buscar**, y **puede tomar decisiones informadas**.

### Prompt Senior: Consulta sobre Protección de Datos

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

### Prompt Senior: Auditoría de Cumplimiento

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

### Prompt Senior: Diseño de Política de Privacidad para IA

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

### Prompt Senior: Respuesta a Incidente de Seguridad

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

## Parte 8: Vibe Coding con Datos Personales — Cómo Hacerlo Bien sin Pecar de Inocente

### ¿Qué es "vibe coding" con datos personales?

El **vibe coding** es programar con la ayuda de IA, escribiendo instrucciones en lenguaje natural y dejando que la IA genere el código. Es poderoso, rápido y accesible.

**Pero:** Cuando los datos son personales, el vibe coding sin conocimiento es como manejar un auto de F1 sin saber frenar. Vas rápido, pero vas a chocar.

### El error del inocente

El error más común del ingeniero principiante con datos personales es pensar:

> "Si no tengo mala intención, no puedo hacer daño"

**Esto es falso.** La LOPDP se basa en el **tratamiento**, no en la **intención**. Si tratás datos personales sin cumplir la ley, violás la ley, sin importar tus buenas intenciones.

### Cómo hacer vibe coding con datos personales sin pecar de inocente

#### 1. Antes de escribir una línea de código

**Preguntas obligatorias:**
- ¿Este código va a manejar datos personales?
- ¿Tengo consentimiento para usar esos datos?
- ¿Estoy seguro de que son necesarios?
- ¿Están cifrados?
- ¿Puedo explicarle a la gente qué hago con sus datos?

**Prompt para el ingeniero:**
```
Antes de empezar a programar, respondé estas preguntas:
1. ¿Qué datos personales va a manejar este código?
2. ¿Para qué se van a usar exactamente?
3. ¿Tengo consentimiento informado?
4. ¿Son estrictamente necesarios?
5. ¿Cómo los voy a proteger?
6. ¿Qué pasaría si alguien ve mi código y mis datos?

Si no podés responder estas preguntas, no estás listo para programar.
```

#### 2. Durante el desarrollo

**Reglas de oro:**

| Regla | Por qué | Ejemplo de código |
|-------|---------|-------------------|
| **Nunca hardcodear datos personales** | Si el código es público, los datos también | ❌ `cedula = "1234567890"` ✅ `cedula = os.getenv("CEDULA")` |
| **Cifrar datos sensibles** | Si se filtra la base, los datos siguen protegidos | `encrypted = encrypt(data, key)` |
| **Loggear datos anonimizados** | Los logs pueden ser públicos | ❌ `log("Usuario Juan Pérez compró")` ✅ `log("Usuario ABC123 compró")` |
| **Validar entradas** | Evitar inyecciones y abusos | `if not is_valid_email(email): raise ValueError` |
| **Usar variables de entorno** | Las credenciales no van en el código | `DB_PASSWORD = os.getenv("DB_PASSWORD")` |

**Prompt para generar código seguro:**
```
Genera código Python para [describir funcionalidad] que:
1. NO almacene datos personales en variables hardcodeadas
2. USE variables de entorno para credenciales
3. CIFRE datos sensibles antes de almacenarlos
4. REGISTRE logs anonimizados
5. VALIDE todas las entradas
6. CUMPLA con el principio de minimización de datos
7. INCLUYA manejo de errores que no exponga datos
8. DOCUMENTE qué datos maneja y por qué
```

#### 3. Después del desarrollo

**Checklist post-desarrollo:**
- [ ] ¿El código expone datos personales en logs?
- [ ] ¿Las credenciales están en el código fuente?
- [ ] ¿Los datos sensibles están cifrados?
- [ ] ¿Se puede explicar a un usuario qué hace el código con sus datos?
- [ ] ¿Hay un mecanismo para eliminar datos cuando ya no se necesiten?
- [ ] ¿Se puede auditar quién accedió a qué datos?

### Ejemplo: Chatbot con datos personales

**Mal ejemplo (innocente):**
```python
# Chatbot que recuerda datos del usuario
import json

# BASE DE DATOS (esto es un desastre)
usuarios = {
    "juan": {
        "nombre": "Juan Pérez",
        "cedula": "1234567890",
        "email": "juan@email.com",
        "historial_medico": "Diabetes tipo 2, hipertensión",
        "direccion": "Av. Amazonas 1234"
    }
}

def responder(mensaje, usuario):
    # Usa datos personales sin protección
    print(f"Hola {usuarios[usuario]['nombre']}, ¿en qué puedo ayudarte?")
    # Registra todo en log (incluyendo datos sensibles)
    print(f"Log: Usuario {usuario} ({usuarios[usuario]['cedula']}) preguntó: {mensaje}")
    return "Hola, ¿cómo puedo ayudarte?"
```

**Buen ejemplo (con gobernanza):**
```python
# Chatbot con protección de datos
import os
from cryptography.fernet import Fernet
import logging

# Configurar logging sin datos personales
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Datos en variables de entorno (nunca hardcodeados)
DB_HOST = os.getenv("DB_HOST")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Cifrado para datos sensibles
CIPHER_KEY = os.getenv("CIPHER_KEY")
cipher = Fernet(CIPHER_KEY)

def cifrar_dato(dato):
    """Cifra datos personales antes de almacenar"""
    return cipher.encrypt(dato.encode()).decode()

def descifrar_dato(dato_cifrado):
    """Descifra datos personales para uso"""
    return cipher.decrypt(dato_cifrado.encode()).decode()

def responder(mensaje, usuario_id):
    """
    Responde al usuario usando solo el ID (anonimizado).
    Los datos personales se obtienen de la base de datos cifrada.
    """
    # Log ANONIMIZADO - no registra datos personales
    logger.info(f"Consulta de usuario {hash(usuario_id)}")
    
    # Obtener datos cifrados de la base de datos
    # (aquí iría la consulta real a la BD)
    nombre_cifrado = obtener_dato(usuario_id, "nombre")
    nombre = descifrar_dato(nombre_cifrado)
    
    # Responder sin exponer datos innecesarios
    respuesta = f"Hola {nombre}, ¿en qué puedo ayudarte?"
    
    # Log de respuesta (sin datos sensibles)
    logger.info(f"Respuesta enviada a usuario {hash(usuario_id)}")
    
    return respuesta
```

### La mentalidad del ingeniero senior con datos personales

| Mentalidad del principiante | Mentalidad del senior |
|----------------------------|----------------------|
| "Si funciona, está bien" | "Si funciona Y es seguro, está bien" |
| "La protección de datos es cosa de abogados" | "La protección de datos es parte de mi trabajo" |
| "Si no tengo mala intención, no hay problema" | "La intención no importa; importa el cumplimiento" |
| "Ya veré la seguridad después" | "La seguridad se diseña desde el inicio" |
| "Los datos son solo strings" | "Los datos son información sobre personas reales" |
| "La LOPDP es un obstáculo" | "La LOPDP es la guía para hacer las cosas bien" |

### Prompt para el ingeniero que quiere hacer las cosas bien

```
Sos un ingeniero de IA senior en Ecuador. Necesitás implementar un sistema que maneja datos personales.

ANTES de escribir código, hacé estas preguntas:

1. LEGALES:
   - ¿Tengo consentimiento informado?
   - ¿La finalidad es específica y documentada?
   - ¿Los datos son proporcionales al fin?
   - ¿Puedo demostrar cumplimiento?

2. TÉCNICAS:
   - ¿Cómo cifro los datos sensibles?
   - ¿Cómo controlo el acceso?
   - ¿Cómo registro auditoría sin exponer datos?
   - ¿Cómo elimino datos cuando ya no se necesiten?

3. ÉTICAS:
   - ¿Le explicaría a mi abuela qué hago con sus datos?
   - ¿Firmaría este código con mi nombre?
   - ¿Estaría tranquilo si esto sale en el periódico?

Si alguna respuesta es "no" o "no sé", no empieces a programar hasta tener la respuesta correcta.
```

---

## Parte 9: La Ley Europea de IA — Cuando tu Producto Debe Llevar Etiqueta

### ¿De qué va esta parte?

Hasta ahora hablamos de la LOPDP ecuatoriana, que protege los datos personales de las personas en Ecuador. Pero hay una ley **mucho más ambiciosa** que ya está vigente y que afecta a **cualquier empresa en el mundo** que cree o use productos de IA. Se llama **AI Act** (Ley de Inteligencia Artificial de la Unión Europea).

Y tiene una regla que cambia todo: **todo producto resultado de IA debe ser identificable**.

### ¿Qué es el AI Act?

El **AI Act** (Reglamento de Inteligencia Artificial) es la **primera ley integral de IA del mundo**. Fue aprobado por el Parlamento Europeo en marzo de 2024 y entró en vigor el 1 de agosto de 2024.

**En lenguaje sencillo:** La Unión Europea se sentó y dijo: "La IA es poderosa, pero necesitamos reglas del juego antes de que se salga de control."

### ¿Por qué importa si no vivimos en Europa?

Porque la UE tiene **450 millones de consumidores** y es el mercado más grande del mundo. Si tu empresa quiere vender productos o servicios en Europa (o competir con empresas que sí lo hacen), necesitás cumplir esta ley.

**Analogía:** Es como cuando el iPhone dejó de traer cargador. Apple no es europea, pero tuvo que adaptarse porque el mercado europeo lo exige. Con la IA pasa lo mismo: la ley europea se convierte en el **estándar global de facto**.

### Las 4 categorías de riesgo del AI Act

La ley clasifica los sistemas de IA según su nivel de riesgo:

| Nivel de riesgo | Qué significa | Ejemplos | ¿Qué exige la ley? |
|-----------------|---------------|----------|---------------------|
| **Riesgo inaceptable** | Prohibidos totalmente | Vigilancia masiva en tiempo real, manipulación de personas, scoring social | **PROHIBIDOS** — no se pueden crear ni usar |
| **Riesgo alto** | Requieren control estricto | Sistemas de IA para contratar personas, diagnosticar médicos, evaluar créditos, conducir autos | Evaluación obligatoria, transparencia, supervisión humana |
| **Riesgo limitado** | Requieren transparencia | Chatbots, deepfakes, reconocimiento de emociones | **Debe decirse que es IA** — etiquetado obligatorio |
| **Riesgo mínimo** | Sin requisitos especiales | Filtros de spam, sistemas de recomendación de películas | Solo buenas prácticas |

### La regla del etiquetado: TODO debe ser identificable

Aquí es donde la ley se pone interesante para lo que nos importa. El AI Act establece que:

**Para sistemas de IA de riesgo limitado y alto:**
> "Los sistemas de IA que generen texto, imágenes, audio o video que parezcan humanos deben hacer saber al usuario que el contenido fue generado por IA."

**Traducción:** Si tu IA escribe un correo, genera una imagen, crea un video o produce un audio, **tiene que decir que no es humano**. Punto.

### ¿Qué significa "marca de agua" (watermarking)?

Una **marca de agua** (watermark) es una señal invisible o visible que indica que algo fue creado por IA. Es como el sello de agua en los billetes: no lo ves a simple vista, pero si lo sabés buscar, está ahí.

**Ejemplos de marcas de agua en IA:**

| Tipo de contenido | Cómo se marca | Ejemplo |
|-------------------|---------------|---------|
| **Texto** | Patrones estadísticos en la elección de palabras | Las IAs tienden a usar ciertas palabras con más frecuencia que los humanos |
| **Imágenes** | Metadatos invisibles en el archivo | C2PA, Steganography, firmas digitales |
| **Audio** | Frecuencias imperceptibles insertadas | Marcas de agua acústicas |
| **Video** | Combinación de marca en imagen + audio | Marcas en cada frame + pista de audio |

### Claude y su marca de agua

**Anthropic** (la empresa detrás de Claude) ha trabajado activamente en sistemas de trazabilidad y seguridad. Aunque Claude no tiene una "marca de agua visible" como un sello en cada respuesta, su enfoque incluye:

1. **Política de uso:** Claude tiene términos de servicio que prohíben usarlo para generar contenido que se haga pasar por humano
2. **Trazabilidad interna:** Cada interacción queda registrada con metadatos que permiten rastrear el origen
3. **Commitment con la transparencia:** Anthropic es miembro de iniciativas como el Partnership on AI y respalda estándares de transparencia
4. **Claude como "consultor":** A diferencia de herramientas que se usan para copiar-pegar, Claude está diseñado para ser un asistente que **ayuda a pensar**, no a reemplazar el pensamiento

**El punto clave:** La marca de agua no es solo técnica; es una **filosofía de diseño**. Una IA bien gobernada facilita la transparencia por diseño. Una IA sin gobernanza facilita la confusión y el engaño.

### ¿Cómo afecta esto a las empresas ecuatorianas?

#### Escenario 1: Una empresa ecuatoriana que USA IA de proveedores extranjeros

Si tu empresa usa herramientas de IA de empresas que venden en Europa (Google, Microsoft, OpenAI, Anthropic, etc.), estas ya están implementando cambios para cumplir el AI Act. Esto significa:

| Qué ya está pasando | Impacto en tu empresa |
|---------------------|----------------------|
| Google agrega etiquetas a imágenes generadas por IA | Tus clientes sabrán que las imágenes no son reales |
| Microsoft marca contenido generado por Copilot | Tus documentos tendrán transparencia de origen |
| OpenAI agrega metadatos a imágenes DALL-E | Tus diseños tendrán trazabilidad |
| Anthropic mejora la transparencia de Claude | Tus consultas a Claude tienen registro de origen |

**¿Tu empresa necesita hacer algo?** Sí: **adaptar tus procesos internos** para que cuando uses IA, lo hagas con transparencia. No es solo cumplir la ley; es construir confianza.

#### Escenario 2: Una empresa ecuatoriana que CREA productos con IA

Si tu empresa crea productos (apps, contenido, herramientas) que usan IA y planea vender fuera de Ecuador (o competir con empresas que sí lo hacen):

| Requisito del AI Act | Qué debes implementar |
|----------------------|-----------------------|
| **Transparencia** | Decir a tus usuarios que tu producto usa IA |
| **Etiquetado** | Marcar el contenido generado por IA |
| **Evaluación de impacto** | Si es riesgo alto, documentar y evaluar riesgos |
| **Supervisión humana** | Asegurar que un humano pueda intervenir en decisiones de IA |
| **Documentación técnica** | Mantener documentación de cómo funciona tu sistema de IA |

#### Escenario 3: Una empresa que YA usa IA para su trabajo

Si tu empresa ya tiene flujos de trabajo con IA (copywriting con ChatGPT, diseño con Midjourney, código con Copilot, etc.), el AI Act impacta así:

| Área | Impacto | Acción recomendada |
|------|---------|-------------------|
| **Marketing** | Los contenidos generados por IA deben marcarse | Agregar disclaimer: "Este contenido fue asistido por IA" |
| **Diseño** | Las imágenes deben indicar su origen | Usar herramientas que incluyan metadatos C2PA |
| **Legal** | Debes poder demostrar qué IA usás y cómo | Documentar qué herramientas de IA usa cada departamento |
| **RRHH** | Si usás IA para evaluar candidatos, es "alto riesgo" | Implementar supervisión humana obligatoria |
| **Ventas** | Si vendés productos con IA en Europa, debes cumplir AI Act | Evaluar si tus productos son de riesgo alto/limitado |

### La conexión entre el AI Act y la LOPDP

La LOPDP ecuatoriana y el AI Act europeo no compiten; se **complementan**:

| Aspecto | LOPDP (Ecuador) | AI Act (Europa) |
|---------|-----------------|-----------------|
| **Enfoque** | Proteger datos personales | Regular sistemas de IA |
| **Alcance** | Empresas que operan en Ecuador | Empresas que venden en Europa |
| **Sanciones** | Hasta 2% de ingresos anuales | Hasta 35 millones de euros o 7% de facturación mundial |
| **Transparencia** | Informar sobre uso de datos | Informar sobre uso de IA |
| **Derechos** | Acceso, rectificación, eliminación | Explicación de decisiones de IA |
| **Obligación principal** | Consentimiento y gobernanza de datos | Etiquetado y evaluación de riesgos |

**La lección:** Si cumplís la LOPDP y además implementás transparencia de IA (etiquetado, documentación), estás cubierto para ambos mercados.

### ¿Qué pasa si no cumplo el AI Act?

Las sanciones del AI Act son **las más duras del mundo en materia de IA**:

| Nivel de infracción | Multa |
|---------------------|-------|
| **Riesgo inaceptable** (prohibido) | Hasta 35 millones de euros o 7% de la facturación mundial |
| **Riesgo alto** (sin evaluación) | Hasta 15 millones de euros o 3% de la facturación mundial |
| **Información incorrecta** | Hasta 7.5 millones de euros o 1% de la facturación mundial |

**Dato:** Para una empresa mediana ecuatoriana, 7 millones de euros son aproximadamente **$7.5 millones**. No es una multa que se pueda ignorar.

### La mentalidad correcta: Transparencia como ventaja competitiva

Muchas empresas ven la regulación como un obstáculo. Los ingenieros inteligentes la ven como una **oportunidad**:

| Empresa que huye de la transparencia | Empresa que abraza la transparencia |
|--------------------------------------|--------------------------------------|
| Oculta que usa IA para no "asustar" clientes | Anuncia que usa IA para mejorar el servicio |
| Copia-pegue de contenido IA sin marcar | Marca cada pieza con origen y proceso |
| Teme ser reemplazada por la regulación | Se adapta y lidera el cumplimiento |
| Pierde confianza cuando la descubren | Gana confianza por ser honesta |

**Ejemplo real:** Empresas como Google, Microsoft y Apple ya están implementando etiquetado de contenido generado por IA en todos sus productos. No lo hacen porque les gusta; lo hacen porque saben que la confianza del usuario es el recurso más valioso.

### Tu rol como Ingeniero de IA

Como ingeniero de IA, no solo debés saber programar. Debés saber:

1. **Qué leyes aplican** a tu producto (LOPDP en Ecuador, AI Act si vendés en Europa)
2. **Cómo implementar transparencia** (etiquetado, metadatos, documentación)
3. **Cómo documentar** decisiones de IA para poder demostrar cumplimiento
4. **Cómo decir "no"** cuando un jefe pida algo que viole la ley, aunque sea "técnicamente posible"
5. **Cómo educar** a tu equipo sobre el uso responsable de IA

**La pregunta que todo ingeniero debe hacerse:**
> "¿Firmaría este producto con mi nombre, sabiendo que cualquier auditor puede revisar cómo funciona?"

Si la respuesta es "no", tenés un problema de gobernanza, no de código.

### Resumen de la Parte 9

| Concepto | Qué significa |
|----------|---------------|
| **AI Act** | Primera ley integral de IA del mundo (Unión Europea, 2024) |
| **Etiquetado obligatorio** | Todo contenido generado por IA debe ser identificable |
| **Marca de agua** | Señal técnica que indica el origen IA de un contenido |
| **Alcance global** | Afecta a cualquier empresa que quiera vender en Europa |
| **Sanciones** | Hasta 7% de facturación mundial (millones de euros) |
| **Oportunidad** | La transparencia construye confianza y ventaja competitiva |
| **Tu rol** | Implementar transparencia, documentar, educar, decir "no" cuando sea necesario |

---

## Resumen: Lo que debés recordar

1. **Gobernanza de datos** es el manual de instrucciones para manejar información ordenada y responsablemente
2. **Los datos personales** son cualquier información que identifica a una persona
3. La **LOPDP** es la ley ecuatoriana que protege los derechos de las personas sobre sus datos
4. Los **5 principios** son: consentimiento, finalidad, proporcionalidad, calidad y seguridad
5. Las personas tienen **derechos** sobre sus datos (acceso, rectificación, eliminación, etc.)
6. Quien maneja datos tiene **obligaciones** claras (informar, proteger, documentar)
7. Para proyectos de IA, la gobernanza es **arquitectura**, no burocracia
8. **Documentar** es parte del trabajo del ingeniero de IA
9. El **AI Act europeo** obliga a que todo producto de IA sea **identificable y etiquetado**
10. La **marca de agua** (watermarking) es la técnica que hace rastreable el contenido generado por IA
11. El AI Act afecta a **cualquier empresa** que quiera vender en Europa, incluidas las ecuatorianas
12. Las **sanciones** del AI Act pueden llegar al 7% de la facturación mundial
13. La **transparencia** no es un obstáculo; es una **ventaja competitiva**
14. Tu rol como ingeniero es **implementar transparencia, documentar y educar**

---

## El Ingeniero de IA en esta Clase

El ingeniero de IA no es solo un técnico que escribe código o diseña modelos. Es un **constructor de confianza**. Cuando diseñás un sistema que maneja datos de personas reales, estás tomando decisiones que afectan vidas reales.

Un buen ingeniero de IA:
- **Piensa en las personas primero**, antes que en la tecnología
- **Documenta** cada decisión de protección de datos
- **Diseña** sistemas que facilitan el ejercicio de derechos
- **Protege** la información como si fuera suya
- **Dice "no"** cuando un uso de datos es éticamente cuestionable, aunque sea técnicamente posible
- **Implementa transparencia** en todo lo que crea (etiquetado, marcas de agua, documentación)
- **Conoce las leyes** que aplican a su producto (LOPDP, AI Act)
- **Educa a su equipo** sobre uso responsable de IA

La gobernanza y la protección de datos no son restricciones; son la **base** para construir sistemas de IA en los que la gente pueda confiar. Y en un mundo donde la confianza es el recurso más escaso, eso no es solo ético: es inteligente.