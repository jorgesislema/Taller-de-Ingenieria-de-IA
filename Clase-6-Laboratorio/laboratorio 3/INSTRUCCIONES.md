# 🧪 Laboratorio 3: ViMusic - Clonación, Seguridad y Ejecución

## 🎯 Objetivo
Clonar el reproductor de música ViMusic, realizar un análisis de ciberseguridad con DeepSeek, e instalar la app para verificar que funciona.

## 🧠 Lo que aprenderás
- A clonar repositorios de GitHub
- A analizar la seguridad de un proyecto de código abierto
- A identificar riesgos al instalar apps de fuentes desconocidas
- A tomar decisiones informadas sobre seguridad
- A usar IA como herramienta de auditoría de seguridad

---

## 📋 Requisitos Previos
- Git instalado
- Navegador web
- Dispositivo Android (OPCIONAL para instalación)
- Cuenta de DeepSeek o ChatGPT

---

## ⏱ Duración Estimada: 90 minutos

---

# 🔍 FASE 1: Exploración y Reconocimiento (15 min)

**Objetivo:** Entender qué es ViMusic y cómo está construido antes de clonar.

## Paso 1.1: Explorar el Repositorio en GitHub

1. Abre tu navegador ve a: **https://github.com/byStackDev/ViMusic-es-ES**
2. Lee el `README.md` del repositorio
3. Explora la estructura de carpetas
4. Identifica los archivos principales

## Paso 1.2: Responde estas Preguntas

| Pregunta | Tu Respuesta |
|----------|--------------|
| ¿Qué hace esta app? | |
| ¿Qué tecnología usa? | |
| ¿En qué idioma está? | |
| ¿Tiene releases listos? | |

## Paso 1.3: Analizar el AndroidManifest.xml

Busca y abre el archivo `app/src/main/AndroidManifest.xml`

**Preguntas para reflexionar:**
1. ¿Qué permisos pide la app?
2. ¿Por qué necesita acceso a internet?
3. ¿Qué servicios externos consulta?

---

# 📝 Prompt 1 - Exploración con DeepSeek

Copia y pega este prompt en DeepSeek o ChatGPT:

```
Actúa como un Analista de Seguridad. Estoy explorando el repositorio 
ViMusic-es-ES (https://github.com/byStackDev/ViMusic-es-ES). Es una 
app de Android para reproducir música desde YouTube Music.

Basado en la estructura del repositorio, explica en lenguaje sencillo:
1. Qué hace cada carpeta principal (app/, innertube/, kugou/, etc.)
2. Qué tecnologías usa (Kotlin, Jetpack Compose, etc.)
3. Qué permisos de Android necesita y por qué
4. Qué servicios externos consulta
5. Qué tan seguro ves este proyecto a primera vista
```

---

# 📥 FASE 2: Clonación y Análisis de Código (20 min)

**Objetivo:** Descargar el código fuente y analizarlo.

## Paso 2.1: Clonar el Repositorio

Abre la terminal y ejecuta:

```bash
git clone https://github.com/byStackDev/ViMusic-es-ES.git
cd ViMusic-es-ES
```

## Paso 2.2: Explorar la Estructura

```bash
# En Windows
dir

# En Mac/Linux
ls -la
```

## Paso 2.3: Listar Archivos Importantes

```bash
# Ver archivos de Android
type app\src\main\AndroidManifest.xml

# Ver configuración de Gradle
type build.gradle.kts
```

## Paso 2.4: Buscar Archivos Sensibles

Busca en el código estas palabras clave:
- `API_KEY`
- `SECRET`
- `PASSWORD`
- `TOKEN`
- `http://` (conexiones no seguras)

---

# 📝 Prompt 2 - Análisis de Código con DeepSeek

```
Actúa como un Ingeniero de Ciberseguridad. He clonado el repositorio 
ViMusic-es-ES. Necesito analizar el código fuente para detectar 
posibles vulnerabilidades.

Revisa los siguientes aspectos y dime si hay problemas de seguridad:
1. ¿Hay API keys o secrets hardcodeados en el código?
2. ¿Los permisos de Android son los mínimos necesarios?
3. ¿Las conexiones a internet son seguras (HTTPS)?
4. ¿Qué datos locales guarda la app?
5. ¿Qué buenas prácticas de seguridad cumple o no cumple?

Escribe un informe sencillo como si le explicaras a un estudiante 
de primer año.
```

---

# 🔒 FASE 3: Análisis Profundo de Ciberseguridad (25 min)

**Objetivo:** Realizar una auditoría completa de seguridad.

## Paso 3.1: Identificar Permisos

Abre `app/src/main/AndroidManifest.xml` y lista todos los permisos:

| Permiso | ¿Es necesario? | Riesgo |
|---------|----------------|--------|
| INTERNET | | |
| ACCESS_NETWORK_STATE | | |
| WAKE_LOCK | | |
| FOREGROUND_SERVICE | | |
| (otros que encuentres) | | |

## Paso 3.2: Analizar Conexiones de Red

Busca en el código todas las URLs a las que se conecta:

| URL | Protocolo | ¿Seguro? |
|-----|-----------|----------|
| | | |

## Paso 3.3: Evaluar Almacenamiento Local

Preguntas para investigar:
1. ¿Dónde guarda la app los datos?
2. ¿Están encriptados?
3. ¿Qué información personal almacena?

---

# 📝 Prompt 3 - Análisis Profundo de Seguridad

