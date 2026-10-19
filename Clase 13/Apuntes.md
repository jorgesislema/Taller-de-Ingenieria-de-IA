
# 1. Vocabulario sin miedo (8 minutos)

**Hilo conductor:** una clínica o un restaurante. Cada concepto técnico se relaciona con una situación conocida.

| Término | Qué significa | Analogía |
|---|---|---|
| Repositorio | Proyecto con archivos y un historial de cambios administrado por Git. | Archivador con documentos y registro de sus versiones. |
| Git | Sistema de control de versiones. | Historial de cambios aplicado a un proyecto completo. |
| Commit | Registro de un conjunto de cambios con un mensaje. | Una fotografía del estado del proyecto, acompañada de una nota. |
| Rama (*branch*) | Línea de trabajo independiente. | Borrador para probar cambios sin alterar directamente la rama principal. |
| GitHub | Plataforma para alojar repositorios y colaborar. | Espacio de colaboración especializado en proyectos de software. |
| Frontend | Interfaz con la que interactúa la persona usuaria. | Recepción y sala de atención. |
| Backend | Lógica del servidor y reglas del negocio. | Cocina y administración. |
| Base de datos | Sistema que organiza y conserva datos. | Archivo organizado de la clínica. |
| API | Contrato para que dos sistemas intercambien solicitudes y respuestas. | Ventanilla que recibe una solicitud y la dirige al área correspondiente. |
| Dependencia | Código externo que el proyecto utiliza. | Ingredientes adquiridos a un proveedor. |
| Framework | Conjunto de herramientas y convenciones que facilita construir una aplicación. | Estructura base sobre la que se construye un local. |
| Módulo | Parte del sistema con una responsabilidad definida. | Departamento de una empresa. |
| Servicio | Componente que ofrece una función. Puede ser interno o independiente. | Área que presta una función concreta. |
| Entorno de desarrollo | Lugar donde se programa y experimenta. | Cocina de ensayo. |
| Entorno de pruebas | Entorno controlado para verificar el comportamiento. | Ensayo antes de abrir al público. |
| Producción | Entorno donde se utiliza el sistema real. | Local atendiendo a clientes. |
| Despliegue | Publicar una versión en un entorno para que funcione allí. | Abrir el local para prestar el servicio. |

> **Mensaje clave:** programar es solo una parte del trabajo. Organizar, nombrar, documentar, probar y proteger también es ingeniería. Con herramientas de IA, estas prácticas son especialmente importantes porque el agente necesita límites y contexto correctos.

---

# 2. Arquitectura: el plano antes de construir 

Antes de construir una clínica se decide cómo se distribuyen los consultorios, por dónde circulan los pacientes y dónde se ubica la recepción. La **arquitectura de software** define las principales partes de un sistema, sus responsabilidades, sus dependencias y la forma en que colaboran.

¿una aplicación con 100 carpetas es necesariamente mejor que una con 10?

No. La calidad depende de que las responsabilidades estén claras, las dependencias sean comprensibles, el sistema se pueda probar y mantener y los riesgos estén controlados. La cantidad de carpetas no mide la calidad.

## 2.1 Monolito: un restaurante que funciona como una sola unidad

Una aplicación monolítica se construye y despliega principalmente como una unidad. Puede tener muchas funcionalidades dentro de la misma aplicación.

En un consultorio, la gestión de profesionales, horarios, reservas y notificaciones podría vivir en un mismo backend.

**Ventajas**

- Suele ser más fácil de crear, ejecutar, depurar y desplegar al principio.
- Requiere menos infraestructura y menos comunicación por red entre componentes.
- Las operaciones que afectan a varios módulos pueden ser más sencillas.
- Es apropiado para aprender, validar una idea y empezar muchos negocios.

**Riesgos**

- Si las responsabilidades no se separan, el código puede quedar fuertemente acoplado.
- Una falla grave puede afectar a toda la aplicación.
- Escalar una función sin escalar el resto puede ser difícil.

## 2.2 Monolito modular: un edificio con departamentos bien delimitados

Es una aplicación que se despliega como una unidad, pero organiza el código en módulos con responsabilidades claras y dependencias controladas.

Por ejemplo, un módulo gestiona reservas, otro profesionales y otro notificaciones. Las reglas de reservas no deberían duplicarse en el frontend, en notificaciones y en distintos controladores.

Un monolito bien diseñado **no es sinónimo de código desordenado**.

## 2.3 Microservicios: un centro comercial de negocios independientes

La aplicación se divide en servicios que pueden desarrollarse y desplegarse de forma independiente. Se comunican mediante APIs, mensajes u otros protocolos.

Una plataforma de reservas podría separar identidad, reservas y notificaciones en servicios distintos, siempre que exista una razón real para hacerlo.

**Ventajas**

- Cada servicio puede desplegarse y escalarse por separado.
- Equipos diferentes pueden trabajar con mayor autonomía.
- Se puede aislar mejor un componente, si se diseña adecuadamente la recuperación ante fallos.

**Costes y riesgos**

- Aumenta la infraestructura y el trabajo operativo.
- Aparecen latencia, fallos de red, tiempos de espera y mensajes que pueden retrasarse o duplicarse.
- La observabilidad, la seguridad y las pruebas de integración se vuelven más complejas.
- Las operaciones que cruzan varios servicios requieren diseñar consistencia, reintentos e idempotencia.

