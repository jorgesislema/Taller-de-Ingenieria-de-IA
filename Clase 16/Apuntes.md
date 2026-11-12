MATERIAL DE CLASE

Gobernanza de datos e inteligencia artificial

Diseño de proyectos y auditoría

Ecuador, Latinoamérica, Unión Europea y Estados Unidos

La gobernanza permite demostrar qué datos utiliza un proyecto, quién autorizó su uso, cómo protege a las personas y qué pruebas respaldan sus decisiones.

Clase para estudiantes, programadores y auditores. Incluye una comparación normativa y listas de control para diseño, eliminación y auditoría.

  

# Contenido

Los títulos permiten navegar por los temas desde Word. Las referencias externas permanecen enlazadas en el texto.

[1 Qué decisiones debe tomar un proyecto](#capitulo_0)

[2 Gobernanza de datos según DAMA](#capitulo_1)

[3 Gobernanza de IA y su relación con los datos](#capitulo_2)

[4 Ecuador como punto de partida](#capitulo_3)

[5 Comparación de Latinoamérica](#capitulo_4)

[6 Unión Europea](#capitulo_5)

[7 Estados Unidos](#capitulo_6)

[8 Derechos y obligaciones del programador](#capitulo_7)

[9 Lista de control antes de escribir código](#capitulo_8)

[10 Qué páginas y canales debe ofrecer la aplicación](#capitulo_9)

[11 Eliminación comprobable y retiro de bases de datos](#capitulo_10)

[12 Lista de auditoría en construcción y producción](#capitulo_11)

[13 Puertas de decisión y caso integrador](#capitulo_12)

  

# [1 Qué decisiones debe tomar un proyecto](https://)

Un proyecto bien gobernado puede demostrar **qué datos utiliza, para qué los necesita, quién decidió ese uso, cómo protege a las personas y qué evidencia prueba que sus controles funcionan**. La gobernanza se refleja en decisiones antes de programar y en controles observables después de publicar. Una política escrita no sustituye el código, la configuración ni las pruebas que la hacen efectiva.

Esta clase sirve a estudiantes, programadores, responsables de producto y auditores. Puede impartirse en dos sesiones de dos horas. La primera cubre conceptos, responsabilidades y regulación; la segunda, diseño, eliminación, auditoría y el caso integrador. El marco jurídico se revisó con corte al 8 de noviembre de 2026. La matriz es selectiva: un proyecto concreto requiere validar jurisdicción, sector, contrato y texto vigente.

## Caso que conecta la clase

Una academia de Quito quiere lanzar un asistente que conteste con sus documentos. Tiene manuales públicos, registros de alumnos y actas internas. Un proveedor externo podría recibir preguntas, fragmentos y telemetría. Antes de programar, la academia separa los datos y decide que el piloto solo indexará manuales públicos aprobados. Esa decisión se comprueba con una búsqueda que intenta recuperar un acta privada, una prueba de aislamiento y una revisión de los datos que salen hacia el proveedor.

El mismo proyecto ilustra dos decisiones distintas. Si una persona pide eliminar su cuenta, el equipo debe localizar sus datos y decidir qué puede suprimir y qué debe conservar por una obligación válida. Si el asistente se equivoca al informar una fecha, el equipo debe comprobar la fuente, el modelo, la configuración y el proceso de revisión. Resolver un problema no resuelve automáticamente el otro.

| Idea             | En palabras simples                                                 | Evidencia                                                   |
| ---------------- | ------------------------------------------------------------------- | ----------------------------------------------------------- |
| Gobernanza       | Establece quién decide, bajo qué reglas y quién responde.           | Política aprobada, dueño y decisión fechada.                |
| Gestión de datos | Ejecuta las decisiones a lo largo del ciclo de vida.                | Inventario, controles de calidad, permisos y retención.     |
| Privacidad       | Protege a personas frente al uso de sus datos.                      | Finalidades, bases, avisos, derechos y revisión de impacto. |
| Seguridad        | Reduce accesos indebidos, alteraciones y pérdida de disponibilidad. | Pruebas de autorización, registros y restauraciones.        |
| Cumplimiento     | Comprueba si se satisfacen normas y obligaciones aplicables.        | Matriz normativa enlazada a controles y pruebas.            |
| Auditoría        | Contrasta controles y evidencia con un criterio definido.           | Hallazgos reproducibles, responsables y revalidación.       |

## Datos que suelen pasar inadvertidos

Un dato es personal si identifica o permite identificar a una persona conforme al marco aplicable. Un identificador de sesión, un correo en un log, una voz grabada o un texto libre pueden ser personales. La sensibilidad depende de la ley y el contexto. La combinación de varias fuentes puede volver identificable un conjunto que parecía inocuo.

Seudonimizar significa reducir la identificación directa, conservando una posibilidad de vinculación. Un hash o identificador sustituto no garantiza anonimización. Anonimizar exige evaluar si la reidentificación sigue siendo razonablemente posible en el contexto aplicable. Los datos sintéticos también se revisan si derivan de registros reales o pueden reproducirlos.

# [2 Gobernanza de datos según DAMA](https://)

DAMA International organiza la gestión en once áreas de conocimiento. Su DMBOK es un cuerpo de buenas prácticas, no una ley ni una certificación de cumplimiento de un producto. Para un equipo pequeño, la mejor entrada es asignar dueño, documentar origen y finalidad, controlar acceso y medir calidad. El equipo añade formalidad conforme crecen el riesgo y la complejidad. [DAMA International y áreas de gestión](https://dama.org/about-dama/what-is-data-management/).

| Área de DAMA                                   | Decisión aplicada al proyecto                           | Ejemplo de evidencia                              |
| ---------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------- |
| Gobernanza                                     | Quién aprueba usos, riesgos y excepciones.              | Acta y matriz de decisión.                        |
| Arquitectura                                   | Dónde se generan, almacenan y transfieren los datos.    | Diagrama de flujo y fronteras de confianza.       |
| Modelado y diseño                              | Qué representa cada entidad, campo y relación.          | Esquema con claves y reglas de integridad.        |
| Almacenamiento y operación                     | Cómo se conserva, restaura y retira información.        | Restauración probada y calendario de expiración.  |
| Seguridad                                      | Quién accede y cómo se limita y verifica el acceso.     | Matriz de roles y pruebas de acceso negativo.     |
| Integración e interoperabilidad                | Cómo se comparten datos, formatos y cambios de esquema. | Contratos de API y trazabilidad de integraciones. |
| Documentos y contenidos                        | Quién aprueba fuentes, versiones y acceso a archivos.   | Catálogo de documentos y fechas de vigencia.      |
| Datos maestros y de referencia                 | Qué fuente define identidades y valores comunes.        | Diccionario y reglas para resolver duplicados.    |
| Almacenes analíticos e inteligencia de negocio | Qué copias analíticas se crean y cómo se protegen.      | Flujo de extracción y permisos de reportes.       |
| Metadatos                                      | Qué sabemos del origen, propósito, dueño y recorrido.   | Catálogo, linaje y etiquetas de retención.        |
| Calidad                                        | Qué exactitud, integridad y vigencia exige cada uso.    | Reglas, mediciones y alertas con dueño.           |

Un dueño de datos decide prioridades y usos de su dominio; un steward mantiene definiciones y sigue la calidad; un custodio administra medios y acceso. Son funciones organizativas. El **responsable del tratamiento** y el **encargado** son roles jurídicos definidos por lo que efectivamente hacen, no por un nombre en el organigrama. El dueño de datos no es dueño de los derechos de los titulares.

## Indicadores con evidencia

| Indicador           | Medición útil                                                                             | Error que evita                              |
| ------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------- |
| Inventario cubierto | Activos con dueño y finalidad / activos identificados mediante catálogo y descubrimiento. | Medir solo lo que ya se conocía.             |
| Calidad             | Registros válidos conforme a una regla y período / registros evaluados.                   | Un promedio que oculta un fallo crítico.     |
| Retención           | Elementos vencidos sin excepción activa, por sistema y antigüedad.                        | Suponer que un job programado terminó bien.  |
| Derechos            | Casos respondidos en plazo / casos que vencían en el período, con atrasos visibles.       | Promediar tiempos y esconder casos vencidos. |
| Acceso              | Roles privilegiados vencidos o sin revisión y pruebas de aislamiento.                     | Confundir autenticación con autorización.    |

# [3 Gobernanza de IA y su relación con los datos](https://)

Gobernar IA implica decidir qué sistemas pueden utilizarse, para qué, con qué supervisión, con qué límites de desempeño y quién puede detenerlos. Incluye modelos propios, servicios externos y sistemas que incorporan IA en un proceso. También incluye cómo el equipo usa asistentes para programar: herramientas autorizadas, reglas de entrada y revisión del código generado.

| Dimensión    | Gobernanza de datos                                                           | Gobernanza de IA                                                                                 |
| ------------ | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Objeto       | Activos, flujos, calidad, acceso, uso y retención.                            | Sistema, modelo, comportamiento y efectos de sus resultados.                                     |
| Pregunta     | ¿Este dato puede usarse aquí y quién lo autoriza?                             | ¿Este sistema puede recomendar, decidir o actuar en este contexto?                               |
| Riesgos      | Uso incompatible, errores de registros, filtraciones, exceso de conservación. | Sesgo, invención, deriva, uso fuera de alcance, automatización indebida o ejecución de acciones. |
| Evidencia    | Inventario, linaje, contratos, permisos, pruebas de supresión.                | Ficha del sistema, versiones, evaluación, supervisión y plan de retiro.                          |
| Intersección | Origen, licencia, representatividad, datos personales y acceso.               | Entradas, entrenamiento, consultas, recuperación, salidas, feedback y telemetría.                |

## NIST AI RMF como marco de trabajo

NIST propone cuatro funciones que se aplican de forma iterativa: **Govern**, establecer responsabilidades y políticas; **Map**, entender uso, personas afectadas y contexto; **Measure**, medir riesgos y desempeño; **Manage**, priorizar, mitigar, vigilar y retirar. Es un marco voluntario que puede apoyar obligaciones o contratos específicos, sin sustituirlos. El perfil de IA generativa aborda riesgos propios de esa tecnología. [AI RMF de NIST](https://www.nist.gov/itl/ai-risk-management-framework) y [perfil para IA generativa](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf).

| Entregable              | Contenido mínimo operativo                                                                                      |
| ----------------------- | --------------------------------------------------------------------------------------------------------------- |
| Inventario de IA        | Dueño, finalidad, usuarios, modelo y versión, proveedor, fuentes, herramientas, permisos y entorno.             |
| Ficha del sistema       | Uso previsto, usos excluidos, población afectada, limitaciones, revisión humana y ruta de reclamo.              |
| Evaluación              | Casos normales, errores, subgrupos pertinentes, abuso, seguridad, privacidad, límites y umbrales de aceptación. |
| Decisión de lanzamiento | Versión aprobada, riesgo residual, controles, responsable, fecha y condiciones de reversión.                    |
| Vigilancia y retiro     | Alertas, revisión de cambios del proveedor, mecanismo de pausa, sustitución y borrado según alcance.            |

En IA generativa se comprueban, entre otros riesgos, filtración de datos, inyección de instrucciones en documentos, citas que no respaldan afirmaciones, acceso entre clientes y llamadas a herramientas sin autorización. En un RAG se mide por separado si se recuperó el pasaje correcto y si la respuesta lo utilizó bien. El filtro de autorización debe actuar antes de incorporar documentos al contexto; las instrucciones al modelo no reemplazan esa barrera.

La supervisión humana es significativa cuando el revisor recibe contexto suficiente, entiende las limitaciones, dispone de tiempo y puede corregir o rechazar el resultado. Un botón de aprobación sin esa capacidad no aporta la misma protección. Para un uso de consecuencias importantes, la organización debe definir un canal de impugnación y un modo alternativo de atención.

# [4 Ecuador como punto de partida](https://)

El artículo 66.19 de la Constitución reconoce la protección de datos personales. El artículo 92 regula la garantía de hábeas data. La **Ley Orgánica de Protección de Datos Personales** (LOPDP), su Reglamento General —Decreto 904— y las normas secundarias de la **SPDP** desarrollan el régimen. El artículo 3 de la ley contempla aplicación en determinados supuestos fuera del país, por ejemplo ofertas o monitoreo de personas residentes en Ecuador bajo las condiciones legales. La ubicación del servidor, por sí sola, no decide la aplicabilidad. [Constitución](https://www.asambleanacional.gob.ec/es/contenido/constitucion-de-la-republica-del-ecuador), [LOPDP](https://spdp.gob.ec/wp-content/uploads/2024/12/03.pdf.pdf) y [Reglamento General](https://spdp.gob.ec/wp-content/uploads/2024/12/04.pdf.pdf).

## De la ley a los controles

| Tema                            | Criterio jurídico                                                                                                                          | Implicación para el sistema                                                                                                |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Finalidad y base                | Arts. 7, 8 y 10: definir finalidad y base aplicable; consentimiento es una de las bases.                                                   | Una fila por finalidad. Separar servicio, analítica y marketing; si hay consentimiento, demostrarlo y permitir revocación. |
| Transparencia                   | Art. 12: informar en forma clara y en el momento que corresponda.                                                                          | Aviso versionado y mensajes donde se recoge el dato.                                                                       |
| Derechos                        | Arts. 13–20 y reglas aplicables: acceso, rectificación, eliminación, oposición, portabilidad, suspensión y salvaguardas de automatización. | Canal de solicitudes, identidad proporcional, expediente y pruebas de cumplimiento.                                        |
| Seguridad y diseño              | Arts. 37–42 y 47: medidas proporcionales y responsabilidad demostrable; evaluación de impacto en los supuestos aplicables.                 | Diseño por defecto restrictivo, análisis de riesgos y controles probados.                                                  |
| Delegado                        | Art. 48, Reglamento y normas secundarias: designación en los supuestos previstos.                                                          | Analizar aplicabilidad y asegurar independencia; el delegado asesora y supervisa.                                          |
| Comunicaciones y transferencias | LOPDP, Reglamento y Resolución SPDP-SPD-2026-0004-R; verificar modificaciones aplicables.                                                  | Registrar destinatarios, finalidades, regiones, accesos remotos, garantías y subencargados.                                |

El interés legítimo exige justificar necesidad y ponderación cuando proceda; no se usa como salida automática para cualquier reutilización. Las categorías especiales, los menores y ciertos usos biométricos requieren análisis específico. Se documenta la evaluación de impacto antes del tratamiento cuando corresponda, por ejemplo en ciertos tratamientos a gran escala, observación sistemática o valoraciones automatizadas de efecto relevante. Si se decide que no aplica, se registra el razonamiento. [Resoluciones y guías de la SPDP](https://www.spdp.gob.ec/resoluciones/).

## Plazos operativos ecuatorianos

| Evento                              | Referencia                                                                                                                                          | Diseño recomendado                                                                                                                       |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Acceso, rectificación y eliminación | Arts. 13–15: 15 días para los supuestos allí previstos; eliminación procedente y gratuita.                                                          | Crear expediente al recibir; verificar sin dilaciones indebidas; alertar con margen. No extender automáticamente por un trámite interno. |
| Encargado conoce vulneración        | Art. 43: informar al responsable tan pronto sea posible; máximo término de 2 días desde conocimiento.                                               | Canal de guardia, contrato, fecha de conocimiento y evidencia de entrega.                                                                |
| Responsable conoce vulneración      | Art. 43: notificar a SPDP y ARCOTEL cuanto antes; máximo término de 5 días desde constancia, salvo que sea improbable el riesgo exigido por la ley. | Evaluar y documentar el riesgo; no esperar al informe final para escalar.                                                                |
| Vulneración con riesgo al titular   | Art. 46: sin dilación, dentro del término de 3 días desde conocimiento del riesgo; con las excepciones del artículo.                                | Mensaje comprensible, medidas y recomendaciones; conservar evidencia de comunicación.                                                    |

**Término, plazo y horas no son equivalentes.** El responsable debe determinar el cómputo aplicable, el hito inicial y los canales vigentes. La Resolución SPDP-SPD-2026-0040-R desarrolla las notificaciones; no sustituye el análisis del supuesto legal ni los plazos de la LOPDP. [Norma técnica de notificaciones](https://www.spdp.gob.ec/wp-content/uploads/2026/10/SPDP-SPD-2026-0040-r.pdf) y [publicación en Registro Oficial](https://www.registroficial.gob.ec/suplemento-no-376/).

## Datos personales en sistemas de IA

La Resolución SPDP-SPD-2026-0009-R, reformada por la 0037-R, regula la protección de datos personales en el uso de sistemas de IA dentro de su alcance. No equivale a un régimen integral para cualquier IA que no trate datos personales. La reforma delimita obligaciones del encargado según su acceso, visibilidad o control efectivo en cada operación o fase. El encargado que alegue no tenerlos debe poder acreditarlo; no es una exoneración general. Cuando provee, desarrolla o mantiene el sistema, la reforma contempla que facilite al responsable información suficiente sobre funcionamiento, límites, riesgos y controles en los términos de la norma.

En el proyecto esto significa mapear si el proveedor puede ver prompts, adjuntos, fragmentos, resultados o logs; evaluar los riesgos antes del desarrollo cuando se traten datos personales y hacer la EIPD cuando corresponda. El art. 20 de la LOPDP tiene condiciones propias sobre valoraciones automatizadas; no se debe copiar literalmente el alcance del art. 22 del RGPD. [Norma original](https://www.spdp.gob.ec/wp-content/uploads/2026/08/ResolIA.pdf), [reforma 0037-R](https://www.spdp.gob.ec/wp-content/uploads/2026/10/SPDP-SPD-2026-0037-R.pdf) y [publicación del 21 de septiembre de 2026](https://www.registroficial.gob.ec/registro-oficial-no-373-21/).

## Multas ecuatorianas y cómo leerlas

| Gravedad        | Entidad de derecho privado o empresa pública en los supuestos legales                                     | Servidor o funcionario del sector público cuya acción u omisión incurra en la infracción |
| --------------- | --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Leve — art. 71  | 0,1 % a 0,7 % del volumen de negocio del ejercicio económico inmediatamente anterior al de la imposición. | 1 a 10 salarios básicos unificados.                                                      |
| Grave — art. 72 | 0,7 % a 1 % de ese volumen de negocio.                                                                    | 10 a 20 salarios básicos unificados.                                                     |

El art. 73 define la base, con deducción del IVA y de otros impuestos directamente relacionados. Si el volumen relevante fuera USD 1.000.000, la aritmética orientativa sería USD 1.000–7.000 para el tramo leve y USD 7.000–10.000 para el grave; no predice una resolución. Importan la tipificación, la metodología, la graduación y el procedimiento. Las medidas correctivas y cautelares pueden tener un impacto operativo distinto de la multa. [LOPDP arts. 65–76](https://spdp.gob.ec/wp-content/uploads/2024/12/03.pdf.pdf) y [metodología SPDP 2025-0022-R en el índice oficial](https://www.spdp.gob.ec/resoluciones/).

# [5 Comparación de Latinoamérica](https://)

No hay una sola ley latinoamericana. La matriz resume marcos seleccionados que suelen aparecer en proyectos regionales. Los importes se presentan en la unidad jurídica original; no conviene convertirlos ni sumar sanciones de distintos países como si fueran comparables. El alcance público y privado, la autoridad, las excepciones y los plazos se revisan país por país.

| Jurisdicción y norma                                        | Punto de diseño                                                                                                                                                                                                                             | Ejemplo de sanción y referencia                                                                                                                                                                                                           |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Brasil — LGPD, Lei 13.709/2018; ANPD                        | Bases, derechos, encargado de protección cuando corresponda y transferencias. Documentar el tratamiento y el rol del proveedor.                                                                                                             | Art. 52: multa simple de hasta 2 % de facturación en Brasil del sujeto o grupo indicado, último ejercicio y sin tributos, con tope de R$ 50 millones por infracción. También hay medidas no pecuniarias. Senado Federal.                  |
| México — LFPDPPP privada, nueva ley del 20 de marzo de 2025 | Aviso de privacidad y derechos ARCO: acceso, rectificación, cancelación y oposición. Diferenciar régimen privado y sujetos obligados públicos; no reutilizar una guía antigua que trate al INAI como autoridad vigente del régimen privado. | Art. 59: tramos de 100–160.000 UMA y 200–320.000 UMA según infracción; reglas adicionales por persistencia o datos sensibles. Aplicación por la Secretaría Anticorrupción y Buen Gobierno. Cámara de Diputados, texto vigente consultado. |
| Colombia — Ley 1581/2012; SIC                               | Autorización cuando corresponda, derechos del titular, obligaciones de responsables y encargados. Diferenciar transferencia y transmisión; verificar registro si aplica.                                                                    | Art. 23: hasta 2.000 salarios mínimos mensuales legales vigentes, con posibilidad de multas sucesivas si persiste el incumplimiento; el régimen de ese artículo se aplica a personas de naturaleza privada. Función Pública.              |
| Perú — Ley 29733; D.S. 016-2024-JUS; ANPD                   | Revisar registro de bancos, seguridad y derechos. Verificar calendario gradual del oficial de datos cuando aplica el Reglamento.                                                                                                            | Art. 39: leves 0,5–5 UIT; graves más de 5–50 UIT; muy graves más de 50–100 UIT; la multa no puede superar el 10 % de los ingresos brutos anuales del ejercicio anterior. Ley y Reglamento.                                                |
| Argentina — Ley 25.326; AAIP                                | Acceso, rectificación, actualización y supresión conforme a supuestos; analizar transferencias y disposiciones complementarias.                                                                                                             | Art. 31: rango nominal legal de ARS 1.000 a 100.000, además de otras medidas. No extrapolarlo a un expediente con varias infracciones. Texto oficial actualizado.                                                                         |
| Uruguay — Ley 18.331; URCDP                                 | Identificar responsable, finalidades y derechos; revisar inscripción y requisitos complementarios según actividad.                                                                                                                          | Art. 35 consolidado: hasta 500.000 unidades indexadas, además de otras potestades. IMPO, texto del artículo.                                                                                                                              |
| Chile — Ley 19.628 y transición a Ley 21.719                | Al corte de la clase, el nuevo régimen general todavía no aplica: entrada en vigor prevista el 1 de diciembre de 2026. Preparar el cambio sin tratar sus multas como vigentes antes de esa fecha.                                           | Nuevo art. 35: hasta 5.000, 10.000 y 20.000 UTM según categoría, con reglas especiales de recargo y reincidencia. BCN, vigencia y texto futuro.                                                                                           |

UMA es la Unidad de Medida y Actualización mexicana; UIT, la Unidad Impositiva Tributaria peruana; UI, la unidad indexada uruguaya; UTM, la unidad tributaria mensual chilena. El valor y momento de cálculo de cada unidad se verifican con su fuente oficial si se necesita cuantificar una exposición real.

# [6 Unión Europea](https://)

## RGPD o GDPR

El Reglamento (UE) 2016/679 establece reglas sobre tratamiento de datos personales. Art. 3: revisar establecimiento, oferta a personas en la Unión o monitoreo de su comportamiento en la Unión, según el supuesto. Art. 5: principios y responsabilidad demostrable. Arts. 6 y 9: base y, cuando haya categorías especiales, condición adicional aplicable. Arts. 12–22: transparencia, derechos y decisiones exclusivamente automatizadas con efectos jurídicos o similar importancia, con excepciones y garantías. [Texto del RGPD](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng).

| Cuestión                    | Artículos y control                                                                                                                                                                                               |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Información y derechos      | 12–15: aviso según origen y acceso; como regla, responder sin dilación y dentro de un mes, con extensión limitada y aviso oportuno cuando proceda.                                                                |
| Supresión                   | 17 y 19: evaluar causas y excepciones, y comunicación a destinatarios en las condiciones aplicables. No promete borrar obligaciones válidas de conservación.                                                      |
| Encargados y transferencias | 28 y 44–49: contrato, instrucciones, subencargados, mecanismo de transferencia y evaluación de garantías según el caso.                                                                                           |
| Diseño y seguridad          | 25, 30 y 32: diseño por defecto, registros cuando correspondan y medidas proporcionales.                                                                                                                          |
| Incidentes e impacto        | 33–35: autoridad sin dilación y, cuando sea viable, en 72 horas desde conocimiento si se cumple el criterio; titular sin dilación si hay alto riesgo, con excepciones. EIPD antes del tratamiento de alto riesgo. |
| Delegado                    | 37–39: designación en supuestos legales e independencia funcional.                                                                                                                                                |

**Sanciones.** El art. 83 prevé topes de EUR 10 millones o 2 %, y EUR 20 millones o 4 %, según el grupo de infracciones. Para empresas se toma el mayor entre el fijo y el porcentaje del volumen mundial anual del ejercicio anterior. Se consideran los factores del artículo, incluidas las reglas para infracciones vinculadas. Una indemnización por daños, una orden correctiva y una multa administrativa son figuras distintas.

## AI Act y calendario

El Reglamento (UE) 2024/1689 regula sistemas y modelos en función de roles y usos. Distingue prácticas prohibidas, sistemas de alto riesgo, deberes de transparencia para ciertos sistemas y obligaciones de proveedores de modelos de propósito general. Un sistema puede estar sujeto a RGPD y AI Act a la vez; cumplir uno no prueba cumplir el otro. El uso interno no equivale automáticamente a exclusión.

El Reglamento (UE) 2026/1744 modificó el calendario. La aplicación de las secciones 1, 2 y 3 del capítulo III se desplaza, según clasificación, al **2 de diciembre de 2027** para alto riesgo del art. 6.2 y anexo III, y al **2 de agosto de 2028** para art. 6.1 y anexo I. No son fechas para todas las obligaciones. Las prohibiciones, transparencia, modelos de propósito general y reglas transitorias tienen calendarios propios. [AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) y [Reglamento modificatorio](https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng).

**Sanciones.** Art. 99: para determinadas prohibiciones, hasta EUR 35 millones o 7 %; para ciertos incumplimientos enumerados, EUR 15 millones o 3 %; por determinada información incorrecta, incompleta o engañosa a autoridades u organismos notificados, EUR 7,5 millones o 1 %. Para empresas rige el mayor importe en esos tramos con la regla especial del art. 99.6 para pymes y empresas emergentes, que aplica el menor de los máximos. La base porcentual es el volumen mundial anual del ejercicio anterior. Los proveedores de modelos de propósito general tienen un régimen separado en el art. 101. No se atribuye automáticamente la sanción al programador individual.

# [7 Estados Unidos](https://)

La evaluación parte de una combinación de normas federales por sector o actividad, reglas de la FTC y leyes estatales. No se traslada mecánicamente el modelo del RGPD. Una misma app puede estar sujeta a varios regímenes: por ejemplo, dirigirse a niños, operar en California y gestionar información de salud bajo un contrato.

| Marco seleccionado                    | Cuándo mirarlo                                                                                                       | Qué cambia en el diseño                                                                                                                                                              |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| FTC Act, sección 5                    | Prácticas desleales o engañosas dentro de su ámbito.                                                                 | Lo que el aviso promete debe coincidir con lo que la app, los SDK y el proveedor hacen. No hay una multa universal por cualquier incidente. FTC.                                     |
| COPPA                                 | Servicios en línea dirigidos a menores de 13 años o con conocimiento efectivo de recolección en supuestos cubiertos. | Aviso, consentimiento parental verificable cuando proceda, límites de recolección, seguridad y conservación; revisar la regla actualizada. FTC y COPPA.                              |
| HIPAA                                 | Entidades cubiertas y socios comerciales, con información de salud protegida en el ámbito correspondiente.           | Contratos y salvaguardas; una app de salud no cae automáticamente bajo HIPAA. Revisar otras reglas si queda fuera. HHS.                                                              |
| GLBA y otras reglas sectoriales       | Instituciones financieras cubiertas, informes de crédito u otros sectores regulados.                                 | Aplicabilidad específica; no asumir que la política general satisface las obligaciones del sector. FTC Safeguards Rule.                                                              |
| California — CCPA con reformas CPRA   | Empresas y tratamientos dentro de umbrales, definiciones y excepciones.                                              | Avisos, derechos de conocer, eliminar y corregir, mecanismos de exclusión de venta o compartición y limitación de ciertos usos sensibles donde proceda. Derechos CCPA y reglas CPPA. |
| Texas — HB 149 sobre gobernanza de IA | Ejemplo estatal de reglas de IA aplicables según actor, uso y disposiciones específicas.                             | Clasificar el caso y verificar prácticas prohibidas, excepciones y remedios propios del estado. Texto legislativo.                                                                   |

**California.** La CPPA publica importes ajustados efectivos desde el 1 de enero de 2025: hasta USD 2.663 por infracción y USD 7.988 por infracción intencional o los supuestos de conocimiento efectivo de menores de 16 años. Los daños legales de USD 107–799 por consumidor e incidente, o daños reales si son mayores, corresponden a acciones privadas limitadas bajo § 1798.150, no a cualquier infracción del CCPA. El paquete reglamentario vigente desde el 1 de enero de 2026 introduce requisitos para determinadas empresas, entre ellos evaluaciones, auditorías de ciberseguridad y derechos sobre ciertas tecnologías de decisión automatizada, con calendarios de cumplimiento propios. [Importes oficiales CPPA](https://www.cppa.ca.gov/announcements/2024/20241217.html) y [reglamentación](https://cppa.ca.gov/regulations/ccpa_updates.html).

**Texas.** La sección 552.105 del texto de HB 149 prevé, cuando procede y considerando su régimen de subsanación y excepciones, USD 10.000–12.000 en ciertas infracciones subsanables o incumplimientos de una declaración, USD 80.000–200.000 en las insubsanables y USD 2.000–40.000 por día de infracción continuada. Es un ejemplo de ley estatal de IA; no es la multa federal de privacidad. [HB 149, secciones 552.104–106](https://capitol.texas.gov/tlodocs/89R/billtext/html/HB00149F.htm).

## Regla de lectura comparada

Identificar primero **hecho, norma, sujeto obligado, autoridad, tipo de infracción, unidad, base y fecha**. Después revisar agravantes, posibilidad de subsanación, medidas correctivas, acciones privadas y procedimiento. Una tabla de máximos sirve para priorizar riesgos; no permite calcular una sanción definitiva ni sumar automáticamente topes.

# [8 Derechos y obligaciones del programador](https://)

El cargo «programador» no determina por sí solo la responsabilidad jurídica. Un empleado que trata datos bajo instrucciones de su organización no se convierte automáticamente en responsable o encargado independiente. Un contratista con acceso a registros y que opera por cuenta del cliente puede actuar como encargado; si decide reutilizar los datos para fines propios, debe analizarse si asume un rol distinto para ese uso. Que el contrato lo llame «proveedor técnico» no resuelve la clasificación.

| Situación                              | Qué corresponde definir                                                                            | Evidencia del programador                                             |
| -------------------------------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Empleado que desarrolla                | Instrucciones, acceso necesario, confidencialidad y canal de incidentes.                           | Permiso aprobado, tickets y código revisado.                          |
| Proveedor que opera datos del cliente  | Rol por operación, contrato, subencargos, incidentes, acceso y devolución o eliminación al cierre. | Anexo contractual, registros de acceso y acta de salida.              |
| Producto propio que decide finalidades | Identificar el responsable, sus obligaciones y recursos para cumplirlas.                           | Decisión de finalidad, aviso, evaluación y canal de derechos.         |
| Integración con proveedor de IA        | Quién recibe qué, para qué lo usa y en qué jurisdicción; verificar condiciones reales.             | Contrato, configuración, trazas y matriz de terceros.                 |
| Auditor externo                        | Alcance, independencia, autorización, mínima exposición y conservación de evidencia.               | Mandato, muestra justificada, evidencias protegidas y plan de cierre. |

Como titular, el programador conserva los derechos sobre sus propios datos conforme a la ley aplicable, también en el entorno laboral cuando corresponda. Como profesional, debe contar con instrucciones, recursos, acceso acotado y un canal de escalamiento para desempeñar su función. Estas son condiciones de trabajo recomendables; no equivalen a un derecho legal universal a vetar un lanzamiento. La propiedad del código, confidencialidad, licencias y responsabilidades contractuales se revisan por separado.

El programador debe usar solo accesos autorizados; no copiar datos reales a equipos o chats personales; proteger secretos; revisar el código generado por IA; documentar cambios; probar restricciones; y reportar incidentes por el canal designado. No improvisa una base legal, no promete plazos que el equipo no puede cumplir y no decide por su cuenta revelar, conservar indefinidamente o destruir datos ajenos. El responsable toma las decisiones jurídicas con apoyo de privacidad y asesoría; seguridad coordina contención; ingeniería ejecuta y demuestra los controles.

**Ejemplo de escalamiento.** El equipo detecta que una librería envía textos completos a un proveedor. El programador conserva evidencia mínima, desactiva o restringe la función según el plan autorizado y reporta alcance y hora. No pega los textos en un chat para depurar. El responsable decide la comunicación y notificación aplicables con el equipo designado. Las responsabilidades administrativas, civiles, laborales o penales dependen de la conducta y las normas concretas; no se presume que toda infracción del producto sea una multa personal al desarrollador.

# [9 Lista de control antes de escribir código](https://)

Usar la tabla como acta de arranque. Cada fila debe tener **estado** (cumple, parcial, no cumple o no aplica justificado), responsable nominal, fecha, evidencia y próxima revisión. La columna de responsables propone funciones, no reemplaza el reparto real del equipo.

| ID y control            | Qué debe quedar decidido                                                                         | Evidencia y función que valida                                             |
| ----------------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| D01 · Necesidad         | Qué problema se resuelve y qué opción requiere menos datos o evita IA.                           | Resumen de alcance y alternativas; producto.                               |
| D02 · Aplicabilidad     | Países, sector, categorías de usuarios, menores, datos sensibles, normas y contratos.            | Matriz con fuentes y fecha; privacidad o jurídico.                         |
| D03 · Roles             | Responsable y encargados por flujo; dueño de datos y de IA; delegado si aplica.                  | Matriz de responsables y contactos; dirección.                             |
| D04 · Inventario        | Campos, origen, entradas, salidas, sistemas y derivados, incluso SDK, logs, IA y copias.         | Catálogo inicial y diagrama; arquitectura.                                 |
| D05 · Finalidad y base  | Justificación separada para servicio, soporte, analítica, marketing y entrenamiento.             | Registro de finalidades y base; responsable del tratamiento.               |
| D06 · Minimización      | Qué dato puede eliminarse, hacerse opcional o sustituirse por un ejemplo sintético.              | Diccionario con motivo por campo; producto y privacidad.                   |
| D07 · Riesgo e impacto  | Evaluar necesidad, proporcionalidad, escenarios y si corresponde EIPD.                           | Análisis fechado, medidas y decisión; privacidad y seguridad.              |
| D08 · Diseño de acceso  | Aislamiento entre clientes, roles, acceso a soporte, privilegios de emergencia y secretos.       | Diagrama, matriz y pruebas previstas; seguridad.                           |
| D09 · Proveedores       | Uso propio, regiones, soporte remoto, subencargos, incidentes y eliminación.                     | Contrato, configuración y evaluación; compras y privacidad.                |
| D10 · Retención         | Evento inicial, plazo por categoría, excepción, eliminación y tratamiento de copias.             | Tabla de retención y prueba de restauración prevista; dueño y operaciones. |
| D11 · Derechos          | Canal, identidad proporcional, plazos, responsables y alcance de exportación o borrado.          | Flujo y criterios de aceptación; privacidad y soporte.                     |
| D12 · Transparencia     | Avisos por punto de recogida, preferencias y canal de derechos.                                  | Borrador enlazado a inventario; producto y jurídico.                       |
| D13 · Incidentes        | Guardias, contención, evidencia, evaluación y comunicaciones.                                    | Procedimiento y ejercicio de mesa previsto; seguridad.                     |
| D14 · Si hay IA         | Uso previsto y excluido, clasificación regulatoria, proveedor, flujos, supervisión y pausa.      | Ficha, decisión de alcance y dueño; producto y riesgo.                     |
| D15 · Validación de IA  | Umbrales por caso, prueba independiente de ajuste, privacidad, abuso, errores y revisión humana. | Conjunto de casos, métricas y criterio de lanzamiento; QA.                 |
| D16 · IA para programar | Herramientas aprobadas, límites de datos y revisión de código, licencias y dependencias.         | Política del equipo, revisión y configuración; ingeniería.                 |
| D17 · Cierre            | Cómo se entrega, devuelve, migra o elimina la información; dependencia del proveedor.            | Plan de salida, respaldo y verificación; operaciones.                      |

## Registro mínimo para copiar al proyecto

| Campo                            | Ejemplo ficticio                                                                            |
| -------------------------------- | ------------------------------------------------------------------------------------------- |
| Identificador, finalidad y dueño | F-01 · gestionar matrícula · coordinación académica.                                        |
| Titulares, datos y origen        | Alumnos; correo y número de matrícula; formulario de inscripción.                           |
| Justificación y alcance          | Base aprobada para matrícula; excluir reutilización para marketing o entrenamiento.         |
| Sistemas y destinatarios         | Aplicación y respaldo; soporte autorizado; listar proveedores y regiones reales.            |
| Acceso y conservación            | Roles autorizados; plazo por finalidad y excepción motivada.                                |
| Controles y evidencia            | Prueba de acceso negativo, canal de derechos, job de eliminación, registro de restauración. |
| Riesgo y versión                 | Riesgo residual, responsable de aceptación, fecha, enlace a evaluación y revisión.          |

**Fila de seguimiento:** ID \_\_\_\_ · Estado \_\_\_\_ · Responsable \_\_\_\_ · Evidencia \_\_\_\_ · Fecha límite \_\_\_\_ · Próxima revisión \_\_\_\_.

Antes de usar datos reales, el equipo debe poder responder qué se recoge, qué sale del entorno, quién puede verlo y cómo se deja de usar. Si una decisión legal no está resuelta, se trabaja con material ficticio y no se activa ese tratamiento en producción.

# [10 Qué páginas y canales debe ofrecer la aplicación](https://)

No todos los marcos exigen las mismas URLs ni un botón con un nombre único. El sistema debe proporcionar información y mecanismos accesibles según su alcance. Se recomienda separar tres elementos: **aviso público**, **canal para ejercer derechos** y **procedimiento interno que ejecuta las decisiones**. Para Ecuador, el art. 12 de la LOPDP determina la información exigida; RGPD arts. 12–14 y reglas estatales o sectoriales aplicables tienen requisitos propios.

## Página pública de privacidad

| Bloque                         | Qué informa y cómo se comprueba                                                                                                                        |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Identidad                      | Quién es responsable, domicilio y canales de contacto; contacto del delegado cuando corresponda. Coincide con contratos y pantallas.                   |
| Datos y origen                 | Categorías, fuentes directas o indirectas, existencia de registros y tipos de tratamiento según el marco. Coincide con inventario y tráfico observado. |
| Finalidad y base               | Motivo por uso, fundamento aplicable y finalidades adicionales. No usar una fórmula genérica para justificar cualquier uso.                            |
| Entrega y elecciones           | Datos necesarios u opcionales, consecuencias de no facilitarlos o de entregarlos incorrectos; revocación cuando proceda.                               |
| Destinatarios y transferencias | Categorías, fines, destinos y garantías exigibles; proveedores y accesos remotos reales.                                                               |
| Conservación                   | Duraciones o criterios admisibles, según la ley, y diferencias por finalidad. No anunciar borrado instantáneo si no puede cumplirse.                   |
| Derechos y reclamos            | Qué derechos existen, cómo ejercerlos y dónde presentar reclamos ante el responsable o autoridad; portabilidad y preferencias cuando aplican.          |
| Automatización e IA            | Usos relevantes, información exigida sobre decisiones automatizadas, impacto y mecanismos de revisión o impugnación aplicables.                        |
| Vigencia                       | Fecha y versión; avisos específicos donde se recoge información; texto comprensible en móvil y con lector de pantalla.                                 |

En Ecuador, los detalles del art. 12 incluyen, según corresponda, forma de ejercer los derechos, consecuencias de la entrega o negativa, efecto de datos inexactos, revocación, reclamos y decisiones automatizadas. Al obtener datos de otra fuente o de una fuente accesible al público, la ley prevé informar dentro de 30 días o en la primera comunicación, lo que ocurra primero, en los términos aplicables. El aviso completo debe ajustarse al texto vigente, no solo a la tabla resumida. [LOPDP art. 12](https://spdp.gob.ec/wp-content/uploads/2024/12/03.pdf.pdf).

Si hay cookies o SDK, la información pública debe corresponder con su comportamiento y con las opciones efectivas. Según jurisdicción, pueden requerirse consentimiento previo o mecanismos de exclusión para determinados usos. Un banner no resuelve el problema si el SDK transmite antes de que la elección se aplique.

## Canal de derechos y eliminación

Una ruta como /privacidad/derechos, un centro de cuenta o un canal accesible equivalente debe explicar qué solicitudes recibe, quién puede presentarlas y qué pasos seguir. Puede incluir «Solicitar eliminación» en cuenta y alternativa accesible para quien no pueda iniciar sesión. Un formulario no debe pedir documentos de identidad excesivos por defecto ni permitir averiguar si un tercero tiene cuenta.

| Momento     | Qué ve la persona                                                  | Qué hace el sistema                                                    |
| ----------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| Solicitar   | Alcance, confirmación clara y alternativa de contacto.             | Registra fecha, tipo y referencia sin exponer datos.                   |
| Verificar   | Petición proporcional de prueba de identidad o representación.     | Reutiliza autenticación cuando sea suficiente; protege el expediente.  |
| Evaluar     | Información comprensible sobre excepciones o alcance.              | Determina qué procede por finalidad, sistema, contrato y conservación. |
| Resolver    | Confirmación total, parcial o negativa motivada según corresponda. | Ejecuta, verifica y registra evidencia; no cierra al encolar.          |
| Seguimiento | Canal de revisión o reclamo aplicable.                             | Registra atrasos, fallas y comunicación.                               |

**Texto ilustrativo para la pantalla de eliminación:** «Puedes solicitar la eliminación de los datos que nos corresponda suprimir. Verificaremos tu identidad y el alcance de la solicitud. Si debemos conservar información por una obligación aplicable, te informaremos qué queda limitado y por qué, cuando corresponda. Recibirás una referencia para consultar el estado». No utilizar el ejemplo sin adaptarlo al servicio y sus obligaciones.

# [11 Eliminación comprobable y retiro de bases de datos](https://)

Eliminar la cuenta, suprimir datos de una persona y retirar una base completa son operaciones diferentes. Desactivar el inicio de sesión no elimina los registros. Marcar una fila como borrada de forma lógica limita su visibilidad, pero puede dejarla recuperable. La eliminación debe comprobarse de acuerdo con el fin, la base legal y la técnica aplicable, sin destruir datos de otras personas o evidencia bajo conservación válida.

## Flujo para una solicitud individual

**Recibir → verificar → decidir alcance → bloquear usos incompatibles → ejecutar por sistemas → verificar → informar → conservar evidencia mínima.**

1\. Crear expediente y fecha límite; registrar identidad comprobada sin duplicar documentos de identidad innecesarios.

2\. Identificar por claves fiables y acotadas al cliente; evitar búsquedas que confundan homónimos o ámbitos de acceso.

3\. Clasificar sistemas activos, copias, terceros y derivados. Determinar qué procede suprimir, devolver, anonimizar de forma eficaz o conservar por base válida.

4\. Ejecutar con permisos acotados y control por ámbito; registrar estados de cada sistema, reintentos y excepciones. El proceso debe ser idempotente: repetirlo no debe borrar datos de otra persona ni generar un nuevo efecto.

5\. Solicitar actuación de encargados y destinatarios cuando proceda; validar su confirmación. Comprobar el resultado tanto con consulta privilegiada como desde interfaces normales.

6\. Comunicar lo realmente completado y lo que subsiste bajo excepción. Conservar solo evidencia mínima protegida, por un plazo definido.

En Ecuador, el art. 15 prevé eliminación procedente en 15 días y sin costo, junto con las excepciones legales aplicables. La Resolución 2025-0030-R desarrolla seudonimización, anonimización, bloqueo y eliminación. Su art. 23 regula comunicación a encargados o terceros y contempla un término de tres días para su ejecución en los supuestos de la norma; el art. 24 regula devolución o eliminación tras el fin de la relación y evidencia, con término de cinco días. No confundir estos supuestos con el plazo general frente al titular. [LOPDP](https://spdp.gob.ec/wp-content/uploads/2024/12/03.pdf.pdf) y [Resolución SPDP-SPD-2025-0030-R](https://www.spdp.gob.ec/wp-content/uploads/2025/12/0030-R_compressed.pdf).

## Dónde puede quedar una copia

| Superficie                       | Riesgo de borrado incompleto                                                        | Prueba o control                                                                                             |
| -------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Base principal y réplicas        | Hijos, tablas históricas, vistas o réplicas desfasadas.                             | Identidad acotada, cascadas revisadas, consulta postborrado y convergencia.                                  |
| Archivos y objetos               | Versiones, exportaciones, adjuntos y papeleras.                                     | Enumerar versiones y políticas de expiración; comprobar acceso.                                              |
| Índice de búsqueda o RAG         | Fragmentos, embeddings, metadatos y resultados en caché.                            | Eliminar por linaje, reindexar donde proceda y hacer búsqueda negativa.                                      |
| Logs y telemetría                | Prompts, correo, tokens, trazas o campos de diagnóstico.                            | Minimizar, limitar acceso y aplicar política compatible con obligaciones.                                    |
| Analítica y desarrollo           | Copias históricas, notebooks, ambientes de prueba y reportes.                       | Inventario de destinos, supresión o anonimización verificada.                                                |
| Proveedores                      | Retención propia, subencargados, exportaciones y soporte.                           | Solicitud trazable, confirmación contractual y prueba posible.                                               |
| Respaldos y snapshots            | Una restauración puede reintroducir datos suprimidos.                               | Aislamiento, expiración autorizada y reaplicación de decisiones antes de reactivar.                          |
| Datos de entrenamiento y modelos | Quitar un registro del dataset no demuestra que deje de influir en pesos o salidas. | Registrar uso y versiones; evaluar proveedor, memorias, mitigación, reentrenamiento o retiro cuando proceda. |

La retención de backups no es una excepción automática al derecho de eliminación. Si hay una limitación técnica o una conservación obligatoria, se justifica jurídicamente y se implementan restricciones, expiración y controles de restauración. Un registro mínimo de supresiones puede evitar la reaparición si se protege, limita y justifica; no debe convertirse en otra copia del perfil. Los controles se prueban en restauración aislada antes de reconectar sistemas.

## Retiro de una base completa

| Paso        | Evidencia de cierre                                                                                    |
| ----------- | ------------------------------------------------------------------------------------------------------ |
| Delimitar   | Base, región, clientes, dependencias, réplicas, snapshots y terceros enumerados.                       |
| Autorizar   | Dueño, operaciones y privacidad validan alcance, conservación obligatoria y reversión permitida.       |
| Desconectar | Se detienen escrituras, integraciones y sincronizaciones; se retiran credenciales y accesos.           |
| Ejecutar    | Eliminar instancias, copias y versiones dentro del alcance; documentar excepciones y método elegido.   |
| Verificar   | Consultas negativas, inventario de infraestructura, comprobación de backups y constancia de proveedor. |
| Cerrar      | Acta con método, alcance, fechas, operador, verificador y excepciones con vencimiento.                 |

Un comando DROP no garantiza sanitización del soporte físico. Para retiro o reutilización de medios, elegir un método adecuado y verificable según el medio, el riesgo y el proveedor. La eliminación criptográfica depende de cómo se gestionaron el cifrado, las claves y sus copias; no equivale a revocar un usuario. [NIST SP 800-88 Rev. 2](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-88r2.pdf).

**Criterio de cierre:** el usuario no puede acceder; la consulta autorizada confirma el resultado; no reaparece tras restauración; los terceros confirman lo que les corresponde; las excepciones tienen base, acceso limitado, vencimiento y revisión. Si un sistema no pudo verificarse, el expediente no se presenta como completado sin explicar esa limitación.

# [12 Lista de auditoría en construcción y producción](https://)

Primero fijar objetivo, criterios, período, sistemas, versiones y alcance autorizado. Una auditoría distingue **diseño** —el control está bien pensado—, **implementación** —existe y está configurado— y **eficacia operativa** —funcionó durante el período—. En construcción puede no existir historial: documentarlo y revisar diseño y pruebas, sin certificar eficacia operativa todavía.

| ID y área                  | En construcción                                                                                    | En producción y evidencia esperada                                                                                                        |
| -------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| A01 · Aplicabilidad        | Revisar países, sector, contratos, roles y análisis de impacto.                                    | Verificar cambios de mercados, proveedores o usos; matriz fechada y aprobaciones.                                                         |
| A02 · Inventario y linaje  | Comparar diagrama, esquema, eventos y dependencias.                                                | Muestrear tráfico y catálogos; rastrear un registro a réplicas, analítica e IA.                                                           |
| A03 · Transparencia        | Comparar aviso, formularios y finalidad declarada.                                                 | Verificar versión visible, consentimientos cuando aplican, revocación y comportamiento de SDK.                                            |
| A04 · Acceso y segregación | Revisar roles y autorización en servidor.                                                          | Prueba negativa con dos cuentas autorizadas de distintos ámbitos; revisar privilegios y accesos de soporte.                               |
| A05 · Seguridad            | Revisar secretos, cifrado, dependencias, despliegue y entornos.                                    | Muestrear rotación, alertas, cambios de roles y corrección de vulnerabilidades. Usar OWASP ASVS como criterio técnico cuando corresponda. |
| A06 · Datos no productivos | Exigir datos ficticios o tratamiento autorizado y minimizado.                                      | Revisar que pruebas, tickets y chats no contengan copias indebidas.                                                                       |
| A07 · Proveedores          | Evaluar contrato, subencargos, región, incidentes y salida.                                        | Contrastarlos con configuración, tráfico, renovaciones y confirmaciones.                                                                  |
| A08 · Derechos             | Probar identidad, plazos, exportación, borrado y negativas motivadas.                              | Muestrear casos completos, tardíos, parciales y rechazados; no solo los exitosos.                                                         |
| A09 · Retención y backups  | Probar vencimiento, bloqueo y reintentos; diseñar restauración aislada.                            | Verificar jobs, excepciones, copias vencidas y ausencia de reaparición tras restaurar.                                                    |
| A10 · Incidentes           | Revisar contactos, cómputo de plazos y simulación autorizada.                                      | Contrastar casos reales con bitácora, contención, decisiones y notificaciones.                                                            |
| A11 · IA y alcance         | Inventariar modelos, versiones, herramientas y usos excluidos.                                     | Comparar inventario con configuración efectiva; rastrear cambios del proveedor y aprobaciones.                                            |
| A12 · Calidad de IA        | Evaluar aciertos, errores relevantes, incertidumbre, abuso y diferencias por grupo cuando proceda. | Comparar versiones, quejas, deriva y revisión humana con umbrales y datos pertinentes.                                                    |
| A13 · RAG y permisos       | Probar filtrado antes del contexto y referencias que respaldan.                                    | Muestrear consultas, verificar que una fuente retirada no reaparece y probar inyección indirecta sin datos reales.                        |
| A14 · Acciones de IA       | Limitar herramientas y exigir validaciones en servidor para acciones sensibles.                    | Revisar trazas, permisos de servicio y evidencia de bloqueos.                                                                             |
| A15 · Cambio y reversión   | Definir quién aprueba despliegue, reversión y retirada.                                            | Verificar que la versión desplegada es la evaluada y que la pausa funciona.                                                               |
| A16 · Evidencia y cierre   | Definir registros mínimos, accesos y conservación.                                                 | Confirmar integridad, fechas, muestras y revalidación; eliminar copias de auditoría según política.                                       |

## Cómo muestrear y formular hallazgos

·         Seleccionar muestras por riesgo y justificar población, período, método y limitaciones. Incluir incidentes, fallas y excepciones; no escoger solo casos convenientes.

·         Triangular tres fuentes cuando sea viable: documentación, configuración y comportamiento observado. Una captura de un botón no prueba que el backend eliminó datos.

·         Reproducir fallas con cuentas y datos autorizados. En producción, no ejecutar pruebas destructivas; usar entornos controlados, evidencia histórica o pruebas acordadas.

·         Minimizar datos en el informe. Registrar versión, hora, sistema y referencia al artefacto protegido; no adjuntar credenciales, volcados o expedientes completos.

·         Documentar criterio, condición encontrada, causa, impacto, severidad razonada, dueño, acción, fecha objetivo y prueba de cierre. «No aplica» requiere explicación.

| Campo                 | Ejemplo de hallazgo                                                                                       |
| --------------------- | --------------------------------------------------------------------------------------------------------- |
| Criterio              | Tras una supresión aprobada, la fuente y sus fragmentos no deben recuperarse en el RAG.                   |
| Condición y evidencia | Se borró el archivo, pero una búsqueda autorizada devolvió su fragmento; registrar versión e ID ficticio. |
| Causa probable        | El evento de eliminación no se propaga al índice y a la caché.                                            |
| Riesgo                | Persistencia de información eliminada y posible exposición.                                               |
| Acción y responsable  | Implementar evento verificable y limpieza del índice; equipo de plataforma.                               |
| Revalidación          | Buscar por ID y texto tras borrado y tras restauración aislada; comprobar registros de ejecución.         |

Una clasificación útil diferencia **crítico** —exposición o decisión de alto impacto sin control efectivo—, **alto** —fallo material con riesgo relevante—, **medio** —control parcial o evidencia insuficiente— y **bajo** —mejora acotada—. Ajustar al contexto, probabilidad, impacto y alcance; la etiqueta no sustituye el razonamiento. No cerrar hallazgos solo porque se abrió un ticket.

# [13 Puertas de decisión y caso integrador](https://)

| Momento             | Evidencia exigida para avanzar                                                                                 | Ejemplo de motivo para detenerse                                                            |
| ------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Idea a diseño       | Finalidad, alcance, roles, inventario, alternativas y análisis de aplicabilidad.                               | Nadie puede explicar para qué se necesita un dato sensible.                                 |
| Diseño a piloto     | Riesgos evaluados, fuentes aprobadas, pruebas con datos ficticios y contrato si hay proveedor.                 | Los prompts se envían a un servicio sin reglas de acceso o retención verificadas.           |
| Piloto a producción | Controles probados, aviso real, derechos operativos, supresión y restauración verificadas, plan de incidentes. | Una cuenta puede leer documentos de otra o no existe forma de cumplir un derecho aplicable. |
| Cambio importante   | Nueva versión, evaluación de cambio, revalidación, decisión de aprobar o revertir.                             | Cambio de proveedor que introduce entrenamiento con datos del cliente sin evaluación.       |
| Retiro              | Datos, accesos, dependencias y copias gestionados; excepciones registradas.                                    | No existe evidencia de retorno o eliminación por un proveedor.                              |

## Demostración docente con el asistente de la academia

1\. **Definir antes de programar.** Mostrar el diagrama y la decisión escrita: el asistente consulta solo manuales públicos aprobados; las actas y notas quedan fuera.

2\. **Mostrar cómo se cumple.** Abrir una consulta válida con referencia. Intentar recuperar una fuente privada desde dos perfiles autorizados de prueba. Verificar que no llegue al contexto ni a los resultados.

3\. **Mostrar un fallo útil.** Sustituir un manual por una versión vigente. Comprobar si el índice y la caché todavía recuperan la anterior. Distinguir problema de vigencia, recuperación y respuesta.

4\. **Mostrar eliminación.** En un entorno ficticio, registrar una solicitud procedente y demostrar qué se retira de la base, del índice y de copias operativas. Verificar una restauración aislada.

5\. **Documentar la decisión.** Comparar lo esperado con lo observado y explicar quién acepta el riesgo residual, quién corrige y cuándo se vuelve a probar.