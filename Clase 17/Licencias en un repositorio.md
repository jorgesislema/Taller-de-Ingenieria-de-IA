Licencias en un repositorio: qué permiten, cuándo elegirlas y qué precauciones tomar

**Taller de Ingeniería de IA · Docente: Jorge Sislema**  
  

**Idea central:** antes de copiar, modificar, vender o publicar un proyecto, debemos saber quién tiene los derechos, qué licencia se aplica y qué obligaciones activa nuestro uso.

Esta guía es educativa. En un contrato, una distribución comercial o una combinación de licencias con consecuencias relevantes, revisa los textos aplicables y solicita una revisión jurídica del caso concreto. Las explicaciones no sustituyen las condiciones completas de cada licencia.

**1\. Objetivos y preparación**

Al terminar la clase, cada participante podrá:

1.  Explicar la diferencia entre un repositorio público, una licencia y la titularidad de los derechos.
2.  Distinguir licencias permisivas, copyleft, Creative Commons y condiciones propietarias.
3.  Comparar MIT, Apache-2.0, BSD, MPL, LGPL, GPL y AGPL con ejemplos.
4.  Elegir una licencia preliminar según el contenido y el objetivo del proyecto.
5.  Reconocer obligaciones de atribución, conservación de avisos y entrega de código fuente.
6.  Documentar una elección de licencia sin atribuirse derechos sobre material ajeno.

**2\. ApSi está en GitHub, ¿puedo usarlo?**

**Caso inicial**

Encontramos en GitHub un programa de reservas. El repositorio es público y funciona bien. Un cliente nos pide adaptarlo y venderle una copia. No encontramos un archivo LICENSE.

¿podemos copiarlo, cambiar el nombre y entregarlo al cliente?

Que una fotografía esté expuesta en una vitrina permite verla. Eso no significa que podamos imprimirla y venderla. De forma parecida, poder leer un repositorio no equivale a recibir todos los permisos de reutilización.

Una **licencia** es una autorización con condiciones. Explica qué permite el titular de derechos y qué debe cumplir quien utiliza la obra. No transfiere automáticamente la propiedad intelectual.

En ausencia de licencia, se aplican las reglas de derechos de autor por defecto, con las excepciones legales que correspondan. No debemos asumir autorización general para redistribuir o crear derivados. En GitHub existen además permisos limitados de visualización y bifurcación dentro de sus términos; eso no convierte el contenido en software de libre reutilización. \[F1\]

**Respuesta al caso:** no hay base para tratarlo como código de libre reutilización. Debemos obtener una licencia o permiso suficiente, o elegir una alternativa que sí los tenga.

**Tres mensajes que deben quedar claros**

-   **Público** describe quién puede acceder.
-   **Licencia** describe qué usos se autorizan y bajo qué condiciones.
-   **Titularidad** describe quién puede conceder esos permisos.

Publicar código de una empresa o de un cliente con una licencia que elegimos nosotros no resuelve la falta de autorización del titular.

**3\. Vocabulario y mapa de familias** <u>**.**</u>

**3.1 Palabras que necesitamos comprender**

| Término              | Explicación sencilla                                                                 | Ejemplo                                                             |
| -------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| Autor                | Persona que crea una obra                                                            | Quien escribe una función o un capítulo                             |
| Titular de derechos  | Persona o entidad que posee los derechos pertinentes                                 | Puede ser el autor, una empresa u otra entidad según acuerdos y ley |
| Uso                  | Emplear el programa o material                                                       | Ejecutar una herramienta                                            |
| Modificación         | Cambiar o adaptar material protegido                                                 | Añadir funciones a un programa                                      |
| Distribución         | Entregar copias a otras personas                                                     | Publicar un instalador o entregar código a un cliente               |
| Código fuente        | Forma preferida para modificar un programa                                           | Archivos de desarrollo y elementos necesarios según la licencia     |
| Binario o ejecutable | Forma preparada para ejecutarse                                                      | Un instalador o una aplicación compilada                            |
| Atribución           | Reconocer la autoría o procedencia conforme a las condiciones                        | Conservar un aviso y enlazar una licencia                           |
| Copyleft             | Condiciones para mantener determinadas libertades en obras cubiertas al compartirlas | Distribuir una versión modificada bajo la licencia exigida          |
| Dependencia          | Componente que utiliza el proyecto                                                   | Una biblioteca instalada con Python o Node                          |
| SaaS                 | Programa ofrecido como servicio a través de una red                                  | Una plataforma que el cliente utiliza desde su navegador            |
| Licencia compatible  | Condiciones que pueden cumplirse conjuntamente en un uso concreto                    | No basta con que ambas licencias sean abiertas                      |

**3.2 Familias principales**

flowchart TD

    A\["Contenido del repositorio"\] --> B\["Código"\]

    A --> C\["Textos e imágenes"\]

    A --> D\["Datos y modelos"\]

    B --> E\["Permisivas: MIT, Apache, BSD"\]

    B --> F\["Copyleft: MPL, LGPL, GPL, AGPL"\]

    B --> G\["Condiciones propietarias o de código visible"\]

    C --> H\["Creative Commons u otros permisos"\]

    D --> I\["Revisión específica de derechos y condiciones"\]

**Si tu visor no representa Mermaid:** la idea es que la licencia se elige según el contenido. El código suele usar licencias de software; los textos e imágenes pueden usar Creative Commons; los datos y modelos necesitan una revisión específica.

**3.3 Software libre no significa software sin precio**

Las licencias de código abierto permiten uso comercial. Es posible cobrar por copias, alojamiento, adaptación, formación o soporte, cumpliendo las condiciones. Una prohibición de uso comercial o una exclusión de determinados sectores no cumple la definición de código abierto de la Open Source Initiative. \[F2\]

**Ejemplo:** una empresa puede cobrar por instalar y mantener un programa GPL. Debe respetar las libertades y obligaciones de esa licencia al entregar el programa. El cliente también puede recibir derechos de redistribución; pagar no elimina esos derechos.

