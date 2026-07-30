# Glosario de la Clase 5: Arquitectura, Estructura y Mentalidad de Ingeniería para IA

## Términos Clave explicados con analogías

### A

#### API (Interfaz de Programación de Aplicaciones)
**Analogía:** Uber Eats para la computadora. Tú no cocinas (no tienes un servidor potente), envías la petición por internet, alguien poderoso cocina (los servidores de OpenAI, Google, etc.), y te devuelven el resultado cocinado.

**En palabras simples:** Es como llamar a un experto por teléfono. Le dices qué necesitas y él te devuelve la respuesta, pero tú no tienes que tener toda la maquinaria en casa.

---

### C

#### CODEX.md
**Analogía:** El manual de instrucciones que le dejas a un empleado de OpenAI. Si el archivo se llama `CODEX.md`, el empleado lo lee automáticamente sin que se lo pidas.

**En palabras simples:** Es el nombre "secreto" que usa la plataforma Codex (de OpenAI) para buscar instrucciones. Si creas un archivo con ese nombre en la raíz de tu proyecto, Codex sabrá cómo comportarse automáticamente.

---

#### camelCase
**Analogía:** Como las jorobas de un camello. La primera palabra va en minúscula y las siguientes empiezan con mayúscula: `procesadorDeTexto`.

**En palabras simples:** Un estilo de escribir nombres sin espacios, donde cada palabra nueva "sube" una letra. Se usa mucho en páginas web, pero NO en archivos de Python/IA.

---

#### CONTEXT.md
**Analogía:** El currículum de vida que le das a un nuevo empleado. Le explicas quién eres, qué hace tu empresa, y qué esperas de él.

**En palabras simples:** Un archivo de texto donde le cuentas a la IA: "Somos esto, hacemos aquello, y nuestro objetivo es este". Sin esto, la IA te responde como si fueras cualquier usuario genérico.

---

#### Convención de nombres
**Analogía:** Las reglas de naming de calles en una ciudad. Si unas calles se llaman "Av. Principal", otras "avenida_principal" y otras "avenidaprincipal", los taxistas se vuelven locos.

**En palabras simples:** Reglas acordadas para nombrar archivos y carpetas (como usar snake_case, cero espacios, etc.) para que todos (humanos, IA, computadoras) se entiendan.

---

### D

#### DATA
**Analogía:** Los ingredientes de una receta. Sin harina, huevos y azúcar, no hay pastel.

**En palabras simples:** La carpeta donde guardas los archivos que la IA va a leer o procesar: PDFs, imágenes, hojas de cálculo, etc.

---

#### DECISIONES.md
**Analogía:** El diario personal de un ingeniero donde anota POR QUÉ tomó cada decisión importante. "Elegí esta carb因为她 porque la otra se rompía".

**En palabras simples:** Un archivo donde documentas las razones detrás de tus decisiones técnicas, para que la IA (y tú mismo dentro de 6 meses) entiendas por qué las cosas son como son.

---

### E

#### Entorno Virtual (.venv)
**Analogía:** Un frasco de cristal esterilizado para cada experimento. Lo que pasa dentro del frasco, no afecta al resto de la cocina.

**En palabras simples:** Una "burbuja" aislada en tu computadora donde instalas las herramientas específicas de un proyecto, para que no choquen con las de otro proyecto.

---

#### Estructura de carpetas
**Analogía:** Un archivero con cajones etiquetados. Si tiras todos los papeles sueltos en un solo cajón, encontrar algo es imposible.

**En palabras simples:** La forma en que organizas los archivos de tu proyecto en carpetas con nombres claros y lógicos.

---

### G

#### GLOSSARY.md
**Analogía:** Un diccionario personalizado para tu empresa. Cuando alguien dice "El Sistema Raptor", el diccionario explica que eso significa "el módulo de facturación antiguo".

**En palabras simples:** Un archivo donde listas todas las siglas, términos raros y jerga específica de tu negocio, para que la IA no se confunda ni se invente significados.

---

#### GLM.md
**Analogía:** El manual de instrucciones que le dejas a un empleado de ChatGLM (Zhipu AI). Si el archivo se llama `GLM.md`, el empleado lo lee automáticamente.

**En palabras simples:** Es el nombre "secreto" que usa la plataforma GLM (ChatGLM de Zhipu AI) para buscar instrucciones. Si creas un archivo con ese nombre, GLM sabrá cómo comportarse automáticamente.

---

#### GROK.md
**Analogía:** El manual de instrucciones que le dejas a un empleado de xAI (la empresa de Elon Musk). Si el archivo se llama `GROK.md`, el empleado lo lee automáticamente.

**En palabras simples:** Es el nombre "secreto" que usa la plataforma Grok (de xAI) para buscar instrucciones. Si creas un archivo con ese nombre, Grok sabrá cómo comportarse automáticamente.

---

#### Gitignore

---

### K

#### KISS (Keep It Simple, Stupid)
**Analogía:** Si necesitas colgar un cuadro, usas un clavo y un martillo. No construyes una grúa telescópica "por si acaso mañana quieres colgar un elefante".

**En palabras simples:** No compliques las cosas. Construye solo lo que necesitas, de la forma más simple posible. Mañana ya verás si necesitas algo más complejo.

---

### M

