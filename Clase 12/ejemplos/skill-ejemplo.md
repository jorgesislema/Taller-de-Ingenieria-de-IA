# Ejemplo Completo: Skill "clasificar-cliente" para Panadería "El Buen Pan"

## Contexto
Este ejemplo muestra una skill profesional y completa diseñada para el caso empresarial de la panadería. El alumno puede copiar y personalizar cada campo.

---

### 1. Identificación *(*)*
| Campo | Valor | Comentario |
|---|---|---|
| **Nombre** | `clasificar-cliente` | Nombre corto, único, sin espacios. |
| **Versión** | `1.0.0` | Versión semántica inicial. Incrementar al hacer cambios incompatibles. |
| **Estado** | `disponible` | Madurez: `proyecto`, `en-desarrollo`, `probando`, `disponible`, `deprecated`. |
| **Responsable** | `administrativo-panaderia` | Quien crea o mantiene la skill. Para equipos, un alias o rol. |

---

### 2. Problema que resuelve *(*)*
**Descripción clara y concreta de la tarea o problema que la skill aborda.**

> **Hazlo así:** "Convierte una solicitud de cliente (persona o empresa) en una clasificación formal con justificación y criterios, aplicando precios y descuentos según el tipo de cliente."
> **Tu problema:**
> Convierte una solicitud de cliente en una clasificación formal con justificación y criterios, aplicando precios y descuentos según el tipo de cliente.

---

### 3. Alcance *(*)*
Qué cubre la skill y, críticamente, qué **queda fuera** de su responsabilidad.

| Sub-campo | Tu respuesta |
|---|---|
| **Incluye** | Clasificación persona/empresa, cálculo de subtotal/descuentos, generación de justificación breve, uso de precios unitarios o al por mayor. |
| **Excluye** | Cálculo de impuestos, generación de contratos, gestión de pagos, inventario, decisiones de contratación. |
| **Usuarios** | Personal administrativo, agentes de atención al cliente de la panadería. |
| **Entorno** | Etapa de atención al cliente, **antes** de generar proforma. |

---

### 4. Condiciones de activación y limitaciones
En qué situaciones la skill **debe** usarse y en cuáles **no debe** usarse.

| Condición | Cuando SÍ activar | Cuando NO activar |
|---|---|---|
| **Número mínimo de datos** | Llegan productos y cantidades solicitadas. | Falta nombre del cliente o cantidades indefinidas. |
| **Contexto necesario** | Se conoce el tipo de producto y cantidades. | No se especifican productos o se enumeran desconocidos. |
| **Contexto prohibido** | Datos que la skill procesa oficialmente. | Datos sensibles (razón social completa, datos financieros del cliente). |
| **Frecuencia** | Ilimitada dentro de la atención al cliente. | Fuera del horario de atención o cierres de negocio. |

**Tus condiciones:**
- **Activar si:** Llega un pedido con productos y cantidades.
- **No activar si:** Falta nombre del cliente o cantidades indefinidas. No usar para decisiones de pago o contratación.

---

### 5. Entradas *(*)*
Todos los campos que la skill necesita para funcionar. Para cada campo:

| Campo | Tipo | Obligatorio | Descripción | Restricciones |
|---|---|---|---|---|
| `tipo-cliente` | `texto` | `sí` | "Persona" o "Empresa" | Must be one of: Persona, Empresa |
| `productos` | `lista` | `sí` | Lista de productos solicitados | Mínimo 1 producto; cada uno debe estar en la lista conocida. |
| `cantidades` | `lista` | `sí` | Cantidad de cada producto | Debe coincidir tamaño con `productos`; enteros positivos. |
| `razón-social` | `texto` | `no` | Razón social o nombre del cliente | Si `tipo-cliente` es "Empresa", es recomendado pero no obligatorio. |

**Tus entradas:**
| Campo | Tipo | Obligatorio | Descripción | Restricciones |
|---|---|---|---|---|
| `tipo-cliente` | `texto` | `sí` | `...` | `...` |
| `productos` | `lista` | `sí` | `...` | `...` |
| `cantidades` | `lista` | `sí` | `...` | `...` |
| `razón-social` | `texto` | `no` | `...` | `...` |

