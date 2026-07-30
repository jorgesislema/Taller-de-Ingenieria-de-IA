# Apuntes de la Clase 5: Arquitectura, Estructura y Mentalidad de Ingeniería para IA

## Introducción

"Hasta ahora hemos aprendido a usar el martillo (VS Code) y el almacén (GitHub). Pero construir una casa no es solo golpear clavos. Hoy vamos a hablar de los planos. Hoy vamos a pensar como Ingenieros. Y un ingeniero no es el que sabe más código, es el que toma mejores decisiones basándose en el contexto."

---

## Fase 1: El Cambio de Paradigma — De "Enciclopedias" a "Directores de Orquesta"

### La muerte del trabajador-enciclopedia

Durante los últimos 30 años, el trabajador del conocimiento fue pagado por su capacidad de almacenar y recordar. Si sabías la sintaxis exacta de 15 librerías de Python, o te sabías de memoria los protocolos de red, eras valioso. Eras una enciclopedia con piernas.

**Eso murió.**

ChatGPT, Claude, DeepSeek y los modelos que vengan tienen absorbida toda la enciclopedia de la humanidad. En un concurso de "quién sabe más datos", un humano pierde 100 a 0 en un segundo.

Entonces, ¿por qué una empresa te va a pagar un buen salario hoy? Te pagará por **tres cosas que la IA no tiene**:

---

### Las 3 cosas que la IA no puede hacer

#### 1. Contexto del Negocio Real

La IA no sabe que tu jefe es terco, que el presupuesto es de 50 dólares, o que el cliente final odia los colores brillantes. **Tú sí.**

La IA puede generate 10 soluciones técnicamente perfectas, pero no sabe cuál se ajusta a la política interna de tu empresa, a las limitaciones presupuestarias del cliente, o al hecho de que el equipo de soporte solo sabe usar Excel.

#### 2. Criterio bajo Incertidumbre

La IA te da 5 opciones técnicas válidas. **¿Cuál eliges?** Depende de factores que no están en un manual. Eso es criterio.

El criterio es lo que te permite decir: "Sé que los microservicios son la moda, pero para nuestro equipo de 3 personas, un Monolito es la decisión correcta". La IA nunca te dirá eso porque no tiene el contexto de tu realidad.

#### 3. Asumir las Consecuencias

Si la IA sugiere borrar una base de datos y lo hace, la IA no va a la cárcel ni es despedida. **Tú sí.** Alguien humano tiene que firmar y ser responsable.

La IA puede sugerir, pero el humano firma con su nombre. Por eso te pagan: no por saber, sino por responsabilidad.

---

### Ejemplos de Criterio vs. Conocimiento (Aplicados a esta clase)

Si leemos la clase que armamos a través de este lente, el "conocimiento" es solo el 10%. El 90% restante es puro criterio arquitectónico:

#### Ejemplo 1: Las Arquitecturas (Monolito vs. Microservicios)

| El Conocimiento (Lo que sabe la IA) | El Criterio (Lo que pagamos a ti) |
|--------------------------------------|-----------------------------------|
| La IA sabe perfectamente definir qué es un microservicio, cómo se configura Kubernetes y cómo hacer un API Gateway. | Darse cuenta de que, para un equipo de 3 personas haciendo un MVP, usar microservicios es un **suicidio financiero y operativo**, y decidir valientemente usar un Monolito (Food Truck) a pesar de que la "moda" diga lo contrario. **Eso es pensamiento crítico.** |

#### Ejemplo 2: La regla del snake_case

| El Conocimiento | El Criterio |
|-----------------|-------------|
| Saber que en Linux los espacios rompen las rutas. | Exigirle a la IA a través de un `RULES.md` que use snake_case **antes de que empiece a programar**, para no tener que perder 2 horas buscando por qué el servidor se cayó por un error tonto. **Eso es previsión.** |

#### Ejemplo 3: El equipo Híbrido (DeepSeek para crear, Claude para auditar)

| El Conocimiento | El Criterio |
|-----------------|-------------|
| Saber que existen dos modelos de IA distintos. | Diseñar el flujo de trabajo de "Red Team". Entender que los modelos tienen "puntos ciegos" y que usar **dos cerebros artificiales distintos** (uno para atacar, otro para defender) genera un resultado superior al de un solo modelo. **Eso es diseño de sistemas.** |

---

### La Analogía del Capitán del Barco

> *"Imaginen un barco carguero gigante. La IA es la sala de máquinas. Tiene una fuerza bruta increíble, sabe cómo mover cada válvula, conoce la termodinámica perfecta y no duerme. Tiene todo el conocimiento físico del barco.*
>
> *Pero si la sala de máquinas decide hacia dónde ir el barco, va a chocar contra la primera isla que encuentre.*
>
> *El trabajador del futuro no es el que está abajo shoveling carbón (escribiendo código repetitivo). El trabajador del futuro es el **Capitán en el puente de mando**. El Capitán no sabe cómo funcionan los tornillos del motor, pero sabe leer el clima, sabe a qué puerto quiere llegar, sabe negociar con otros barcos y, sobre todo, tiene el criterio para decidir si debe ir a toda velocidad o detenerse por la tormenta."*

---

### Conclusión de la Analogía

Lo que les estás enseñando en esta clase **no es a "usar herramientas de IA"**. Les estás enseñando a **subir al puente de mando**.

El `.md`, las carpetas, las decisiones de VPS vs Serverless... **no son archivos técnicos**. Son los **instrumentos de navegación del capitán**. Y por eso, el que sabe usarlos, será imparable y altamente cotizado, sin importar si sabe escribir una sola línea de código.

---

### El Criterio como Multiplicador

El criterio no es una línea recta que sube con el tiempo. Es un **multiplicador**. Y la fórmula es esta:

> **Criterio = (Cantidad de Errores Comprendidos) × (Densidad de Reflexión)**

Fíjate que en la fórmula **no aparece el tiempo**. Puedes tener 20 años de experiencia y no haber cometido un error porque nunca te arriesgaste, o porque siempre hiciste lo que te dijeron. Tu criterio será de cero.

---

### Cómo Aumentar tu Criterio (Sin ImportAR si Eres Principiante o Veterano)

#### 1. El Secreto: El "Fracaso Digerido" (No basta con fallar)

El éxito no te da criterio. El éxito te da **confianza** (que a veces es peligrosa). El criterio nace exclusivamente del **dolor de haberse equivocado y haber entendido por qué**.

| Sin experiencia | Construyendo criterio |
|-----------------|----------------------|
| Si hoy creas tu archivo `.md`, se lo das a la IA, el código falla, te frustras y lo borras... **no ganaste criterio**. | Si el código falla, te detienes, analizas y dices: "Ah, falló porque le di a la IA un `CONTEXT.md` muy vago y se inventó una librería que no existe". **Acabas de ganar +10 puntos de criterio.** |

**Cómo aplicarlo sin experiencia:** Fuerza errores pequeños y baratos. En un entorno de pruebas, dile a la IA que haga algo mal a propósito solo para ver cómo se rompe el sistema. **Estudiar el rompimiento construye criterio más rápido que estudiar el éxito.**

#### 2. La Densidad vs. La Longitud (Calidad de las decisiones)

Una persona que en un mes tiene que tomar **50 decisiones difíciles** sobre arquitectura de IA (aunque se equivoque en 30), desarrollará mucho más criterio que alguien que en 5 años solo toma **2 decisiones al año** porque trabaja en una empresa burocrática donde todo ya está decidido.