**Pregunta de comprobación:** «Quiero que cualquiera pueda estudiar mi código, pero nadie pueda vender productos con él. ¿Estoy eligiendo una licencia de código abierto?» Respuesta: no, esa restricción comercial cambia la categoría.

**4\. Licencias de software: lista y comparación ·**

No existe una lista breve que abarque todas las licencias. Las siguientes cubren las principales decisiones de un repositorio educativo o profesional. Siempre importa la **versión exacta**, las excepciones y los avisos del componente.

**4.1 Tabla de consulta**

| Licencia o situación             | Para qué se usa                                                                | Cuándo considerarla                                                                                     | Obligación o precaución principal                                                                        |
| -------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| MIT                              | Compartir código con pocas condiciones                                         | Ejemplos, bibliotecas y herramientas con reutilización amplia                                           | Conservar el aviso de copyright y el permiso en copias o partes sustanciales; permite derivados cerrados |
| Apache-2.0                       | Reutilización amplia con concesión expresa de ciertas patentes                 | Bibliotecas y proyectos que valoran ese tratamiento de patentes                                         | Conservar licencia y avisos, identificar archivos modificados y atender NOTICE cuando corresponda        |
| BSD-2-Clause                     | Reutilización permisiva en fuente y binario                                    | Proyectos que prefieren la estructura BSD                                                               | Conservar avisos, condiciones y descargo en las formas exigidas                                          |
| BSD-3-Clause                     | Lo anterior, con una condición de no respaldo                                  | Cuando no quieres que usen nombres de titulares o contribuidores para promocionar derivados sin permiso | La cláusula no impide mencionar correctamente la procedencia                                             |
| ISC                              | Licencia permisiva breve                                                       | Herramientas y bibliotecas que buscan condiciones sencillas                                             | Conservar avisos exigidos; no confundir brevedad con ausencia de obligaciones                            |
| MPL-2.0                          | Copyleft normalmente limitado a archivos cubiertos                             | Compartir mejoras de esos archivos y permitir un producto mayor con otras licencias                     | Al distribuir, mantener disponibles los fuentes cubiertos y sus cambios según la licencia                |
| LGPL-3.0                         | Bibliotecas utilizables por aplicaciones bajo otras condiciones                | Querer apertura de la biblioteca con integración en aplicaciones diversas                               | Cumplir avisos, fuente de la biblioteca y requisitos de sustitución o reenlazado que correspondan        |
| GPL-3.0                          | Copyleft fuerte para programas                                                 | Querer que los derivados distribuidos mantengan esas libertades                                         | Al distribuir obras cubiertas, cumplir licencia y entrega del código fuente correspondiente              |
| AGPL-3.0                         | Copyleft con condición adicional para versiones modificadas utilizadas por red | Querer que los usuarios remotos puedan obtener el fuente de la versión modificada que usan              | La sección 13 exige ofrecer ese fuente a quienes interactúan remotamente con ella                        |
| Boost Software License 1.0       | Reutilización permisiva de software                                            | Bibliotecas con condiciones sencillas, especialmente donde ya se usa esta licencia                      | Su tratamiento de avisos en distribuciones binarias difiere de MIT; leer el texto                        |
| Unlicense                        | Dedicación al dominio público acompañada de permisos amplios                   | Cuando se busca renunciar ampliamente a derechos de autor en la medida posible                          | Revisar efectos por jurisdicción; no garantiza derechos de patente o marca                               |
| CC0-1.0                          | Dedicación al dominio público con mecanismos subsidiarios                      | Principalmente ciertos datos o contenidos propios que se desean liberar ampliamente                     | No elimina derechos ajenos, privacidad, marcas ni derechos de patente                                    |
| Propietaria                      | Reservar usos y conceder permisos específicos                                  | Software de cliente o producto con condiciones comerciales propias                                      | Necesita términos claros y derechos suficientes; «privado» no redacta un contrato                        |
| Código visible con restricciones | Mostrar el fuente limitando usos                                               | Modelos de distribución que restringen servicios, producción u otros usos                               | No asumir que es código abierto; leer la licencia exacta y sus parámetros                                |
| Sin licencia                     | Ausencia de una autorización general explícita                                 | Puede ser una decisión de reserva, pero genera incertidumbre para colaboradores                         | No equivale a dominio público ni a permiso para copiar                                                   |

Referencias generales de comparación: \[F1\], \[F3\]. Para Apache, MPL, LGPL, GPL y AGPL, consultar además \[F4\]–\[F8\].

**4.2 MIT: «Puedes reutilizar, conserva estos avisos»**

**Caso didáctico:** publicamos una calculadora de presupuestos escrita por nosotros. Queremos que estudiantes y empresas la adapten, incluso dentro de productos cerrados.

MIT permite ese enfoque. Su condición central es conservar el aviso de copyright y el texto de permiso en las copias o partes sustanciales del software. No obliga en general a publicar los cambios ni a mantener abierto todo el producto derivado.

**Cuándo elegirla:** cuando buscas pocas barreras de reutilización y aceptas que alguien pueda incorporar el código en una solución propietaria.

**Precauciones:**

-   No significa «sin autor» o «sin condiciones».
-   No debes sustituir el aviso del autor original por el tuyo. Puedes añadir avisos de tus aportes cuando corresponda.
-   No contiene una concesión de patentes expresa comparable a la de Apache-2.0.
-   El descargo de garantía no autoriza cualquier conducta ni elimina automáticamente responsabilidades legales ajenas al alcance de la licencia.

**Pregunta:** «Si una empresa vende un programa basado en mi código MIT, ¿tiene que pagarme regalías por esa licencia?» No, MIT no impone ese pago. Debe cumplir sus condiciones y los demás derechos aplicables.

**4.3 Apache-2.0: permisos amplios y patentes expresas**

**Caso didáctico:** un equipo publica una biblioteca para procesar documentos y quiere facilitar su incorporación en productos de otras empresas, con reglas expresas sobre patentes de los contribuidores.

