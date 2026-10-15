# PLANTILLA: Diseño Profesional de Skill

> **Objetivo:** Esta plantilla guía el diseño de una skill de IA estructurada, reutilizable y verificable.  
> **Nivel:** Pensado para personas que ya manejan prompts pero que desean empaquetar capacidades profesionales.  
> **Uso:** Completa cada campo con la información de tu tarea. Los campos con `*` son obligatorios.  
> **Nota:** Una skill no es código ejecutable por sí sola; es un documento de diseño que da forma a un prompt estructurado o a un agente.

---

## 1. Identificación *(*)*
| Campo | Instrucción | Ejemplo |
|---|---|---|
| **Nombre** | Nombre corto y único de la skill. Evita espacios; usa guión bajo o PascalCase. | `clasificar-cliente` |
| **Versión** | Número de versión semántico (MAJOR.MINOR.PATCH). Incrementa al hacer cambios incompatibles. | `1.0.0` |
| **Estado** | `proyecto`, `en-desarrollo`, `probando`, `disponible`, `deprecated`. Indica madurez. | `disponible` |
| **Responsable** | Quien creó o mantiene la skill. Para equipos, usa un alias o rol. | `administrativo-panaderia` |

---

## 2. Problema que resuelve *(*)*
**Descripción clara y concreta de la tarea o problema que la skill aborda.**

> **Hazlo así:** "Convierte notas de reunión en una minuta estructurada con decisiones, responsables y fechas."
> **Evita:** "Hace cosas con el texto." (Demasiado vago)

**Tu problema:**
```
...
```

---

## 3. Alcance *(*)*
Qué cubre la skill y, críticamente, qué **queda fuera** de su responsabilidad.

| Sub-campo | Instrucción | Tu respuesta |
|---|---|---|
| **Incluye** | Tareas, datos o formatos que SÍ procesa la skill. | `...` |
| **Excluye** | Tareas, datos o formatos que la skill **no** toca. Especifica límites claros. | `...` |
| **Usuarios** | Quién puede usar esta skill (rol, nivel, contexto). | `...` |
| **Entorno** | Dónde se aplica (sistema, departamento, etapa del flujo). | `...` |

**Tu alcance:**
- **Incluye:** `...`
- **Excluye:** `...`
- **Usuarios:** `...`
- **Entorno:** `...`

---

## 4. Condiciones de activación y limitaciones
En qué situaciones la skill **debe** usarse y en cuáles **no debe** usarse.

| Condición | Cuando SÍ activar | Cuando NO activar |
|---|---|---|
| **Número mínimo de datos** | `...` | `...` |
| **Contexto necesario** | `...` | `...` |
| **Contexto prohibido** | `...` (ej. datos sensibles) | `...` |
| **Frecuencia** | `...` (reutilizable X veces) | `...` |
| **Errores críticos** | Si detecta `...`, detener y alertar. | `...` |

**Tus condiciones:**
- **Activar si:** `...`
- **No activar si:** `...`

---

## 5. Entradas *(*)*
Todos los campos que la skill necesita para funcionar. Para cada campo:

| Campo | Tipo | Obligatorio | Descripción | Restricciones |
|---|---|---|---|---|
| `*` | `*` | `*` | `*` | `*` |

> **Tipos comunes:** `texto`, `número`, `fecha`, `lista`, `objeto`, `archivo`.  
> **Obligatorio:** `sí` o `no`.  
> **Restricciones:** longitud máxima, formato, rango, valores permitidos.

**Tus entradas:**
| Campo | Tipo | Obligatorio | Descripción | Restricciones |
|---|---|---|---|---|
| `*` | `*` | `sí/no` | `...` | `...` |
| `*` | `*` | `sí/no` | `...` | `...` |
| `*` | `*` | `sí/no` | `...` | `...` |

**Tus entradas:**
| Campo | Tipo | Obligatorio | Descripción | Restricciones |
|---|---|---|---|---|
| `*` | `*` | `sí/no` | `...` | `...` |
| `*` | `*` | `sí/no` | `...` | `...` |
| `*` | `*` | `sí/no` | `...` | `...` |

---

## 6. Dependencias, fuentes de información y herramientas autorizadas
Qué recursos externos necesita la skill y cómo se accede a ellos.

| Dependencia | Tipo | Descripción | Cómo se accede | ¿Crítica? |
|---|---|---|---|---|
| `*` | `*` | `*` | `*` | `sí/no` |

> **Dependencias:** plantillas, bases de datos, APIs, archivos, sistemas internos.  
> **Crítica:** `sí` si el skill falla sin ella; `no` si puede operar independiente.  
> **Fuentes:** docs, tablas, catálogos, catálogos de productos.