**Cómo aplicarlo sin experiencia:** Aumenta tu densidad. En lugar de pedirle a la IA "Hazme el proyecto entero", pártelo en 10 pedacitos. En cada pedacito, **tú toma una decisión de diseño** (¿Cómo llamo esta carpeta? ¿Pongo esto en un `.md` o en otro?). Toma **50 micro-decisiones al día**, aunque al principio no sepas cuál es la correcta.

#### 3. El Método del "Por Qué" en Cadena (El arte de incomodar)

El criterio se destruye cuando aceptamos las cosas porque "así se hace siempre".

**Cómo aplicarlo sin experiencia:** Conviértete en un niño de 3 años. Cuando veas un tutorial, un libro, o cuando la IA te dé una solución, aplica la **regla de los 3 Porqués**:

```
La IA dice: "Usa un archivo .env para la contraseña."
Tú: ¿Por qué?
La IA: "Para no subirla a GitHub."
Tú: ¿Y por qué es malo subirla a GitHub?
La IA: "Porque los bots escanean los repositorios públicos para robar claves 
       y cobrar en AWS."
Tú: ¡Aha! Ya no es una regla memorizada, es un criterio de seguridad interno.
```

#### 4. Desarrollar la "Simulación Mental" (El Gym del Cerebro)

Los grandes arquitectos de software y los grandes ajedrecistas no son más rápidos calculando; son mejores **simulando el futuro** en su cabeza antes de mover la pieza.

**Cómo aplicarlo sin experiencia:** Antes de escribirle a la IA o de crear una carpeta, siéntate 60 segundos. Cierra los ojos y visualiza:

> *"Si yo creo esta carpeta llamada `archivos` y mañana vienen 5 personas más al equipo... ¿van a saber qué va ahí? Si la IA genera 100 archivos ahí, ¿será fácil encontrar algo?"*

Ese segundo de pausa, esa **proyección al futuro**, es criterio puro. Y no requiere saber programar, requiere **imaginación estructural**.

---

### La Ventaja del que "No Tiene Experiencia"

Tengo una buena noticia como docente: **El que no tiene experiencia tiene una ventaja gigantesca sobre el veterano: NO tiene prejuicios.**

El programador con 15 años de experiencia va a querer hacer las cosas como se hacían en 2015. Va a resistirse a usar archivos `.md` para controlar la IA porque "eso no es programar de verdad". Su conocimiento viejo bloquea su criterio nuevo.

**Tú, al empezar desde cero con la IA, tienes la mente en blanco.** Tu cerebro es plastilina fresca. Si te concentras en tomar decisiones conscientes (aunque duelen), analizar tus errores y no memorizar recetas, puedes alcanzar en 6 meses un nivel de criterio arquitectónico que a un tradicional le tomó 4 años.

> **El criterio no es saber la respuesta correcta. El criterio es saber hacer las preguntas correctas antes de actuar.** Y para hacer preguntas, no se necesitan años de experiencia, se necesita **curiosidad implacable**.

---

## Fase 2: Arquitectura Física y Lógica

### ¿Dónde corre nuestra IA?

Antes de construir, debemos decidir **dónde vivirá** nuestro sistema. Esta es una decisión de arquitectura fundamental.

### Opción A: Local (Tu propia computadora)

**Analogía:** Cocinar en tu casa.

| Ventajas | Desventajas |
|----------|-------------|
| Gratis | Si se daña tu PC, se cae el sistema |
| Tus datos no salen de la PC (máxima privacidad) | Si quieres que tu vecino lo use, tiene que ir a tu casa |
| No necesitas internet | Limitado por el hardware de tu PC |

**Pensamiento crítico:** ¿Manejo datos médicos súper sensibles? → **Local**.

### Opción B: API (Interfaz de Programación de Aplicaciones)

**Analogía:** Pedir comida a domicilio por Uber Eats. Tú no cocinas, envías la petición, alguien poderoso cocina, y te devuelve el resultado.

| Ventajas | Desventajas |
|----------|-------------|
| No necesitas una súper computadora con tarjetas gráficas carísimas | Necesitas internet siempre |
| Pagas solo por lo que usas | Cada vez que mandas un dato, sale de tu empresa |
| Escalable automáticamente | Dependes de un tercero |

**Pensamiento crítico:** ¿Mi aplicación va a tener miles de usuarios y no quiero comprar servidores de $10,000? → **API**.

### Opción C: VPS (Servidor Privado Virtual) o Cloud

**Analogía:** Alquilar un local comercial. Es tuyo, está encendido 24/7, cualquiera puede entrar por la puerta principal.

| Ventajas | Desventajas |
|----------|-------------|
| Control total | Tienes que mantenerlo (actualizarlo, protegerlo) |
| Accesible desde cualquier lugar del mundo | Cuesta dinero mensual |
| Personalizable | Requiere conocimientos básicos de administración |

**Pensamiento crítico:** ¿Voy a conectar mi IA con una página web para que la usen clientes reales a cualquier hora? → **VPS**.

### Lección de Ingeniería

**No existe la mejor arquitectura. Existe la arquitectura que mejor resuelve tu problema específico.**

```
¿Tienes datos sensibles? → LOCAL
¿Tienes presupuesto limitado pero muchos usuarios? → API
¿Necesitas control total y disponibilidad 24/7? → VPS
```

---

## Fase 3: La Gramática del Software

### La Regla de Oro Absoluta: CERO ESPACIOS

En programación, **LOS ESPACIOS EN BLANCO NO EXISTEN** en los nombres de archivos o carpetas.

```
❌ MAL: Mi proyecto de IA / archivo de datos.py
✅ BIEN: mi_proyecto_de_ia/ archivo_de_datos.py
```

**¿Por qué?** Los sistemas operativos basados en Linux (donde vive el 99% de la IA y los servidores VPS) leen el espacio como un "Enter" (un salto de línea). Si la IA intenta abrir `archivo de datos.py`, el servidor busca un archivo llamado `archivo`, no lo encuentra, y explota.

### Las "Tarjetas de Identificación" (Extensiones de Archivos)

Todo archivo en programación tiene un "apellido" de 2 a 4 letras después del punto. Esto le dice a la computadora y a la IA qué idioma hablar.

| Extensión | Significado | ¿Para qué sirve en IA? |
|-----------|-------------|-------------------------|
| `.py` | Python | El rey actual de la IA. Aquí va la lógica, los modelos, el análisis de datos. |
| `.js` / `.ts` | JavaScript / TypeScript | Si tu IA va a tener una página web interactiva, esto es el "motor visual". |
| `.md` | Markdown | Los archivos de instrucciones para humanos e IAs (RULES.md, etc.). |
| `.json` | JavaScript Object Notation | Cómo la IA y las computadoras intercambian datos estructurados. |
| `.env` | Environment (Entorno) | **¡ALERTA ROJA!** Aquí guardamos contraseñas y claves API. **NUNCA se comparte.** |
| `.txt` / `.csv` | Texto / Valores separados por comas | La "comida" de la IA. Los datos que leemos para entrenar o procesar. |
| `.gitignore` | Git Ignore | La lista negra de GitHub (sin apellido porque es una directriz). |

### Los 3 "Idiomas" para escribir nombres (Cases)

Como no podemos usar espacios, los ingenieros inventaron sistemas para unir palabras.

#### A. snake_case (El caso serpiente) - **EL ESTÁNDAR DE PYTHON E IA**