## 2.4 Comparación práctica

| Criterio | Monolito modular | Microservicios |
|---|---|---|
| Analogía | Restaurante con departamentos | Centro comercial con negocios independientes |
| Despliegue | Una unidad principal | Varios servicios independientes |
| Complejidad inicial | Generalmente menor | Generalmente mayor |
| Comunicación interna | Llamadas dentro del proceso | Red, APIs o mensajería |
| Escalado | Normalmente de la aplicación | Puede hacerse por servicio |
| Operación | Menos componentes que vigilar | Más infraestructura y observabilidad |
| Adecuado para | MVP, pymes y equipos pequeños | Dominios o equipos con necesidad demostrada de independencia |

### Regla profesional

Empieza con un **monolito modular** si todavía no tienes evidencia de que necesitas distribuir el sistema. Extrae un servicio cuando exista una razón verificable, no por moda.

### Señales que pueden justificar separar un servicio

- Una función necesita escalar de forma muy distinta al resto.
- Varios equipos necesitan desplegar componentes sin coordinar cada lanzamiento.
- Un componente requiere aislamiento operativo, de seguridad o de disponibilidad.
- Hay una exigencia técnica o regulatoria que justifica una frontera independiente.

### Dos mitos que conviene desmontar

- **«Microservicios es lo moderno; por tanto, siempre es mejor».** Falso: ofrecen ventajas concretas, pero tienen costes operativos.
- **«Si divido el código en carpetas, ya tengo microservicios».** Falso: los microservicios son componentes que pueden desplegarse de manera independiente, no simples carpetas.

### Ejercicio en parejas (3 minutos dentro del bloque)

| Caso | Respuesta inicial razonable | Justificación |
|---|---|---|
| Consultorio con tres profesionales y una persona administrativa | Monolito modular | Equipo pequeño y pocas necesidades de operación independiente. |
| Startup que quiere validar una aplicación de reservas en dos meses | Monolito modular | Permite validar la idea con menos infraestructura. |
| Plataforma nacional con muchos equipos, millones de usuarios y necesidades de escalado distintas | Evaluar microservicios o una transición gradual | La autonomía y el escalado podrían justificar la complejidad adicional. |

**Pregunta final:** ¿qué evidencia necesitarías para cambiar tu decisión arquitectónica?

---

# 3. El árbol de carpetas: el mapa del proyecto (12 minutos)
El árbol de carpetas es el plano del sistema. Ayuda a una persona nueva o a un agente de IA a encontrar cada responsabilidad sin tener que leer todos los archivos.

Una analogía posible:

- `README.md`: recepción e instrucciones de entrada.
- `docs/`: archivo de documentación.
- `frontend/`: sala de atención.
- `backend/`: cocina y administración.
- `tests/`: control de calidad.
- `scripts/`: caja de herramientas.
- `AGENTS.md`: reglas de trabajo para agentes compatibles.

## 3.1 Ejemplo A: monolito modular para un consultorio

Punto de partida para una aplicación con interfaz web, backend Node.js y PostgreSQL. Los comentarios después de `#` explican el propósito; no forman parte de los nombres.

```text
reservas-clinica/
├── README.md
├── AGENTS.md
├── .gitignore
├── .env.example
├── package.json
├── package-lock.json
├── docker-compose.yml
├── docs/
│   ├── arquitectura.md
│   ├── seguridad.md
│   └── decisiones/
│       └── 001-monolito-modular.md
├── frontend/
│   ├── package.json
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── services/
│   └── tests/
├── backend/
│   ├── src/
│   │   ├── app.js
│   │   ├── server.js
│   │   ├── modules/
│   │   │   ├── auth/
│   │   │   ├── reservas/
│   │   │   ├── profesionales/
│   │   │   └── notificaciones/
│   │   ├── shared/
│   │   └── infrastructure/
│   ├── migrations/
│   └── tests/
├── scripts/
└── .github/
    └── workflows/
        └── ci.yml
```

Este árbol es un ejemplo, no una plantilla universal. Si el frontend y el backend tienen dependencias distintas, cada uno debe documentar cómo instalarse y probarse. Si se usa un único `package.json` en la raíz, los scripts deben reflejar realmente la estructura elegida.

| Carpeta | Responsabilidad |
|---|---|
| `docs/` | Documentación técnica y decisiones de arquitectura. |
| `frontend/` | Interfaz de usuario. |
| `backend/` | API y lógica del servidor. |
| `modules/` | Funcionalidades organizadas por dominio. |
| `shared/` | Componentes comunes con límites claros. |
| `infrastructure/` | Adaptadores de base de datos, correo y servicios externos. |
| `migrations/` | Cambios versionados del esquema de base de datos. |
| `tests/` | Pruebas automatizadas. |
| `scripts/` | Tareas de desarrollo, mantenimiento o despliegue. |
| `.github/workflows/` | Automatizaciones de GitHub Actions. |

## 3.2 Ejemplo B: arquitectura de microservicios

