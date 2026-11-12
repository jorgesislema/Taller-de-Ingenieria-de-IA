# Clase — Bases de Datos: Tipos, Lenguajes, Cómo Elegir y Cómo Modelar
### SQL, NoSQL, grafos y bases vectoriales (la base de RAG y de la memoria de la IA)

> Material de apoyo para el estudiante y guía para el docente.
> **Ejemplos incluidos:** `ejemplos_bases_de_datos.zip` con cuatro scripts que se ejecutan sin instalar nada. El SQL usa SQLite real; los de NoSQL, grafos y vectores son simulaciones didácticas para ver la idea.
> **Formato sugerido:** 2 horas, mitad explicación y mitad práctica. Si es una sesión corta, dividila en **A (qué es una base de datos, cómo se guarda, los cuatro tipos)** y **B (cómo elegir, modelado y práctica)**.

---

## Filosofía de la clase

> **Una IA sin datos bien guardados es un talento sin archivo: inteligente, pero sin memoria ni información propia. Casi todo lo que viene en el taller (RAG, memoria, agentes) descansa sobre una base de datos bien elegida y bien diseñada.**

Si te llevás una sola cosa de esta clase, que sea esta:

> **No existe "la mejor base de datos". Existe la que se ajusta a la forma de tus datos y a las preguntas que vas a hacerles. Elegir mal cuesta más que elegir lento.**

Al terminar vas a poder explicar qué es cada tipo de base de datos, cómo se distingue, cuál elegir para un proyecto, cómo se diseña y cómo se guardan los datos dentro de un servidor.

---

## 1. ¿Qué es una Base de Datos y Por Qué No Alcanza con un Excel?

Una **base de datos** es un sistema que **guarda información de forma organizada** para poder **encontrarla, modificarla y protegerla** rápido, aunque sean millones de datos y muchas personas la usen a la vez.

Un **Sistema Gestor de Bases de Datos** (SGBD, o DBMS en inglés) es el **programa** que administra esos datos: PostgreSQL, MongoDB, Neo4j. Cuando se dice "usamos PostgreSQL", se habla del programa; la "base de datos" son los datos que guarda.

### 1.1 Las cuatro operaciones básicas (CRUD)

| Letra | Operación | Ejemplo de panadería |
|---|---|---|
| **C**reate | Crear | Registrar un cliente nuevo |
| **R**ead | Leer | Consultar los pedidos de Marta |
| **U**pdate | Actualizar | Cambiar el precio del croissant |
| **D**elete | Borrar | Eliminar un producto descontinuado |

### 1.2 Excel vs. base de datos

| | Hoja de cálculo | Base de datos |
|---|---|---|
| **Usuarios a la vez** | Pocos, con riesgo de pisarse | Muchos, de forma controlada |
| **Volumen** | Se vuelve lenta con muchos datos | Preparada para millones |
| **Errores** | Nada impide escribir "abc" en un precio | **Reglas** que rechazan datos inválidos |
| **Relaciones** | Se copian datos entre hojas | Se conectan tablas por claves |
| **Seguridad** | Acceso al archivo completo | Permisos por usuario y por dato |
| **Programas que la usan** | Difícil de automatizar | Pensada para ser usada por programas y por IA |

---

## 2. ¿Cómo se Guardan los Datos en un Servidor? (Explicación Breve)

### 2.1 La idea general

Una base de datos es, en el fondo, **archivos en un disco**, administrados por un **programa que está siempre en ejecución** (el servidor de base de datos) y que atiende pedidos de otros programas.

```
TU APLICACIÓN / PÁGINA WEB / AGENTE DE IA
        │   "dame los pedidos de Marta"   (por la red, a un puerto)
        ▼
┌─────────────────────────────────────────────┐
│        PROGRAMA SERVIDOR DE BASE DE DATOS    │
│  1. Revisa permisos (¿quién pregunta?)       │
│  2. Interpreta la consulta (SQL u otra)      │
│  3. Busca primero en la MEMORIA (caché)      │
│  4. Si no está, lee del DISCO                │
│  5. Devuelve el resultado                    │
└──────────┬───────────────────────┬──────────┘
           ▼                       ▼
   ARCHIVOS DE DATOS         REGISTRO DE CAMBIOS
   (tablas e índices,        (log: anota cada cambio
    en el disco)              ANTES de aplicarlo)
```

### 2.2 Las piezas, en palabras simples

