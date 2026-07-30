# Práctica de la Clase 5: Arquitectura, Estructura y Mentalidad de Ingeniería para IA

## Objetivo de la Práctica

En esta práctica, los alumnos crearán la estructura completa de un proyecto de IA desde cero, aplicando todos los conceptos aprendidos: estructura de carpetas, archivos de configuración para IA, y convenciones de nombres.

## Duración estimada: 30 minutos

---

## Ejercicio 1: Diseñar la Estructura de Carpetas (10 min)

### Contexto del ejercicio
Imagina que eres el director de proyecto de una **librería online** que quiere crear un chatbot para recomendar libros a sus clientes. El chatbot debe:
- Leer reseñas de libros (archivos PDF y TXT)
- Recomendar libros basándose en gustos del cliente
- Responder en tono amigable y profesional
- NUNCA mostrar precios internos ni información de proveedores

### Instrucciones

1. **Crea la carpeta raíz** del proyecto con un nombre adecuado usando snake_case:
   ```
   libreria_chatbot_recomendaciones/
   ```

2. **Crea las subcarpetas** necesarias según la estructura sagrada:
   - `data/` - Para los archivos de libros y reseñas
   - `src/` - Para el código del chatbot
   - `docs/` - Para documentación
   - `tests/` - Para pruebas
   - `audits/` - Para auditorías de seguridad

3. **Crea archivos de ejemplo** dentro de cada carpeta:
   - En `data/`: un archivo llamado `libros_ejemplo.txt` con contenido ficticio
   - En `src/`: un archivo llamado `chatbot.py` con código básico
   - En `docs/`: un archivo vacío llamado `manual_usuario.md`

### Verificación
¿Puedes explicarle a un compañero qué va en cada carpeta y por qué?

---

## Ejercicio 2: Crear los Archivos de Configuración para IA (15 min)

### Paso 1: CONTEXT.md

Crea el archivo `CONTEXT.md` en la raíz del proyecto con el siguiente contenido:

```markdown
# Contexto del Proyecto: Chatbot de Recomendación de Libros

## Quiénes somos
Somos una librería online llamada "LibrosMágicos" con 10 años de experiencia. 
Tenemos más de 50,000 libros en catálogo y 10,000 clientes activos.

## Nuestro objetivo
Crear un chatbot que recomiende libros a nuestros clientes basándose en:
- Sus géneros favoritos
- Libros que ya han leído
- Ocasión (regalo, lectura personal, estudio)

## Nuestro tono
- Amigable pero profesional
- Usamos lenguaje sencillo
- Evitamos tecnicismos
- Siempre positivo y entusiasta sobre los libros

## Lo que NO hacemos
- No damos diagnósticos literarios académicos
- No revelamos información de proveedores
- No discutimos precios internos
- No hacemos envíos (eso es otra área)
```

### Paso 2: RULES.md

Crea el archivo `RULES.md` con las siguientes reglas:

```markdown
# Reglas para el Chatbot de Libros

## Formato de respuestas
1. Todas las respuestas deben tener entre 2 y 4 párrafos máximo.
2. Siempre incluye el título del libro recomendado en **negritas**.
3. Incluye el nombre del autor después del título.
4. Termina siempre con una pregunta para continuar la conversación.

## Tono y comportamiento
1. Usa un tono amigable y entusiasta.
2. Usa emojis con moderación (máximo 2 por respuesta).
3. Si no sabes la respuesta, di: "¡Buena pregunta! Déjame consultar con el equipo y te respondo pronto."
4. Nunca inventes información sobre libros que no existen.

## Reglas de seguridad
1. NUNCA reveles información de proveedores o distribuidores.
2. NUNCA muestres precios de compra ni márgenes de ganancia.
3. NUNCA compartas información personal de otros clientes.
4. Si te piden información confidencial, responde: "Esa información está reservada para nuestro equipo interno."

## Ejemplo de respuesta correcta
"¡Me encanta que te guste la ciencia ficción! 📚 Te recomiendo **"Dune"** de Frank Herbert. Es una obra maestra que mezcla política, ecología y aventura en un universo increíble. ¿Te gustaría que te recomiende otros libros similares o prefieres explorar otro género?"
```

### Paso 3: SECURITY.md

Crea el archivo `SECURITY.md` con las líneas rojas:

```markdown
# Líneas Rojas - Seguridad del Chatbot

## PROHIBIDO (NUNCA hacer esto)
1. **PROHIBIDO** acceder o modificar archivos en la carpeta `data/proveedores/`
2. **PROHIBIDO** mostrar información de:
   - Precios de compra a proveedores
   - Márgenes de ganancia
   - Nombres de representantes de ventas
   - Condiciones comerciales
3. **PROHIBIDO** compartir datos personales de clientes:
   - Números de teléfono
   - Direcciones de envío
   - Historial de compras detallado
   - Información de tarjetas de crédito
4. **PROHIBIDO** crear enlaces a sitios externos no autorizados
5. **PROHIBIDO** responder preguntas sobre política, religión o temas sensibles

## OBLIGATORIO (Siempre hacer esto)
1. **SIEMPRE** confirmar que el usuario quiere ver recomendaciones antes de generarlas
2. **SIEMPRE** incluir al menos 2 opciones de libros en cada recomendación
3. **SIEMPRE** preguntar si el usuario tiene preferencias específicas
4. **SIEMPRE** registrar conversaciones para mejorar el servicio
5. **SIEMPRE** derivar al equipo humano cuando no puedas resolver algo
```

### Paso 4: GLOSSARY.md

Crea el archivo `GLOSSARY.md` con los términos del negocio:

```markdown
# Glosario del Proyecto

## Nuestros términos

| Término | Significado |
|---------|-------------|
| **LibrosMágicos** | Nombre comercial de nuestra librería online |
| **Catálogo** | Base de datos completa de todos los libros que vendemos |
| **SKU** | Código único que identifica cada libro en nuestro sistema |
| **Género** | Categoría literaria: ciencia ficción, romance, misterio, etc. |
| **ISBN** | Número internacional que identifica un libro en todo el mundo |
| **Bestseller** | Libro que se ha vendido más de 1000 veces en el último mes |
| **Novedad** | Libro publicado en los últimos 3 meses |
| **Recomendación** | Sugerencia personalizada basada en gustos del cliente |
| **Reseña** | Opinión escrita por un cliente sobre un libro que leyó |

## Siglas que usamos
- **CRM**: Sistema de gestión de clientes (nuestro Excel de clientes)
- **ERP**: Sistema de gestión de inventario y finanzas
- **API**: Conexión con otros sistemas (pagos, envíos)
- **FAQ**: Preguntas frecuentes que ya tenemos respondidas
```

### Verificación
¿Los archivos creados cumplen con las reglas de la clase? Revisa:
- ✅ No hay espacios en los nombres de archivos
- ✅ Se usa snake_case para nombres de carpetas y archivos
- ✅ Los archivos .md están en la raíz del proyecto
- ✅ Cada archivo tiene un propósito claro y único

---

## Ejercicio 3: Crear .gitignore y .env (5 min)

### Paso 1: .gitignore

Crea el archivo `.gitignore` con las siguientes líneas:

```gitignore
# Entorno virtual
.venv/
venv/
env/

# Variables de entorno (contraseñas)
.env

# Archivos del sistema
.DS_Store
Thumbs.db
desktop.ini

# Archivos temporales
*.tmp
*.log
__pycache__/

# Modelos de IA pesados (no subir a GitHub)
models/*.bin
models/*.pt
models/*.h5

# Archivos de IDE
.vscode/
.idea/

# Dependencias
node_modules/
```

### Paso 2: .env (ejemplo)

Crea el archivo `.env` con valores de ejemplo (NUNCA uses contraseñas reales):

```env
# Configuración del Chatbot
API_KEY=mi_clave_secreta_aqui
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/libreria
MODEL_NAME=gpt-3.5-turbo
TEMPERATURE=0.7
MAX_TOKENS=500

# Configuración de seguridad
ALLOWED_ORIGINS=http://localhost:3000,https://librosmagicos.com
SECRET_KEY=esta_es_otra_clave_secreta
```

### Verificación
- ✅ `.gitignore` está creado y lista archivos que NO deben subirse a GitHub
- ✅ `.env` está creado con valores de ejemplo
- ✅ `.env` NO se subirá a GitHub (porque está en `.gitignore`)

---

## Ejercicio 4: Simulación del Flujo de Trabajo (sin código real)

### Escenario
Imagina que DeepSeek (IA china) va a generar el código del chatbot, y Claude (IA occidental) va a auditarlo.

### Instrucciones