```text
reservas-plataforma/
├── README.md
├── AGENTS.md
├── .gitignore
├── .env.example
├── docs/
│   ├── arquitectura.md
│   ├── seguridad.md
│   └── adr/
├── apps/
│   └── frontend/
├── services/
│   ├── api-gateway/
│   ├── auth-service/
│   ├── booking-service/
│   └── notification-service/
├── contracts/
│   └── openapi/
├── deploy/
│   └── compose.yaml
├── tests/
│   └── integration/
└── .github/
    └── workflows/
```

Responsabilidades orientativas:

- `api-gateway/`: entrada y enrutamiento de solicitudes, si la arquitectura necesita un gateway.
- `auth-service/`: identidad y permisos.
- `booking-service/`: reservas y disponibilidad.
- `notification-service/`: envío de avisos.
- `contracts/openapi/`: contratos de APIs.
- `deploy/`: configuración de despliegue.
- `tests/integration/`: pruebas de interacción entre servicios.

En una implementación real, cada servicio suele tener sus propias dependencias, pruebas, configuración y proceso de construcción. La propiedad de los datos debe definirse explícitamente. Separar carpetas no obliga por sí solo a crear una base de datos por servicio.

**Observación:** este árbol contiene más piezas que el ejemplo monolítico. Esa complejidad solo compensa cuando resuelve necesidades reales.

## 3.3 Siete reglas de oro para organizar carpetas

1. **Una responsabilidad clara por módulo.** Debe poder explicarse en una frase qué hace.
2. **Nombrar por función.** Preferir `reservas/` a `trabajo-de-maria/` o `nuevo-2026/`.
3. **Evitar cajones de sastre.** Carpetas como `varios/`, `otros/`, `final/` o `copia/` suelen indicar falta de criterio.
4. **No profundizar sin motivo.** Una estructura demasiado anidada dificulta encontrar archivos.
5. **Evitar duplicar reglas de negocio.** Una misma regla no debe tener implementaciones contradictorias en distintos módulos.
6. **Organizar las pruebas de forma coherente.** Pueden estar cerca del módulo o en una estructura espejo, según el proyecto.
7. **No versionar secretos ni datos sensibles.** La estructura del proyecto no sustituye las medidas de seguridad.

### Actividad de observación (3 minutos dentro del bloque)

Abrir un repositorio público conocido y pedir al grupo que interprete el árbol de carpetas solo por los nombres. Después, abrir algunos archivos para comprobar si las suposiciones eran correctas.

---

# 4. Archivos esenciales y nomenclatura (15 minutos)

Cada archivo tiene un propósito. Antes de memorizar nombres, hay que comprender qué problema resuelve cada uno.

## 4.1 Archivos y carpetas frecuentes

| Nombre | Para qué sirve | ¿Se versiona normalmente? |
|---|---|---|
| `README.md` | Explica qué es el proyecto, cómo instalarlo y cómo utilizarlo. | Sí |
| `LICENSE` | Define las condiciones de uso, modificación y distribución del código. | Sí |
| `.gitignore` | Indica a Git qué archivos no debe empezar a seguir. | Sí |
| `.env` | Contiene configuración local; puede incluir secretos. | No |
| `.env.example` | Plantilla de variables requeridas sin secretos reales. | Sí |
| `.venv/` | Entorno virtual local de Python. | No |
| `node_modules/` | Dependencias instaladas de Node.js. | No |
| `package.json` | Metadatos, dependencias y scripts de un proyecto Node.js. | Sí |
| `package-lock.json` | Registra la resolución concreta de dependencias de npm. | Sí, en aplicaciones npm |
| `pyproject.toml` | Metadatos y configuración de herramientas de Python. | Sí |
| `requirements.txt` | Lista de dependencias según la estrategia del proyecto Python. | Normalmente sí |
| `Dockerfile` | Instrucciones para construir una imagen de contenedor. | Sí |
| `compose.yaml` o `docker-compose.yml` | Define servicios que se ejecutan juntos mediante Docker Compose. | Sí |
| `CONTRIBUTING.md` | Explica cómo contribuir al proyecto. | Sí |
| `tests/` | Contiene pruebas automatizadas. | Sí |
| `.github/workflows/` | Contiene flujos de automatización de GitHub Actions. | Sí |
| `.vscode/` | Configuración de VS Code; puede contener ajustes compartidos o personales. | Depende |
| `.idea/` | Configuración de IDE de JetBrains. | Depende |

Los nombres que comienzan con punto suelen ser archivos o directorios ocultos en ciertos sistemas. Si no aparecen en el explorador, puede ser necesario activar la opción para mostrar archivos ocultos.

## 4.2 `.venv`: el entorno de Python

Cada proyecto de Python puede necesitar versiones específicas de bibliotecas. El entorno virtual crea un espacio separado para instalar sus dependencias.

Ideas esenciales:

- No se edita manualmente como si fuera código fuente.
- Normalmente no se sube a Git: se puede reconstruir.
- Se recrea a partir de la configuración de dependencias del proyecto.
- El archivo que permite reconstruirlo debe estar actualizado.

Comandos habituales:

```bash
# Crear un entorno virtual
python -m venv .venv

# Activar en Windows PowerShell
.venv\Scripts\Activate.ps1

# Activar en macOS o Linux
source .venv/bin/activate

# Instalar dependencias si el proyecto usa requirements.txt
python -m pip install -r requirements.txt
```