Apache-2.0 permite derivados con otras condiciones, pero exige cumplir sus reglas de redistribución. Entre ellas: entregar una copia de la licencia, conservar avisos pertinentes, indicar modificaciones en los archivos cambiados y reproducir los avisos de atribución aplicables de NOTICE cuando el proyecto distribuido lo incluya. No todos los proyectos necesitan inventar un NOTICE vacío. \[F4\]

**Cuándo elegirla:** cuando encaja una licencia permisiva y se valora una concesión expresa de las reivindicaciones de patente cubiertas por su texto.

**Precaución sobre patentes:** no es un seguro frente a cualquier patente del mundo. El alcance se limita a lo que concede cada contribuidor bajo la licencia; además, existen condiciones de terminación ante determinados litigios.

**Precaución sobre marcas:** usar el código no autoriza a presentar tu producto como oficial ni a usar libremente nombres o logotipos.

**4.4 BSD e ISC: alternativas permisivas**

BSD-2-Clause y BSD-3-Clause permiten reutilización amplia, incluidas modificaciones y distribución comercial. BSD-3-Clause añade que no se pueden utilizar los nombres del titular o de los contribuidores para respaldar o promocionar derivados sin permiso escrito previo. \[F9\]

**Ejemplo:** puedes indicar de forma correcta que utilizas un componente. No puedes afirmar que sus autores recomiendan tu producto si no lo hacen.

ISC tiene un texto breve de permisos y conservación de avisos. Estas opciones son útiles cuando el proyecto o su comunidad ya las emplean. No es necesario cambiar una licencia permisiva existente solo porque otra sea más conocida.

**4.5 MPL-2.0: compartir los archivos cubiertos**

**Caso didáctico:** distribuyes una aplicación con un archivo MPL que modificaste y otros archivos propios independientes. Normalmente puedes mantener otras licencias para esos archivos propios, mientras cumples las obligaciones sobre los archivos cubiertos por MPL. \[F5\]

**Cuándo elegirla:** cuando quieres que las mejoras de los archivos cubiertos permanezcan disponibles sin exigir por ese solo hecho la misma licencia a todo el producto mayor.

**Precaución:** «copyleft por archivo» es una explicación inicial, no permiso para trasladar código MPL a otro archivo y ocultarlo. Revisa cómo define la licencia las modificaciones y el software cubierto. El uso interno sin distribución no activa las mismas obligaciones de entrega.

**4.6 LGPL: una biblioteca con condiciones de integración**

**Caso didáctico:** una aplicación comercial utiliza una biblioteca LGPL. La aplicación puede distribuirse bajo otras condiciones si se respetan los requisitos de LGPL, que no se reducen a poner un enlace a su página. \[F6\]

Según el caso, hay que conservar avisos y licencias, proporcionar el fuente requerido y permitir que el usuario sustituya o reenlace una versión modificada de la biblioteca. El tipo de enlace y el modo de distribución importan.

**Cuándo considerarla:** cuando desarrollas una biblioteca y quieres permitir su uso en aplicaciones con otras licencias, manteniendo obligaciones sobre la biblioteca.

**Precaución:** «enlace dinámico» no significa cumplimiento automático. Tampoco hay que afirmar que el enlace estático es siempre imposible: puede requerir materiales y condiciones adicionales para el reenlazado.

**4.7 GPL: compartir libertades al distribuir**

**Caso didáctico:** modificas un programa GPL y entregas la versión resultante a un cliente. Debes cumplir las obligaciones aplicables de la GPL, incluido el código fuente correspondiente de la obra cubierta y los avisos requeridos. Entregar a un único cliente también puede ser distribución. \[F7\]

**Cuándo elegirla:** cuando quieres que los derivados distribuidos del programa mantengan sus libertades de uso, modificación y redistribución.

**Lo que no debemos enseñar:**

-   «GPL prohíbe vender». Es falso.
-   «Cualquier archivo junto a uno GPL pasa automáticamente a GPL». La mera agregación de obras independientes no tiene ese efecto.
-   «Ejecutar una herramienta GPL convierte mis resultados en GPL». No ocurre por el simple hecho de ejecutarla; importa si el resultado incorpora material cubierto y las condiciones concretas.
-   «Toda modificación privada debe publicarse en GitHub». GPL no exige eso de forma general.

El alcance sobre programas combinados y enlaces merece revisión específica. Proporcionar código a los destinatarios conforme a la licencia no es necesariamente lo mismo que publicarlo para todo Internet.

**4.8 AGPL: atención a los servicios por red**

**Caso didáctico:** modificas una plataforma AGPL y permites que clientes la utilicen desde el navegador. La sección 13 exige que la versión modificada ofrezca de forma visible a los usuarios que interactúan remotamente la posibilidad de recibir su código fuente correspondiente. \[F8\]

**Cuándo elegirla:** cuando deseas cubrir también ese escenario de servicio remoto, además de las obligaciones de distribución.

**Precauciones:**

-   No enseñar simplemente que «usar Internet es distribuir». AGPL tiene una obligación específica para interacción remota con una versión modificada.
-   No asumir que todo el código de la empresa debe abrirse. Hay que delimitar la obra cubierta y la integración concreta.
-   No asumir que consumir cualquier API AGPL convierte automáticamente al cliente en AGPL. El protocolo, la independencia de las partes y la forma de combinación importan.
-   El fuente correspondiente no equivale a publicar contraseñas, datos personales o registros de clientes. Los secretos operativos deben mantenerse separados del código.

**4.9 Comparación de situaciones**