**Tus dependencias:**
| Dependencia | Tipo | Descripción | Cómo se accede | ¿Crítica? |
|---|---|---|---|---|
| `*` | `*` | `*` | `*` | `sí/no` |
| `*` | `*` | `*` | `*` | `sí/no` |

---

## 7. Procedimiento secuencial
Guía paso a paso de qué hace la skill, en orden. Cada paso debe ser:

- **Atómico:** una acción clara, no "procesa y analiza".
- **Descriptivo:** suficiente para que otro persona lo imite.
- **Validado:** ¿algún paso puede fallarse? ¿Cómo se maneja?

> **Formato:** Paso 1:acción. Paso 2:acción. O bien: `1. hacer X. 2. validar Y. 3. si-no-hacer Z.`

**Tu procedimiento:**
```
Paso 1: `...`
Paso 2: `...`
Paso 3: `...`
```

---

## 8. Reglas de negocio y restricciones
Normativas internas que la skill debe respetar. Incluye:

- **Fórmulas o fórmulas de cálculo** si aplica.
- **Límites de negocio** (máximos, mínimos, umbrales).
- **Prohibiciones** ("nunca hacer X", "solo hacer Y bajo Z condición").
- **Formato obligatorio** de fechas, números, identificadores.

> **Ejemplo:** "No aplicar descuento si el total es menor a $10." "Usar formato ISO 8601 para fechas."

**Tus reglas:**
```
- `...`
- `...`
- `...`
```

---

## 9. Formato de salida y esquema esperado
Cómo entrega la skill su resultado. Define:

| Elemento | Descripción | Formato | Ejemplo |
|---|---|---|---|
| **Estructura** | Cómo se organiza la salida (tabla, lista, texto estructurado). | `...` | `...` |
| **Campos obligatorios** | Qué campos SÍ deben aparecer. | `...` | `...` |
| **Campos opcionales** | Qué campos pueden aparecer bajo condiciones. | `...` | `...` |
| **Formato de datos** | Fechas, números, monedas, URLs. | `...` | `...` |
| **Encabezado/pie de página** | Información fija que siempre aparece. | `...` | `...` |

**Tu formato de salida:**
```
Estructura: `...`
Campos obligatorios: `...`
Formato de datos: `...`
```

---

## 10. Validaciones de calidad y factualidad
Cómo la skill asegura que el resultado es correcto y digno de confianza.

| Tipo de validación | Qué comprueba | Cómo se hace | Frecuencia |
|---|---|---|---|
| **Formato** | Estructura cumple especificación. | `...` | `...` |
| **Regla de negocio** | Se cumplen condiciones del negocio. | `...` | `...` |
| **Factual** | La información coincide con fuentes. | `...` | `...` |
| **Consistencia** | No hay contradicciones internas. | `...` | `...` |

**Tus validaciones:**
- **Formato:** `...`
- **Regla de negocio:** `...`
- **Factual:** `...`
- **Consistencia:** `...`

---

## 11. Tratamiento de errores, información ausente y contradicciones
Qué pasa y qué hace la skill cuando falta datos, hay conflictos o algo falla.

| Escenario | Comportamiento de la skill | Resultado para el usuario |
|---|---|---|
| **Campo obligatorio ausente** | `...` | `...` |
| **Datos contradictorios** | `...` | `...` |
| **Herramienta falla** | `...` | `...` |
| **Entrada inválida** | `...` | `...` |
| **Límite superado** | `...` | `...` |

**Tu tratamiento de errores:**
- **Campo ausente:** `...`
- **Datos contradictorios:** `...`
- **Herramienta falla:** `...`
- **Entrada inválida:** `...`
- **Límite superado:** `...`

---

## 12. Seguridad, privacidad y límites de acceso
Medidas para que la skill no exponga datos sensibles ni actúe fuera de su ámbito.

| Medida | Descripción | Implementación |
|---|---|---|
| **Mínimo privilegio** | La skill solo accede a lo estrictamente necesario. | `...` |
| **Filtro de datos** | Evita exponer información sensible en la salida. | `...` |
| **Límites de acción** | La skill nunca ejecuta acciones sensibles sin supervisión. | `...` |
| **Aislamiento** | La skill no comparte credenciales ni tokens entre instancias. | `...` |

**Tus medidas de seguridad:**
- **Mínimo privilegio:** `...`
- **Filtro de datos:** `...`
- **Límites de acción:** `...`
- **Aislamiento:** `...`

---

## 13. Casos de prueba y criterios de aceptación
Conjunto mínimo de escenarios que demuestran que la skill funciona como se espera.