En proyectos Node.js, `node_modules/` contiene dependencias instaladas y normalmente se reconstruye con `npm install` o, cuando corresponde, `npm ci`.

## 4.3 `.gitignore`: qué no debe seguir Git

`.gitignore` contiene patrones de archivos y carpetas que Git debe ignorar cuando todavía no están bajo seguimiento. **No borra archivos del disco ni deja de versionar automáticamente archivos que Git ya está siguiendo.**

Ejemplo inicial para un proyecto mixto de Node.js y Python:

```gitignore
# Dependencias de Node.js
node_modules/

# Variables locales y secretos
.env
.env.*
!.env.example

# Registros
*.log
logs/

# Salidas de compilación y cobertura
dist/
build/
coverage/

# Entornos virtuales y caché de Python
.venv/
venv/
__pycache__/
*.py[cod]
.pytest_cache/

# Archivos del sistema
.DS_Store
Thumbs.db

# Configuración local de editores
.idea/

# Bases de datos locales de desarrollo: revisar antes de usar
*.sqlite
*.sqlite3

# Claves y certificados privados
*.pem
*.key
*.p12
*.pfx
```

### Cuatro advertencias

1. Si una clave ya se publicó, ignorar el archivo no resuelve el problema. Hay que revocar o rotar la credencial y evaluar la exposición del historial.
2. No ignores toda la carpeta `.vscode/` sin revisar si contiene configuraciones útiles para el equipo.
3. No ignores bases de datos de forma indiscriminada: algunos proyectos mantienen fixtures o datos de prueba controlados.
4. Revisa los patrones de un `.gitignore` copiado de Internet. Una regla amplia puede ocultar archivos necesarios.

La regla `!.env.example` permite incluir la plantilla aunque se ignoren los demás archivos `.env.*`, siempre que otras reglas no impidan llegar a esa ruta.

## 4.4 `.env` y `.env.example`: configuración local y plantilla

La configuración separa el código de los valores que cambian entre entornos. `.env` puede contener credenciales y valores privados; por eso debe mantenerse fuera de Git. `.env.example` documenta las variables que otra persona necesita definir.

Ejemplo de `.env.example`:

```dotenv
# Aplicación
NODE_ENV=development
PORT=3000

# Base de datos local de ejemplo
DATABASE_URL=postgresql://usuario:CAMBIAR@localhost:5432/reservas_dev

# Generar un secreto local; no reutilizar este texto
JWT_SECRET=REEMPLAZAR_POR_UN_SECRETO_LOCAL

# Correo de demostración
SMTP_HOST=localhost
SMTP_PORT=1025
SMTP_USER=
SMTP_PASSWORD=

# IA: completar solo si la función está habilitada
AI_PROVIDER=
AI_API_KEY=
```

Reglas importantes:

1. El programa debe validar las variables obligatorias al arrancar y explicar con claridad qué falta, sin imprimir secretos.
2. En producción, los secretos deben gestionarse mediante el entorno de despliegue o un gestor de secretos apropiado.
3. Las variables que se incorporan al frontend pueden quedar visibles para el usuario. Por ejemplo, una variable `VITE_*` no debe contener una clave privada del servidor.
4. No pegues el contenido de `.env` en un chat de IA. Si una credencial se expone, rótala.
5. Los nombres de variables deben coincidir con los que realmente espera el programa. La plantilla no configura la aplicación por sí sola.

## 4.5 `README.md`: la puerta de entrada

Un README útil responde cinco preguntas: ¿qué hace el proyecto?, ¿qué necesito?, ¿cómo lo instalo?, ¿cómo lo pruebo? y ¿dónde encuentro más información?

```markdown
# Sistema de reservas para consultorios

## Descripción

Aplicación para gestionar horarios, profesionales y reservas.

## Requisitos

- Git.
- Node.js en una versión compatible con el proyecto.
- PostgreSQL, si se utiliza la configuración de base de datos indicada.

## Instalación

1. Clonar el repositorio.
2. Instalar las dependencias.
3. Copiar `.env.example` a `.env`.
4. Completar las variables locales necesarias.
5. Ejecutar las migraciones documentadas.
6. Iniciar la aplicación con el comando configurado.

## Pruebas

Ejecutar el comando de pruebas definido en los archivos de configuración.

## Seguridad

No subir secretos ni datos reales de pacientes.
Consultar `docs/seguridad.md`.

## Arquitectura

Consultar `docs/arquitectura.md`.
```

**Regla de honestidad:** los comandos finales deben copiarse de la configuración real del proyecto. Un README que describe comandos inexistentes es peor que una documentación breve y correcta.

## 4.6 Nomenclatura: ponerle una buena etiqueta a todo

| Evitar | Preferir | Motivo |
|---|---|---|
| `Nueva carpeta (2)/` | `notificaciones/` | Describe el contenido. |
| `Reserva FINAL v3 (copia).js` | `reservas.service.js` | Git conserva el historial; el nombre describe la función. |
| `Gestión de Citas.md` | `gestion-citas.md` | Facilita la compatibilidad entre herramientas. |
| `prueba.js` | `reservas.test.js` | Indica qué se prueba. |

### Siete reglas de nomenclatura

