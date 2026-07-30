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

---

## Terminos de Licencias (Fase 8)

### BSD (Berkeley Software Distribution)
**Analogía:** La licencia mas simple del mundo. Es como decir: "Toma mi codigo, haz lo que quieras, solo no digas que yo te lo recomendé si sale mal".

**En palabras simples:** Una licencia permisiva con solo 2 o 3 reglas basicas. Muy usada en proyectos academicos y cientificos. No tiene proteccion de patentes como Apache.

---

### Copyleft
**Analogía:** Es como una regla magica que dice: "Si modificas esta receta, tu version nueva DEBE ser compartida gratis con el mundo. No puedes hacer una version secreta".

**En palabras simples:** Un tipo de licencia que obliga a que, si modificas el codigo y lo compartes, tu version modificada sea tambien de codigo abierto con la misma licencia. GPL es el ejemplo mas conocido.

---

### Creative Commons (CC)
**Analogía:** Licencias para contenido, no para codigo. Es como poner un letrero en tus fotos que dice: "Puedes usar mis fotos, PERO pon mi nombre" o "Puedes usarlas, pero no para vender".

**En palabras simples:** Un conjunto de licencias para fotos, textos, videos y datasets. Si entrenas una IA con datos con licencia CC, debes respetar las condiciones (por ejemplo, no usarlos para fines comerciales si la licencia lo prohibe).

---

### Dominio Publico (CC0)
**Analogía:** Es como si el contenido nunca hubiera tenido dueño. Nadie posee nada, todos pueden hacer lo que quieran.

**En palabras simples:** Cuando algo esta en dominio publico, no hay copyright ni restricciones. Puedes copiar, modificar y vender sin pedir permiso ni dar creditos.

---

### EULA (End User License Agreement)
**Analogía:** El contrato largo y aburrido que aceptas sin leer cuando instalas un programa. "Acepto" sin saber que aceptaste.

**En palabras simples:** Un contrato de licencia de usuario final. Es el documento legal que aceptas cuando instalas software propietario (como Microsoft Office o un juego de Steam).

---

### GPL (GNU General Public License)
**Analogía:** Es como dar una receta con una regla magica: "Si cambias un ingrediente, TODA la receta nueva DEBE ser compartida gratis. No puedes tener partes secretas".

**En palabras simples:** La licencia "viral" mas conocida. Si usas codigo GPL en tu proyecto y lo distribuyes, TODO tu proyecto se vuelve GPL. Debes abrir todo el codigo fuente. Linux usa GPL.

---

### LGPL (GNU Lesser General Public License)
**Analogía:** Como GPL pero mas suave. "Puedes usar mi libreria en tu restaurante privado, pero si modificas la libreria en si, esa parte DEBE ser abierta".

**En palabras simples:** Una version de GPL que permite que software propietario use la libreria sin contagiarse. Solo aplica si modificas la libreria misma, no si solo la llamas.

---

### Licencia
**Analogía:** Un letrero en la puerta de tu casa que dice quien puede entrar, que puede hacer, y que no puede hacer. Sin letrero, cualquiera entra y hace lo que quiera.

**En palabras simples:** Un contrato legal que el creador de un programa pone para decirle al mundo que puede, que no puede, y que debe hacer si usa su codigo. Sin licencia, el codigo es propietario por defecto.

---

### Licencia Propietaria / Comercial
**Analogía:** Un restaurante con receta secreta. No puedes ver la receta, no puedes copiarla, y si intentas, te demandan. Solo puedes comer ahi si pagas.

**En palabras simples:** Una licencia que no permite ver, modificar ni compartir el codigo fuente. Solo puedes usar el software segun lo que pagaste. Ejemplos: Adobe Photoshop, Microsoft Office.

---

### MIT License
**Analogía:** Darle una receta de cocina a alguien. Puede vender el plato, cambiar los ingredientes, ponerle su nombre, y no te debe nada. Solo tiene que poner una nota diciendo "La receta original fue de fulano".

**En palabras simples:** La licencia mas permisiva y popular del mundo. Puedes usar, modificar, vender y distribuir el codigo sin casi ninguna restriccion. Solo debes incluir el aviso de copyright. Python, React y TensorFlow la usan.

---

### MPL (Mozilla Public License)
**Analogía:** Como tener un apartamento en un edificio. Tu puedes pintar tu pared de color rosa, pero no puedes cambiar las paredes del edificio. Cada archivo tiene su propia "region".

**En palabras simples:** Un copyleft "por archivo". Si modificas un archivo con MPL, ese archivo debe ser abierto. Pero el resto de tu proyecto puede ser propietario. Firefox usa MPL.

---

### No Comercial (NC en Creative Commons)
**Analogía:** "Puedes usar mi foto para tu album familiar, pero no la uses para vender algo o hacer publicidad".

**En palabras simples:** Una restriccion de Creative Commons que impide usar el contenido para fines que generen dinero. Si entrenas una IA con datos NC, no puedes vender el modelo entrenado con esos datos.