| Situación                    | MIT / Apache                                                                 | MPL                                                     | GPL                                                            | AGPL                                                                                     |
| ---------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Ejecutar sin distribuir      | No obliga por sí solo a divulgar cambios                                     | No obliga por sí solo a divulgar cambios                | No obliga por sí solo a divulgar cambios                       | Revisar si hay versión modificada e interacción remota                                   |
| Distribuir cambios           | Conservar avisos y cumplir condiciones; no exige normalmente divulgar fuente | Fuente de archivos cubiertos y obligaciones pertinentes | Fuente correspondiente de la obra cubierta y demás condiciones | Obligaciones de distribución y demás condiciones                                         |
| Ofrecer solo servicio remoto | Sin obligación general de divulgar fuente por ese hecho                      | Sin obligación general de divulgar fuente por ese hecho | Sin obligación general de divulgar fuente por ese hecho        | La sección 13 puede exigir ofrecer el fuente de la versión modificada a usuarios remotos |
| Uso comercial                | Permitido                                                                    | Permitido                                               | Permitido                                                      | Permitido                                                                                |

La tabla presupone las licencias estándar, sin excepciones añadidas, y resume escenarios. No determina por sí sola el alcance de una obra derivada o combinada.

**5\. Licencias para cursos, documentación y otros recursos · 38–50**

**5.1 Un repositorio puede contener varias clases de obras**

Un curso puede incluir código Python, explicaciones en Markdown, diapositivas, fotografías, datos y un modelo de IA. No debemos asumir que una licencia pensada para uno de esos contenidos es la mejor opción para todos.

Creative Commons recomienda licencias específicas de software para el código. Sus licencias son útiles para textos, imágenes y otros contenidos creativos, pero no sustituyen de forma adecuada cuestiones habituales del software como código fuente y patentes. \[F10\]

**5.2 Creative Commons: qué significa cada elemento**

| Elemento | Significado    | Consecuencia práctica                                                                                    |
| -------- | -------------- | -------------------------------------------------------------------------------------------------------- |
| BY       | Atribución     | Reconocer autoría/procedencia conforme a la licencia                                                     |
| SA       | CompartirIgual | Las adaptaciones compartidas deben usar las condiciones exigidas, incluida compatibilidad cuando proceda |
| NC       | NoComercial    | Solo permite usos no comerciales bajo esa autorización                                                   |
| ND       | SinDerivadas   | No permite compartir adaptaciones bajo esa autorización                                                  |

En las licencias 4.0, ND no significa que no puedas realizar ninguna adaptación privada: la limitación clave es compartir el material adaptado. Las excepciones legales y los permisos separados siguen teniendo su propio papel. \[F10\]

**5.3 Las seis licencias CC principales**

| Licencia 4.0 | ¿Permite uso comercial?                | ¿Permite compartir adaptaciones?   | Para qué usarla y cuándo                                                                | Precaución                                                                |
| ------------ | -------------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| CC BY        | Sí                                     | Sí                                 | Material que quieres que se reutilice ampliamente con atribución                        | Exige atribución y demás avisos aplicables, no solo «mencionar un nombre» |
| CC BY-SA     | Sí                                     | Sí, bajo condiciones SA            | Cursos colaborativos cuyas adaptaciones compartidas deben mantener apertura equivalente | No prohíbe vender el curso o sus adaptaciones                             |
| CC BY-NC     | No, salvo permiso separado u otra base | Sí, dentro del ámbito no comercial | Material que deseas compartir para usos no comerciales                                  | «Educativo» no garantiza «no comercial»                                   |
| CC BY-NC-SA  | No, salvo permiso separado u otra base | Sí, con NC y SA                    | Material con restricción comercial y continuidad de condiciones                         | Puede impedir usos en cursos de pago o materiales empresariales           |
| CC BY-ND     | Sí                                     | No bajo esta licencia              | Material cuya versión adaptada no quieres autorizar a compartir                         | Una traducción normalmente es una adaptación                              |
| CC BY-NC-ND  | No, salvo permiso separado u otra base | No bajo esta licencia              | Compartir copias no adaptadas y para usos no comerciales                                | Es muy restrictiva para enseñanza colaborativa y traducciones             |

**CC0** es una herramienta distinta de dedicación al dominio público, no una séptima combinación de BY, SA, NC y ND. Referencias: \[F10\], \[F11\].

**5.4 Ejemplo de atribución**

Supongamos que adaptamos una guía propia de un tercero publicada bajo CC BY 4.0. Un aviso podría ser:

Adaptado de «Introducción a los repositorios», de Ana Ejemplo.

Original: https://example.org/guia

Licencia: CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/

Cambios: se añadieron ejercicios y se actualizaron capturas.

El nombre y la dirección son ficticios. En un caso real, conserva también los avisos suministrados que sean pertinentes. La atribución se realiza razonablemente según el medio; no debe sugerir que el autor original respalda tu adaptación.

**Ejemplo:** código original bajo MIT y explicaciones originales bajo CC BY-SA 4.0 puede ser una combinación razonable si buscas reutilización del código y continuidad de la apertura de las adaptaciones del material. Debes delimitar qué archivos están bajo cada licencia y separar recursos ajenos. Es una opción de diseño, no una licencia asignada automáticamente a tus repositorios.

**5.5 Datos, imágenes, fuentes tipográficas y modelos**

| Contenido                   | Qué revisar                                                                           | Precaución específica                                                                 |
| --------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Dataset                     | Licencia del conjunto, procedencia, términos y posibles derechos sobre bases de datos | Una licencia no elimina protección de datos ni autoriza publicar información personal |
| Fotografías e ilustraciones | Autor, licencia y derechos de imagen pertinentes                                      | Estar en un buscador no concede permiso                                               |
| Tipografías                 | Licencia de la fuente concreta, por ejemplo OFL-1.1 si corresponde                    | Puede haber condiciones de redistribución y nombres reservados                        |
| Pesos de un modelo          | Licencia exacta del modelo, versión y restricciones adicionales                       | La licencia del código de inferencia no cubre automáticamente los pesos               |
| Código generado por IA      | Procedencia, posibles coincidencias y derechos para publicarlo                        | «Lo escribió una IA» no sustituye una revisión de licencias                           |
| Respuestas de una API       | Condiciones del servicio y derechos de terceros pertinentes                           | La licencia del SDK no determina por sí sola los derechos sobre las respuestas        |
| Notebook .ipynb             | Código, texto, recursos y resultados almacenados                                      | Puede reunir contenidos con licencias distintas y además contener secretos            |