**Cómo es:** Todo en minúsculas, palabras separadas por guion bajo (`_`).

```
Ejemplo: analisis_de_sentimientos.py
         carpeta_de_modelos/
         base_de_datos_clientes.csv
```

**Regla de Ingeniería:** Si trabajas con IA (Python), el 90% de tus archivos y carpetas deben llevar snake_case.

#### B. camelCase (El caso camello) - **EL ESTÁNDAR DE LA WEB**

**Cómo es:** Primera palabra en minúscula, las siguientes empiezan con mayúscula (las "jorobas" del camello).

```
Ejemplo: procesadorDeTexto.js
         calcularTotal()
```

**Uso:** Casi exclusivo para nombrar variables o funciones dentro de archivos `.js` o `.ts`. No se usa para nombres de carpetas.

#### C. PascalCase (El caso pascal) - **EL ESTÁNDAR DE COMPONENTES**

**Cómo es:** Todas las palabras empiezan con mayúscula, sin espacios.

```
Ejemplo: ModeloDeIA.py
         MenuPrincipal.tsx
```

**Uso:** Se usa para nombrar "Clases" (moldes para crear cosas) en programación orientada a objetos, o componentes visuales en web.

#### D. kebab-case (El caso kebab) - **SOLO PARA RUTAS WEB**

**Cómo es:** Minúsculas separadas por guion medio (`-`).

```
Ejemplo: mi-pagina-web.com/analisis-de-datos
```

**⚠️ Regla de Oro:** **NUNCA** nombres un archivo o carpeta local con kebab-case si vas a usar Python/IA. Muchas librerías de Python se rompen si ven un guion medio en el nombre de un archivo. Usen kebab-case solo para URLs.

### Singular vs. Plural (El debate eterno)

Una pregunta clásica de arquitectura: ¿La carpeta se llama `model/` o `models/`?

**La convención moderna aceptada:**

- **Carpetas (Plural):** Como son "contenedores" que guardan muchas cosas, se usa plural.
  ```
  ✅ models/, docs/, images/, tests/
  ```

- **Archivos (Singular):** Porque un archivo suele representar una sola entidad lógica o un solo módulo.
  ```
  ✅ model.py, database.py, user.py
  ```

### El "Prompt de Arquitectura"

Si le pides a ChatGPT: "Escríbeme un programa", te va a crear un desastre llamado `Mi Programa Final v2.py`. Pero si eres un ingeniero, le agregas a tu `RULES.md` la siguiente regla:

**Añadir a RULES.md:**
```
REGLA ESTRICTA DE NOMBRAMIENTO:
1. No uses espacios en blanco en ningún nombre de archivo o carpeta.
2. Usa exclusivamente snake_case (minúsculas y guiones bajos) para todos los archivos .py y carpetas del proyecto.
3. Nombra las carpetas en plural (ej: models/) y los archivos en singular (ej: model.py).
4. Prohíbido el uso de caracteres especiales como tildes (á, é) o la letra ñ en nombres de archivos.
```

**El resultado mágico:** A partir de ese momento, la IA dejará de ser un novato desordenado y empezará a generar código con estándares de nivel empresarial (Google, Microsoft, OpenAI).

---

## Fase 4: Los 4 Mandamientos del Arquitecto

### REGLA 1: "Cada quien a su casa" (Separación de Conceptos)

**El Concepto Técnico:** Dividir el sistema en partes donde cada una tiene una única responsabilidad.

**La Traducción Simple:** No mezcles las cosas.

**La Analogía:** Imagina un restaurante. Tienes la cocina (donde se cocina), el comedor (donde se come) y la caja (donde se cobra). ¿Qué pasaría si el chef cocina en la misma mesa donde los clientes comen y el cajero cuenta dinero ahí? Un caos.

**Aplicado a la IA:**
```
archivos_para_leer/ (El comerdon)
codigo_inteligencia/ (La cocina)
resultados/ (La caja)
```

### REGLA 2: "Cero Adornos" (KISS + YAGNI)

**El Concepto Técnico:** No añadir complejidad innecesaria ni implementar funcionalidades "por si acaso" se necesitan en el futuro.

**La Traducción Simple:** Construye solo lo que necesitas, ahora mismo, de la forma más tonta y simple posible.

**La Analogía:** Si necesitas colgar un cuadro en la pared de tu cuarto, usas un clavo y un martillo. No construyes una grúa telescópica "por si acaso mañana quieres colgar un elefante en la pared".

**Aplicado a la IA:** Si necesitas que la IA resuma un texto, pídele que use una función básica. No le pidas a la IA que cree un sistema de base de datos con 15 servidores "por si acaso" un día tienes un millón de textos. Mañana, cuando tengas el millón, ya verás cómo ampliarlo. Hoy, usa un clavo.

### REGLA 3: "No uses Super Pegamento" (Bajo Acoplamiento)

**El Concepto Técnico:** Módulos que tienen mínimas dependencias entre sí.

**La Traducción Simple:** Que las piezas de tu proyecto se puedan desarmar y cambiar sin que todo se venga abajo.

**La Analogía:** Imagina que armas un mueble de IKEA, pero en lugar de tornillos, usas Super Pegamento. Si se rompe una pata, no puedes cambiar solo la pata, tienes que tirar todo el mueble a la basura. Si usas tornillos (bajo acoplamiento), desatornillas la pata y pones una nueva.

**Aplicado a la IA:** Si hoy tu IA se conecta a ChatGPT, y mañana ChatGPT se pone muy caro y quieres cambiar a Claude. Si tu programa está "pegado con Super Pegamento" a ChatGPT, tienes que reescribir todo. Si usas "tornillos" (una carpeta intermedia de conexión), solo cambias esa pieza y el resto del programa ni se entera.

### REGLA 4: "El Especialista, no el Hombre Orquesta" (Responsabilidad Única)

**El Concepto Técnico:** Una clase/módulo debe tener una, y solo una, razón para cambiar.

**La Traducción Simple:** Contrata profesionales específicos, no intentes que un solo archivo haga todo.

**La Analogía:** No contrates a una persona que sea a la vez médico, contador, mecánico y chef. Si se enferma (hay un error en el código), se arruina tu salud, tu dinero, tu auto y tu cena a la vez.

**Aplicado a la IA:**
```
Archivo 1: extractor_de_texto.py (Solo sabe sacar letras de un PDF).
Archivo 2: limpiador_de_texto.py (Solo sabe borrar signos de puntuación).
Archivo 3: llamador_de_ia.py (Solo sabe enviar el texto a la IA).
```

Si la IA cambia de precio, solo tocas el Archivo 3. Los demás siguen trabajando tranquilos.

### Los 2 Monstruos que Debemos Evitar

#### El Monstruo Espagueti (Spaghetti Code)

Es cuando los archivos están tan enredados entre sí como un plato de pasta. Tiritas de un hilo (de un archivo) y el plato entero se mueve. Se arregla aplicando la **Regla 3** (No uses Super Pegamento).

#### El Dios Objeto (La Clase Diosa)

Es un solo archivo de código que hace absolutamente todo. Sabe de bases de datos, sabe de matemáticas, sabe dibujar en pantalla. Es un dios todopoderoso pero inmanejable. Si ese archivo falla, todo el universo se apaga. Se arregla aplicando la **Regla 4** (El Especialista).

---

## Fase 5: El Plano Físico - Estructura de Carpetas

### La Estructura Sagrada