1. Usa nombres descriptivos y consistentes.
2. Evita espacios en nombres de archivos técnicos; los guiones suelen ser cómodos.
3. Evita tildes y símbolos poco comunes en rutas compartidas si no son necesarios.
4. No uses `final`, `definitivo` o `copia` como estrategia de versiones; utiliza Git.
5. Para fechas, usa `AAAA-MM-DD`, por ejemplo `2026-10-19`.
6. Decide una convención de idioma para el código y la documentación. La consistencia es más importante que una elección universal.
7. Respeta las convenciones del lenguaje, framework y herramienta del proyecto.

### Cinco estilos frecuentes

| Estilo | Forma | Uso típico | Ejemplo |
|---|---|---|---|
| `kebab-case` | `palabras-con-guiones` | Carpetas y Markdown | `guia-instalacion.md` |
| `snake_case` | `palabras_con_guion_bajo` | Python | `crear_reserva.py` |
| `camelCase` | `palabrasConJorobas` | Funciones y variables JavaScript | `crearReserva()` |
| `PascalCase` | `PalabrasConInicialGrande` | Clases y componentes | `ReservaService` |
| `UPPER_SNAKE_CASE` | `TODO_EN_MAYUSCULAS` | Variables de entorno y constantes según convención | `DATABASE_URL` |

No son leyes universales. Python suele usar `snake_case`; React suele usar `PascalCase` para componentes; una migración debe respetar el formato que espera el framework.

### Otras convenciones frecuentes

| Elemento | Ejemplo |
|---|---|
| Pruebas | `reservas.test.js` o `test_reservas.py` |
| Migraciones | `20261019090000-create-reservas.js` |
| Decisiones de arquitectura | `001-monolito-modular.md` |
| Ramas de Git | `feature/crear-reserva` |
| Mensajes de commit | `feat: agrega cancelación de reservas` |

Tipos comunes de mensajes de commit:

- `feat`: nueva funcionalidad.
- `fix`: corrección.
- `docs`: documentación.
- `test`: pruebas.
- `refactor`: reorganización sin cambio funcional intencional.
- `chore`: mantenimiento.

### Mini-ejercicio (3 minutos)

Proponer nombres mejores para:

- `Nueva Carpeta (2)/`
- `Reserva FINAL v3.js`
- `ñoño.txt`
- `prueba.js`

Pedir que el grupo justifique cada respuesta.

---

# 5. Repositorios preparados para IA: agentes, instrucciones y skills (23 minutos)

Un agente de IA se parece a una persona competente que llega a una empresa sin conocer el proyecto. Necesita instrucciones, información pertinente y herramientas con permisos adecuados. Si falta contexto, puede asumir cosas incorrectas.

## 5.1 Seis conceptos esenciales

| Concepto | Qué significa | Analogía |
|---|---|---|
| Modelo | Sistema que procesa información y genera respuestas, como GPT, Claude, Gemini o Qwen. | Cerebro y formación. |
| Agente | Sistema que combina un modelo, instrucciones, contexto y herramientas para realizar tareas. | Empleado con una función definida. |
| Instrucciones | Reglas sobre cómo trabajar, qué respetar y qué evitar. | Reglamento interno. |
| Contexto | Información disponible para resolver una tarea. | Expediente del caso. |
| Skill | Procedimiento reutilizable para una tarea concreta. | Manual de procedimiento. |
| Herramienta | Capacidad externa: leer archivos, ejecutar pruebas o llamar una API. | Computadora, teléfono o equipo de trabajo. |

Otros dos conceptos:

- **MCP (Model Context Protocol):** protocolo para conectar aplicaciones de IA con herramientas y fuentes de información compatibles.
- **Subagente:** agente especializado al que otro agente puede delegar una parte del trabajo, si la plataforma admite esa función.

### Modelo y herramienta no son lo mismo

DeepSeek, GLM, Qwen, Kimi K2 y GPT son familias o modelos de IA. Claude Code, Codex, Gemini CLI, Qwen Code, Kimi Code, Cursor y otros son herramientas o entornos que pueden proporcionar acceso a modelos y capacidades de programación.

La distinción importa porque **el modelo no decide por sí solo qué archivo de instrucciones carga el entorno**. Esa conducta depende de la herramienta, su versión y su configuración.

## 5.2 Una regla fundamental: el archivo puede existir y no haberse leído

Cada herramienta tiene mecanismos propios para cargar instrucciones. Guardar un archivo en Git no garantiza que una aplicación de IA lo haya incorporado a su contexto.

Para comprobarlo:

1. Revisa la documentación de la herramienta y su versión.
2. Identifica los nombres y ubicaciones admitidos.
3. Pregunta al agente qué instrucciones del proyecto ha cargado.
4. Haz una prueba pequeña y revisa si respeta una regla verificable.
5. No concluyas que una instrucción se aplicó solo porque el archivo existe.

## 5.3 Referencia de archivos por herramienta

**Importante:** los nombres y mecanismos de carga pueden cambiar. Esta tabla es una orientación técnica para verificar en la documentación de la versión instalada; no es una garantía universal ni una afirmación de que cada función esté habilitada en todas las modalidades.