---

### 6. Dependencias, fuentes de información y herramientas autorizadas
Qué recursos externos necesita la skill y cómo se accede a ellas.

| Dependencia | Tipo | Descripción | Cómo se accede | ¿Crítica? |
|---|---|---|---|---|
| `archivo-precios` | `archivo` | `datos/precios.md` de la panadería. | Archivo Markdown en la carpeta `datos/`. | `sí` |
| `reglas-descuento` | `texto` | Reglas de descuento adicionales. | Texto fijo: "Si el total supera $200, aplicar 5% adicional. Si el total supera $500, aplicar 10% adicional. Los descuentos no son acumulables entre sí; se aplica el mayor." | `sí` |

**Tus dependencias:**
| Dependencia | Tipo | Descripción | Cómo se accede | ¿Crítica? |
|---|---|---|---|---|
| `archivo-precios` | `archivo` | `...` | `...` | `sí/no` |
| `reglas-descuento` | `texto` | `...` | `...` | `sí/no` |

---

### 7. Procedimiento secuencial
Guía paso a paso de qué hace la skill, en orden. Cada paso debe ser **atómico**, **descriptivo** y **validado**.

> **Formato:** `Paso 1: acción. Paso 2: acción.` O bien: `1. hacer X. 2. validar Y. 3. si-no-hacer Z.`

**Tu procedimiento:**
```
Paso 1: Revisa el `tipo-cliente` para determinar la ruta de precios (persona/empresa).
Paso 2: Si `tipo-cliente` es "Persona", usa precios unitarios del `archivo-precios`.
Paso 3: Si `tipo-cliente` es "Empresa", usa precios al por mayor y tabla de descuentos del `archivo-precios`.
Paso 4: Calcula el subtotal multiplicando precio × cantidad de cada producto.
Paso 5: Aplica descuentos por cantidad según la tabla del `archivo-precios`.
Paso 6: Si el subtotal es > $200, aplica 5% adicional; si es > $500, aplica 10% adicional.
        Recuerda: los descuentos no son acumulables; se aplica el mayor.
Paso 7: Genera una justificación breve coherente con las cantidades y el tipo de cliente.
Paso 8: Entrega el resultado con formato estructurado (tabla + totales + justificación).
```

---

### 8. Reglas de negocio y restricciones
Normativas internas que la skill debe respetar. Incluye:

- **Fórmulas o fórmulas de cálculo** si aplica.
- **Límites de negocio** (máximos, mínimos, umbrales).
- **Prohibiciones** ("nunca hacer X", "solo hacer Y bajo Z condición").
- **Formato obligatorio** de fechas, números, identificadores.

**Tus reglas:**
- No aplicar descuento de persona a empresa.
- Los descuentos no son acumulables; se aplica el mayor.
- Si falta `razón-social` para cliente empresa, preguntar antes de calcular.
- Mostrar cálculo paso a paso en la salida.

---

### 9. Formato de salida y esquema esperado
Cómo entrega la skill su resultado. Define:

| Elemento | Descripción | Formato | Ejemplo |
|---|---|---|---|
| **Estructura** | Cómo se organiza la salida (tabla, lista, texto estructurado). | Tabla con Producto | Cantidad | Precio unitario | Subtotal, más totales y justificación. |
| **Campos obligatorios** | Qué campos SÍ deben aparecer. | Producto, Cantidad, Precio unitario, Subtotal, Total, Tipo de cliente, Justificación. |
| **Campos opcionales** | Qué campos pueden aparecer bajo condiciones. | Razón social (solo si tipo-cliente es Empresa). |
| **Formato de datos** | Fechas, números, monedas, URLs. | Precio en formato `$XX.XX`, totales sumados automáticamente. |
| **Encabezado/pie de página** | Información fija que siempre aparece. | Nombre de la panadería, fecha de generación, versión de la skill. |