```
mi_proyecto_de_ia/
│
├── data/           # (LOS INGREDIENTES) Aquí van los PDFs, Excels, imágenes que le daremos a la IA.
├── src/            # (LA COCINA) "Source". Aquí va el código de tu programa.
├── models/         # (EL CEREBRO) Si descargas un modelo de IA propio, vive aquí.
├── docs/           # (EL MANUAL DE USUARIO) Documentación para humanos.
├── tests/          # (EL CONTROL DE CALIDAD) Código para probar que nuestro programa no se rompa.
│
├── .gitignore      # (EL GUARDIA DE SEGURIDAD)
├── .venv/          # (LA BURBUJA)
├── CONTEXT.md      # (La memoria de la IA)
├── RULES.md        # (Las reglas de la IA)
└── SECURITY.md     # (Las reglas rojas)
```

**Pensamiento Crítico en las carpetas:** ¿Si tienen 50 archivos de Excel y 10 scripts de código en la misma carpeta... es fácil mantener eso a los 6 meses? La respuesta es no. **La regla de oro: Separa los datos de la lógica.**

### Los Archivos Invisibles

#### .venv (El Entorno Virtual)

**¿Qué es?** Es una "burbuja" o "cuarto de pruebas" aislada dentro de tu computadora.

**El Problema que resuelve:** Imagina que el Proyecto A necesita la versión 1 de una herramienta, y el Proyecto B necesita la versión 2. Si las instalas en toda tu computadora, chocan y todo se rompe.

**Analogía:** `.venv` es como tener un frasco de cristal esterilizado para cada experimento. Lo que pasa dentro del frasco, no afecta al resto de la cocina.

**Regla de oro:** **NUNCA** se sube el `.venv` a GitHub. Es basura para otros, cada quien debe crear su propia burbuja.

#### .gitignore

**¿Qué es?** Es la lista negra de GitHub. Le dice a Git: "Cuando vayas a sincronizar, **IGNORA** estas cosas".

**¿Qué se pone ahí?** El `.venv`, las contraseñas, los modelos pesados de IA, y carpetas temporales del sistema.

**Pensamiento Crítico:** Si no usas `.gitignore`, puedes subir accidentalmente la contraseña de tu base de datos o de tu tarjeta de crédito a internet. **Como ingenieros, la seguridad no es una característica, es un requisito.**

---

## Fase 6: Programando a la IA sin Código (Los .md)

### La Revolución

"Ustedes no saben Python, no saben JavaScript, y ESTÁ BIEN. Porque hoy van a aprender a programar el comportamiento de la IA usando archivos de texto plano llamados Markdown (.md). Esto sirve para ChatGPT, Claude, Cursor, Copilot... da igual el modelo."

Los archivos `.md` son el "Contexto" que la IA lee antes de ayudarte. Si la IA tiene estos archivos, pasará de ser un asistente genérico a un empleado tuyo que conoce tu empresa al dedillo.

### CATEGORÍA 1: La Identidad y el Comportamiento (El "cerebro" de la IA)

Estos archivos definen quién es la IA y cómo debe actuar.

#### CONTEXT.md (El Currículum / El Brief)

**Para qué sirve:** Explicarle a la IA quiénes somos y qué estamos construyendo.

**Ejemplo de contenido:**
```
Somos una clínica veterinaria. Nuestro objetivo es crear un chatbot que responda 
dudas básicas de nutrición de perros y gatos. Nuestro tono es amigable pero profesional. 
No damos diagnósticos médicos, solo recomendaciones de alimento.
```

#### RULES.md (El Manual del Empleado)

**Para qué sirve:** Dictar cómo debe trabajar la IA. Las reglas del juego.

**Ejemplo de contenido:**
```
REGLA 1: Nunca inventes datos de medicamentos. Si no lo sabes, di 'Consulte con su veterinario'.
REGLA 2: Todas las respuestas deben tener menos de 3 párrafos.
REGLA 3: Al escribir código, usa siempre español para los nombres de variables y comentarios.
```

#### SECURITY.md (Las Líneas Rojas)

**Para qué sirve:** Proteger la integridad del negocio y los datos.

**Ejemplo de contenido:**
```
PROHIBIDO: Borrar o modificar la carpeta 'data/' bajo ninguna circunstancia.
PROHIBIDO: Mostrar en las respuestas del chatbot los datos de los dueños de las mascotas 
           (número de teléfono, dirección).
PROHIBIDO: Escribir código que acceda a internet sin permiso.
```

#### PERSONAS.md (El Actor) - Opcional

**Para qué sirve:** Define a quién le habla la IA.

**Ejemplo:**
```
Hablas con Pedro, un contador de 50 años que sabe usar Excel pero odia la tecnología. 
Sé muy paciente y usa analogías de contabilidad.
```

### CATEGORÍA 2: El Conocimiento del Negocio (La "Biblioteca" de la IA)

Los no programadores son los expertos en su negocio. Estos archivos inyectan esa sabiduría en la IA sin necesidad de bases de datos complejas.

#### GLOSSARY.md (El Traductor)

**Fundamental.** Explica las siglas y términos raros de la empresa.

**Ejemplo:**
```
"Cuando digamos 'El Sistema Raptor', nos referimos al módulo de facturación antiguo. 
Cuando digamos 'CRM', es el archivo de Excel de clientes".
```

#### FAQ.md (Preguntas Frecuentes)

Un archivo con preguntas y respuestas exactas. Si la IA lee esto antes de responder, no se inventará nada (evita alucinaciones).

#### PRODUCT_KNOWLEDGE.md (La Ficha Técnica)

Detalles específicos de lo que se está construyendo o vendiendo. (Ej: Precios, medidas, características técnicas del producto que la IA debe conocer al pie de la letra).

### CATEGORÍA 3: La Arquitectura y el Mapa (El "GPS" del Proyecto)

Aquí le decimos a la IA cómo está construido el entorno físico.

#### ARCHITECTURE.md (El Plano del Edificio)

Explica la relación entre las carpetas.

**Ejemplo:**
```
La carpeta data/ tiene los PDFs de entrada. 
La carpeta src/ tiene el código que los procesa. 
NUNCA modifiques archivos en models/.
```

#### DECISIONES.md (El Diario del Ingeniero)

Aquí se anota el "Por qué" de las cosas.

**Ejemplo:**
```
Decisión: Usamos una API externa en lugar de un modelo local. 
Razón: Porque no tenemos tarjeta gráfica y el presupuesto es de 50 dólares al mes.
```

La IA necesita saber esto para no sugerir cambiar de tecnología constantemente.

#### PROGRESS.md (El Tablero de Control)

¿En qué punto vamos?

**Ejemplo:**
```
Paso 1: Hecho. 
Paso 2: En progreso. 
Paso 3: Pendiente.
```

Esto es vital si usas IA para continuar un proyecto día a día, para que no se pierda.

### CATEGORÍA 4: Calidad y Mantenimiento (El "Control de Calidad")

#### TESTING.md (El Protocolo de Pruebas)

Cómo sabemos que la IA hizo bien su trabajo.

**Ejemplo:**
```
Para probar que el código funciona, pídele al usuario que suba un PDF en blanco. 
El sistema debe dar el error 'Archivo vacío' y no colapsar.
```

#### ERROR_HANDLING.md (El Manual de Incidencias)

Qué debe hacer la IA si algo falla.