| Pieza | Qué es | Analogía |
|---|---|---|
| **Archivos en disco** | Donde los datos viven de forma permanente, divididos en bloques ("páginas") | El archivo físico de una oficina |
| **Memoria (caché)** | Copia de lo más usado, en RAM, para responder más rápido | Los papeles que tenés sobre el escritorio |
| **Índices** | Estructuras auxiliares que permiten encontrar sin leer todo | El índice de un libro |
| **Registro de cambios (log)** | Cada modificación se anota antes de aplicarse, para recuperarse si se corta la luz | El cuaderno donde el contador anota antes de pasar al libro mayor |
| **Transacciones** | Un grupo de cambios que se aplican **todos o ninguno** | "O se cobra y se entrega el pan, o no pasa nada" |
| **Cliente y servidor** | El programa servidor espera pedidos; los clientes (tu app) los envían por la red | Un mostrador y sus clientes |
| **Puerto** | El "número de ventanilla" por el que el servidor atiende | Ventanilla número 5432 |
| **Cadena de conexión** | La dirección y las credenciales para entrar | Dirección + usuario + contraseña |
| **Réplicas y copias de seguridad** | Copias de los datos en otro lugar | Una fotocopia guardada en otra sucursal |

### 2.3 Dos formas de tener una base de datos

| | **Embebida (en un archivo)** | **Con servidor** |
|---|---|---|
| **Ejemplo** | SQLite | PostgreSQL, MySQL, MongoDB, Neo4j |
| **Cómo funciona** | Toda la base es **un archivo** dentro de tu aplicación, sin programa aparte | Un programa independiente, que atiende por la red |
| **Ventaja** | Cero instalación; ideal para aprender y apps pequeñas | Muchos usuarios a la vez, seguridad, escalado |
| **Límite** | Pensada para un uso más reducido y local | Hay que instalarla, configurarla y mantenerla |

> **En los ejemplos de esta clase:** al ejecutar `01_sql_panaderia.py` se crea `panaderia.db`, un archivo de unos 36 KB que contiene toda la base. Esa es la idea de "base embebida".

### 2.4 Dónde corre el servidor

- **En tu computadora (local):** para desarrollar y practicar.
- **En un servidor propio:** una máquina que administrás vos.
- **En la nube (servicio administrado):** otra empresa la instala, la actualiza y hace las copias. Pagás por uso.

### 2.5 Puertos habituales

| Programa | Puerto por defecto (típico) |
|---|---|
| PostgreSQL | 5432 |
| MySQL | 3306 |
| MongoDB | 27017 |
| Redis | 6379 |
| Neo4j (conexión de programas) | 7687 |

> Verificá estos números en la documentación de cada programa antes de configurarlos.

### 2.6 Lo que protege los datos en un servidor

1. **Contraseñas y permisos** por usuario y por tabla.
2. **Cifrado** en el disco y en el viaje por la red.
3. **Copias de seguridad** probadas (una copia que nunca se restauró no es una copia).
4. **Credenciales fuera del código** (archivo `.env`, nunca en GitHub; clase de Git).

---

## 3. Los Lenguajes de las Bases de Datos

Cada tipo de base de datos "habla" un lenguaje distinto. **La misma pregunta se escribe diferente según la base.**

**Pregunta de ejemplo: "¿Cuántos croissants se vendieron?"**

| Tipo | Lenguaje | Cómo se escribe (ilustrativo) |
|---|---|---|
| **SQL (relacional)** | **SQL** | `SELECT SUM(cantidad) FROM detalle_pedido WHERE producto_id = 2;` |
| **Documentos** | Consultas en formato de documento (JSON) | Se filtran documentos con `producto: "Croissant"` y se suman las cantidades |
| **Clave-valor** | Comandos simples | `GET ventas:croissant` |
| **Grafos** | **Cypher** / **GQL** | `MATCH (:Cliente)-[c:COMPRO]->(:Producto {nombre:'Croissant'}) RETURN sum(c.cantidad)` |
| **Vectorial** | Búsqueda por similitud (con una API o con SQL en algunos casos) | "Dame los 3 elementos más parecidos en significado a este vector" |

### 3.1 SQL: las tres familias de instrucciones

| Familia | Qué hace | Ejemplos |
|---|---|---|
| **DDL** (definir) | Crea la estructura | `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE` |
| **DML** (manipular) | Cambia los datos | `INSERT`, `UPDATE`, `DELETE` |
| **DQL** (consultar) | Lee los datos | `SELECT ... FROM ... WHERE ... JOIN ... GROUP BY` |

### 3.2 Un dato sobre grafos

En 2024 se publicó **GQL** (ISO/IEC 39075), el primer lenguaje de consulta estándar de ISO para grafos desde que se estandarizó SQL. Está basado en gran medida en **Cypher** (el lenguaje de Neo4j) y funciona con el mismo estilo `MATCH ... RETURN`. No confundir **GQL** (consultar bases de grafos) con **GraphQL** (un lenguaje para construir APIs): no están relacionados.

---

## 4. Los Cuatro Tipos de Bases de Datos

### 4.1 SQL (relacionales): "el archivador con fichas conectadas"

**Cómo guarda:** en **tablas** (filas y columnas) con estructura definida de antemano. Las tablas se conectan mediante **claves**.

