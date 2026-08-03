# Glosario — Clase 7: Bases de Datos para IA

> Cada término con su definición en lenguaje simple y una analogía cotidiana.

---

## A

### ACID
**Qué es:** Conjunto de 4 garantías (Atomicidad, Consistencia, Aislamiento, Durabilidad) que aseguran que las transacciones en bases de datos SQL nunca fallen a medias.

**Analogía:** Un cajero automático. Si sacás plata y se corta la luz justo cuando está contando los billetes, el banco no te descuenta plata que no recibiste. La operación entera falla o se completa, nunca queda a medias.

### API Key
**Qué es:** Una contraseña larguísima que te identifica como usuario autorizado para usar un servicio (como Google Gemini o un proveedor de bases de datos).

**Analogía:** La llave electrónica de un hotel. Abre tu habitación y nada más. Si la perdés, cualquiera puede entrar. Por eso NUNCA se sube a GitHub (va en el `.env`).

### Arquitectura Poliglota
**Qué es:** Sistema que usa varios tipos de bases de datos al mismo tiempo, cada una especializada en una tarea distinta.

**Analogía:** Un restaurante. La cocina no tiene un solo electrodoméstico. Tiene horno (para pizzas), freidora (para papas) y freezer (para helados). En IA es igual: PostgreSQL para seguridad, ChromaDB para búsqueda semántica, Redis para velocidad.

---

## B

### Base de Datos
**Qué es:** Sistema que organiza, guarda y recupera información de forma ultrarrápida, sin importar cuántos datos tengas.

**Analogía:** El sistema de logística de un almacén de Amazon. No importa si hay 100 productos o 100 millones, el sistema sabe exactamente dónde está cada uno y te lo entrega en 0.003 segundos.

### Base de Datos Relacional (SQL)
**Qué es:** Base de datos organizada en tablas (como hojas de Excel) con columnas fijas y reglas estrictas. Las tablas se conectan entre sí mediante "llaves" (IDs). Habla el idioma SQL.

**Analogía:** Un archivero de metal con cajones perfectamente etiquetados. Si intentás meter una carpeta de tamaño oficio en un cajón de tamaño carta, no te deja. Todo está medido al milímetro.

### Base de Datos NoSQL (Documentos)
**Qué es:** Base de datos que guarda "documentos" (en formato JSON) donde cada uno puede tener una estructura completamente distinta. Flexibilidad total, sin reglas estrictas.

**Analogía:** Una caja de cartón. Hoy metés un libro, mañana una laptop, pasado mañana 5 manzanas. No hay reglas. Es flexible y rápido, pero difícil de organizar para búsquedas complejas.

### Base de Datos Clave-Valor
**Qué es:** La forma más simple de base de datos. Cada dato tiene una CLAVE única (como una etiqueta) y un VALOR (el contenido). Solo busca por clave exacta. Vive en RAM, por eso es brutalmente rápida.

**Analogía:** Un diccionario. Buscás "Gato" → "Mamífero felino". Si buscás "Ga..." no encuentra nada. Si buscás "minino" tampoco. Solo funciona con la clave exacta.

### Base de Datos Vectorial (Vector DB)
**Qué es:** Base de datos que convierte texto (o imágenes, audio) en matemáticas (vectores) y busca por SIGNIFICADO, no por palabras exactas.

**Analogía:** Buscar por "olor" o "color". Si buscás algo que "huela a cítrico y sea amarillo", te devuelve una naranja, aunque no supieras la palabra "naranja".

---

## C

### Cache / Caché
**Qué es:** Memoria ultrarrápida que guarda respuestas ya calculadas para no tener que recalcularlas cada vez.

**Analogía:** El menú del día pegado en la pared de un restaurante. En lugar de que el mozo le explique a cada cliente los 20 platos disponibles (20 minutos), el cliente lee el cartel y pide en 10 segundos. Redis es ese cartel.

### ChromaDB
**Qué es:** Base de datos vectorial open source, escrita en Python. La más fácil de usar para empezar con búsqueda semántica y RAG.

**Analogía:** El "Word" de las bases de datos vectoriales. Simple, gratuito, y hacés el 90% de lo que necesitás sin complicaciones.

### Chunk / Chunking
**Qué es:** Técnica de dividir un documento largo en pedazos (chunks) más pequeños antes de guardarlos en una base de datos vectorial.

**Analogía:** Una pizza. No te la comés entera. La cortás en porciones (chunks) para digerirla mejor. La base de datos vectorial hace lo mismo con tus PDFs: los corta en pedazos de ~500 palabras antes de guardarlos.

---

## D

### DBA (Database Administrator)
**Qué es:** El profesional que administra físicamente los servidores de bases de datos: instalación, respaldos, rendimiento, seguridad.

**Analogía:** El administrador del almacén. No decide qué tipo de almacén construir (eso lo hace el ingeniero), pero se asegura de que las grúas funcionen, los estantes no se caigan y nadie robe la mercancía.

