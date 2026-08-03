# Práctica — Clase 7: El Arquitecto de Datos

> Ejercicio práctico: Tomar decisiones de arquitectura de bases de datos para un proyecto real.

---

## 🎯 El Reto: Banco Digital con IA

### Contexto

Acaban de contratarte como **Arquitecto de Datos** para un banco digital que quiere implementar IA en su app. Te describen 3 módulos que necesitan construir. **Tu trabajo es decidir qué tipo de base de datos usar para cada uno**, y —más importante aún— explicar POR QUÉ.

No necesitas saber programar. Necesitas saber **pensar**.

---

## 📋 Los 3 Módulos

### Módulo 1: Login y Transferencias
> *"Necesitamos un sistema que permita a los usuarios iniciar sesión con usuario y contraseña, y transferir dinero entre cuentas. Si se corta la luz a la mitad de una transferencia de $10,000, el dinero NO puede perderse ni desaparecer."*

**Preguntas para pensar:**
- ¿Qué pasa si la operación falla a la mitad?
- ¿Necesito precisión absoluta o "aproximada"?
- ¿Los datos tienen siempre la misma estructura?

---

### Módulo 2: Chatbot que Lee Facturas (PDFs)
> *"Los usuarios suben fotos o PDFs de sus facturas y preguntan cosas como '¿Por qué me cobraron esta comisión?' o '¿Qué significa este cargo?'. El chatbot debe leer el PDF y responder basado en su contenido."*

**Preguntas para pensar:**
- ¿El usuario busca por palabra exacta o por significado?
- ¿Puedo buscar "cargo extraño" en un PDF que solo dice "comisión administrativa"?
- ¿Qué tipo de "inteligencia" necesita la búsqueda?

---

### Módulo 3: Promociones Diarias
> *"Todos los días a las 12:00 PM publicamos las promociones del día. Exactamente a esa hora, 10,000 usuarios abren la app y preguntan '¿Cuáles son las promociones de hoy?'. No podemos colapsar los servidores."*

**Preguntas para pensar:**
- ¿Cuántas veces se repite la misma pregunta?
- ¿Vale la pena llamar a una API de IA 10,000 veces para la misma respuesta?
- ¿Qué puedo hacer para responder más rápido y gastar menos?

---

## ✍️ Tu Tarea (Individual o en Parejas)

Para cada módulo, completá esta tabla:

| Módulo | Tipo de BD | ¿Por qué? (Escribí al menos 2 razones) |
|--------|------------|---------------------------------------|
| **1. Login y Transferencias** | | |
| **2. Chatbot lee PDFs** | | |
| **3. Promociones Diarias** | | |

### Opciones de Tipos de BD:
- [ ] Relacional (SQL): PostgreSQL, MySQL, SQLite
- [ ] NoSQL / Documentos: MongoDB, Firestore
- [ ] Clave-Valor: Redis, Memcached
- [ ] Vectorial: ChromaDB, Pinecone

---

## 🧠 Preguntas de Reflexión (para discutir en grupo)

1. **¿Qué pasaría si usara la misma base de datos (ej. solo PostgreSQL) para los 3 módulos?**
   ¿Funcionaría? ¿Cuáles serían los problemas?

2. **En el Módulo 2, ¿podría usar PostgreSQL para buscar en los PDFs?**
   ¿Por qué sí o por qué no?

3. **¿Cuánto dinero ahorraría Redis en el Módulo 3 si cada consulta a la API de IA cuesta $0.01?**
   Con 10,000 usuarios preguntando lo mismo al día.

4. **¿Qué otros ejemplos de la vida real se te ocurren donde aplicarías estos 4 tipos de bases de datos?**

---

## 🎯 La Respuesta Correcta (para discutir al final)

> **⚠️ NO LEAS ESTO hasta haber completado tu tabla. Intentá resolverlo primero por tu cuenta o discutiéndolo con un compañero. El aprendizaje está en el intento, no en la respuesta correcta.**

---

*(Espacio para que no veas la respuesta por accidente...)*

---

---

---

---

---

---

---

---

---

### Respuesta del Arquitecto de Datos

#### Módulo 1: Login y Transferencias → **Relacional (PostgreSQL/Microsoft SQL Server)**

**Razones:**

1. **ACID obligatorio:** El dinero no admite errores. Si transfiero $100 de Juan a María, y se corta la luz a la mitad, PostgreSQL garantiza que la operación entera falla (Juan mantiene sus $100) o se completa (María recibe sus $100). NUNCA queda a medias. Esto se llama transacción ACID.

2. **Datos estructurados y fijos:** Una cuenta bancaria SIEMPRE tiene número de cuenta, titular, saldo. Una transferencia SIEMPRE tiene origen, destino, monto, fecha. Son datos que no cambian de forma. SQL es perfecto porque espera estructuras fijas.