**Analogía:** varios Excel con reglas estrictas, donde la hoja "Pedidos" no repite el nombre del cliente: apunta a su número en la hoja "Clientes".

| Fortalezas | Límites |
|---|---|
| Datos consistentes y validados | Estructura rígida: cambiarla exige planificar |
| Consultas muy potentes (cruzar tablas) | Crecer a volúmenes enormes en muchos servidores es más complejo |
| Transacciones seguras (ACID) | Poco natural para datos muy irregulares |
| Lenguaje estándar (SQL) | |

**Cuándo usarla:** pedidos, clientes, facturas, inventario, contabilidad, cualquier dato donde **la exactitud y las relaciones importan**.

### 4.2 NoSQL: "lo que no es una tabla"

"NoSQL" no es un único tipo: es un **grupo** de bases con modelos distintos. Los dos más usados:

#### a) Documentos

**Cómo guarda:** cada registro es un **documento** (como un archivo JSON) que contiene todo junto, incluso datos anidados. Cada documento puede tener campos distintos.

**Analogía:** una carpeta por cada pedido, con todo adentro: el cliente, los productos y las notas.

```json
{
  "_id": 1,
  "cliente": {"nombre": "Marta", "telefono": "0991111111"},
  "fecha": "2026-10-01",
  "items": [
    {"producto": "Baguette", "cantidad": 2, "precio": 2.50},
    {"producto": "Croissant", "cantidad": 4, "precio": 1.80}
  ],
  "nota": "Entregar antes de las 8"
}
```

**Cuándo usarla:** catálogos con productos de atributos muy distintos, perfiles de usuario, contenido, datos que cambian de forma seguido.

#### b) Clave-valor

**Cómo guarda:** un valor asociado a una **clave**, como un casillero con llave. Muy rápido; las claves pueden **caducar** solas.

**Cuándo usarla:** caché, sesiones de usuario, contadores, datos temporales (por ejemplo, "el menú del día" durante 1 hora).

#### Otros NoSQL que conviene reconocer

| Tipo | Uso típico |
|---|---|
| **Columnares / de columna ancha** | Volúmenes gigantes con escrituras constantes (registros, sensores) |
| **Series de tiempo** | Datos que llegan con fecha y hora (mediciones, métricas) |
| **Motores de búsqueda de texto** | Buscar palabras en documentos (tipo buscador) |

| Fortalezas | Límites |
|---|---|
| Flexibles: no exigen una estructura fija | Más libertad significa más riesgo de datos desordenados |
| Fáciles de escalar en muchos servidores | Las relaciones entre datos son menos naturales |
| Muy rápidas en su especialidad | Cada tipo se especializa en pocas cosas |

### 4.3 Grafos: "el mapa de relaciones"

**Cómo guarda:** **nodos** (las cosas: personas, productos) y **relaciones** (las conexiones: "COMPRÓ", "ES AMIGO DE"). Las relaciones son **ciudadanas de primera clase**: se guardan directamente.

**Analogía:** un árbol genealógico o la red de contactos de una red social.

```
(Marta)──COMPRÓ──►(Croissant)◄──COMPRÓ──(Luis)──COMPRÓ──►(Éclair)
   └──AMIGO_DE──►(Ana)──COMPRÓ──►(Pan de masa madre)
```

| Fortalezas | Límites |
|---|---|
| Preguntas sobre **conexiones** y **caminos** | Menos adecuadas para cálculos tabulares masivos |
| Recomendaciones, detección de fraude, redes | Hay que pensar bien qué es nodo y qué es relación |
| Muy útiles para dar **contexto estructurado** a la IA (GraphRAG, memoria con grafos) | Ecosistema más pequeño que el de SQL |

**Cuándo usarla:** "¿quiénes compraron lo mismo que Marta y qué más compraron?", redes de contactos, conocimiento conectado, memoria de un agente.

### 4.4 Vectoriales: "la biblioteca ordenada por significado"

**Cómo guarda:** cada texto (o imagen) se convierte con un **modelo de embeddings** en una **lista de números** (un **vector**) que representa su **significado**. Textos con significado parecido tienen vectores cercanos. La base guarda el vector, el texto original y datos extra (metadatos).

**Analogía:** un bibliotecario que ordena los libros no por título, sino por **de qué tratan**. Si le pedís "algo dulce para el postre", te trae los libros cercanos aunque ninguno diga "postre".

```
"algo dulce para el postre"  ──► [0.8, 0.0, 0.1, 0.1]
Tarta de manzana              ──► [0.9, 0.0, 0.0, 0.2]   ← muy cercano
Café americano                ──► [0.0, 0.0, 0.9, 0.9]   ← lejano
```

(En la práctica los vectores tienen cientos o miles de números, generados automáticamente.)