**Ejemplo:**
```
Si la API de internet se cae, no muestres un error de código rojo. 
Muestra al usuario: 'El sistema está tomando un café, intenta en 5 minutos'.
```

#### TROUBLESHOOTING.md (El Libro de Soluciones)

Un historial de problemas que ya tuvimos y cómo se resolvieron. Si la IA vuelve a cometer el mismo error, le decimos: "Lee el TROUBLESHOOTING.md, ya tuvimos este problema ayer".

### La Regla de Oro de los .md

"Chicos, si abren su proyecto y tienen 15 archivos .md, la IA se va a confundir. Las IA tienen lo que llamamos una 'Ventana de Contexto' (es como la memoria a corto plazo de un humano). Si le damos 50 páginas de instrucciones, olvidará las primeras. **La ingeniería no es acumular, es sintetizar.**"

---

## Fase 7: Herramientas y Flujo de Trabajo

### Estándar Universal vs. Atajos Privativos

**La Metáfora:** Los archivos `.md` genéricos (RULES.md, CONTEXT.md) son un Manual de Instrucciones en Español que dejas sobre la mesa. Cualquier IA (GPT, Claude, Gemini) sabe leer español, así que si le dices "Lee el manual", funcionará.

Las herramientas específicas (Cursor, Copilot) son como empleados bilingües muy eficientes. Para no perder tiempo buscando el manual, ellos tienen un "protocolo secreto": si ven un archivo con un nombre muy especial y extraño (como `.cursorrules`), lo leen automáticamente sin que tú se lo pidas cada vez que abres el proyecto.

### TABLA DE EQUIVALENCIAS: Estándar vs. Todas las Plataformas

**IMPORTANTE:** Cada plataforma de IA tiene su propio nombre "secreto" para el archivo de configuración. Si usas el estándar (RULES.md, CONTEXT.md), funciona en todas. Pero si quieres que la IA lea automáticamente sin que se lo pidas, usa el nombre correcto para cada plataforma.

| Concepto Genérico | Codex (OpenAI) | GitHub Copilot | Claude | Gemini | GLM (ChatGLM) | DeepSeek | Qwen | Z.ai (Zhipu) | Grok (xAI) | OpenCode |
|-------------------|----------------|----------------|--------|--------|---------------|----------|------|--------------|------------|----------|
| **Reglas y Comportamiento** | `CODEX.md` | `.github/copilot-instructions.md` | `CLAUDE.md` | `.gemini/instructions.md` | `GLM.md` | `RULES.md` | `RULES.md` | `ZAI.md` | `GROK.md` | `RULES.md` |
| **Contexto y Arquitectura** | Dentro de `CODEX.md` | Al final de instrucciones | Dentro de `CLAUDE.md` | En `.gemini/instructions.md` | Dentro de `GLM.md` | `CONTEXT.md` | `CONTEXT.md` | Dentro de `ZAI.md` | Dentro de `GROK.md` | `CONTEXT.md` |
| **Seguridad** | Dentro de `CODEX.md` | En instrucciones | Dentro de `CLAUDE.md` | En instrucciones | Dentro de `GLM.md` | `SECURITY.md` | `SECURITY.md` | Dentro de `ZAI.md` | Dentro de `GROK.md` | `SECURITY.md` |
| **Glosario** | Dentro de `CODEX.md` | En instrucciones | Dentro de `CLAUDE.md` | En instrucciones | Dentro de `GLM.md` | `GLOSSARY.md` | `GLOSSARY.md` | Dentro de `ZAI.md` | Dentro de `GROK.md` | `GLOSSARY.md` |

### ¿Por qué hay tantos nombres diferentes?

Cada empresa que creó una IA quiso que su herramienta fuera "la mejor". Para mejorar la experiencia del usuario, programaron sus herramientas para que, al abrir un proyecto, buscaran automáticamente un archivo con **su nombre especial** en la carpeta raíz.

**Analogía:** Es como si cada empleado llegara y buscara su nombre en la puerta de la oficina. Si no encuentra su nombre, no sabe dónde sentarse.

**La solución inteligente:** Si tú creas tus archivos con los nombres estándar (`RULES.md`, `CONTEXT.md`, `SECURITY.md`), **funcionan en todas las plataformas**. Luego, si usas una plataforma específica, solo haces un "copiar y pegar" al nombre correcto.

### Grupo 1: Plataformas con Nombre Propio (usan su propio archivo)

Estas plataformas tienen un archivo "secreto" que leen automáticamente:

| Plataforma | Archivo que lee | Empresa |
|------------|-----------------|---------|
| **Codex** | `CODEX.md` | OpenAI |
| **Claude** | `CLAUDE.md` | Anthropic |
| **Gemini** | `.gemini/instructions.md` | Google |
| **GitHub Copilot** | `.github/copilot-instructions.md` | GitHub/Microsoft |
| **GLM (ChatGLM)** | `GLM.md` | Zhipu AI |
| **Z.ai** | `ZAI.md` | Zhipu AI |
| **Grok** | `GROK.md` | xAI (Elon Musk) |
| **Cursor** | `.cursorrules` | Cursor |

### Grupo 2: Plataformas con Nombres Estándar (usan los genéricos)

Estas plataformas no tienen un archivo "secreto". Usan los nombres genéricos:

| Plataforma | Archivos que busca | Empresa |
|------------|-------------------|---------|
| **DeepSeek** | `RULES.md`, `CONTEXT.md`, `SECURITY.md` | DeepSeek |
| **Qwen** | `RULES.md`, `CONTEXT.md`, `SECURITY.md` | Alibaba |
| **OpenCode** | `RULES.md`, `CONTEXT.md`, `SECURITY.md` | Varias |
| **Cualquier IA web** | Los que tú le pidas que lea | Varias |

### La Lección de Ingeniería

**"Si aprenden a hacer bien sus archivos CONTEXT.md, RULES.md y SECURITY.md, SON INVENCIBLES."**

¿Por qué? Porque si mañana una empresa nueva saca una herramienta llamada "SuperAI" y exige un archivo `.superrules`, ustedes no se asustan. Simplemente abren su RULES.md, copian el texto, lo pegan en `.superrules`, y siguen trabajando.

**Los archivos propietarios (como .cursorrules) cambian. El estándar humano (Markdown bien estructurado) es para siempre.** Construyan primero su conocimiento en `.md` estándar, y luego, si usan Cursor, solo hagan un "copiar y pegar" o una referencia.

### La Gran Lección para los Alumnos

"Chicos, si aprenden a hacer bien sus archivos CONTEXT.md, RULES.md y SECURITY.md, **SON INVENCIBLES**. ¿Por qué? Porque si mañana una empresa nueva saca una herramienta llamada 'SuperAI' y exige un archivo `.superrules`, ustedes no se asustan. Simplemente abren su RULES.md, copian el texto, lo pegan en `.superrules`, y siguen trabajando."

**Los archivos propietarios (como .cursorrules) cambian. El estándar humano (Markdown bien estructurado) es para siempre.** Construyan primero su conocimiento en `.md` estándar, y luego, si usan Cursor, solo hagan un "copiar y pegar" o una referencia.

### Arquitectura Híbrida: "El Equipo Rojo" (Red Teaming)

Este patrón se le llama "Red Teaming" cruzado. Usas un modelo (ej. DeepSeek Coder o Qwen) para **construir** (porque son extremadamente rápidos y buenos generando código estructural), y usas otro modelo (Claude 3.5 Sonnet o GPT-4o) para **destruir/auditar** (porque sobresalen en razonamiento lógico y detección de vulnerabilidades).