| Caso | Entrada | Resultado esperado | Aprobado si... |
|---|---|---|---|
| `*` | `*` | `*` | `*` |

> **Casos mínimos recomendados:**
> 1. Entrada completa y válida.
> 2. Campo obligatorio ausente.
> 3. Información contradictoria.
> 4. Formato incorrecto de entrada.
> 5. Éxito con borde (límite exacto).

**Tus casos de prueba:**
| Caso | Entrada | Resultado esperado | Aprobado si... |
|---|---|---|---|
| 1 | `...` | `...` | `...` |
| 2 | `...` | `...` | `...` |
| 3 | `...` | `...` | `...` |
| 4 | `...` | `...` | `...` |
| 5 | `...` | `...` | `...` |

---

## 14. Mantenimiento, historial de cambios y responsable
Cómo se lleva el control de la skill a lo largo del tiempo.

| Campo | Propósito | Registro |
|---|---|---|
| **Última revisión** | Cuándo se revisó o actualizó por última vez. | `...` |
| **Cambios principales** | Qué cambió en la última versión. | `...` |
| **Próxima revisión** | Cuándo está programada la siguiente revisión. | `...` |
| **Historial completo** | Lista cronológica de versiones y qué cambió. | `...` |

**Tu mantenimiento:**
- **Última revisión:** `...`
- **Cambios principales:** `...`
- **Próxima revisión:** `...`
- **Historial:** `...`

---

## Ejemplo completo: Skill "clasificar-cliente" para Panadería "El Buen Pan"

### 1. Identificación
- **Nombre:** `clasificar-cliente`
- **Versión:** `1.0.0`
- **Estado:** `disponible`
- **Responsable:** `administrativo-panaderia`

### 2. Problema que resuelve
Convierte una solicitud de cliente (persona o empresa) en una clasificación formal con justificación y criterios, aplicando precios y descuentos según el tipo de cliente.

### 3. Alcance
- **Incluye:** Clasificación persona/empresa, cálculo de subtotal/descuentos, generación de justificación.
- **Excluye:** Cálculo de impuestos, generación de contratos, gestión de pagos, inventario.
- **Usuarios:** Personal administrativo, agentes de atención al cliente.
- **Entorno:** Etapa de atención al cliente, antes de generar proforma.

### 4. Condiciones de activación y limitaciones
- **Activar si:** Llega un pedido con productos y cantidades.
- **No activar si:** Falta nombre del cliente o cantidades indefinidas. No usar para decisiones de pago o contratación.

### 5. Entradas
| Campo | Tipo | Obligatorio | Descripción | Restricciones |
|---|---|---|---|---|
| `tipo-cliente` | `texto` | `sí` | "Persona" o "Empresa" | Must be one of: Persona, Empresa |
| `productos` | `lista` | `sí` | Lista de productos solicitados | Mínimo 1 producto |
| `cantidades` | `lista` | `sí` | Cantidad de cada producto | Debe coincidir tamaño con `productos` |
| `razón-social` | `texto` | `no` | Razón social o nombre del cliente | Si `tipo-cliente` es "Empresa", es recomendado |

### 6. Dependencias
| Dependencia | Tipo | Descripción | Cómo se accede | ¿Crítica? |
|---|---|---|---|---|
| `archivo-precios` | `archivo` | `sí` | `datos/precios.md` de la panadería | `sí` |
| `reglas-descuento` | `texto` | `sí` | Reglas de descuento adicionales | `sí` |

### 7. Procedimiento secuencial
Paso 1: Revisa `tipo-cliente` para determinar ruta de precios.
Paso 2: Si "Persona", usa precios unitarios de `archivo-precios`.
Paso 3: Si "Empresa", usa precios al por mayor y tabla de descuentos.
Paso 4: Calcula subtotal multiplicando precio × cantidad.
Paso 5: Aplica descuentos por cantidad según tabla.
Paso 6: Si subtotal > $200, aplica 5% adicional; si > $500, aplica 10%.
Paso 7: Genera justificación breve coherente con cantidades.
Paso 8: Entrega resultado con formato estructurado.

### 8. Reglas de negocio y restricciones
- No aplicar descuento de persona a empresa.
- Los descuentos no son acumulables; se aplica el mayor.
- Si falta `razón-social` para cliente empresa, preguntar antes de calcular.
- Mostrar cálculo paso a paso en la salida.

### 9. Formato de salida y esquema esperado
- **Estructura:** Tabla de productos + subtotal + descuentos + total + justificación.
- **Campos obligatorios:** Producto, cantidad, precio unitario, subtotal, total, tipo-cliente, justificación.
- **Formato de datos:** Precio en formato `$XX.XX`, totales sumados automáticamente.
- **Encabezado:** Nombre de la panadería, fecha, tipo de cliente.