**Cómo busca:** compara el vector de la pregunta con los guardados usando una medida de cercanía (por ejemplo, la **similitud coseno**), y para hacerlo rápido con millones de vectores usa **índices de vecinos aproximados** (ANN, como HNSW).

| Fortalezas | Límites |
|---|---|
| Busca por **significado**, no por palabras exactas | Es **aproximada**: puede traer algo no relevante |
| Base de **RAG** (la IA responde con tus documentos) | No reemplaza a una base SQL: no es buena para "datos exactos" |
| Encuentra contenido similar aunque use otras palabras | La calidad depende del modelo de embeddings y de cómo se dividen los textos |

**Cuándo usarla:** responder preguntas sobre tus documentos (RAG), buscar recetas o preguntas frecuentes parecidas, recomendaciones por similitud.

---

## 5. Los Programas Principales de Cada Tipo

> Estas listas muestran los programas más conocidos al momento de preparar la clase. El panorama cambia: verificá estado y licencia antes de decidir.

| Tipo | Programas principales | Nota |
|---|---|---|
| **SQL** | **PostgreSQL**, **MySQL / MariaDB**, **SQLite**, Microsoft SQL Server, Oracle | PostgreSQL y MySQL son de código abierto muy extendidos. SQLite es embebida |
| **Documentos** | **MongoDB**, Firestore (Google), CouchDB | MongoDB es el más conocido |
| **Clave-valor** | **Redis**, DynamoDB (AWS), Memcached | Redis es el estándar para caché |
| **Grafos** | **Neo4j**, Amazon Neptune, ArangoDB, Memgraph | Neo4j es el más difundido; ArangoDB es "multimodelo" (documentos, clave-valor y grafos) |
| **Vectoriales** | **Qdrant**, **Chroma**, **Pinecone**, **Weaviate**, **Milvus**, **pgvector**, LanceDB | Ver comparación abajo |

### 5.1 Vectoriales: cuándo se suele recomendar cada uno

| Programa | Perfil habitual |
|---|---|
| **Chroma** | Prototipos y aprendizaje; fácil de usar de forma local |
| **pgvector** | Una **extensión de PostgreSQL**. Si ya usás PostgreSQL, es la opción de menor fricción |
| **Qdrant** | Código abierto, de buen rendimiento, filtrado por metadatos, fácil de autoalojar |
| **Pinecone** | Servicio administrado: casi sin mantenimiento, pero es de pago y no es de código abierto |
| **Weaviate** | Búsqueda híbrida (palabras + significado) |
| **Milvus** | Escala muy grande (miles de millones de vectores); más complejo de operar |

> **Regla práctica citada en varias guías de 2026:** si ya trabajás con PostgreSQL y tenés hasta unos pocos millones de vectores, **pgvector suele alcanzar**. Es una orientación de la industria, no una ley: probalo con tus datos.

> **Dato de aclaración:** **FAISS** es una **biblioteca** de búsqueda por similitud, no una base de datos completa (no gestiona usuarios, copias ni persistencia por sí sola). La diferencia entre biblioteca, índice y base de datos importa.

---

## 6. Cómo Distinguir Cada Tipo (Tres Pruebas)

Ante cualquier proyecto, hacé estas tres preguntas.

### Prueba 1: ¿Qué forma tienen mis datos?

| Si mis datos son... | Pienso en... |
|---|---|
| Filas y columnas con campos fijos (cliente, producto, precio) | **SQL** |
| "Carpetas" con contenido variable y anidado | **Documentos** |
| Pares simples "etiqueta → valor" que se consultan por la etiqueta | **Clave-valor** |
| Cosas **conectadas** entre sí, donde las conexiones son el tema | **Grafos** |
| Textos o imágenes que quiero buscar por **significado** | **Vectorial** |

### Prueba 2: ¿Qué pregunta voy a hacer más seguido?

| Pregunta típica | Tipo |
|---|---|
| "Sumá, agrupá, filtrá y cruzá datos exactos" | SQL |
| "Dame todo lo del pedido 1 de una vez" | Documentos |
| "Dame ya el valor de esta clave" | Clave-valor |
| "¿Cómo se relacionan A y B? ¿Qué más compraron quienes compraron esto?" | Grafos |
| "¿Qué documento habla de algo parecido a esto?" | Vectorial |

### Prueba 3: ¿Cuánto me importa la exactitud?

| Necesidad | Qué implica |
|---|---|
| **Dinero, inventario, facturas:** nada puede perderse ni duplicarse | **SQL con transacciones** (propiedades **ACID**: todo o nada, coherente, aislado, durable) |
| **Velocidad y volumen** más que perfección absoluta | NoSQL o caché |
| **Relevancia "suficientemente buena"** | Vectorial (siempre aproximada) |

### 6.1 Pistas rápidas en la vida real