**¿Por qué es genial esto?** Porque los modelos de IA tienen "puntos ciegos" dependiendo de con qué datos fueron entrenados. Si DeepSeek se equivoca en una librería de Python, es muy probable que Claude lo atrape, porque sus "cerebros" son arquitectónicamente distintos.

**La Analogía: La Fábrica de Autos**
- **DeepSeek/Qwen:** Son los operarios en la línea de ensamblaje. Construyen las piezas rápido.
- **GPT/Claude:** Son los inspectores de Control de Calidad (QA). Revisan el auto, pero no tienen permiso para tocar las herramientas de la fábrica.
- **Tú:** Eres el Gerente de Planta. Tú decides qué se integra y qué se tira.

### La Estructura de Carpetas Híbrida

```
mi_proyecto_hibrido/
│
├── src/                  # [LA FÁBRICA] Aquí DeepSeek/Qwen escribe el código.
│                         # El auditor NO toca esta carpeta.
│
├── data/                 # [MATERIA PRIMA] Datos que usa el programa.
│
├── .github/              # [REGLAS GLOBALES DE GITHUB] (Por si usas Copilot)
│   └── copilot-instructions.md
│
├── docs/                 # [LA BIBLIOTECA DE CONTEXTO] Ambas IAs leen de aquí.
│   ├── CONTEXT.md        # (Compartido) Qué es el proyecto.
│   ├── GLOSSARY.md       # (Compartido) Términos del negocio.
│   │
│   ├── RULES_CODER.md    # ⚡ NUEVO: Reglas SOLO para el generador.
│   └── RULES_AUDITOR.md  # ⚡ NUEVO: Reglas SOLO para el inspector.
│
├── audits/               # ⚡ NUEVA CARPETA: [LA OFICINA DE CALIDAD]
│   ├── review_v1.md      # Aquí Claude/GPT deja sus informes.
│   ├── security_audit.md # Aquí GPT/Claude anota agujeros de seguridad.
│   └── approved_tasks.md # Tareas que pasaron la auditoría y ya se pueden hacer.
│
├── .gitignore            # Ignora basura y claves.
└── README.md             # Manual del proyecto para humanos.
```

### Los Archivos de Reglas Divididos

#### RULES_CODER.md (Lo que lee DeepSeek/Qwen)

Aquí le dices cómo construir:

```
Eres un desarrollador senior. Escribe código en Python. Usa la librería X. 
Comenta el código en español. No uses funciones obsoletas. 
Entrega el código exclusivamente en la carpeta src/.
```

#### RULES_AUDITOR.md (Lo que lee GPT/Claude) - **¡El archivo más importante!**

Aquí le das el "poder" de destruir, pero con límites estrictos:

```
Eres un Auditor de Ciberseguridad y Código Limpio. 
Tu trabajo NO es escribir código. 
Tu trabajo es leer lo que está en la carpeta src/ y buscar: 
1. Vulnerabilidades de seguridad. 
2. Código ineficiente. 
3. Si cumplió las reglas de RULES_CODER.md.

PROHIBIDO: Modificar ningún archivo en src/.
OBIGATORIO: Escribe todos tus hallazgos y correcciones sugeridas en un nuevo archivo 
dentro de la carpeta audits/.
```

### El Flujo de Trabajo (Cómo se trabaja en la vida real)

1. **Preparación:** Tú creas el CONTEXT.md y las reglas.
2. **Generación (DeepSeek):** Le pides a la IA china que construya el módulo de login. Ella lee RULES_CODER.md, escribe el código y lo pone en `src/login.py`.
3. **Auditoría (Claude/GPT):** Copias el contenido de `src/login.py`, se lo pegas a Claude/GPT junto con RULES_AUDITOR.md y le dices: "Audita esto".
4. **El Informe:** Claude te responde: "Encontré un fallo de seguridad grave en la línea 12, están guardando la contraseña sin encriptar. Además, el código es ineficiente. Sugiero cambiar X por Y".
5. **Corrección (El humano o DeepSeek de nuevo):** Tú (o le pides a DeepSeek) tomas el informe de la auditoría y arreglas el `src/login.py`.

**Lección de Pensamiento Crítico:**

"Chicos, el error del principiante es poner a dos IAs a hablar en el mismo chat y decirles: 'Oigan, compórtense'. Eso genera caos. El trabajo del ingeniero es diseñar tuberías (carpetas y archivos .md) para que la información fluya en una sola dirección. **Construcción -> Auditoría -> Corrección**."

---

## Fase 8: Las Licencias de Software — El "Contrato de Vecindad" de tu Proyecto

### ¿Qué es una licencia y por qué debería importarme?

**La Analogía:** Imagina que construyes una casa. Si no pones un letrero en la puerta que diga "Propiedad Privada" o "Entrada Permitida", cualquier persona puede entrar, usar tu cocina, dormir en tu cama y llevarse tus muebles. Una **licencia de software** es ese letrero. Le dice al mundo: "Esto es mío, y estas son las reglas si quieres usarlo".

**En palabras simples:** Una licencia es un contrato legal (escrito en lenguaje simple) que el creador de un programa pone para decirle a la gente qué puede, qué no puede, y qué debe hacer si usa su código.

**¿Por qué importa en IA?** Porque cuando usas una librería de Python, un modelo de IA pre-entrenado, o cualquier herramienta de código abierto, **estás aceptando una licencia**. Si no la lees, podrías estar rompiendo la ley sin saberlo. Un ingeniero de IA debe saber reconocer y respetar las licencias.

---

### Las 3 Grandes Categorías de Licencias

Piensa en las licencias como un semáforo de tres colores:

```
🟢 VERDE (Permisivas)     → Puedes hacer casi lo que quieras.
🟡 AMARILLO (Copyleft)    → Puedes usar, PERO si modificas, debes compartir.
🔴 ROJO (Propietarias)    → Solo el dueño puede usar, modificar o vender.
```

---

### 🟢 CATEGORÍA 1: Licencias Permisivas (El "Haz lo que quieras")

Estas licencias son como decir: "Toma mi código, úsalo, mételo en tu proyecto comercial, no me tienes que dar nada a cambio. Solo acuérdate de que yo lo hice".

#### A. MIT — La licencia más popular del mundo

**Analogía:** Es como darle una receta de cocina a alguien. Puede vender el plato, cambiar los ingredientes, ponerle su nombre al restaurante, y no te debe ni un centavo. Solo tiene que poner una小 nota en algún lado diciendo "La receta original fue de fulano".

**Cómo la reconoces:** El archivo `LICENSE` o `LICENSE.txt` empieza así:

```
MIT License

Copyright (c) [año] [nombre del autor]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software")...
```

**Qué puedes hacer:**
- Usar el código en proyectos personales o comerciales
- Modificarlo libremente
- Distribuirlo
- Vender productos que lo incluyan

**Qué DEBES hacer:**
- Incluir el aviso de copyright (el "acuérdate de quién lo hizo")
- Incluir la licencia MIT completa en tu copia

**Cuándo elegirla:** Cuando quieres que tu proyecto sea lo más abierto posible y no te importa que otros se lucran de él. Es la licencia de Python, React, TensorFlow, y miles de herramientas de IA.

**Ejemplo real:** Si descargas una librería de Python con licencia MIT, puedes meterla en tu app de IA y venderla sin pagarle nada al creador original.

---

#### B. Apache 2.0 — La MIT "con seguro incluido"