No prometas que una licencia CC permite o prohíbe todos los usos relacionados con entrenamiento de IA. La respuesta depende del material, los derechos implicados, la actividad y la ley aplicable; no hay una regla universal deducible solo del nombre de la licencia.

**6\. Elegir con criterio y revisar compatibilidad · 50–60**

**6.1 Método de seis preguntas**

1.  **¿Qué estoy licenciando?** Código, texto, imagen, datos, pesos o una combinación.
2.  **¿Tengo autoridad para hacerlo?** Revisar autoría, empleo, contrato, colaboraciones y materiales externos.
3.  **¿Qué quiero permitir?** Uso comercial, modificaciones, redistribución, integración en productos cerrados.
4.  **¿Qué quiero exigir?** Avisos, fuente, continuidad de licencia, apertura de versiones modificadas por red.
5.  **¿Qué condiciones ya existen?** Dependencias, recursos copiados, versiones y excepciones.
6.  **¿Puedo explicar y cumplir la decisión?** Una licencia elegida por popularidad sin comprender sus obligaciones es una decisión incompleta.

**6.2 Orientación por objetivo**

| Objetivo del titular                                                      | Opciones a evaluar                                         | Consecuencia que debe aceptar                                               |
| ------------------------------------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------------------------------------- |
| Facilitar reutilización del código con pocas condiciones                  | MIT, BSD, ISC                                              | Otros pueden incorporar el código en derivados cerrados                     |
| Permisos amplios con concesión expresa de patentes                        | Apache-2.0                                                 | Avisos y condiciones más detalladas                                         |
| Mantener abiertos ciertos archivos distribuidos                           | MPL-2.0                                                    | Revisar qué archivos y cambios están cubiertos                              |
| Abrir una biblioteca permitiendo otras licencias para aplicaciones        | LGPL                                                       | Cumplimiento técnico de integración y distribución                          |
| Mantener libertades en derivados distribuidos del programa                | GPL                                                        | No es adecuada si el plan exige cerrar esos derivados sin otra autorización |
| Incluir obligaciones de fuente para versiones modificadas usadas por red  | AGPL                                                       | Planificar acceso al fuente correspondiente para usuarios remotos           |
| Difundir un manual con atribución                                         | CC BY                                                      | Permite usos comerciales y adaptaciones                                     |
| Difundir un curso manteniendo condiciones de las adaptaciones compartidas | CC BY-SA                                                   | Permite usos comerciales                                                    |
| Reservar explotación comercial exclusiva de material propio               | Evaluar condiciones propietarias o CC con NC según el caso | No presentarlo como código abierto; comprobar alcance y derechos            |

**6.3 Compatibilidad: no es una suma de etiquetas**

Poner MIT en tu repositorio no vuelve MIT todas las dependencias. Cada componente conserva sus condiciones. Una aplicación con dependencias permisivas puede distribuirse bajo condiciones propias si cumple los permisos, avisos y demás requisitos aplicables.

Con copyleft, hay que determinar si existe una obra cubierta o combinada, qué se entrega y qué obligación se activa. Tener dos programas independientes en la misma carpeta no equivale necesariamente a combinarlos en un único programa. Separar archivos o llamar a algo «microservicio» tampoco decide por sí solo la cuestión. \[F7\]

**Ejemplo de versión relevante:** Apache-2.0 puede ser compatible con GPLv3 en determinadas combinaciones, pero no con GPLv2-only de la misma forma. No basta con escribir «compatible con GPL» sin versión. Consulta la explicación GNU y las condiciones concretas. \[F7\]

**6.4 Licencia dual, OR y AND**

Un titular con derechos suficientes puede ofrecer el mismo código bajo licencias alternativas; por ejemplo, una opción de copyleft y otra comercial. Eso no permite quitar condiciones de código ajeno sobre el que no tiene esos derechos.

SPDX permite expresar licencias con identificadores y operadores: \[F12\]

MIT OR Apache-2.0

Significa que el destinatario puede elegir una alternativa si esa es realmente la concesión del titular.

MIT AND Apache-2.0

Significa que deben cumplirse ambas; el significado práctico depende del material al que se aplique la expresión. No se debe usar AND simplemente porque no sabemos cuál escoger.

En las licencias GNU conviene distinguir GPL-3.0-only y GPL-3.0-or-later: esta última permite optar por versiones posteriores autorizadas. No se debe añadir «or later» si el titular no ha concedido esa opción.

**6.5 Cambiar de licencia no borra lo anterior**

Si eres titular de todos los derechos pertinentes, puedes elegir otras condiciones para futuras versiones. Sin embargo, una licencia ya concedida sobre copias anteriores no desaparece simplemente al cambiar LICENSE; importan sus condiciones, incluida su continuidad o terminación. En CC, la concesión no se revoca a quienes cumplen la licencia. \[F10\]

Si hay contribuidores, componentes externos o cesiones, puede ser necesario obtener autorizaciones. Un CLA o una declaración DCO no deben tratarse como una cesión automática de derechos: depende de lo que realmente documenten.

**7\. Práctica guiada: documentar un repositorio ·**

**Escenario**

Prepararemos la decisión de licencias de un repositorio ficticio llamado **Taller de presupuestos con Python**:

-   src/calculadora.py: código original del equipo.
-   docs/guia.md: explicación original del equipo.
-   imagenes/portada.svg: imagen original del equipo.
-   datos/ejemplo.csv: tabla con productos y precios ficticios creada para la clase.
-   Una biblioteca externa cuyo permiso debe registrarse por separado.

**Objetivo del proyecto:** permitir uso comercial y reutilización amplia del código; permitir adaptar el manual, conservando condiciones de apertura de las adaptaciones compartidas. No usaremos material de clientes ni datos personales.

**Paso 1 · Inventario de contenido ·**