| Si escuchás... | Probablemente es... |
|---|---|
| "tabla", "JOIN", "clave foránea" | SQL |
| "colección", "documento", "JSON" | Documentos |
| "caché", "sesión", "TTL" | Clave-valor |
| "nodo", "relación", "Cypher" | Grafos |
| "embedding", "similitud", "RAG", "top-k" | Vectorial |

---

## 7. Cómo Escoger una Base de Datos

### 7.1 La regla de partida

> **Empezá simple.** Para la gran mayoría de proyectos pequeños y medianos, **SQLite (para empezar) o PostgreSQL** es la elección correcta. Se agrega otro tipo solo cuando aparece una necesidad que SQL no resuelve bien.

### 7.2 Árbol de decisión

```
¿Mis datos tienen estructura clara y relaciones (clientes, pedidos)?
   └─ Sí ──► SQL (SQLite para aprender, PostgreSQL para algo serio)
   └─ No / es muy variable ──► ¿Es un conjunto de documentos flexibles? ──► Documentos

¿Necesito una respuesta instantánea a datos temporales?
   └─ Sí ──► Clave-valor (caché)

¿Lo importante son las CONEXIONES entre cosas?
   └─ Sí ──► Grafos

¿Necesito que una IA encuentre textos por SIGNIFICADO?
   └─ Sí ──► Vectorial  (¿ya usás PostgreSQL? Probá pgvector primero)
```

### 7.3 Criterios de decisión

| Criterio | Preguntas a hacerte |
|---|---|
| **Forma de los datos** | ¿Tabla, documento, grafo, vector? |
| **Preguntas frecuentes** | ¿Qué consulta es la más importante del negocio? |
| **Exactitud** | ¿Un dato perdido o duplicado cuesta dinero? |
| **Volumen y crecimiento** | ¿Miles, millones, miles de millones de registros? |
| **Equipo y mantenimiento** | ¿Quién la va a administrar? ¿Prefiero un servicio administrado? |
| **Costo** | ¿Código abierto autoalojado o servicio de pago? |
| **Privacidad** | ¿Contiene datos personales? ¿Dónde se guarda? (Clase 2) |

### 7.4 Ejemplo: la panadería con varios tipos a la vez

En un proyecto real es común **combinar** varios tipos, cada uno para lo que hace mejor (se llama *persistencia políglota*):

| Necesidad de la panadería | Base elegida | Por qué |
|---|---|---|
| Clientes, productos, pedidos, facturas | **SQL (PostgreSQL)** | Exactitud, relaciones, transacciones |
| "El menú del día" que se consulta miles de veces | **Clave-valor (Redis)** | Respuesta instantánea y caduca sola |
| Catálogo de productos con atributos muy distintos | **Documentos (MongoDB)** o columnas flexibles en SQL | Flexibilidad |
| "Quienes compraron esto también compraron..." | **Grafos (Neo4j)** | Recomendaciones por conexiones |
| Asistente que responde preguntas sobre recetas y políticas | **Vectorial (pgvector, Qdrant o Chroma)** | Búsqueda por significado (RAG) |

> **Cuidado con la sobreingeniería:** una panadería pequeña probablemente necesite **solo la primera fila**. Agregar tipos de base de datos "porque están de moda" suma costo, mantenimiento y puntos de falla sin beneficio.

### 7.5 Errores de elección frecuentes

| Error | Consecuencia |
|---|---|
| Elegir por moda ("todos usan vectoriales") | Complejidad sin necesidad |
| Usar una base vectorial para datos exactos | Resultados aproximados donde se necesitaba exactitud |
| Guardar dinero o inventario en una base sin transacciones | Datos inconsistentes |
| Usar SQL para todo, incluida la búsqueda por significado | Búsquedas pobres |
| No pensar en el crecimiento ni en las copias de seguridad | Problemas cuando ya es tarde |

---

## 8. Modelado de Bases de Datos

> **Modelar** es diseñar cómo se organizan los datos **antes** de crear nada. Es como hacer el plano antes de construir la casa.

### 8.1 Los pasos del modelado

1. **Identificar las entidades:** las "cosas" del negocio (Cliente, Producto, Pedido).
2. **Definir los atributos** de cada una (nombre, precio, fecha).
3. **Definir las relaciones** entre entidades.
4. **Definir la cardinalidad:** cuántos de un lado se relacionan con cuántos del otro.
5. **Elegir las claves** que identifican cada registro.
6. **Definir reglas** (restricciones) y **tipos de datos**.
7. **Pensar los índices** según las consultas frecuentes.

### 8.2 Relaciones y cardinalidad