**Analogía:** Es como la MIT pero con una cláusula extra: "Si mi código le causa un problema a alguien y te demandan, yo no me hago responsable. Tú te haces cargo". Además, si modificas el código, **debes avisar** qué cambiaste.

**Cómo la reconoces:**

```
Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/

Licensed under the Apache License, Version 2.0...
```

**Qué puedes hacer:**
- Todo lo que en MIT (usar, modificar, vender, distribuir)

**Qué DEBES hacer:**
- Incluir el aviso de copyright
- Indicar si hiciste cambios en el código
- Incluir la licencia Apache completa

**Diferencia clave con MIT:** Apache 2.0 tiene una **cláusula de patentes** que protege al usuario. Si el creador original tiene una patente sobre el código, no te puede demandar por usarlo. MIT no tiene esta protección.

**Cuándo elegirla:** Cuando tu proyecto usa patentes o cuando quieres protección extra para los usuarios. Google la usa mucho (TensorFlow, Android).

---

#### C. BSD 2-Clause — La MIT "abuela"

**Analogía:** La licencia más simple que existe. Es como decir: "Haz lo que quieras, pero no digas que yo te lo recomendé si sale mal".

**Cómo la reconoces:**

```
BSD 2-Clause License

Copyright (c) [año], [nombre del autor]
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met...
```

**Las 2 condiciones (las únicas):**
1. Debes mantener el aviso de copyright
2. No puedes usar el nombre del creador para promocionar tu producto sin permiso

**Cuándo elegirla:** Para proyectos muy simples donde no necesitas la protección de patentes de Apache. Muchos proyectos científicos y académicos la usan.

---

#### D. BSD 3-Clause — La BSD 2-Clause "con una regla más"

**Analogía:** Igual que BSD 2-Clause, pero con una regla extra: "Y tampoco puedes poner mi nombre en los créditos de tu producto como si yo hubiera participado".

**Cómo la reconoces:** Similar a BSD 2-Clause pero con esta línea adicional:

```
Neither the name of the copyright holder nor the names of its
contributors may be used to endorse or promote products derived from
this software without specific prior written permission.
```

**Cuándo elegirla:** Cuando no quieres que nadie use tu nombre (o el de tu empresa) para darle "credibilidad" a su producto sin tu permiso.

---

### 🟡 CATEGORÍA 2: Licencias Copyleft (El "Compártilo o Else")

Estas licencias son como decir: "Puedes usar mi código, PERO si lo modificas y lo distribuyes, tu versión modificada DEBE ser también de código abierto con la misma licencia".

#### E. GPL v3 (GNU General Public License) — La licencia "viral"

**Analogía:** Es como darle una receta de cocina con una regla mágica: "Si cambias un ingrediente, **toda** la receta nueva que creaste DEBE ser compartida gratis con el mundo. No puedes hacer una versión secreta".

**Cómo la reconoces:**

```
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright (C) 2007 Free Software Foundation, Inc.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation...
```

**Qué puedes hacer:**
- Usar el código libremente
- Modificarlo
- Distribuirlo

**Qué DEBES hacer:**
- Si distribuyes tu producto (lo vendes o lo das), **TODO** el código fuente que use GPL también debe ser abierto
- Tus modificaciones deben llevar la misma licencia GPL
- Debes incluir el código fuente completo

**⚠️ La trampa del "viral":** Si tu proyecto usa una librería GPL y tú lo distribuyes, **todo tu proyecto se vuelve GPL**. No puedes tener partes propietarias. Es como un virus: se contagia a todo lo que toca.

**Cuándo elegirla:** Cuando quieres garantizar que tu código y el de todos los que lo usen sea siempre libre. Linux usa GPL. Si haces una herramienta de IA para uso interno de tu empresa (no la vendes), GPL no te afecta. Solo aplica cuando distribuyes.

---

#### F. LGPL v3 — La GPL "suave"

**Analogía:** Es como la GPL pero con una excepción: "Si tu programa solo **llama** a mi librería pero no la modifica, no tienes que abrir todo tu código. Solo si abres la librería misma".

**Cómo la reconoces:**

```
GNU LESSER GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

This library is free software...
```

**Diferencia con GPL:** LGPL permite que software propietario use la librería sin contagiarse. Solo aplica si modificas la librería en sí.

**Cuándo elegirla:** Cuando quieres que tu librería sea abierta pero permitas que otros la usen en software cerrado.

---

#### G. MPL 2.0 (Mozilla Public License) — La "pared de ladrillos"

**Analogía:** Es como tener un apartamento en un edificio. Tú puedes pintar tu pared de color rosa si quieres, pero **no puedes cambiar las paredes del edificio** (el código que compartes con otros). Cada archivo tiene su propia "región".

**Cómo la reconoces:**

```
Mozilla Public License Version 2.0
==================================

1. Definitions.
1.1. "Contributor"
...
```

**Qué significa en la práctica:** Si modificas un archivo con MPL, ese archivo debe ser abierto. Pero el resto de tu proyecto puede ser propietario.

**Cuándo elegirla:** Cuando quieres copyleft pero sin ser tan "viral" como GPL. Firefox usa MPL.

---

### 🔴 CATEGORÍA 3: Licencias Propietarias (El "No Tocar")

#### H. Licencias Propietarias / Comerciales

**Analogía:** Es como un restaurante con receta secreta. No puedes ver la receta, no puedes copiarla, y si intentas, te demandan. Solo puedes comer ahí (usar el software) si pagas.

**Cómo las reconoces:** No tienen el texto de una licencia estándar. En su lugar, ves algo como:

```
PROPRIETARY AND CONFIDENTIAL

Copyright (c) [Empresa]. All rights reserved.

This software is proprietary and confidential. Unauthorized copying,
modification, distribution, or use of this software is strictly prohibited.
```

O simplemente un "Acuerdo de Licencia de Usuario Final" (EULA) largo y complicado.

**Qué puedes hacer:**
- Usar el software según lo que pagaste
- Nada más

**Qué NO puedes hacer:**
- Ver el código fuente
- Modificarlo
- Compartirlo
- Vender copias

**Ejemplos:** ChatGPT Plus, Claude Pro, herramientas de Adobe, Microsoft Office.

**Cuándo las ves en IA:** Cuando usas una API como la de OpenAI, estás aceptando sus condiciones de uso (que son propietarias). Puedes usar el resultado, pero no el modelo en sí.

---

### 🔵 CATEGORÍA 4: Creative Commons (Para Contenido, No Código)

**Analogía:** Creative Commons no es para software, sino para **contenido**: fotos, textos, videos, datasets. Si estás entrenando una IA con imágenes o textos, necesitas saber de esto.

#### I. CC BY — La más permisiva

"Puedes usar mi foto para lo que quieras, solo pon mi nombre".

#### J. CC BY-SA — "Pon mi nombre y si la modificas, compártela igual"

Igual que CC BY, pero tu versión modificada debe llevar la misma licencia.

#### K. CC BY-NC — "Pon mi nombre, pero NO la uses para ganar dinero"

No puedes usar el contenido en productos comerciales.

#### L. CC BY-ND — "Pon mi nombre, pero NO la modifiques"

Puedes compartirla, pero no puedes hacer remixes.

#### M. CC0 — "No necesitas mi permiso"

Es como si no hubiera licencia. El contenido es de dominio público.