```
Actúa como un Auditor de Seguridad especializado en aplicaciones Android. 

Realiza un análisis de ciberseguridad completo del repositorio ViMusic-es-ES 
y genera un informe que incluya:

## 1. Análisis de Permisos
- Lista de permisos en AndroidManifest.xml
- Evalúa si cada permiso es necesario o excesivo
- Riesgo asociado a cada permiso

## 2. Análisis de Red
- ¿A qué servidores se conecta?
- ¿Usa HTTPS o HTTP?
- ¿Qué datos envía/recibe?

## 3. Almacenamiento Local
- ¿Qué datos guarda en el dispositivo?
- ¿Están encriptados?
- ¿Podría un atacante acceder a ellos?

## 4. Dependencias
- ¿Hay librerías con vulnerabilidades conocidas?
- ¿Están actualizadas?

## 5. Recomendaciones
- Medidas de seguridad a tomar al clonar repositorios
- Buenas prácticas para desarrollo seguro
- Lista de verificación antes de instalar apps de terceros

## 6. Puntuación
- Del 1 al 10, ¿cuán seguro es este proyecto?
- Justifica la puntuación

Explica todo en lenguaje sencillo.
```

---

# 📱 FASE 4: Instalación y Prueba (20 min)

**Objetivo:** Descargar, instalar y probar la app.

## ⚠️ IMPORTANTE: Lee esto ANTES de instalar

> Instalar apps de fuentes desconocidas tiene riesgos. Solo hazlo si 
> confías en el repositorio y entiendes los permisos que le estás dando.

## Paso 4.1: Descargar el APK

### Opción A: Desde GitHub Releases
1. Ve a: https://github.com/byStackDev/ViMusic-es-ES/releases
2. Descarga la última versión (.apk)

### Opción B: Desde Google Drive
1. Ve al README del repositorio
2. Haz clic en el badge "Get it on Google Drive"
3. Descarga el archivo

## Paso 4.2: Verificar el Archivo

Antes de instalar, verifica:
- [ ] El tamaño del archivo es razonable (no muy grande ni muy pequeño)
- [ ] La extensión es `.apk`
- [ ] Lo descargaste del repositorio oficial

## Paso 4.3: Instalar en Android

1. Transfiere el APK a tu dispositivo Android
2. Habilita "Fuentes desconocidas" en Ajustes > Seguridad
3. Abre el archivo APK
4. Sigue las instrucciones de instalación

## Paso 4.4: Probar la App

1. Abre ViMusic
2. Busca una canción
3. Reproduce algo
4. Verifica que funciona correctamente

---

# 📝 Prompt 4 - Verificación de Seguridad

```
Estoy a punto de instalar la app ViMusic-es-ES en mi dispositivo Android.

Antes de instalarla, explícame:
1. ¿Es seguro instalar APKs de GitHub?
2. ¿Qué debo verificar antes de instalar?
3. ¿Qué permisos le estoy dando a la app?
4. ¿Qué riesgos corro al instalar apps de fuentes desconocidas?
5. ¿Cómo puedo verificar que el APK no tiene malware?
6. ¿Qué hago si detecto comportamiento sospechoso?

Dame una lista de verificación que pueda usar siempre que instale 
apps de fuentes desconocidas.
```

---

# 💡 FASE 5: Reflexión y Cierre (10 min)

**Objetivo:** Aprender de la experiencia y aplicar en el futuro.

## Preguntas de Reflexión

Responde en tu cuaderno:

### 1. Sobre el Repositorio
- ¿Qué tan seguro consideras que es ViMusic? (1-10)
- ¿Qué encontrarías que fuera un deal-breaker de seguridad?

### 2. Sobre la Experiencia
- ¿Qué aprendiste sobre ciberseguridad?
- ¿Harías algo diferente la próxima vez?

### 3. Sobre el Uso de IA
- ¿Cómo te ayudó DeepSeek en el análisis?
- ¿Encontraste algo que la IA no vio?

### 4. Sobre Decisiones
- ¿Instalarías esta app en tu dispositivo personal?
- ¿Qué factores consideraste para decidir?

---

# 📋 Checklist Final

Marca con ✓ cuando completés:

### Fase 1: Exploración
- [ ] Exploré el repositorio en GitHub
- [ ] Entiendo qué hace ViMusic
- [ ] Identifiqué las tecnologías que usa

### Fase 2: Clonación
- [ ] Cloné el repositorio exitosamente
- [ ] Exploré la estructura de archivos
- [ ] Busqué archivos sensibles

### Fase 3: Análisis de Seguridad
- [ ] Identifiqué los permisos de Android
- [ ] Analicé las conexiones de red
- [ ] Usé DeepSeek para análisis profundo
- [ ] Generé un informe de seguridad

### Fase 4: Instalación (OPCIONAL)
- [ ] Descargué el APK
- [ ] Verifiqué el archivo
- [ ] Instalé la app
- [ ] Probé que funciona

### Fase 5: Reflexión
- [ ] Respondí las preguntas de reflexión
- [ ] Puedo explicar los riesgos de instalar apps de terceros

---

# 🚀 Comandos Útiles

| Comando | Qué hace |
|---------|----------|
| `git clone [URL]` | Descarga un repositorio |
| `cd [carpeta]` | Entra a una carpeta |
| `dir` o `ls` | Lista archivos |
| `type [archivo]` | Muestra contenido (Windows) |
| `cat [archivo]` | Muestra contenido (Mac/Linux) |

---

# 🛡️ Medidas de Seguridad al Clonar Repositorios

1. **Verifica la reputación** del autor y el proyecto
2. **Lee el README** antes de clonar
3. **Revisa los issues** para ver problemas reportados
4. **Analiza el código** antes de ejecutar
5. **No ejecutes** código que no entiendas
6. **Usa entornos virtuales** cuando sea posible
7. **Verifica integridad** de archivos descargados
8. **Ten antivirus** actualizado
9. **No compartas** credenciales o datos sensibles
10. **Confía pero verifica** siempre

---

**⏱ Tiempo total: 90 minutos**