| Tipo | Significa | Ejemplo |
|---|---|---|
| **Uno a uno (1:1)** | Un registro con uno solo del otro lado | Un cliente tiene un perfil |
| **Uno a muchos (1:N)** | Un registro con muchos del otro lado | **Un cliente hace muchos pedidos** |
| **Muchos a muchos (N:M)** | Muchos con muchos; requiere una **tabla puente** | **Un pedido tiene muchos productos y un producto está en muchos pedidos** |

### 8.3 Diagrama entidad-relación de la panadería

```
 CLIENTES                 PEDIDOS                 DETALLE_PEDIDO             PRODUCTOS
┌──────────────┐        ┌──────────────┐        ┌────────────────┐        ┌──────────────┐
│ id  (PK)     │1      N│ id  (PK)     │1      N│ pedido_id (FK) │N      1│ id  (PK)     │
│ nombre       │────────│ cliente_id(FK)│────────│ producto_id(FK)│────────│ nombre       │
│ telefono     │        │ fecha        │        │ cantidad       │        │ precio       │
└──────────────┘        └──────────────┘        └────────────────┘        └──────────────┘
```

- **PK** (clave primaria): identifica de forma única cada fila.
- **FK** (clave foránea): apunta a la clave primaria de otra tabla.
- **DETALLE_PEDIDO** es la **tabla puente** que resuelve la relación muchos a muchos.

### 8.4 El mismo modelo en SQL

```sql
CREATE TABLE clientes (
    id       INTEGER PRIMARY KEY,
    nombre   TEXT NOT NULL,
    telefono TEXT UNIQUE
);
CREATE TABLE productos (
    id     INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL UNIQUE,
    precio REAL NOT NULL CHECK (precio > 0)
);
CREATE TABLE pedidos (
    id         INTEGER PRIMARY KEY,
    cliente_id INTEGER NOT NULL REFERENCES clientes(id),
    fecha      TEXT NOT NULL
);
CREATE TABLE detalle_pedido (
    pedido_id   INTEGER NOT NULL REFERENCES pedidos(id),
    producto_id INTEGER NOT NULL REFERENCES productos(id),
    cantidad    INTEGER NOT NULL CHECK (cantidad > 0),
    PRIMARY KEY (pedido_id, producto_id)
);
```

Este modelo se ejecuta y se prueba en `01_sql_panaderia.py`. Allí se comprueba que la base **rechaza** un pedido de un cliente inexistente, un precio negativo y un teléfono repetido.

### 8.5 Normalización: no repetir datos

**Mal diseño (todo en una sola tabla):**

| pedido | cliente | teléfono | producto | precio | cantidad |
|---|---|---|---|---|---|
| 1 | Marta | 0991111111 | Baguette | 2.50 | 2 |
| 1 | Marta | 0991111111 | Croissant | 1.80 | 4 |
| 2 | Marta | 0991111111 | Pan de masa madre | 6.00 | 1 |

**Problemas:** el teléfono de Marta está repetido tres veces. Si cambia, hay que modificarlo en todas las filas, y si se olvida una, los datos se contradicen.

**Regla simple:** cada dato se guarda **una sola vez**, en el lugar al que pertenece, y los demás lugares **apuntan** a él con una clave. Eso es lo que hace el modelo de las cuatro tablas.

| Forma normal | Idea en palabras simples |
|---|---|
| **1FN** | Un valor por celda; nada de listas dentro de una celda |
| **2FN** | Cada dato depende de la clave completa |
| **3FN** | Cada dato depende solo de la clave, no de otro dato |

### 8.6 Modelado en los otros tipos

| Tipo | Cómo se modela | Principio |
|---|---|---|
| **Documentos** | Un documento por cada "unidad de consulta" | **Embeber** (guardar junto) lo que se consulta junto; **referenciar** lo que se comparte o cambia mucho |
| **Clave-valor** | Diseñar bien los **nombres de claves** (`menu:2026-10-28`) | La clave es la única forma de buscar |
| **Grafos** | **Sustantivos = nodos; verbos = relaciones; datos = propiedades** | Cliente `COMPRÓ` Producto; la cantidad es una propiedad de la relación |
| **Vectoriales** | Registro = **vector + texto original + metadatos** (fuente, fecha, categoría, permisos) | La calidad depende de cómo se **dividen los textos en fragmentos** (chunks) |

### 8.7 Modelado vectorial: un registro típico

```
id:        "receta-042-frag-3"
vector:    [0.021, -0.113, 0.874, ...]     ← lo genera el modelo de embeddings
texto:     "Para la masa madre, mezclar 100 g de harina..."
metadatos: {fuente: "recetario.pdf", pagina: 12, categoria: "masas", publico: true}
```

Los **metadatos** permiten filtrar ("solo documentos públicos", "solo de 2026") y conectan con la gobernanza de datos del taller.

### 8.8 Errores de modelado frecuentes