#### Markdown (.md)
**Analogía:** Un archivo de texto con "decoraciones" sencillas (negritas, listas, títulos) que se ve bonito tanto en la computadora como en internet.

**En palabras simples:** Un formato de escribir texto plano que cualquier IA puede leer y entender, y que tú puedes leer sin ser programador. Es el idioma universal para dar instrucciones a la IA.

---

#### Microservicios
**Analogía:** Un restaurante gigante con 10 equipos especializados: uno solo para cobrar, otro solo para parrilla, otro solo para bebidas. Cada equipo tiene su propia nevera.

**En palabras simples:** Dividir un programa grande en muchos programas pequeños e independientes. Es ideal para empresas gigantes como Netflix, pero es un infierno si eres principiante.

---

#### Monolito
**Analogía:** Un food truck. Tú tomas el pedido, tú cocinas, tú cobras, y todo está en un espacio de 5 metros.

**En palabras simples:** Un programa donde TODO está junto: la lógica, los datos, la conexión con la IA. Es barato, rápido de armar, y perfecto para empezar.

---

### P

#### PascalCase
**Analogía:** Como un nombre propio donde todas las palabras empiezan con mayúscula: `ModeloDeIA`.

**En palabras simples:** Un estilo de escribir nombres donde cada palabra nueva empieza con mayúscula. Se usa para nombrar "Clases" (moldes para crear cosas) en programación.

---

#### PERSONAS.md
**Analogía:** La ficha de un actor que va a interpretar un papel. Le defines su edad, su forma de ser, y cómo debe hablar.

**En palabras simples:** Un archivo donde defines A QUIÉN le habla la IA. Ej: "Hablas con Pedro, un contador de 50 años que sabe usar Excel pero odia la tecnología."

---

### R

#### RESPONSABILIDAD ÚNICA
**Analogía:** No contrates a una persona que sea a la vez médico, contador, mecánico y chef. Si se enferma, se arruina todo.

**En palabras simples:** Cada archivo o programa debe hacer UNA sola cosa bien. Un archivo que lee PDFs no debería también enviar correos.

---

#### RULES.md
**Analogía:** El manual de empleo que le das a un nuevo trabajador. Le dices cómo debe comportarse, qué debe hacer y qué NO debe hacer.

**En palabras simples:** Un archivo donde escribes las reglas estrictas que la IA debe seguir. Ej: "Nunca inventes datos", "Responde en máximo 3 párrafos".

---

### S

#### Seguridad
**Analogía:** El candado de tu casa. No es una característica "bonita", es algo que NECESITAS para que no te roben.

**En palabras simples:** Proteger tus datos sensibles (contraseñas, información de clientes) para que la IA no los muestre accidentalmente o que se suban a internet.

---

#### Separación de Conceptos
**Analogía:** En un restaurante, la cocina no es la caja. El chef no cuenta dinero, y el cajero no cocina.

**En palabras simples:** No mezcles cosas diferentes en el mismo archivo o carpeta. Los datos van en `data/`, el código en `src/`, y la documentación en `docs/`.

---

#### Serverless
**Analogía:** En lugar de comprar un auto (VPS), usas Uber. Pagas solo el viaje. Si te quedas en casa todo el día, pagas $0.

**En palabras simples:** Un sistema donde no alquilas un servidor encendido 24/7. Pagas solo los milisegundos que tu IA tarda en pensar. Ideal para tareas esporádicas.

---

#### snake_case
**Analogía:** Como una serpiente que se arrastra entre palabras: `mi_archivo_de_ia.py`.

**En palabras simples:** Un estilo de escribir nombres donde todo va en minúsculas y las palabras se separan con guion bajo (_). **Es el estándar para archivos de Python/IA.**

---

### Z

#### ZAI.md
**Analogía:** El manual de instrucciones que le dejas a un empleado de Zhipu AI (la empresa china que creó ChatGLM). Si el archivo se llama `ZAI.md`, el empleado lo lee automáticamente.

**En palabras simples:** Es el nombre "secreto" que usa la plataforma Z.ai (de Zhipu AI) para buscar instrucciones. Si creas un archivo con ese nombre, Z.ai sabrá cómo comportarse automáticamente.

---

### O

#### OpenCode
**Analogía:** Una herramienta de programación que funciona como un "asistente general". No tiene un archivo "secreto" propio, así que usa los nombres estándar (RULES.md, CONTEXT.md, SECURITY.md).

**En palabras simples:** Es una plataforma de IA para programar que no tiene un nombre especial para sus archivos. Por eso usa los genéricos. Si ya tienes tus archivos estándar creados, OpenCode los leerá sin problemas.

---

### V

#### VPS (Servidor Privado Virtual)
**Analogía:** Alquilar un local comercial. Es tuyo, está encendido 24/7, cualquiera puede entrar por la puerta principal.

**En palabras simples:** Un servidor en internet que alquilas por un precio mensual. Ahí puedes instalar tu programa y que esté disponible para todos, siempre.

---

### Y

#### YAGNI (You Ain't Gonna Need It)
**Analogía:** No construyas una grúa para colgar un cuadro. Si mañana necesitas la grúa, ya la construyes.

**En palabras simples:** No hagas cosas "por si acaso" las necesitas en el futuro. Construye solo lo que necesitas HOY.