Crea una tabla como esta y completa la procedencia antes de elegir licencias:

| Ruta                 | Autor o titular   | Procedencia                | Licencia propuesta o existente | Acción pendiente                          |
| -------------------- | ----------------- | -------------------------- | ------------------------------ | ----------------------------------------- |
| src/calculadora.py   | Equipo del taller | Original                   | MIT, propuesta                 | Confirmar acuerdo del equipo              |
| docs/guia.md         | Equipo del taller | Original                   | CC BY-SA 4.0, propuesta        | Obtener texto y aviso                     |
| imagenes/portada.svg | Equipo del taller | Original                   | CC BY-SA 4.0, propuesta        | Confirmar autoría                         |
| datos/ejemplo.csv    | Equipo del taller | Datos ficticios originales | CC0-1.0, propuesta             | Verificar que no se copiaron datos ajenos |
| Biblioteca externa   | Tercero           | Versión exacta del paquete | La que tenga ese paquete       | Revisar fuente oficial y avisos           |

No inventes la licencia del paquete externo: si no está comprobada, escribe **pendiente de verificación**. Eso es mejor que registrar una certeza falsa.

**Paso 2 · Decidir por contenido ·**

Escribe tres frases:

1.  «Elegimos MIT para nuestro código original porque…»
2.  «Elegimos CC BY-SA 4.0 para la guía porque…»
3.  «No aplicamos estas decisiones al código de terceros porque…»

**Resultado esperado:** justificar permisos y consecuencias, no limitarse a decir «es la más usada».

**Paso 3 · Preparar archivos y textos**

En la carpeta de práctica crea o prepara estos archivos:

| Archivo                   | Para qué sirve                                                      |
| ------------------------- | ------------------------------------------------------------------- |
| LICENSE                   | Texto completo de MIT aplicable al código original del ejercicio    |
| LICENSES/CC-BY-SA-4.0.txt | Texto completo de la licencia de documentación y recursos señalados |
| LICENSES/CC0-1.0.txt      | Texto completo aplicable a los datos originales señalados           |
| README.md                 | Mapa explícito de alcance de cada licencia                          |
| THIRD_PARTY_NOTICES.md    | Inventario y avisos de terceros cuando corresponda                  |

Obtén los textos oficiales desde las fuentes. En una licencia con campos de año y titular, completa esos campos correctamente. No traduzcas, resumas ni modifiques las cláusulas para crear el archivo legal; la explicación en español va en el README.