**¿Por qué importa esto en IA?** Si entrenas una IA con imágenes con licencia CC BY-NC (no comercial), y luego vendes un producto con esas imágenes, estás violando la licencia. **Los datos tienen licencia, y los ingenieros de IA deben respetarlas.**

---

### Tabla Resumen: ¿Cuál Elijo?

| Situación | Licencia Recomendada | ¿Por qué? |
|-----------|---------------------|------------|
| Quiero que todos usen mi código sin problemas | **MIT** | La más simple y permisiva |
| Mi proyecto usa patentes | **Apache 2.0** | Protección de patentes incluida |
| Quiero que todos compartan sus mejoras | **GPL v3** | "Viral": obliga a abrir código modificado |
| Quiero copyleft pero sin ser tan estricto | **LGPL v3** o **MPL 2.0** | Copyleft parcial |
| No quiero que nadie vea mi código | **Propietaria** | Control total |
| Tengo fotos, textos o datasets | **Creative Commons** | Licencias para contenido |
| Quiero dedicarlo al dominio público | **CC0** | Sin restricciones |

---

### Cómo Reconocer una Licencia (El Truco del Ingeniero)

No necesitas leer 50 páginas de texto legal. Hay 3 pasos rápidos:

**Paso 1: Busca el archivo `LICENSE` o `LICENSE.txt`**
En la carpeta raíz de cualquier proyecto de código abierto, siempre hay un archivo con ese nombre. Si no lo ves, busca `COPYING`.

**Paso 2: Lee las primeras 3 líneas**
- Si ves "MIT License" → Es MIT
- Si ves "Apache License" → Es Apache
- Si ves "GNU GENERAL PUBLIC" → Es GPL
- Si ves "BSD" → Es BSD
- Si ves "Mozilla Public" → Es MPL

**Paso 3: Busca la palabra clave**
- "permitted" o "free of charge" → Permisiva (verde)
- "must distribute under the same license" → Copyleft (amarillo)
- "proprietary" o "confidential" → Propietaria (rojo)

---

### El Ingeniero de IA y las Licencias

**¿Por qué un ingeniero de IA necesita saber esto?**

1. **Al usar librerías:** Si tu proyecto usa una librería GPL y la vas a vender, necesitas abrir todo tu código. Apache o MIT no te obligan a eso.

2. **Al entrenar modelos:** Si entrenas un modelo con datos con licencia CC BY-NC, no puedes vender el modelo entrenado con esos datos.

3. **Al compartir código:** Si creas una herramienta de IA y la compartes, la licencia que elijas determina si otros pueden usarla, modificarla o venderla.

4. **Al recibir código:** Si la IA te genera código basado en una librería GPL, tú estás recibiendo código con esas restricciones. Debes saberlo.

**Regla de oro del ingeniero:** "Si no sé qué licencia tiene, **no la uso** hasta averiguarlo."

---

### Ejemplo Práctico: Decisión de Licencia para un Proyecto de IA

Imagina que estás construyendo un chatbot para una clínica veterinaria:

```
Opción 1: MIT
→ La clínica puede usarlo, modificarlo, y venderlo si quiere.
→ Cualquier otra clínica puede copiarlo.
→ Ventaja: Simple. Desventaja: Sin protección.

Opción 2: GPL v3
→ Si la clínica lo distribuye, debe abrir todo el código.
→ Ventaja: Contribución a la comunidad. Desventaja: La clínica pierde control.

Opción 3: Propietaria
→ Solo la clínica puede usarlo. Nadie puede copiarlo.
→ Ventaja: Control total. Desventaja: No puede compartir mejoras con otras clínicas.
```

**¿Cuál es la correcta?** Depende del contexto del negocio. **Ahí es donde entra el criterio del ingeniero.**

---

### La Estructura de Carpetas con Licencias

Cuando creas un proyecto, agrega la licencia en la raíz:

```
mi_proyecto_de_ia/
│
├── data/
├── src/
├── models/
├── docs/
├── tests/
│
├── LICENSE              # ← AQUÍ VA TU LICENCIA
├── README.md            # (Opcional: mencionar la licencia aquí también)
├── .gitignore
└── RULES.md
```

**Consejo:** En el `README.md` de tu proyecto, siempre agrega una sección:

```markdown
## Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.
```

---

### Errores Comunes (y Cómo Evitarlos)

| Error | Consecuencia | Cómo Evitarlo |
|-------|-------------|---------------|
| Usar código GPL sin saberlo en un producto comercial | Te pueden demandar para que abras todo tu código | **Siempre lee la LICENSE antes de usar una librería** |
| No incluir la licencia cuando redistribuyes | Estás violando la licencia | **Copia el archivo LICENSE a tu proyecto** |
| Confundir Creative Commons con licencias de software | Entrenar una IA con datos con restricciones | **CC es para contenido, no para código** |
| Poner "Copyright © Mi Empresa" sin licencia | Nadie puede usar tu código (es propietario por defecto) | **Siempre incluye una licencia explícita** |

---

### Resumen Visual de Licencias

```
                    PERMISIVIDAD
    ◄─────────────────────────────────────►
    MÁS LIBRE                         MENOS LIBRE

    CC0    MIT    Apache    MPL    LGPL    GPL    Propietaria
     │      │       │       │       │       │        │
     │      │       │       │       │       │        │
     ▼      ▼       ▼       ▼       ▼       ▼        ▼
   Todo   Usar   Usar +   Usar +  Usar +  Usar +  Solo
   libre  libre  patentes parede  lib     viral   pagar
                               abierta          y usar
```

---

## Cierre de la Clase

### Reflexión Final

"Como directores de proyecto de IA, su trabajo no es saberse de memoria cómo se instala Python. Su trabajo es **diseñar el entorno** para que la IA y los programadores puedan trabajar de forma segura, ordenada y eficiente. Un buen RULES.md y una buena estructura de carpetas vale más que mil líneas de código desordenado."

### La IA es un Aprendiz de Obra

"¿Por qué les estoy enseñando esto si nosotros NO vamos a programar? Porque la IA es como un aprendiz de obra súper rápido, pero muy torpe y desordenado por naturaleza. Si tú no le aplicas estas reglas, la IA te va a construir un Monstruo Espagueti pegado con Super Pegamento en 3 segundos."

**Nuestro trabajo como directores de IA no es escribir el código. Nuestro trabajo es usar los archivos .md para gritarle las reglas al aprendiz antes de que empiece a trabajar.** Si ponemos en nuestro RULES.md la regla del "Especialista", la IA generará archivos ordenados. Si no, nos entregará un desastre.

---

## El Ingeniero de IA en esta Clase

En esta clase hemos aprendido que el Ingeniero de IA es **el diseñador del entorno**. No es el que escribe más código, sino el que:

1. **Decide dónde vive la IA** (local, API, VPS)
2. **Diseña la estructura de carpetas** (data/, src/, models/)
3. **Escribe las reglas** (CONTEXT.md, RULES.md, SECURITY.md)
4. **Protege los datos** (.gitignore, .env, SECURITY.md)
5. **Supervisa el trabajo** (flujo de generación -> auditoría -> corrección)

**Herramientas que usamos hoy:**
- Archivos `.md` para controlar el comportamiento de la IA
- Estructura de carpetas para organizar el proyecto
- Convenciones de nombres para evitar errores
- Principios de ingeniería para mantener la calidad

**Próximos pasos:** En las siguientes clases, aprenderemos a aplicar estos principios en proyectos reales, conectando la arquitectura con las herramientas de desarrollo.