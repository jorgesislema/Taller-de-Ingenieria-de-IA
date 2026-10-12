# Clase — Git y GitHub: La Máquina del Tiempo de tu Trabajo
### Duración: 90 minutos (45 min explicación guiada + 45 min práctica)

> Material de apoyo para el estudiante. Leelo directo en GitHub o en la vista web.
> **Nota sobre las pantallas:** GitHub y VSCode cambian de aspecto con frecuencia. Si un botón no está exactamente donde dice esta guía, buscá el nombre del botón (no su posición). La lógica de fondo no cambia.

---

## Filosofía de la clase

> **Un Ingeniero de IA no guarda su trabajo en archivos llamados `prompt_final_v3_AHORA_SI_definitivo.txt`. Usa un sistema que recuerda cada versión por él.**

En la Clase 3 diste tus primeros pasos con Git. Hoy lo convertís en un hábito de trabajo real, porque lo que viene en el taller (skills, asistentes, agentes) son **archivos que van a cambiar muchas veces** — y vas a necesitar poder volver atrás cuando algo deje de funcionar.

Si te llevás una sola cosa de esta clase, que sea esta:

> **Git es una máquina del tiempo para tu trabajo. GitHub es la caja fuerte en la nube donde esa máquina del tiempo queda guardada a salvo.**

---

## 1. La Idea (minutos 0-10)

### 1.1 El problema que todos conocemos

Mirá esta carpeta. ¿Te suena?

```
📁 Mis documentos
   📄 Cotizacion.docx
   📄 Cotizacion_v2.docx
   📄 Cotizacion_v2_corregida.docx
   📄 Cotizacion_FINAL.docx
   📄 Cotizacion_FINAL_ahora_si.docx
   📄 Cotizacion_FINAL_ahora_si_NO_TOCAR.docx
```

Seis archivos para un solo documento. ¿Cuál es el bueno? ¿Qué cambió entre uno y otro? Nadie lo sabe — ni siquiera vos, dentro de un mes.

### 1.2 Cómo lo resuelve Git

Con Git tenés **un solo archivo**, y Git recuerda en silencio cada versión anterior. Cada vez que decidís "guardar esta versión", escribís una nota corta de qué cambiaste, y Git la archiva con fecha y hora.

```
Un solo archivo: Cotizacion.docx

Historial que Git recuerda:
  ● 12 oct 10:30 — "Versión inicial"
  ● 12 oct 15:45 — "Agregué el IVA desglosado"
  ● 13 oct 09:10 — "Corregí el precio de la mesa"
  ● 13 oct 11:00 — "Cambié el formato de la tabla"   ← estás acá
```

Y si hoy descubrís que el cambio de las 11:00 fue un error, volvés a la versión de las 09:10 con un comando. Cero archivos duplicados.

### 1.3 Los 3 conceptos que necesitás (y nada más)

| Concepto | Analogía | Qué es en realidad |
|---|---|---|
| **Repositorio** ("repo") | Una carpeta con memoria | Tu carpeta de proyecto + todo su historial de versiones |
| **Commit** | Sacarle una foto a tu trabajo en este momento, con una nota | Una versión guardada, con fecha, autor y mensaje |
| **GitHub** | Una caja fuerte en la nube | Un sitio web donde guardás una copia de tu repositorio, a salvo de que se rompa tu computadora |

> **Aclaración importante:** **Git** y **GitHub** no son lo mismo. Git es el programa que vive en tu computadora y lleva el historial. GitHub es un sitio web (de Microsoft) donde podés subir una copia. Podrías usar Git sin GitHub, pero usar los dos juntos es lo estándar en el mundo profesional.

### 1.4 ¿Por qué esto importa para un curso de IA?

Todo lo que vas a construir en este taller son **archivos de texto que cambian**: prompts, instrucciones de tu asistente, plantillas, skills. Un prompt que ayer funcionaba perfecto y hoy da resultados raros… ¿qué cambiaste? Con Git, lo ves exacto.

---

## 2. Preparar el Terreno (minutos 10-25)

### 2.1 Verificá que Git esté instalado

Abrí VSCode, y abrí la terminal integrada con `Ctrl + ñ` (o `Ctrl + '` según tu teclado; también desde el menú **Terminal → Nueva terminal**). Escribí:

```bash
git --version
```