| Herramienta o producto | Punto de entrada habitual | Skills, reglas o contexto |
|---|---|---|
| OpenAI Codex | `AGENTS.md` | Puede admitir skills y otros mecanismos según el entorno y la versión. |
| ChatGPT en web o aplicación | Instrucciones de la conversación, archivos adjuntos o configuración del GPT | No lee un repositorio local automáticamente solo porque exista. |
| Claude Code | `CLAUDE.md` | Reglas y skills dentro de ubicaciones admitidas por Claude Code. |
| Claude en Projects | Instrucciones del proyecto y archivos añadidos | El contexto depende del proyecto y de los archivos disponibles. |
| Gemini CLI | `GEMINI.md` | Puede configurarse para cargar archivos de contexto adicionales; verifica la versión. |
| Gemini Gems | Instrucciones del Gem y conocimiento añadido | No equivale a leer automáticamente el disco local. |
| GitHub Copilot | `.github/copilot-instructions.md`; también admite instrucciones de agente en contextos compatibles | `.github/instructions/*.instructions.md` y `AGENTS.md` según producto y función. |
| Cursor | Reglas de proyecto en ubicaciones admitidas por Cursor; puede reconocer `AGENTS.md` | La configuración exacta depende de la versión. |
| Windsurf | Reglas de proyecto en ubicaciones admitidas por Windsurf | Verificar compatibilidad con archivos compartidos y reglas heredadas. |
| Aider | Archivos de convenciones incorporados mediante su configuración o comandos | No asumir que carga cualquier archivo del repositorio automáticamente. |
| Qwen Code | `QWEN.md` y mecanismos compatibles con `AGENTS.md`, según la versión | Skills y reglas en ubicaciones documentadas por Qwen Code. |
| Kimi Code CLI | Instrucciones de agente y mecanismos compatibles con `AGENTS.md`, según la versión | Skills en directorios reconocidos por la herramienta. |
| Trae | Reglas de proyecto en las ubicaciones que documente la versión instalada | Confirmar diferencias entre ediciones y versiones. |
| DeepSeek | Depende de la herramienta donde se utilice el modelo | El nombre del modelo no define por sí solo un archivo de instrucciones. |
| GLM / Z.ai | Depende de la herramienta o agente que lo utilice | Revisar el producto concreto; modelo y entorno de ejecución son capas distintas. |
| MiniMax o Kimi usados por API | Depende de la aplicación cliente | La API del modelo no implica carga automática de archivos del repositorio. |

Documentación oficial o repositorios de referencia:

- [GitHub Copilot: instrucciones personalizadas](https://docs.github.com/en/copilot).
- [Anthropic: documentación de Claude](https://docs.anthropic.com/).
- [Gemini CLI](https://github.com/google-gemini/gemini-cli).
- [Qwen Code](https://github.com/QwenLM/qwen-code).
- [Kimi Code](https://github.com/MoonshotAI/kimi-code).
- [Formato de skills en Kimi Code](https://github.com/MoonshotAI/kimi-code/tree/main/docs/en/customization/skills).

Antes de enseñar una ubicación exacta como norma, comprueba la documentación actual de la herramienta instalada.

### Tres mensajes para el grupo

- Los nombres cambian con rapidez; verifica la documentación y la versión.
- Un archivo común como `AGENTS.md` puede reducir duplicaciones, pero no todas las herramientas lo cargan de la misma manera.
- La privacidad importa tanto como el código. Antes de enviar información sensible a una plataforma, revisa sus condiciones, permisos, tratamiento de datos y configuración. En una clínica no deben copiarse datos reales de pacientes en herramientas externas sin autorización y salvaguardas adecuadas.

## 5.4 Estrategia práctica: un manual principal y archivos puente

Una estructura posible:

```text
reservas-clinica/
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
├── .github/
│   └── copilot-instructions.md
├── .agents/
│   └── skills/
│       ├── auditar-repositorio/
│       │   └── SKILL.md
│       └── revisar-migracion/
│           └── SKILL.md
└── agents/
    ├── README.md
    ├── PROCESO.md
    ├── rules/
    │   ├── seguridad.md
    │   ├── pruebas.md
    │   └── documentacion.md
    ├── context/
    │   ├── arquitectura.md
    │   ├── dominio-reservas.md
    │   └── decisiones-vigentes.md
    ├── prompts/
    │   ├── auditoria-integral.md
    │   └── pruebas-concurrencia.md
    └── reports/
        └── auditoria-inicial.md
```

Esta es una propuesta organizativa, no una estructura que todas las herramientas interpreten automáticamente.

- `AGENTS.md`: instrucciones generales para herramientas compatibles.
- `CLAUDE.md`, `GEMINI.md` y `.github/copilot-instructions.md`: puntos de entrada específicos cuando correspondan.
- `.agents/skills/`: ubicación compartida de skills en algunas herramientas compatibles; verifica el mecanismo exacto de descubrimiento.
- `agents/rules/`: políticas detalladas.
- `agents/context/`: arquitectura, dominio y decisiones vigentes.
- `agents/prompts/`: solicitudes preparadas para tareas repetidas.
- `agents/reports/`: resultados de auditorías.
- `agents/PROCESO.md`: estado verificado y siguientes pasos.

La carpeta `agents/` es una convención organizativa del proyecto: no des por hecho que una herramienta la lee completa automáticamente. El archivo de entrada debe indicar qué documentos consultar y cuándo.

## 5.5 Ejemplo de `AGENTS.md`

Mantén este archivo corto, concreto y verificable. Los detalles extensos pueden vivir en documentos enlazados.

```markdown
# AGENTS.md

## Proyecto

Sistema de reservas para consultorios.
Arquitectura: monolito modular.
Frontend: `frontend/`.
Backend: `backend/`.

## Antes de modificar código

1. Lee `README.md` y `agents/PROCESO.md`.
2. Consulta `docs/arquitectura.md` y el contexto pertinente.
3. Inspecciona el código y las pruebas existentes.
4. Identifica los riesgos y las dependencias afectadas.

## Comandos

Usa solo comandos que existan en la configuración real.
Confirma los scripts de `package.json` antes de ejecutarlos.

## Arquitectura

- Mantén las responsabilidades separadas por módulo.
- Evita duplicar reglas de negocio.
- No introduzcas microservicios sin una decisión documentada.
- No cambies el esquema de datos sin revisar sus dependencias.

## Seguridad

- No expongas secretos ni datos personales.
- No muestres valores de archivos `.env`.
- Valida las entradas en el servidor.
- No debilites controles de seguridad para hacer pasar pruebas.
- No afirmes que una prueba pasó si no la ejecutaste.

## Límites de actuación

- No borres datos ni ejecutes operaciones destructivas sin autorización.
- No modifiques producción.
- Si una decisión crítica está sin resolver, presenta alternativas antes de implementarla.

## Informe final

Indica:
- Archivos modificados y cambios realizados.
- Pruebas ejecutadas y resultados reales.
- Riesgos y limitaciones pendientes.
- Próximo paso recomendado.
```

Este archivo expresa instrucciones, pero no sustituye los permisos del sistema operativo, del entorno de ejecución o de la plataforma. Una frase como «no toques producción» no bloquea técnicamente el acceso si la herramienta conserva esos permisos.

## 5.6 Ejemplo de archivo puente: `CLAUDE.md`

En Claude Code, una forma habitual de incluir instrucciones compartidas es:

```markdown
# CLAUDE.md

@AGENTS.md

## Notas específicas

- Antes de modificar varios archivos, presenta un plan breve.
- Consulta las skills disponibles cuando la tarea lo requiera.
```

La sintaxis de inclusión y su comportamiento deben verificarse en la documentación de la versión instalada. No copies esta técnica a otra herramienta suponiendo que la interpretará igual.

## 5.7 Ejemplo de skill: procedimiento reutilizable

Ruta propuesta: `.agents/skills/auditar-repositorio/SKILL.md`.

```markdown
---
name: auditar-repositorio
description: Audita estructura, arquitectura, seguridad, pruebas
  y documentación de un repositorio existente.
---

# Skill: auditar-repositorio

## Objetivo

Identificar defectos verificables antes de modificar código.

## Procedimiento

1. Inspeccionar el árbol del repositorio.
2. Identificar lenguajes, frameworks y dependencias.
3. Leer las instrucciones aplicables.
4. Revisar la gestión de secretos sin mostrar sus valores.
5. Examinar la arquitectura y las dependencias entre módulos.
6. Revisar las pruebas existentes.
7. Ejecutar únicamente pruebas no destructivas autorizadas.
8. Clasificar los hallazgos por severidad y evidencia.
9. Proponer correcciones ordenadas por riesgo.

## Reglas

- No modificar archivos durante una auditoría de solo lectura.
- No inventar resultados de pruebas.
- Referenciar archivos y líneas cuando estén disponibles.
- Diferenciar hechos verificados, hipótesis y cuestiones pendientes.

## Resultado esperado

- Resumen ejecutivo.
- Hallazgos con evidencia.
- Severidad e impacto.
- Recomendaciones.
- Pruebas realizadas.
- Limitaciones de la auditoría.
```

Una skill es un procedimiento que se carga o utiliza cuando corresponde. No equivale a las instrucciones generales del agente y no garantiza que el modelo la invoque siempre. El formato de metadatos y la ubicación reconocida dependen de la herramienta.

## 5.8 Ejemplo de `agents/PROCESO.md`: bitácora de continuidad

```markdown
# Estado del proceso

## Proyecto

Sistema de reservas para consultorios.

## Fase actual

Diseño inicial de arquitectura.

## Verificado

- Se documentó una propuesta de estructura.
- Se definieron convenciones iniciales de nomenclatura.

## Pendiente de verificar

- Framework definitivo.
- Configuración de la base de datos.
- Pruebas automatizadas.
- Compatibilidad de las instrucciones con cada herramienta.

## Próximos pasos

1. Confirmar decisiones de arquitectura.
2. Crear la estructura mínima.
3. Configurar el entorno de desarrollo.
4. Ejecutar pruebas iniciales.
5. Registrar resultados y decisiones.
```

La bitácora debe reflejar lo que realmente se ha comprobado, no lo que se espera conseguir.

## 5.9 Ocho hábitos para escribir buenas instrucciones

1. **Concretas y verificables:** «ejecuta las pruebas definidas y registra el resultado» es mejor que «hazlo perfecto».
2. **Breves:** lo extenso puede mantenerse en documentos especializados.
3. **Comandos reales:** no inventar comandos para completar una plantilla.
4. **Límites claros:** definir qué acciones necesitan autorización.
5. **Una fuente de verdad:** evitar instrucciones contradictorias entre archivos.
6. **Sin secretos:** los archivos de instrucciones suelen versionarse y pueden ser enviados a proveedores externos.
7. **Revisión como código:** una instrucción incorrecta puede afectar a muchas tareas.
8. **Verificación de carga:** comprobar que la herramienta reconoce las instrucciones previstas.

## 5.10 Cinco hábitos de seguridad con agentes

- **Permisos mínimos:** dar al agente únicamente los accesos necesarios.
- **Entornos aislados:** evitar que trabaje directamente en producción.
- **Revisión humana:** revisar los cambios antes de integrarlos.
- **Cambios pequeños:** facilitan la inspección y la reversión.
- **Contenido externo no confiable:** instrucciones encontradas en páginas, archivos o correos deben tratarse como datos, no como órdenes con autoridad automática.

---

# 6. Taller práctico: diseñar el repositorio de un consultorio 

## Escenario

Una clínica quiere gestionar profesionales, horarios, reservas y notificaciones. Más adelante podría incorporar un asistente de IA que responda preguntas sobre horarios y políticas.

El sistema debe evitar reservas incompatibles, proteger credenciales y no almacenar información clínica que no necesite.

## Actividad del estudiante

Marca cada tarea cuando la hayas completado:

- [ ] Elegir monolito modular o microservicios y justificarlo.
- [ ] Diseñar el árbol de carpetas.
- [ ] Definir nombres coherentes para al menos ocho archivos o carpetas.
- [ ] Preparar un `README.md` con requisitos, instalación y pruebas.
- [ ] Crear un `.gitignore` adecuado a las tecnologías.
- [ ] Crear un `.env.example` sin credenciales reales.
- [ ] Preparar instrucciones iniciales para el agente de IA.
- [ ] Identificar al menos tres riesgos de seguridad.
- [ ] Definir cómo se comprobará que la aplicación funciona.

## Solución de referencia

Para un consultorio pequeño, una elección inicial razonable es un **monolito modular**, con frontend y backend separados de forma clara y módulos de negocio bien delimitados.

Las reservas, los profesionales y las notificaciones pueden comenzar como módulos internos. El asistente de IA debería acceder a funciones controladas y autorizadas, no tener acceso indiscriminado a la base de datos.

Solo se extraerían componentes como servicios independientes si los requisitos de escalado, aislamiento, disponibilidad o despliegue justifican su coste.

---

# 7. Evaluación y cierre 

## Cinco preguntas

**1. ¿Un proyecto con muchas carpetas es necesariamente más profesional?**

No. Importan la claridad de las responsabilidades, la facilidad de prueba y la mantenibilidad.

**2. ¿Qué arquitectura suele ser razonable para empezar una aplicación pequeña?**

Un monolito modular, salvo que existan requisitos concretos que justifiquen otra arquitectura.

**3. ¿Qué hace `.gitignore`?**

Indica a Git qué patrones debe ignorar cuando no están bajo seguimiento. No elimina archivos ni protege secretos ya publicados.

**4. ¿Cualquier modelo de IA lee automáticamente `AGENTS.md`?**

No. Depende de la herramienta, la versión y su configuración.

**5. ¿Qué debe contener `.env.example`?**

Los nombres de las variables y valores de ejemplo seguros, sin credenciales reales.

## Criterios de logro

Al final de la clase, cada estudiante debería poder:

- Explicar la diferencia entre arquitectura, repositorio, módulo y servicio.
- Defender una elección entre monolito modular y microservicios.
- Interpretar un árbol de carpetas.
- Explicar la función de los archivos esenciales.
- Distinguir modelo, agente, instrucción, contexto, skill y herramienta.
- Reconocer que la seguridad requiere permisos y controles reales, no solo instrucciones escritas.

---

# Material de consulta

- [GitHub Docs: repositorios](https://docs.github.com/en/repositories)
- [GitHub Copilot: instrucciones personalizadas](https://docs.github.com/en/copilot)
- [OpenAI: documentación de modelos y APIs](https://platform.openai.com/docs)
- [Anthropic: documentación de Claude](https://docs.anthropic.com/)
- [Gemini CLI](https://github.com/google-gemini/gemini-cli)
- [Qwen Code](https://github.com/QwenLM/qwen-code)
- [Kimi Code](https://github.com/MoonshotAI/kimi-code)
- [The Twelve-Factor App](https://12factor.net/)
- [Docker Compose](https://docs.docker.com/compose/)

---

# Conclusión

La arquitectura define cómo se organiza el sistema. El árbol de carpetas hace visible esa organización. Las convenciones permiten mantenerla. Las pruebas verifican el comportamiento. La documentación explica cómo utilizar y modificar el proyecto. Las instrucciones para agentes ayudan a que las herramientas de IA trabajen dentro de límites explícitos.

Un repositorio profesional no necesita cientos de archivos. Necesita una estructura coherente, decisiones justificadas, configuración reproducible, secretos protegidos, pruebas verificables y reglas claras para las personas y los agentes que lo mantienen.
'''
