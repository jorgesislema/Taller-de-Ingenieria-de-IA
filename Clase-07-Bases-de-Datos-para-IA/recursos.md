# Recursos — Clase 7: Bases de Datos para IA

> Material complementario para profundizar lo aprendido en clase. Videos, artículos, guías y herramientas.

---

## 🎥 Videos Recomendados

| Título | Duración | ¿Por qué verlo? |
|--------|----------|-----------------|
| [SQL vs NoSQL Explained](https://www.youtube.com/watch?v=ZS_kXvOeQ5Y) | 7 min | Comparación visual perfecta para principiantes |
| [What is a Vector Database?](https://www.youtube.com/watch?v=klTvEwg3oJ4) | 5 min | Explica bases de datos vectoriales sin matemáticas complejas |
| [Redis Crash Course](https://www.youtube.com/watch?v=Wxd6oCK2yDQ) | 20 min | Tutorial completo de Redis para principiantes |
| [RAG Explained Simply](https://www.youtube.com/watch?v=T-D1OfcDW1M) | 8 min | Qué es RAG y por qué es la técnica más importante hoy |

---

## 📖 Lecturas

| Título | Tipo | ¿Por qué leerlo? |
|--------|------|------------------|
| [ACID Explained in Plain English](https://www.freecodecamp.org/news/acid-databases-explained/) | Artículo | Explica las 4 garantías de SQL sin jerga |
| [ChromaDB Documentation](https://docs.trychroma.com/) | Documentación oficial | La guía más simple para empezar con bases vectoriales |
| [MongoDB vs PostgreSQL](https://www.mongodb.com/compare/mongodb-postgresql) | Comparativa | Comparación oficial de MongoDB con PostgreSQL |
| [The Total Economic Impact of Redis](https://redis.io/resources/forrester-tei/) | Reporte | Cuánto dinero real ahorran las empresas con Redis |

---

## 🛠️ Herramientas para Probar

| Herramienta | URL | ¿Para qué sirve? |
|-------------|-----|------------------|
| **DB Fiddle** | https://www.db-fiddle.com/ | Practicar SQL online sin instalar nada |
| **ChromaDB** | https://www.trychroma.com/ | Base vectorial más simple para empezar |
| **RedisInsight** | https://redis.com/redis-enterprise/redis-insight/ | Interfaz gráfica para Redis |
| **MongoDB Atlas** | https://www.mongodb.com/atlas | MongoDB gratis en la nube |
| **Supabase** | https://supabase.com/ | PostgreSQL gratis con interfaz visual |

---

## 📊 Infografías y Diagramas

### Los 4 Tipos de Bases de Datos (Resumen Visual)

```
┌────────────────────┬───────────────────┬───────────────────┬───────────────────┐
│      SQL           │      NoSQL        │    Key-Value      │     Vectorial     │
│   (Relacional)     │   (Documentos)    │    (Diccionario)  │    (Cerebro IA)   │
├────────────────────┼───────────────────┼───────────────────┼───────────────────┤
│ Organiza en tablas │ Guarda documentos │ Clave → Valor     │ Busca significado │
│ con filas/columnas │ sin estructura    │ búsqueda exacta   │ no palabras      │
│                    │ fija              │                   │ exactas           │
├────────────────────┼───────────────────┼───────────────────┼───────────────────┤
│ PostgreSQL         │ MongoDB           │ Redis             │ ChromaDB          │
│ MySQL              │ Firebase          │ Memcached         │ Pinecone          │
│ SQLite             │ CouchDB           │                   │ Qdrant            │
├────────────────────┼───────────────────┼───────────────────┼───────────────────┤
│ 🔒 Dinero          │ 💬 Chats          │ ⚡ Caché          │ 🧠 RAG            │
│ 👤 Usuarios        │ 🛒 Catálogos      │ 🔄 Sesiones       │ 📄 PDFs           │
│ 📅 Citas           │ 📱 Perfiles       │ 💰 FAQs           │ 🔍 Búsqueda       │
│                    │                   │                   │    semántica       │
└────────────────────┴───────────────────┴───────────────────┴───────────────────┘
```

---

## 🎯 Ejercicios Extra (para practicar en casa)

### Ejercicio 1: Identificar la base de datos correcta

Para cada caso, decidí qué tipo de base de datos usarías:

| Caso | Tu elección | ¿Por qué? |
|------|-------------|-----------|
| Una tienda online con 10,000 productos diferentes | | |
| Un bot de WhatsApp que responde FAQs | | |
| Un sistema de votación en tiempo real | | |
| Un buscador de imágenes por similitud visual | | |

### Ejercicio 2: Calcular ahorro con Redis

Un asistente virtual recibe 5,000 consultas diarias. El 60% son preguntas repetidas (las mismas FAQs). Cada consulta a la API de IA cuesta $0.008.

**Sin Redis:** ¿Cuánto gasta al día? ¿Al mes? ¿Al año?

```
Gasto diario = 5,000 × $0.008 = $__________
Gasto mensual = $__________ × 30 = $__________
Gasto anual = $__________ × 12 = $__________
```

**Con Redis:** Respondiendo solo la primera de cada FAQ repetida:

```
Consultas repetidas = 5,000 × 60% = 3,000 consultas repetidas
Consultas únicas = 5,000 - 3,000 = 2,000 consultas que van a la API

Gasto diario = 2,000 × $0.008 = $__________
Ahorro diario = $__________ - $__________ = $__________
Ahorro anual = $__________ × 365 = $__________
```

### Ejercicio 3: Diseñar mi propia arquitectura

Diseñá la arquitectura de bases de datos para tu propio proyecto de IA. Responde:

1. ¿Qué proyecto de IA te gustaría construir?

2. ¿Qué tipo de datos manejaría? (marcá todos los que apliquen)
   - [ ] Usuarios y contraseñas
   - [ ] Chat / conversaciones
   - [ ] Documentos PDF / manuales
   - [ ] Preguntas frecuentes (FAQs)
   - [ ] Transacciones / dinero
   - [ ] Búsqueda por significado
   - [ ] Imágenes / audio

3. Basado en tus respuestas, ¿qué bases de datos necesitarías?

| Base de Datos | ¿Para qué la usarías? |
|---------------|----------------------|
| | |
| | |
| | |

---

## 📚 Documentales y Charlas

| Título | Duración | ¿Por qué verlo? |
|--------|----------|-----------------|
| [How Netflix Uses Databases](https://www.youtube.com/watch?v=O3xGos6E6rY) | 15 min | Cómo Netflix maneja millones de usuarios con múltiples bases de datos |
| [Spotify's Architecture](https://www.youtube.com/watch?v=6q4JhVQy2jI) | 25 min | La arquitectura de datos de Spotify |
| [The Story of Redis](https://www.youtube.com/watch?v=DMWWl8DL_hA) | 30 min | Cómo un solo desarrollador creó la base de datos más rápida del mundo |

---

## 🔗 Enlaces Útiles

- [SQL Playground (Practicar online)](https://sqliteonline.com/) — Practicá SQL en el navegador
- [Redis Try (Practicar online)](https://try.redis.io/) — Practicá Redis en el navegador
- [MongoDB University](https://learn.mongodb.com/) — Cursos gratuitos de MongoDB
- [ChromaDB Cookbook](https://cookbook.chromadb.dev/) — Ejemplos prácticos de ChromaDB

---

## 💡 Citas para Recordar

> *"Elegir la base de datos correcta determina si tu IA será un juguete de demostración o un sistema empresarial que mueve millones."*

> *"No existe la mejor base de datos. Existe la base de datos correcta para cada problema."*

> *"Si tu única herramienta es un martillo, todos los problemas parecen clavos." — Ley de Maslow*

> *"Un sistema profesional no usa una base de datos. Usa la mezcla correcta de varias. Arquitectura poliglota."*