3. **Seguridad y auditoría:** Los bancos necesitan saber exactamente quién hizo qué, cuándo y desde dónde. SQL tiene 40+ años de madurez en seguridad y auditoría. MongoDB no tiene el mismo nivel de garantías transaccionales.

**¿Qué pasaría si usara MongoDB?** En 2018, una startup de fintech usó MongoDB para transferencias. Perdieron $50,000 en transacciones inconsistente porque MongoDB no tiene ACID robusto por defecto. **Con dinero, no se experimenta.**

---

#### Módulo 2: Chatbot Lee PDFs → **Vectorial (ChromaDB / Pinecone / Qdrant)**

**Razones:**

1. **Búsqueda por significado, no por palabra exacta:** El usuario pregunta "¿por qué me cobraron esta comisión rara?" y el PDF dice "cargo administrativo mensual". Una base de datos SQL buscaría "comisión rara" en el texto y no encontraría nada (FAIL). Una base de datos vectorial entiende que "comisión rara" y "cargo administrativo" son conceptos similares y encuentra el párrafo correcto.

2. **RAG (lo que hace útil a la IA):** Sin base vectorial, la IA puede responder cualquier cosa (alucinación). Con base vectorial, la IA responde basándose en el contenido REAL del PDF de tu banco. Pasa de ser "una IA genérica" a ser "la IA de TU banco con información REAL".

3. **Soporta múltiples formatos:** Los PDFs, imágenes de facturas, extractos bancarios... todo se puede convertir a texto y luego a vectores. SQL no puede "entender" una imagen escaneada de una factura. ChromaDB sí (a través de embeddings).

**¿Qué pasaría si usara PostgreSQL?** Podrías guardar el texto del PDF en una tabla, pero solo podrías buscar palabras exactas. Si el usuario pregunta "cargo misterioso" y el PDF dice "comisión eventual", PostgreSQL te dice "0 resultados". La base vectorial encuentra ambos porque sabe que significan lo MISMO.

---

#### Módulo 3: Promociones Diarias → **Clave-Valor (Redis)**

**Razones:**

1. **Velocidad extrema ante tráfico masivo:** 10,000 usuarios preguntando exactamente lo mismo al mismo tiempo. Si cada consulta va a la base de datos SQL, PostgreSQL podría colapsar (10,000 consultas simultáneas son muchas). Redis responde a los 10,000 instantáneamente porque vive en memoria RAM.

2. **Ahorro económico brutal:** Si cada consulta a la API de IA cuesta $0.01, responder "¿cuáles son las promociones?" a 10,000 usuarios cuesta $100/día = $3,000/mes = $36,000/año. Con Redis, la primera consulta cuesta $0.01 (se guarda en caché), las otras 9,999 cuestan $0.00. **Ahorro: $36,000 al año.**

3. **Expiación automática:** Las promociones cambian cada día. Podés configurar Redis para que la respuesta "expire" en 24 horas. Al día siguiente, la primera consulta regenera la caché con las nuevas promociones. Cero mantenimiento manual.

**¿Qué pasaría si usara PostgreSQL?** Podría funcionar con 100 usuarios. Con 10,000 usuarios simultáneos, PostgreSQL se pondría lento o colapsaría porque no está diseñado para servir la misma consulta masivamente en paralelo. Redis fue diseñado exactamente para este caso.

---

### Resumen del Arquitecto

```
Módulo 1 → PostgreSQL (Seguridad y precisión con dinero)
Módulo 2 → ChromaDB  (Búsqueda inteligente por significado)
Módulo 3 → Redis     (Velocidad extrema y ahorro económico)
```

Como bonus: este banco **ya tiene arquitectura poliglota** — usa 3 tipos distintos de bases de datos, cada una especializada en su tarea. Así se diseñan los sistemas profesionales.

---

## 🏆 Criterios de Éxito

Completaste el ejercicio exitosamente si:
- [ ] Elegiste un tipo de base de datos para cada módulo
- [ ] Escribiste al menos 2 razones para cada elección
- [ ] Entendés por qué la respuesta correcta es la correcta (incluso si elegiste otra)
- [ ] Podés explicarle a un compañero por qué NO usarías SQL para leer PDFs
- [ ] Entendés el valor económico de Redis (cuánto dinero ahorra)

---

## 💡 Bonus: Pregunta para Pensar en Casa

**Si mañana crearas tu propio proyecto de IA (un asistente de recetas de cocina con IA), ¿qué bases de datos usarías?**

Pensá en:
- ¿Dónde guardarías los usuarios y contraseñas?
- ¿Dónde guardarías el libro de recetas de 1,000 páginas para que la IA lo "entienda"?
- Si 5,000 personas preguntan "¿cómo hago arroz?" al mismo tiempo, ¿cómo ahorrarías dinero?