**Tu formato de salida:**
- **Estructura:** Tabla con Producto | Cantidad | Precio unitario | Subtotal, más Subtotal general, Descuento y Total, Justificación.
- **Campos obligatorios:** Producto, Cantidad, Precio unitario, Subtotal, Total, Tipo de cliente, Justificación.
- **Formato de datos:** Precio en formato `$XX.XX`, totales sumados automáticamente.
- **Encabezado:** "PANADERÍA EL BUEN PAN", fecha de generación, Tipo de cliente.

---

### 10. Validaciones de calidad y factualidad
Cómo la skill asegura que el resultado es correcto y digno de confianza.

| Tipo de validación | Qué comprueba | Cómo se hace | Frecuencia |
|---|---|---|---|
| **Formato** | Estructura cumple especificación. | Revisar que todos los campos obligatorios aparezcan y el formato es el correcto. | Cada ejecución. |
| **Regla de negocio** | Se cumplen condiciones del negocio. | Comprobar que los descuentos se aplicaron según la tabla y no son acumulables. | Cada ejecución. |
| **Factual** | La información coincide con fuentes. | Validar que los precios consultados están en `archivo-precios.md`. | Cada ejecución. |
| **Consistencia** | No hay contradicciones internas. | Asegurar que la justificación coincida con las cantidades y tipos de descuento aplicados. | Cada ejecución. |

**Tus validaciones:**
- **Formato:** Revisar que todos los campos obligatorios aparezcan y el formato es el correcto.
- **Regla de negocio:** Comprobar que los descuentos se aplicaron según la tabla y no son acumulables.
- **Factual:** Validar que los precios consultados están en `archivo-precios.md`.
- **Consistencia:** Asegurar que la justificación coincida con las cantidades y tipos de descuento aplicados.

---

### 11. Tratamiento de errores, información ausente y contradicciones
Qué pasa y qué hace la skill cuando falta datos, hay conflictos o algo falla.

| Escenario | Comportamiento de la skill | Resultado para el usuario |
|---|---|---|
| **Campo obligatorio ausente** | Preguntar al usuario antes de calcular; no asumir valores. | ` "Falta información. ¿El pedido es para una empresa o para uso personal?" ` |
| **Datos contradictorios** | Si `tipo-cliente` es ambiguo, pedir clarificación; no adivinar. | ` "No puedo determinar el tipo. ¿Podría aclarar si es para una empresa o persona?" ` |
| **Herramienta falla** | Si `archivo-precios` no disponible, usar precios por defecto y marcar como "precios estimados". | ` "No puedo acceder a la lista de precios actual. Usaré valores estimados y le avisaré." ` |
| **Entrada inválida** | Si `productos` no están en la lista conocida, pedir selección válida. | ` "El producto solicitado no está en nuestra lista. Opciones disponibles: Pan francés, Pan integral, ..." ` |
| **Límite superado** | Si el cálculo excede rangos esperados, mostrar warning y solicitar confirmación. | ` "El cálculo resulta en un total muy alto. ¿Desea continuar o ajustar cantidades?" ` |

**Tu tratamiento de errores:**
- **Campo ausente:** Preguntar al usuario antes de calcular; no asumir valores.
- **Datos contradictorios:** Si `tipo-cliente` es ambiguo, pedir clarificación; no adivinar.
- **Herramienta falla:** Si `archivo-precios` no disponible, usar precios por defecto y marcar como "precios estimados".
- **Entrada inválida:** Si `productos` no están en la lista conocida, pedir selección válida.
- **Límite superado:** Si el cálculo excede rangos esperados, mostrar warning y solicitar confirmación.

---

### 12. Seguridad, privacidad y límites de acceso
Medidas para que la skill no exponga datos sensibles ni actúe fuera de su ámbito.