| Error | Consecuencia |
|---|---|
| Repetir datos en muchos lugares | Inconsistencias |
| No definir claves ni restricciones | Datos inválidos entran a la base |
| Modelar sin pensar en las consultas | Consultas lentas o imposibles |
| Guardar varios valores en una celda ("pan, café, torta") | Imposible buscar y contar bien |
| Nombres confusos (`dato1`, `x`) | Nadie entiende la base en seis meses |
| Poner nombres de relaciones inconsistentes en un grafo (`AMIGO_DE` y `AMIGA_DE`) | Las consultas no encuentran todo |

---

## 9. Seguridad y Privacidad de los Datos

Conecta con las clases de privacidad y de Git.

| Tema | Regla |
|---|---|
| **Inyección SQL** | **Nunca** armar consultas pegando texto del usuario. Usar **parámetros** |
| **Credenciales** | Nunca en el código ni en GitHub: archivo `.env` ignorado por Git |
| **Permisos** | Cada usuario o programa accede solo a lo que necesita |
| **Datos personales** | Guardar solo lo necesario; anonimizar cuando se pueda |
| **Copias de seguridad** | Automáticas y **probadas** (restaurar al menos una vez) |
| **Respuestas de IA** | Si una IA escribe consultas por vos, revisá cada una antes de ejecutarla |

### 9.1 La inyección SQL, demostrada

Es el equivalente en bases de datos de la inyección de prompts que viste en la clase de seguridad. En `01_sql_panaderia.py`:

```python
entrada = "x' OR '1'='1"

# INSEGURO: pegar el texto dentro de la consulta
con.execute(f"SELECT nombre FROM clientes WHERE nombre = '{entrada}'")
# Resultado: ['Marta', 'Luis', 'Ana']  -> ¡devolvió TODOS los clientes!

# SEGURO: usar un parámetro (?)
con.execute("SELECT nombre FROM clientes WHERE nombre = ?", (entrada,))
# Resultado: []  -> trata el texto como un dato, no como una orden
```

> **Por qué importa con IA:** los asistentes a veces generan código con consultas armadas por concatenación de texto. **Es un error clásico.** Revisá que usen parámetros.

---

## 10. El Mapa Hacia el Resto del Taller

| Lo que viste hoy | Dónde se vuelve a usar |
|---|---|
| Base **vectorial** y embeddings | **RAG**: tu agente responde con tus propios documentos |
| Metadatos y permisos | **Gobernanza de datos**: quién puede ver qué fragmento |
| Base **de grafos** | **Memoria con grafos / GraphRAG**: memoria estructurada en relaciones |
| Base **SQL** | La fuente de datos "exacta" del agente (pedidos, precios, clientes) |
| Clave-valor | Memoria de corto plazo y caché de un agente |
| Modelado | Cada proyecto empieza por la hoja de papel y el modelo |

```
PIPELINE DE RAG (lo que vas a construir)
Documentos → dividir en fragmentos → embeddings → BASE VECTORIAL
Pregunta del usuario → embedding → búsqueda por similitud → fragmentos relevantes
→ se los das a la IA en el prompt → respuesta con fuentes
```

---

## 11. Práctica (con los ejemplos incluidos)

### Ejercicio 1 — Ejecutá y observá (15 min)
1. Descomprimí `ejemplos_bases_de_datos.zip` y abrí la carpeta en VSCode.
2. Ejecutá `python 01_sql_panaderia.py`. Leé cada bloque de la salida: consultas, integridad, transacción, inyección e índice.
3. Ejecutá los otros tres y respondé: ¿qué tipo de pregunta resuelve cada uno mejor?

### Ejercicio 2 — Modelá tu propio negocio (25 min)
1. En papel: listá las **entidades**, sus **atributos** y las **relaciones** de tu negocio o de tu casa (por ejemplo, un taller de costura: Clientes, Servicios, Pedidos).
2. Dibujá el diagrama y marcá la cardinalidad (1:N, N:M).
3. Identificá qué relación necesita una **tabla puente**.

### Ejercicio 3 — Pasalo a SQL con ayuda de la IA y verificalo (20 min)

Plantilla de prompt:

```
Actúa como un diseñador de bases de datos senior.

Contexto: mi negocio es {NEGOCIO}. Las entidades son {ENTIDADES}.
Las relaciones son {RELACIONES}.

Tarea: diseñá un esquema SQL para SQLite con claves primarias, claves foráneas,
restricciones (NOT NULL, UNIQUE, CHECK) y una tabla puente para cada relación
muchos a muchos.

Restricciones:
- No repitas datos (normalizá hasta 3FN).
- Explicá en una línea por qué elegiste cada tabla.
- Agregá 3 filas de ejemplo por tabla y 3 consultas útiles, usando parámetros (?).
- Si algo no está claro, preguntame antes de diseñar.
```