### 10. Validaciones de calidad y factualidad
- **Formato:** Verificar que todos los campos obligatorios aparecen y el formato es el correcto.
- **Regla de negocio:** Comprobar que los descuentos se aplicaron según la tabla y no son acumulables.
- **Factual:** Validar que los precios consultados están en `archivo-precios`.
- **Consistencia:** Asegurar que la justificación coincida con las cantidades y tipos de descuento aplicados.

### 11. Tratamiento de errores, información ausente y contradicciones
- **Campo obligatorio ausente:** Preguntar al usuario antes de calcular; no asumir valores.
- **Datos contradictorios:** Si `tipo-cliente` es ambiguo, pedir clarificación; no adivinar.
- **Herramienta falla:** Si `archivo-precios` no disponible, usar precios por defecto y marcar como "precios estimados".
- **Entrada inválida:** Si `productos` no están en la lista conocida, pedir selección válida.
- **Límite superado:** Si el cálculo excede rangos esperados, mostrar warning y solicitar confirmación.

### 12. Seguridad, privacidad y límites de acceso
- **Mínimo privilegio:** La skill solo lee `archivo-precios.md`; no toca bases de datos de ventas ni historiales.
- **Filtro de datos:** La salida nunca incluye datos sensibles del cliente (usar solo "Tipo de cliente: Persona/Empresa").
- **Límites de acción:** La skill **nunca** genera una proforma ni cobra un pedido; solo clasifica y calcula. Acción de firma requiere humano.
- **Aislamiento:** La skill no comparte su contexto con otras skills ni con sistemas externos.

### 13. Casos de prueba y criterios de aceptación
| Caso | Entrada | Resultado esperado | Aprobado si... |
|---|---|---|---|
| 1 | `tipo-cliente`: "Persona", `productos`: ["Pan francés"], `cantidades`: [300] | Tipo: Persona, Subtotal: $150.00, Sin descuento al por mayor | Se usaron precios unitarios y no se aplicó descuento mayorista |
| 2 | `tipo-cliente`: "Empresa", `productos`: ["Pan francés"], `cantidades`: [300] | Tipo: Empresa, Subtotal: $120.00, Descuento 20%: -$24.00 | Se usaron precios al por mayor y se aplicó el descuento correcto |
| 3 | `tipo-cliente`: "", `productos`: ["Pan francés"], `cantidades`: [300] | Pregunta: "¿El pedido es para una empresa o para uso personal?" | No asume sin evidencia; pregunta al usuario |
| 4 | `tipo-cliente`: "Persona", `productos`: ["Pan integral"], `cantidades`: [10] | Tipo: Persona, Subtotal: $8.00 | Precios unitarios correctos, sin descuento por volumen |
| 5 | `tipo-cliente`: "Empresa", `productos`: ["Pastel chocolate"], `cantidades`: [5] | Tipo: Empresa, Subtotal: $47.50, Sin descuento por cantidad (menor a 20) | Precios al por mayor correctos, descuento solo si aplica por cantidad |

### 14. Mantenimiento, historial de cambios y responsable
- **Última revisión:** `2024-01-15`
- **Cambios principales:** Versión 1.0.0 lanzamiento inicial.
- **Próxima revisión:** `2024-04-15`
- **Historial:**
  - `v1.0.0` (2024-01-15): Lanzamiento inicial con clasificación persona/empresa, cálculo de precios y validaciones básicas.

---

## Cómo usar esta plantilla

1. **Copia** este archivo a tu repositorio o espacio de trabajo.
2. **Completa cada sección** con tu tarea específica. No omita ningún campo `*`.
3. **Usa el ejemplo** completo (al final) como referencia de qué nivel de detalle se espera.
4. **Guarda como** `NOMBRE-SKILL.md` en tu carpeta `skills/`.
5. **Comparte** con tu equipo o para la sesión práctica.
6. **Vuelve a ella** al diseñar nuevas skills o al mantener existentes.

---

## Recuerda

- **Una skill es un documento de diseño**, no código que se ejecute directamente.
- **Cada campo `*` es obligatorio** para que la skill sea usable y evaluable.
- **Los ejemplos reales deben ser coherentes** con tu contexto de negocio.
- **La validación humana sigue siendo necesaria**; la skill ayuda, pero no reemplaza el juicio.
- **Mantén la skill actualizada**; las reglas de negocio y precios cambian.

---
*Plantilla version 1.0 - Diseñada para la Clase 12: Agentes y Skills - Taller de Ingeniería IA*