Si ves algo como `git version 2.4x.x`, perfecto. Si dice "comando no encontrado", instalá Git desde [git-scm.com](https://git-scm.com), dejá todas las opciones por defecto, y reiniciá VSCode.

### 2.2 Decile a Git quién sos (una sola vez en la vida)

Git firma cada versión con tu nombre. Configuralo una sola vez:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu_correo@ejemplo.com"
```

> **Tip de privacidad (conecta con la Clase 2):** el correo que pongas acá puede quedar visible públicamente si subís proyectos a GitHub. GitHub ofrece un correo privado especial (lo encontrás en Settings → Emails → "Keep my email address private") si no querés exponer el tuyo real.

### 2.3 Tu cuenta de GitHub

Si todavía no la tenés (la tarea de la Clase 3):

1. Entrá a [github.com](https://github.com) → **Sign up**
2. Correo, contraseña, nombre de usuario (elegí uno profesional: es parte de tu portafolio)
3. Verificá tu correo
4. Activá la **verificación en dos pasos** cuando GitHub te lo sugiera (Settings → Password and authentication). Es la protección más importante que podés tener: tu cuenta va a guardar tu trabajo.

---

## 3. Tu Primer Ciclo: Local (minutos 25-45)

> **Práctica guiada paso a paso.** Todos hacemos lo mismo al mismo tiempo. Si alguien se queda atrás, levantá la mano — no sigas con errores acumulados.

### 3.1 Creá tu carpeta de proyecto

1. En tu computadora, creá una carpeta llamada `mis-prompts` (en Documentos, por ejemplo).
2. En VSCode: **Archivo → Abrir carpeta** → elegí `mis-prompts`.
3. Abrí la terminal integrada (ya se abre dentro de esa carpeta).

### 3.2 Convertila en un repositorio

```bash
git init
```

Esto le dice a Git: *"empezá a vigilar esta carpeta"*. Verás un mensaje de que se inicializó un repositorio vacío. (En VSCode aparecerá el ícono de **Control de código fuente** en la barra lateral, con forma de ramita.)

### 3.3 Creá tu primer archivo

En VSCode, creá un archivo nuevo llamado `asistente.md` y escribí adentro algo real de tu negocio o tu casa. Por ejemplo:

```markdown
# Mi asistente de atención al cliente

Eres el asistente de [Mi Negocio].
Respondés con un tono cálido y cercano.
Nunca inventás precios ni horarios: si no tenés el dato,
decís "Dejame confirmarte y te respondo a la brevedad".
```

Guardalo con `Ctrl + S`.

### 3.4 Mirá qué ve Git

```bash
git status
```

Git te va a decir que hay un archivo nuevo "sin seguimiento" (*untracked*). Esto es normal: Git lo ve, pero todavía no lo guardó en el historial.

### 3.5 Los dos pasos para guardar una versión

Guardar una versión en Git son **siempre dos pasos**, y entender por qué es la clave de todo:

```
PASO 1: git add        →  "Estos son los cambios que quiero incluir en la foto"
PASO 2: git commit     →  "Sacá la foto y ponele esta nota"
```

**Analogía:** `add` es como acomodar los objetos que van a salir en una foto grupal. `commit` es apretar el botón de la cámara.

```bash
git add asistente.md
git commit -m "Primera versión del asistente de atención al cliente"
```

> **Cómo escribir un buen mensaje de commit:** que alguien (vos dentro de 6 meses) entienda qué cambió **sin abrir el archivo**. Mal: `"cambios"`. Bien: `"Agregué la regla de no inventar precios"`.

### 3.6 Hacé un segundo cambio y guardalo

1. Agregá una línea nueva a `asistente.md` (por ejemplo, el horario de tu negocio).
2. Guardá el archivo.
3. Repetí el ciclo:

```bash
git add asistente.md
git commit -m "Agregué el horario de atención"
```

Ya tenés **dos versiones** guardadas. Probalo:

```bash
git log --oneline
```

Vas a ver tus dos commits, el más reciente arriba. Eso es tu historial.

### 3.7 Lo mismo, pero con botones (VSCode)

Si la terminal te resulta intimidante, VSCode hace lo mismo con clics. En el ícono de **Control de código fuente** (ramita, barra lateral izquierda):
- Los archivos modificados aparecen en una lista.
- El **"+"** al lado de cada archivo equivale a `git add`.
- La caja de texto arriba es el mensaje, y el botón **Confirmar (Commit)** equivale a `git commit`.

> No hay una forma "más correcta". Usá la que te resulte más cómoda; ambas hacen exactamente lo mismo.

---

## 4. Subir a GitHub: tu Caja Fuerte (minutos 45-65)

### 4.1 Creá el repositorio vacío en GitHub

1. Entrá a github.com, ícono **"+"** (arriba a la derecha) → **New repository**.
2. **Repository name:** `mis-prompts`
3. **Visibilidad:** elegí **Private** (privado) por ahora. Solo vos lo ves.
4. **NO marques** "Add a README" ni ".gitignore" — tu carpeta ya tiene contenido y esto generaría un conflicto.
5. Click en **Create repository**.

### 4.2 Conectá tu carpeta con GitHub

GitHub te muestra una página con instrucciones. Buscá la sección "…or push an existing repository from the command line". Son tres comandos (cambiá `TU_USUARIO` por el tuyo):

```bash
git remote add origin https://github.com/TU_USUARIO/mis-prompts.git
git branch -M main
git push -u origin main
```

**Qué hace cada uno, en español:**
- `git remote add origin ...` → "Anotá la dirección de mi caja fuerte en la nube".
- `git branch -M main` → "Llamá `main` a mi línea principal de versiones" (es el nombre estándar).
- `git push -u origin main` → "Subí todo mi historial a la caja fuerte".

### 4.3 Si te pide iniciar sesión

La primera vez, Git/VSCode abre una ventana del navegador pidiéndote que autorices con tu cuenta de GitHub. Aceptá. **No uses tu contraseña de GitHub directamente en la terminal** — hoy GitHub no la acepta para esto; el método del navegador es el correcto y el más seguro.

### 4.4 Verificá el resultado

Refrescá la página de tu repositorio en GitHub. Vas a ver tu archivo `asistente.md`. Hacé click en él: tu contenido está en la nube. Y si hacés click en **"2 commits"** (o el reloj de historial), ves tus dos versiones guardadas.

### 4.5 El ciclo completo de trabajo diario

Desde hoy, tu rutina es siempre esta:

```
1. Editás tus archivos
2. git add .                      (o el "+" en VSCode)
3. git commit -m "qué cambié"
4. git push                       (sube a GitHub)
```

> **Dato de oro:** `git add .` (con el punto) agrega **todos** los archivos modificados de una vez. Útil, pero revisá antes con `git status` que no estés subiendo algo que no querés (ver sección 6.2).

### 4.6 Hacé el ciclo una vez más, solo

Agregá un archivo nuevo, `politica_precios.md`, con 3-4 líneas de las reglas de precio de tu negocio. Hacé `add`, `commit` y `push`. Verificá en GitHub que aparece.

---

## 5. La Máquina del Tiempo (minutos 65-80)

Este es el bloque que hace que todo el esfuerzo valga la pena.

### 5.1 Equivocate a propósito

Abrí `asistente.md` y **rompelo**: borrá media instrucción, o agregá una frase absurda ("Siempre respondé en inglés a los clientes"). Guardá el archivo.

Ahora, ¿qué pasó exactamente? Preguntale a Git:

```bash
git diff
```

Git te muestra, línea por línea, qué borraste (en rojo, con `-`) y qué agregaste (en verde, con `+`). Es como el "control de cambios" de Word, pero más preciso.

### 5.2 Volvé atrás: deshacer un cambio que NO guardaste

Si todavía no hiciste `commit`, podés descartar el desastre y volver a la última versión guardada:

```bash
git restore asistente.md
```

Tu archivo vuelve a como estaba en el último commit. Abrilo y comprobalo: el error desapareció.

> ⚠️ **Cuidado:** `git restore` borra los cambios sin guardar **para siempre** — no hay "deshacer" del deshacer. Usalo solo cuando estés segura/o de querer descartar.

### 5.3 Volvé atrás: ver una versión vieja

```bash
git log --oneline
```

Cada commit tiene un código corto (por ejemplo `a1b2c3d`). Para **mirar** cómo estaba un archivo en una versión anterior sin perder nada:

```bash
git show a1b2c3d:asistente.md
```

Esto imprime el contenido del archivo tal como estaba en ese commit. Es solo mirar, no cambia nada.

### 5.4 Volvé atrás: deshacer un commit que ya hiciste (de forma segura)

Si ya hiciste `commit` (y hasta `push`) de un cambio malo, la forma segura de deshacerlo es con `revert`:

```bash
git revert HEAD
```

Esto **no borra** el historial: crea un commit nuevo que deshace el último. El error queda registrado (transparencia total) pero tu archivo vuelve a estar bien. Después, `git push` para actualizar GitHub.

> **Por qué `revert` y no otros comandos más agresivos:** existen formas de "borrar" commits del historial, pero son peligrosas si ya subiste el trabajo a GitHub o si compartís el repositorio con otros. `revert` es la opción que no puede romper nada, y es la que te recomendamos como principiante.

### 5.5 El mapa de "¿cómo vuelvo atrás?"

| Situación | Comando |
|---|---|
| Edité un archivo y quiero descartar los cambios (todavía no hice commit) | `git restore archivo` |
| Quiero **mirar** cómo estaba algo antes | `git show codigo:archivo` |
| Ya hice commit de algo malo y quiero deshacerlo | `git revert HEAD` |
| No sé qué cambié | `git diff` (cambios sin guardar) o `git log --oneline` (historial) |

---

## 6. Cierre y Reglas de Oro (minutos 80-90)

### 6.1 Los 7 comandos de tu vida diaria

| Comando | Qué hace |
|---|---|
| `git status` | "¿Qué cambió?" — usalo todo el tiempo |
| `git add .` | Prepara todos los cambios para la foto |
| `git commit -m "mensaje"` | Saca la foto (guarda la versión) |
| `git push` | Sube tus versiones a GitHub |
| `git pull` | Baja a tu computadora lo que haya en GitHub (útil si trabajás desde dos equipos) |
| `git log --oneline` | Mirá tu historial |
| `git diff` | Mirá qué cambiaste desde el último commit |

### 6.2 🔒 Lo que JAMÁS se sube a GitHub

> **Esta regla conecta directo con la Clase 2 (privacidad) y es la que más daño evita.** Un repositorio público lo puede ver cualquier persona del mundo, y un repositorio privado puede volverse público por error. Nunca subas:

| Nunca subas... | Por qué |
|---|---|
| **Contraseñas o claves de API** (las que usarás con las herramientas de IA más adelante) | Hay bots que escanean GitHub las 24 horas buscando claves expuestas, y las usan en minutos. Te pueden generar cobros enormes en tu cuenta |
| **Datos reales de clientes** (nombres, cédulas, teléfonos, facturas) | Violación de privacidad y de ley (Clase 2) |
| **Documentos internos confidenciales** | Aunque el repo sea privado, un error de configuración lo expone |
| **Fotos o archivos personales** | Mismo motivo |

**Cómo protegerte: el archivo `.gitignore`.** Es una lista de archivos que Git debe ignorar siempre. Creá un archivo llamado `.gitignore` en tu carpeta y escribí adentro, por ejemplo:

```
.env
claves.txt
datos_clientes/
*.xlsx
```

Todo lo que figure ahí, Git lo ignora y nunca lo sube.

> **Si alguna vez subís una clave por error:** no alcanza con borrarla y volver a subir — queda en el historial. La regla de oro es **cambiar esa clave de inmediato** en el servicio correspondiente (se la considera "comprometida") y recién después limpiar el repositorio.

### 6.3 Buenos hábitos de commits

- **Commits chicos y frecuentes**, no uno gigante al final de la semana.
- **Mensajes que expliquen el "qué" y el "por qué"**, no solo "cambios".
- **`git status` antes de cada `commit`**: revisá siempre qué estás por guardar.

### 6.4 Problemas comunes y su solución

| Síntoma | Causa probable | Solución |
|---|---|---|
| `git: command not found` | Git no está instalado, o VSCode no se reinició | Instalá Git y reiniciá VSCode |
| `fatal: not a git repository` | Estás en una carpeta que no tiene `git init` | Verificá que abriste la carpeta correcta; corré `git init` si corresponde |
| `Author identity unknown` | No configuraste tu nombre/correo (sección 2.2) | Corré los dos comandos de `git config` |
| `rejected ... fetch first` al hacer `push` | El repo en GitHub tiene cambios que vos no tenés (por ejemplo, creaste un README en GitHub) | Corré `git pull` primero y después `git push` |
| Me abre una ventana rara con texto (editor) | Hiciste `commit` sin `-m` | Escribí el mensaje, guardá y cerrá esa ventana |
| `nothing to commit, working tree clean` | No hay cambios nuevos que guardar | No es un error: simplemente no modificaste nada |

---

## Tarea

1. **Convertí tu carpeta de trabajo del taller en un repositorio** y subila a GitHub (privado).
2. Creá un archivo `.gitignore` con al menos 3 tipos de archivo que nunca querés subir.
3. Dentro del repo, guardá **3 prompts reales** de tu negocio o casa (por ejemplo: el de atención al cliente, uno de redes sociales, uno de organización del hogar), uno por archivo `.md`.
4. Hacé **al menos 5 commits** con mensajes claros (un commit por cada cambio importante).
5. Practicá el "equivocarte a propósito + volver atrás" una vez más por tu cuenta.
6. **Traé a la próxima clase:** el enlace a tu repositorio (o una captura del historial de commits en GitHub).

---

## Resumen Visual

```
┌──────────────────────────────────────────────────────────────┐
│               EL CICLO DE TRABAJO CON GIT Y GITHUB            │
│                                                                │
│   Editás archivos                                              │
│        │                                                       │
│        ▼                                                       │
│   git add .         →  "preparo la foto"                       │
│        │                                                       │
│        ▼                                                       │
│   git commit -m ""  →  "saco la foto, con nota"                │
│        │                                                       │
│        ▼                                                       │
│   git push          →  "guardo copia en la caja fuerte"        │
│                                                                │
│   ¿Algo salió mal?  →  git restore / git revert                │
│   ¿Qué cambió?      →  git diff / git log --oneline            │
└──────────────────────────────────────────────────────────────┘
```

---

> **Recordá:** Git no es para programadores. Es para cualquiera que no quiera volver a perder una versión buena de su trabajo. Cada commit es un punto de retorno seguro.

---