Para la demostración de MIT, usa [el texto estándar](https://choosealicense.com/licenses/mit/). Para CC, abre [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode) y [CC0](https://creativecommons.org/publicdomain/zero/1.0/legalcode). Si no hay conexión, deja indicado que falta incorporar el texto y no declares la práctica lista para publicar.

**Paso 4 · Escribir el alcance en README ·**

El siguiente aviso pertenece al **ejercicio ficticio**. No debe copiarse a otro proyecto sin verificar que sea verdadero.

\## Licencias

El código original de \`src/\` se distribuye bajo MIT; véase \`LICENSE\`.

El contenido original de \`docs/\` y la imagen original

\`imagenes/portada.svg\` se distribuyen bajo CC BY-SA 4.0;

véase \`LICENSES/CC-BY-SA-4.0.txt\`.

El conjunto ficticio original \`datos/ejemplo.csv\` se ofrece bajo

CC0-1.0; véase \`LICENSES/CC0-1.0.txt\`.

Los componentes de terceros conservan sus propias licencias.

Su inventario se documenta en \`THIRD\_PARTY\_NOTICES.md\`.

Los avisos particulares de archivos y recursos deben respetarse.

Un README no autoriza usos que no puedes conceder. Si contradice el archivo LICENSE o los avisos de los archivos, hay que corregir la inconsistencia.

**Paso 5 · Identificar un archivo de código ·**

En el código original de prueba puedes añadir un identificador SPDX y un aviso de titularidad verdadero:

\# SPDX-License-Identifier: MIT

\# Copyright (c) 2026 Equipo del taller

def calcular\_total(precio, cantidad):

    return precio \* cantidad

«Equipo del taller» es un titular ficticio usado solo para la demostración. En un repositorio real identifica a quien corresponda. El identificador SPDX ayuda a reconocer la licencia; no sustituye conservar los textos y avisos requeridos. \[F12\]

**Paso 6 · Revisión por parejas · 2 minutos**

Cada pareja debe poder responder:

-   ¿Qué licencia se aplica al código y dónde está su texto?
-   ¿Qué licencia se aplica a la guía?
-   ¿Se permite uso comercial en ambas?
-   ¿Puede saberse qué archivos son originales y cuáles ajenos?
-   ¿Hay algo pendiente que impida publicar con confianza?

**Entrega:** mapa de contenido, justificación de tres frases y aviso de README. Si se incorporaron los textos completos, revisar que no sean resúmenes o páginas guardadas por error como HTML.

**7.      Casos para discutir y evaluación ·**

**Caso A: vender una herramienta MIT**

Una persona adapta una herramienta MIT y cobra por entregarla a una empresa. Conserva el aviso de copyright y la licencia.

**Pregunta:** ¿el cobro está prohibido por MIT? ¿Qué comprobarías además?

**Caso B: curso CC BY-SA**

Una academia adapta un manual CC BY-SA 4.0 y lo ofrece dentro de un curso pagado. Identifica cambios, atribuye y comparte la adaptación bajo las condiciones SA aplicables.

**Pregunta:** ¿el hecho de cobrar viola por sí solo esa licencia?

**Caso C: traducción ND**

Un profesor traduce una guía CC BY-ND 4.0 y quiere publicar la traducción en su repositorio.

**Pregunta:** ¿la atribución basta para que esa publicación esté autorizada por la licencia?

**Caso D: SaaS AGPL**

Un equipo modifica una plataforma AGPL y la ofrece por navegador. Afirma que no tiene obligaciones porque no entrega instaladores.

**Pregunta:** ¿qué condición debe revisar?

**Caso E: repositorio sin licencia**

Una persona copia un repositorio público sin LICENSE, le añade MIT y lo presenta como proyecto propio.

**Pregunta:** ¿el archivo nuevo le permite conceder esos derechos sobre el contenido copiado?

**Caso F: biblioteca LGPL**

Una aplicación incorpora una biblioteca LGPL. El equipo decide no revisar nada porque «el enlace es dinámico».

**Pregunta:** ¿es suficiente esa explicación para afirmar cumplimiento?

**Comprobación individual**

Completa en una o dos frases:

1.  Para un ejemplo de código propio que quiero reutilizable en productos cerrados, evaluaría \_\_\_\_\_\_ porque \_\_\_\_\_\_.
2.  Antes de copiar un componente de terceros, revisaré \_\_\_\_\_\_.
3.  Una precaución sobre documentación o datos es \_\_\_\_\_\_.

**Solucionario del docente**

| Caso | Respuesta esperada                     | Matiz que demuestra comprensión                                                                         |
| ---- | -------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| A    | MIT permite uso comercial              | Revisar avisos, dependencias y derechos de otros contenidos; no solo el precio                          |
| B    | Cobrar no viola por sí solo CC BY-SA   | Hay que cumplir atribución, indicación de cambios, SA y demás condiciones; delimitar qué es adaptación  |
| C    | No basta                               | Una traducción suele ser adaptación; hace falta permiso adicional u otra base jurídica para compartirla |
| D    | Revisar AGPL, especialmente sección 13 | Ofrecer el fuente correspondiente de la versión modificada a usuarios remotos, según sus términos       |
| E    | No                                     | No puede otorgar derechos que no tiene; debe obtener autorización o una alternativa licenciada          |
| F    | No                                     | Revisar avisos, licencias, fuente y condiciones de sustitución/reenlazado aplicables                    |

**Rúbrica breve:**

| Criterio                                                      | Puntos |
| ------------------------------------------------------------- | ------ |
| Distingue acceso público de permiso                           | 2      |
| Diferencia permisiva y copyleft sin negar el uso comercial    | 2      |
| Asigna licencias según el contenido y justifica               | 2      |
| Reconoce avisos, fuente o condiciones específicas pertinentes | 2      |
| Identifica un riesgo de terceros o una verificación pendiente | 2      |
| Total                                                         | 10     |

**9\. Precauciones profesionales que conviene conservar**

| Error frecuente                                                | Por qué es un problema                                          | Acción correcta                                               |
| -------------------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------- |
| «Si está en Internet, lo puedo copiar»                         | Visibilidad no equivale a permiso                               | Identificar licencia y condiciones del material               |
| «Una estrella o un fork me concede todos los derechos»         | Las funciones de una plataforma no equivalen a licencia general | Revisar licencia y términos pertinentes                       |
| «Añadí MIT y todo quedó resuelto»                              | Puede haber código ajeno y condiciones anteriores               | Inventariar y conservar licencias externas                    |
| «GPL no permite ganar dinero»                                  | Confunde libertad con precio                                    | Revisar obligaciones de distribución                          |
| «AGPL obliga a publicar todos mis datos»                       | Confunde código correspondiente con información operativa       | Separar fuente, secretos y datos; revisar alcance             |
| «No comercial significa cualquier actividad sin cobro directo» | El carácter comercial no depende únicamente de un cobro puntual | Revisar finalidad, contexto y definición aplicable            |
| «Dar crédito autoriza cualquier uso»                           | La atribución es una condición, no un permiso ilimitado         | Revisar también adaptación, comercio y redistribución         |
| «Borré el autor original porque modifiqué mucho»               | Las modificaciones no eliminan avisos exigidos                  | Conservar avisos pertinentes y registrar aportaciones propias |
| «La licencia cubre el logotipo»                                | Pueden existir derechos de marca distintos                      | Revisar condiciones de identidad visual                       |
| «La licencia evita toda responsabilidad»                       | Su alcance tiene límites legales                                | No prometer inmunidad ni garantía universal                   |
| «El escáner aprobó y ya terminamos»                            | Las herramientas pueden omitir archivos, versiones o contexto   | Usar inventario y revisión humana                             |
| «Como trabajo para un cliente, puedo publicarlo»               | Puede no existir autorización del titular                       | Revisar contrato y autorización antes de publicar             |

**Inventario mínimo de terceros**

Un registro profesional puede contener:

| Componente        | Versión o revisión | Fuente         | Licencia exacta             | Uso                             | Obligaciones           | Evidencia                 |
| ----------------- | ------------------ | -------------- | --------------------------- | ------------------------------- | ---------------------- | ------------------------- |
| Nombre verificado | Versión concreta   | Enlace oficial | Identificador y excepciones | Interno, distribuido o servicio | Avisos, fuente u otras | Archivo y fecha revisados |

Incluye dependencias indirectas cuando corresponda. Un archivo de bloqueo ayuda a conocer versiones, pero no garantiza por sí solo que todas las licencias estén verificadas. Un SBOM, inventario de componentes de software, puede ayudar a organizar esa información; tampoco sustituye el análisis del uso concreto.

**Antes de publicar o entregar**

-   Tengo derechos o autorizaciones suficientes sobre lo que publico.
-   La licencia seleccionada responde al objetivo del proyecto.
-   El texto es completo y la versión está identificada.
-   El README explica el alcance y no contradice los archivos.
-   Se conservan los avisos de terceros pertinentes.
-   Se revisaron dependencias y recursos además del código principal.
-   Se preparó el código fuente o la oferta de acceso si corresponde.
-   Se revisaron datos personales, secretos y derechos de imagen/marca.
-   Las contribuciones tienen una política de entrada comprensible.
-   Lo que sigue pendiente está indicado; no se afirma una revisión inexistente.

**11\. Preguntas frecuentes**

**¿Qué licencia es la mejor?**

No existe una mejor para todos los proyectos. Primero identifica el contenido, tus derechos, el uso que deseas permitir y las condiciones heredadas. La elección debe servir al objetivo y ser compatible con lo que ya utilizas.

**¿Puedo poner copyright y una licencia abierta a la vez?**

Sí. La licencia concede permisos apoyándose en derechos existentes; no exige renunciar automáticamente a la autoría o titularidad. En muchas licencias conservar el aviso es una condición.

**¿Puedo cobrar por un proyecto MIT, GPL o AGPL?**

Sí, esas licencias permiten uso comercial. Cobrar no elimina las condiciones ni permite impedir a los destinatarios derechos que la licencia les concede.

**¿Una licencia obliga a poner el nombre del autor en la portada?**

Depende del texto, el medio y los avisos aplicables. Conservar avisos legales no equivale siempre a poner créditos en la pantalla principal. No inventes obligaciones ni elimines las que sí existen.

**¿Mi programa pasa a GPL porque uso Git o un editor GPL?**

No por ese mero uso. Diferencia las herramientas que ejecutas de los componentes que copias, incorporas, enlazas o redistribuyes. El contenido del resultado y las excepciones concretas pueden importar. \[F7\]

**¿Puedo hacer privado un repositorio que era abierto?**

Puedes controlar el acceso a tu copia según tus derechos y la plataforma, pero no recuperar automáticamente las copias ya distribuidas ni retirar derechos ya concedidos a sus destinatarios conforme a la licencia. Hacer privado tampoco elimina forks o copias previas. \[F1\]

**¿Puedo usar Creative Commons para todo el repositorio?**

No es una buena regla universal. Para software, se recomiendan licencias específicas; para contenidos creativos puede ser adecuado CC. Un notebook puede necesitar un mapa claro porque combina código y texto. \[F10\]

**¿Puedo prohibir que una determinada empresa use mi software y llamarlo open source?**

Las licencias que discriminan personas, grupos o campos de actividad no cumplen esos criterios de la definición OSI. Puede haber otras formas de licenciar material propio, pero hay que describirlas correctamente. \[F2\]

**12\. Fuentes oficiales y textos de referencia**

Consultadas el **18 de noviembre de 2026**. Los textos jurídicos completos y sus condiciones prevalecen sobre las tablas didácticas. Los casos y ejemplos del taller son hipotéticos.

-   **\[F1\] GitHub — Licensing a repository:** permisos por defecto, repositorios públicos, ubicación y detección de licencias. [https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
-   **\[F2\] Open Source Initiative — Open Source Definition:** criterios de redistribución, no discriminación y uso comercial. [https://opensource.org/osd](https://opensource.org/osd)
-   **\[F3\] GitHub / Choose a License — Comparación y textos estándar:** panorama de MIT, Apache, MPL, LGPL, GPL, AGPL, Boost y Unlicense. [https://choosealicense.com/licenses/](https://choosealicense.com/licenses/)
-   **\[F4\] Apache Software Foundation — Apache License 2.0:** especialmente secciones 3, 4 y 6 sobre patentes, redistribución y marcas. [https://www.apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0)
-   **\[F5\] Mozilla — MPL 2.0 FAQ:** alcance por archivos, distribución y obras mayores. [https://www.mozilla.org/en-US/MPL/2.0/FAQ/](https://www.mozilla.org/en-US/MPL/2.0/FAQ/)
-   **\[F6\] GNU — LGPLv3:** condiciones para bibliotecas y obras combinadas, especialmente sección 4. [https://www.gnu.org/licenses/lgpl-3.0.html](https://www.gnu.org/licenses/lgpl-3.0.html)
-   **\[F7\] GNU — Preguntas frecuentes de licencias:** distribución, uso comercial, combinaciones, herramientas y compatibilidad. [https://www.gnu.org/licenses/gpl-faq.html](https://www.gnu.org/licenses/gpl-faq.html)
-   **\[F8\] GNU — AGPLv3:** especialmente sección 13 sobre interacción remota con versiones modificadas. [https://www.gnu.org/licenses/agpl-3.0.html](https://www.gnu.org/licenses/agpl-3.0.html)
-   **\[F9\] Choose a License — BSD-3-Clause:** texto estándar y cláusula de no respaldo. [https://choosealicense.com/licenses/bsd-3-clause/](https://choosealicense.com/licenses/bsd-3-clause/)
-   **\[F10\] Creative Commons — FAQ:** software, atribución, adaptaciones, efectos de NC/ND y continuidad de permisos. [https://creativecommons.org/faq/](https://creativecommons.org/faq/)
-   **\[F11\] Creative Commons — Licencias:** comparación de las seis licencias CC. [https://creativecommons.org/cc-licenses/](https://creativecommons.org/cc-licenses/)
-   **\[F12\] SPDX — Handling license information:** identificadores, expresiones OR/AND y versiones GNU. [https://spdx.dev/learn/handling-license-info/](https://spdx.dev/learn/handling-license-info/)

**Enlaces para obtener los textos durante la práctica**

| Licencia     | Texto o página de acceso                           |
| ------------ | -------------------------------------------------- |
| MIT          | https://choosealicense.com/licenses/mit/           |
| Apache-2.0   | https://www.apache.org/licenses/LICENSE-2.0        |
| MPL-2.0      | https://www.mozilla.org/en-US/MPL/2.0/             |
| GPLv3        | https://www.gnu.org/licenses/gpl-3.0.html          |
| LGPLv3       | https://www.gnu.org/licenses/lgpl-3.0.html         |
| AGPLv3       | https://www.gnu.org/licenses/agpl-3.0.html         |
| CC BY 4.0    | https://creativecommons.org/licenses/by/4.0/       |
| CC BY-SA 4.0 | https://creativecommons.org/licenses/by-sa/4.0/    |
| CC0-1.0      | https://creativecommons.org/publicdomain/zero/1.0/ |

**Criterio final de trabajo:** describir lo que realmente sabemos, dejar identificadas las dudas y no conceder derechos sobre material que no controlamos.