---

## E

### Embedding
**Qué es:** La representación matemática (vector de números) que captura el SIGNIFICADO de un texto, imagen o audio.

**Analogía:** El ADN de una palabra. Así como tu ADN te hace único y diferente a otros, el embedding de "perro" es distinto al de "gato". Pero "perro" y "can" tienen embeddings muy similares (mismo significado = ADN parecido).

### .env
**Qué es:** Archivo oculto donde guardamos las contraseñas y cadenas de conexión. NUNCA se sube a GitHub.

**Analogía:** La caja fuerte del proyecto. Contiene las llaves del almacén. Si alguien la roba, tiene acceso a TODO.

---

## J

### JSON (JavaScript Object Notation)
**Qué es:** Formato de texto estándar para guardar y transmitir datos. Usa llaves `{}` y pares clave-valor. Lo entienden humanos y máquinas.

**Analogía:** Una ficha de inscripción. Dice claramente "Nombre:", "Edad:", "Email:" y las respuestas. Fácil de leer para cualquiera.

---

## M

### MongoDB
**Qué es:** La base de datos NoSQL más popular del mundo. Guarda documentos en formato JSON/BSON. Flexible y escalable.

**Analogía:** Google Drive pero para datos. Puede guardar cualquier tipo de archivo sin importar su formato. Pero no es bueno para cálculos matemáticos complejos (para eso usás Excel/SQL).

### Mock
**Qué es:** Versión falsa de un servicio o base de datos que usamos durante las pruebas para no gastar recursos reales ni tocar datos reales.

**Analogía:** Un simulador de vuelo. Practicás aterrizar sin riesgo de estrellar un avión de verdad. Con mocks practicás consultar una base de datos sin riesgo de borrar datos reales.

---

## P

### Pinecone
**Qué es:** Base de datos vectorial como servicio en la nube (SaaS). No tenés que instalar nada, ellos administran todo. Ideal para empresas.

**Analogía:** Un servicio de valet parking. Dejás tu auto en la entrada y ellos lo estacionan, lo cuidan y te lo traen cuando lo necesitás. No te preocupás por nada.

### PostgreSQL
**Qué es:** Base de datos relacional open source, considerada la más potente del mundo. Cumple con ACID. Gratuita.

**Analogía:** El Ferrari del SQL. Potente, rápido, confiable, y no pagás un centavo por él.

---

## R

### RAG (Retrieval Augmented Generation)
**Qué es:** Técnica que combina una base de datos vectorial con una IA generativa. La base de datos busca la información relevante, y la IA la usa para responder preguntas con datos REALES (no alucinaciones).

**Analogía:** Un bibliotecario con superpoderes. El usuario pregunta algo, el bibliotecario (base vectorial) busca los libros correctos en segundos, y la IA los lee y responde usando información REAL de esos libros.

### Redis
**Qué es:** Base de datos clave-valor que vive en memoria RAM. Es la base de datos más rápida que existe (10,000x más rápida que PostgreSQL).

**Analogía:** Tu memoria a corto plazo. Recordás tu nombre al instante sin "buscarlo" en ningún lado. Redis hace lo mismo con datos que se preguntan muy seguido.

---

## S

### SQL (Structured Query Language)
**Qué es:** El idioma universal que hablan todas las bases de datos relacionales. Con comandos como SELECT, INSERT, UPDATE, DELETE.

**Analogía:** El inglés en el mundo de los negocios. No importa si estás en Japón o Brasil, si hablás inglés, te entendés. SQL es el "inglés" de las bases de datos.

---

## T

### Transacción
**Qué es:** Una operación que agrupa varios pasos y garantiza que o TODOS se completen o NINGUNO se complete. Fundamental para operaciones con dinero.

**Analogía:** Transferir plata entre dos cuentas: sacar de la cuenta A y poner en la cuenta B. Si falla alguno de los dos pasos, NINGUNO se hace. No existe "saqué plata de A pero no llegó a B".

---

## V

### Vector
**Qué es:** Lista de números que representa matemáticamente el SIGNIFICADO de un texto, imagen o audio.

**Analogía:** Las coordenadas GPS de una palabra en el espacio del significado. "Perro" tiene coordenadas (x=2, y=5, z=8). "Can" tiene coordenadas (x=2.1, y=5.2, z=7.9). Están en el mismo vecindario porque significan lo mismo.

### Variable de Entorno
**Qué es:** Dato que el sistema operativo guarda para todos los programas. Se usa para guardar configuraciones secretas SIN escribirlas en el código.

**Analogía:** Un cartel en la entrada del edificio que dice "La calefacción está a 22°C". Todos los departamentos (programas) pueden leer el cartel, pero ninguno lo modifica. Si viene un visitante (GitHub), no ve el cartel (está en `.env`).
