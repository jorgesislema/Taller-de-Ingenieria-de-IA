# 🗂️ Cheat Sheet — Git y GitHub
### Tu máquina del tiempo + tu caja fuerte en la nube

> **Git** = el programa en tu computadora que recuerda cada versión de tu trabajo.
> **GitHub** = el sitio web donde guardás una copia a salvo.

---

## 🔁 El ciclo diario (lo único que necesitás el 90% del tiempo)

```
1. Editás tus archivos
2. git add .                       → "preparo la foto"
3. git commit -m "qué cambié"      → "saco la foto, con nota"
4. git push                        → "guardo copia en la nube"
```

> **Antes de cada commit:** corré `git status` para revisar qué estás por guardar.

---

## 🧰 Comandos esenciales

| Comando | Qué hace |
|---|---|
| `git --version` | Verifica que Git esté instalado |
| `git init` | Convierte la carpeta actual en un repositorio |
| `git status` | **¿Qué cambió?** Usalo todo el tiempo |
| `git add archivo.md` | Prepara UN archivo para guardar |
| `git add .` | Prepara TODOS los archivos modificados |
| `git commit -m "mensaje"` | Guarda la versión con una nota |
| `git push` | Sube tus versiones a GitHub |
| `git pull` | Baja a tu computadora lo que haya en GitHub |
| `git clone <url>` | Descarga un repositorio de GitHub a tu computadora |
| `git log --oneline` | Muestra tu historial resumido |
| `git diff` | Muestra qué cambiaste desde el último commit |

---

## ⚙️ Configuración inicial (una sola vez en la vida)

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu_correo@ejemplo.com"
```

---

## 🚀 Subir un proyecto nuevo a GitHub (primera vez)

```bash
git init
git add .
git commit -m "Primera versión"
git remote add origin https://github.com/TU_USUARIO/nombre-repo.git
git branch -M main
git push -u origin main
```

> Antes, creá el repositorio **vacío** en github.com (botón **+** → *New repository*), **sin** marcar "Add a README".

---

## ⏪ ¿Algo salió mal? Cómo volver atrás

| Situación | Comando |
|---|---|
| Edité un archivo y quiero **descartar** los cambios (sin commit aún) | `git restore archivo` ⚠️ *no se puede deshacer* |
| Hice `add` por error y quiero **sacarlo** de la foto | `git restore --staged archivo` |
| Quiero **mirar** cómo estaba un archivo antes | `git show codigo:archivo` |
| Ya hice commit de algo malo y quiero **deshacerlo** de forma segura | `git revert HEAD` |
| No sé qué cambié | `git diff` (sin guardar) · `git log --oneline` (historial) |

> `git revert` **no borra** el historial: crea un commit nuevo que deshace el anterior. Es la opción segura.

---

## ✍️ Cómo escribir un buen mensaje de commit

| ❌ Mal | ✅ Bien |
|---|---|
| `"cambios"` | `"Agregué la regla de no inventar precios"` |
| `"arreglé"` | `"Corregí el horario de los domingos"` |
| `"v2"` | `"Cambié el tono del asistente a más cercano"` |

**Regla:** que vos, dentro de 6 meses, entiendas qué cambió **sin abrir el archivo**.

---

## 🔒 Lo que JAMÁS se sube a GitHub

| Nunca subas... | Por qué |
|---|---|
| 🔑 Contraseñas y **claves de API** | Hay bots que las buscan en GitHub y las usan en minutos |
| 👤 Datos reales de **clientes** (nombres, cédulas, teléfonos, facturas) | Violación de privacidad y de ley |
| 📄 Documentos internos confidenciales | Un repo privado puede volverse público por error |
| 🖼️ Fotos o archivos personales | Mismo motivo |

### El archivo `.gitignore`

Lista de archivos que Git **ignora siempre**. Creá un archivo llamado `.gitignore` en tu carpeta:

```
.env
claves.txt
datos_clientes/
*.xlsx
```

> **Si subiste una clave por error:** borrarla no alcanza (queda en el historial). **Cambiá la clave de inmediato** en el servicio correspondiente y después limpiá el repositorio.

---

## 🖱️ En VSCode (sin escribir comandos)

| Quiero... | Hago... |
|---|---|
| Ver qué cambió | Ícono de **Control de código fuente** (ramita, barra lateral izquierda) |
| `git add` | Click en el **+** al lado del archivo |
| `git commit` | Escribo el mensaje arriba y click en **Confirmar (Commit)** |
| `git push` | Botón **Sincronizar cambios** / **Push** |
| Abrir la terminal | Menú **Terminal → Nueva terminal** |

---

## 🩺 Problemas comunes

| Síntoma | Solución |
|---|---|
| `command not found` | Instalá Git desde git-scm.com y **reiniciá VSCode** |
| `not a git repository` | Estás en la carpeta equivocada, o falta `git init` |
| `Author identity unknown` | Corré los dos comandos de `git config` (arriba) |
| `rejected ... fetch first` al hacer `push` | Corré `git pull` y después `git push` |
| Se abre una ventana de texto rara | Hiciste `commit` sin `-m`. Escribí el mensaje, guardá y cerrá |
| `nothing to commit, working tree clean` | No es un error: no hay cambios nuevos |

---

## ✅ Checklist antes de cada `push`

- [ ] Corrí `git status` y revisé qué voy a subir
- [ ] No hay claves, contraseñas ni datos de clientes en los archivos
- [ ] Mi mensaje de commit explica qué cambié
- [ ] Mi `.gitignore` está al día

---

> **Recordá:** Git no es para programadores. Es para cualquiera que no quiera volver a perder una versión buena de su trabajo. **Cada commit es un punto de retorno seguro.**