---

### Permisiva (Licencia)
**Analogía:** Un vecino que te dice: "Toma mi herramienta, usala como quieras, no me des nada a cambio". Es el tipo de licencia mas generosa.

**En palabras simples:** Licencias que permiten usar, modificar y distribuir el codigo con muy pocas restricciones (generalmente solo incluir el creditos del autor). MIT, Apache y BSD son permisivas.

---

### Viral (Licencia)
**Analogía:** Un virus que se contagia a todo lo que toca. Si tu codigo "toca" codigo GPL, todo tu codigo se vuelve GPL automaticamente.

**En palabras simples:** Una licencia (como GPL) que se "propaga" a cualquier codigo que la use. Si integras codigo GPL en tu proyecto, todo tu proyecto debe ser GPL tambien.

---

## Terminos de API y Seguridad (Practica 2)

### API Key (Llave de API)
**Analogia:** Es como la llave de tu casa. Si alguien la tiene, puede entrar. Tu llave abre TU puerta, no la de tu vecino.

**En palabras simples:** Una cadena de texto larga (como `sk-abc123...`) que le dice al servicio de IA: "Soy fulano, y tengo permiso para usar este servicio". Sin ella, el servicio no te deja pasar. **NUNCA la compartas ni la subas a GitHub.**

---

### .env (Archivo de Variables de Entorno)
**Analogia:** Es como una caja fuerte donde guardas tus llaves secretas. El codigo la lee, pero nadie mas puede verla.

**En palabras simples:** Un archivo de texto donde guardas las llaves de API (contrasenas). El script lo lee al iniciar, pero NUNCA se sube a GitHub porque esta en el `.gitignore`.

---

### .venv (Entorno Virtual)
**Analogia:** Un frasco de cristal esterilizado para cada experimento. Lo que pasa dentro del frasco, no afecta al resto de la cocina.

**En palabras simples:** Una "burbuja" aislada en tu computadora donde instalas las librerias especificas de un proyecto, para que no choquen con las de otro proyecto. Se crea con `python -m venv .venv` y se activa con `.venv\Scripts\activate`.

---

### Google Gemini
**Analogia:** El asistente personal gratuito de Google. Le puedes hacer preguntas por la terminal y te responde. Es como tener un chatGPT gratis.

**En palabras simples:** La IA de Google. Tiene un nivel gratuito generoso (1500 preguntas al dia sin pagar). Es la mejor opcion para empezar a aprender sobre APIs.

---

### DeepSeek
**Analogia:** El operario chino super eficiente. Hace el mismo trabajo que GPT pero cuesta una fraccion del precio ($0.14 por millon de caracteres).

**En palabras simples:** Una IA china muy potente y muy barata. Usa la misma "interface" que OpenAI, asi que el codigo es casi identico.

---

### OpenRouter
**Analogia:** Un supermercado de IAs. Con UNA sola llave, puedes elegir entre docenas de modelos (GPT, Claude, Llama, Gemini, etc.).

**En palabras simples:** Un servicio que te da acceso a multiples IAs con una sola cuenta. Algunos modelos son gratuitos. Ideal para comparar respuestas de diferentes IAs.

---

### OpenAI / GPT
**Analogia:** La marca "Coca-Cola" de las IAs. Es la mas conocida, la mas usada, pero tambien la mas cara.

**En palabras simples:** La empresa que creo ChatGPT. Su API es la mas popular pero requiere tarjeta de credito. El modelo mas barato es `gpt-4o-mini`.

---

### Claude (Anthropic)
**Analogia:** El profesor universitario. Muy preciso, muy cuidadoso con la seguridad, pero cobra mas que el resto.

**En palabras simples:** La IA de Anthropic. Es conocida por ser muy precisa y segura. Usa su propia libreria `anthropic` (no es compatible con OpenAI).

---

### Temperature (Temperatura)
**Analogia:** Un dial que va de "robot exacto" (0.0) a "artista loco" (1.0). En 0.0 siempre dice lo mismo. En 1.0 se inventa cosas diferentes cada vez.

**En palabras simples:** Un numero que le dice a la IA que tan creativa debe ser. 0.0 = respuestas exactas y predecibles. 1.0 = respuestas creativas y variables. 0.7 = buen punto medio.

---

### Tokens
**Analogia:** Las "palabras" que la IA usa para medir. Cuesta dinero por cada 1000 tokens que usa.

**En palabras simples:** La unidad de medida de las IAs. Un token es aproximadamente 3/4 de una palabra en ingles. Las APIs cobran por tokens: mas tokens = mas caro. Por eso hay limites de longitud en las respuestas.

---

### Terminal / Linea de Comandos
**Analogia:** Es como hablar con la computadora por texto, sin usar el mouse ni iconos bonitos. Es como un chat antiguo de los anos 80.

**En palabras simples:** Una ventana donde escribes comandos de texto para decirle a la computadora que haga cosas. En Windows se llama "PowerShell" o "CMD". En Mac/Linux se llama "Terminal".