**Verificación (no confíes a ciegas, Clase 6):**
- [ ] ¿Cada tabla tiene clave primaria?
- [ ] ¿Las relaciones N:M tienen tabla puente?
- [ ] ¿Hay datos repetidos que deberían estar en otra tabla?
- [ ] ¿Las consultas usan parámetros y no concatenan texto?
- [ ] Ejecutalo en SQLite: ¿corre sin errores y rechaza datos inválidos?

### Ejercicio 4 — Elegí la base (10 min)
Para tu proyecto, completá:

| Necesidad | Prueba 1 (forma) | Prueba 2 (pregunta) | Prueba 3 (exactitud) | Tipo elegido | ¿Por qué? |
|---|---|---|---|---|---|
| | | | | | |

---

## 12. Plan de la Sesión (2 horas)

| Min | Bloque | Qué hacemos |
|---|---|---|
| 0-10 | **Qué es una base de datos** | Excel vs. base de datos, CRUD |
| 10-25 | **Cómo se guardan los datos en un servidor** | El diagrama, las piezas, embebida vs. servidor |
| 25-55 | **Los cuatro tipos y sus lenguajes** | Analogías, ejemplo de cada uno, ejecutar los scripts 01 a 04 |
| 55-70 | **Programas, distinguir y escoger** | Las tres pruebas, el árbol de decisión, el caso de la panadería |
| 70-95 | **Modelado** | Entidades y relaciones, diagrama, normalización, ejercicio 2 |
| 95-110 | **IA y verificación** | Ejercicio 3, inyección SQL |
| 110-120 | **Cierre** | Mapa hacia RAG, tarea |

---

## Mini Glosario

| Término | En palabras simples |
|---|---|
| **Base de datos** | Datos organizados que se pueden buscar, cambiar y proteger |
| **SGBD** | El programa que administra la base (PostgreSQL, MongoDB...) |
| **Tabla / fila / columna** | La hoja, cada registro y cada campo |
| **Clave primaria (PK)** | Lo que identifica de forma única cada fila |
| **Clave foránea (FK)** | Un dato que apunta a la fila de otra tabla |
| **JOIN** | Unir tablas por sus claves en una consulta |
| **Índice** | Atajo para encontrar datos sin leer todo |
| **Transacción** | Cambios que se aplican todos o ninguno |
| **ACID** | Las garantías de una transacción segura |
| **Nodo / relación** | Una cosa / una conexión entre cosas (grafos) |
| **Embedding / vector** | Lista de números que representa el significado de un texto |
| **Similitud coseno** | Medida de qué tan cercanos son dos vectores |
| **ANN** | Búsqueda aproximada de vecinos cercanos, para ser rápida con millones |
| **Chunk** | Fragmento de un documento que se convierte en vector |
| **Metadatos** | Datos sobre los datos (fuente, fecha, permisos) |
| **Inyección SQL** | Ataque que aprovecha consultas armadas pegando texto del usuario |

---

## Tarea

1. Completá el modelo de **tu propio negocio**: entidades, relaciones, diagrama y tabla puente.
2. Implementalo en **SQLite** (con ayuda de la IA, verificando con el checklist) y guardá el archivo `.sql` en tu repositorio de GitHub.
3. Escribí **3 consultas** con parámetros: una con `JOIN`, una con `GROUP BY` y una con filtro por fecha.
4. Respondé por escrito: ¿en qué parte de tu proyecto usarías una base **vectorial** y en cuál una de **grafos**? ¿O no hace falta ninguna?
5. **Traé a la próxima clase:** el enlace al repositorio, el diagrama y tu tabla de decisión.

---

## Cierre

### Lo que aprendimos hoy

1. Una base de datos es un **sistema** que guarda, busca y protege información; sus datos viven en **archivos en un disco** administrados por un programa.
2. Hay **cuatro familias principales**: SQL, NoSQL (documentos y clave-valor), grafos y vectoriales. Cada una responde mejor a un tipo de pregunta.
3. Cada tipo tiene **su lenguaje**: SQL, consultas de documentos, comandos clave-valor, Cypher/GQL y búsqueda por similitud.
4. Se distinguen y se eligen con **tres pruebas**: forma de los datos, pregunta más frecuente y necesidad de exactitud.
5. **Empezá simple** (SQLite o PostgreSQL) y combiná tipos solo cuando haya una necesidad real.
6. **Modelar antes de construir:** entidades, relaciones, claves, restricciones y no repetir datos.
7. **Las bases vectoriales** son la base de RAG; **los grafos**, de la memoria estructurada; **SQL**, de los datos exactos.
8. **Seguridad:** parámetros en las consultas, credenciales fuera del código, permisos y copias probadas.

---

> **Recordá:** la mejor base de datos es la que se ajusta a la forma de tus datos y a tus preguntas. Elegirla bien, y modelarla antes de usarla, ahorra más trabajo que cualquier herramienta.

---