| Medida | Descripción | Implementación |
|---|---|---|
| **Mínimo privilegio** | La skill solo lee `archivo-precios.md`; no toca bases de datos de ventas ni historiales. | `solo lectura de archivo`. |
| **Filtro de datos** | La salida nunca incluye datos sensibles del cliente (usar solo "Tipo de cliente: Persona/Empresa"). | `usar etiqueta genérica en salida`. |
| **Límites de acción** | La skill **nunca** genera una proforma ni cobra un pedido; solo clasifica y calcula. Acción de firma requiere humano. | `etiqueta: "Solo cálculo, firma requiere humano".` |
| **Aislamiento** | La skill no comparte su contexto con otras skills ni con sistemas externos. | `contexto aislado por sesión`. |

**Tus medidas de seguridad:**
- **Mínimo privilegio:** La skill solo lee `archivo-precios.md`; no toca bases de datos de ventas ni historiales.
- **Filtro de datos:** La salida nunca incluye datos sensibles del cliente (usar solo "Tipo de cliente: Persona/Empresa").
- **Límites de acción:** La skill **nunca** genera una proforma ni cobra un pedido; solo clasifica y calcula. Acción de firma requiere humano.
- **Aislamiento:** La skill no comparte su contexto con otras skills ni con sistemas externos.

---

### 13. Casos de prueba y criterios de aceptación
Conjunto mínimo de escenarios que demuestran que la skill funciona como se espera.

| Caso | Entrada | Resultado esperado | Aprobado si... |
|---|---|---|---|
| **1** | `tipo-cliente`: "Persona", `productos`: ["Pan francés"], `cantidades`: [300] | Tipo: Persona, Subtotal: 300 × $0.50 = $150.00, Sin descuento al por mayor | Se usaron precios unitarios y no se aplicó descuento mayorista (criterio: precios unitarios). |
| **2** | `tipo-cliente`: "Empresa", `productos`: ["Pan francés"], `cantidades`: [300] | Tipo: Empresa, Subtotal: 300 × $0.40 = $120.00, Descuento 20%: -$24.00 | Se usaron precios al por mayor y se aplicó el descuento correcto (criterio: precios al por mayor + descuento). |
| **3** | `tipo-cliente`: "", `productos`: ["Pan francés"], `cantidades`: [300] | Resultado: Pregunta "¿El pedido es para una empresa o para uso personal?" | No asume sin evidencia; pide al usuario (criterio: sin evidencia, no asumir). |
| **4** | `tipo-cliente`: "Persona", `productos`: ["Pan integral"], `cantidades`: [10] | Tipo: Persona, Subtotal: 10 × $0.80 = $8.00 | Precios unitarios correctos, sin descuento por volumen (criterio: precios unitarios + sin umbral). |
| **5** | `tipo-cliente`: "Empresa", `productos`: ["Pastel chocolate"], `cantidades`: [5] | Tipo: Empresa, Subtotal: 5 × $9.50 = $47.50, Sin descuento por cantidad (menor a 20 unidades) | Precios al por mayor correctos, descuento solo si aplica por cantidad (criterio: precios al por mayor + condición de cantidad). |

---

### 14. Mantenimiento, historial de cambios y responsable
Cómo se lleva el control de la skill a lo largo del tiempo.

| Campo | Registro |
|---|---|
| **Última revisión** | `2024-01-15` |
| **Cambios principales** | `v1.0.0: lanzamiento inicial con clasificación persona/empresa, cálculo de precios y validaciones básicas.` |
| **Próxima revisión** | `2024-04-15` |
| **Historial** | `v1.0.0 (2024-01-15): Lanzamiento inicial con clasificación persona/empresa, cálculo de precios y validaciones básicas.` |

---

## Cómo usar este ejemplo

1. **Copia** cada sección a tu propia skill `clasificar-cliente.md`.
2. **Personaliza** los valores según tu panadería o negocio real.
3. **Úsala** como referencia para diseñar otras skills siguiendo la misma estructura.
4. **Guárdala** en `skills/clasificar-cliente.md` o el nombre que elijas.
5. **Pruébala** con los casos de prueba incluidos o crea los tuyos propios.

---
*Ejemplo creado para la Clase 12: Agentes y Skills - Taller de Ingeniería IA. Base en panadería "El Buen Pan".*