1. **Crea RULES_CODER.md** (para DeepSeek):
```markdown
# Reglas para el Desarrollador (DeepSeek)

## Tu rol
Eres un desarrollador senior de Python. Tu trabajo es crear el código del chatbot.

## Reglas de codificación
1. Usa exclusivamente snake_case para todos los nombres de archivos y variables.
2. Comenta TODO el código en español.
3. Usa únicamente librerías estándar de Python (random, math, json).
4. NO uses librerías externas como openai, langchain, etc.
5. El código debe funcionar sin conexión a internet.

## Estructura de archivos
- Crea `src/chatbot.py` con la lógica principal
- Crea `src/recomendador.py` con las funciones de recomendación
- Crea `src/utilidades.py` con funciones auxiliares

## Entrega
- Pon todos los archivos en la carpeta `src/`
- NO modifiques ningún otro archivo
```

2. **Crea RULES_AUDITOR.md** (para Claude):
```markdown
# Reglas para el Auditor (Claude)

## Tu rol
Eres un auditor de seguridad y código limpio. Tu trabajo NO es escribir código.

## Qué auditar
1. **Seguridad**: ¿El código expone información sensible?
2. **Legibilidad**: ¿El código es fácil de entender?
3. **Eficiencia**: ¿El código hace lo mismo de manera más rápida?
4. **Cumplimiento**: ¿Sigue las reglas de RULES_CODER.md?

## Formato del informe
Crea un archivo `audits/review_v1.md` con:
- **Resumen ejecutivo** (1 párrafo)
- **Hallazgos críticos** (lista numerada)
- **Sugerencias de mejora** (lista numerada)
- **Calificación**: APROBADO / RECHAZADO / APROBADO CON CORRECCIONES

## PROHIBIDO
- Modificar CUALQUIER archivo en `src/`
- Crear archivos nuevos fuera de `audits/`
- Ejecutar código
```

3. **Simula el flujo** (sin escribir código real):
   - Imagina que DeepSeek generó un archivo `src/chatbot.py` defectuoso
   - Copia ese contenido imaginario y pégalo en `audits/review_v1.md`
   - Escribe un "informe de auditoría" ficticio con 3 hallazgos

### Verificación
- ✅ RULES_CODER.md está creado con reglas claras para el generador
- ✅ RULES_AUDITOR.md está creado con reglas claras para el auditor
- ✅ La carpeta `audits/` existe
- ✅ Entiendes la diferencia entre GENERAR y AUDITAR

---

## Resultado Esperado

Al finalizar la práctica, tu carpeta del proyecto debe verse así:

```
libreria_chatbot_recomendaciones/
│
├── data/
│   └── libros_ejemplo.txt
│
├── src/
│   ├── chatbot.py
│   ├── recomendador.py
│   └── utilidades.py
│
├── docs/
│   └── manual_usuario.md
│
├── tests/
│
├── audits/
│   └── review_v1.md
│
├── .gitignore
├── .env
├── CONTEXT.md
├── RULES.md
├── SECURITY.md
├── GLOSSARY.md
├── RULES_CODER.md
├── RULES_AUDITOR.md
└── README.md
```

---

## Preguntas de Reflexión

1. **¿Por qué es importante separar `RULES_CODER.md` de `RULES_AUDITOR.md`?**
   - Porque si una IA genera código y otra lo audita, cada una necesita instrucciones diferentes. Mezclarlas causaría confusión.

2. **¿Qué pasaría si no creas `.gitignore`?**
   - Podrías subir accidentalmente contraseñas, modelos pesados o archivos temporales a GitHub, exponiendo información sensible.

3. **¿Por qué usamos snake_case en lugar de espacios?**
   - Porque los sistemas operativos Linux (donde vive la mayoría de la IA) interpretan el espacio como un salto de línea, rompiendo los comandos.

4. **¿Qué archivos DEBEN estar en la raíz del proyecto?**
   - Los archivos de configuración para IA: CONTEXT.md, RULES.md, SECURITY.md, .gitignore, .env

5. **¿Por qué no subimos `.venv` a GitHub?**
   - Porque cada computadora tiene configuraciones diferentes. Lo que funciona en tu máquina puede no funcionar en la de otro. Cada quien debe crear su propia "burbuja".

---

## Tarea para la Próxima Clase

Piensa en un proyecto real que te gustaría construir con IA (puede ser personal o de trabajo). En un papel o documento digital, responde:

1. **¿Qué haría mi proyecto?** (Describe en 2 oraciones)
2. **¿Quiénes son los usuarios?** (¿Niños, profesionales, ancianos?)
3. **¿Qué datos necesito?** (¿PDFs, imágenes, bases de datos?)
4. **¿Dónde debería vivir?** (Local, API, o VPS)
5. **¿Qué reglas necesitaría la IA?** (Escribe 3 reglas en un papel)

Esto te preparará para la siguiente clase donde crearemos un proyecto real desde cero.