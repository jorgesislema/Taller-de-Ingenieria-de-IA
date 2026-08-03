# 📌 Guía Rápida - Laboratorio 3: ViMusic

## 🗂️ Comandos Esenciales

| Comando | Qué hace |
|---------|----------|
| `git clone https://github.com/byStackDev/ViMusic-es-ES.git` | Clona el repositorio |
| `cd ViMusic-es-ES` | Entra a la carpeta |
| `dir` (Windows) / `ls` (Mac/Linux) | Lista archivos |
| `type app\src\main\AndroidManifest.xml` | Ver permisos |
| `find . -name "*.xml"` | Buscar archivos XML |

---

## 📁 Estructura del Repositorio

```
ViMusic-es-ES/
├── app/                    ← Código principal de la app
│   └── src/main/
│       ├── AndroidManifest.xml  ← Permisos de la app
│       └── java/           ← Código Kotlin
├── innertube/              ← Cliente de YouTube Music
├── kugou/                  ← Servicio de letras
├── compose-persist/        ← Persistencia de datos
├── compose-reordering/     ← Reordenar elementos
├── compose-routing/        ← Navegación
├── gradle/                 ← Configuración de compilación
├── build.gradle.kts        ← Dependencias principales
├── settings.gradle.kts     ← Configuración del proyecto
├── gradlew                 ← Wrapper de Gradle (Mac/Linux)
├── gradlew.bat             ← Wrapper de Gradle (Windows)
├── .gitignore              ← Archivos excluidos de Git
├── LICENSE                 ← Licencia GPL-3.0
└── README.md               ← Documentación principal
```

---

## 🔐 Permisos de Android (Qué buscar)

| Permiso | Descripción | ¿Necesario? |
|---------|-------------|-------------|
| `INTERNET` | Acceso a internet | ✅ Sí |
| `ACCESS_NETWORK_STATE` | Verificar conexión | ✅ Sí |
| `WAKE_LOCK` | Mantener pantalla activa | ⚠️ Opcional |
| `FOREGROUND_SERVICE` | Servicio en segundo plano | ✅ Sí |
| `POST_NOTIFICATIONS` | Enviar notificaciones | ⚠️ Opcional |
| `READ_EXTERNAL_STORAGE` | Leer archivos | ⚠️ Revisar |
| `WRITE_EXTERNAL_STORAGE` | Escribir archivos | ⚠️ Revisar |

---

## 🔍 Qué Buscar en el Código

### Palabras Clave de Seguridad

| Palabra | Significado | Riesgo |
|---------|-------------|--------|
| `API_KEY` | Llave de API | ⚠️ No debe estar hardcodeada |
| `SECRET` | Secreto/contraseña | 🔴 Alto |
| `PASSWORD` | Contraseña | 🔴 Alto |
| `TOKEN` | Token de autenticación | ⚠️ Depende |
| `http://` | Conexión no segura | 🔴 Alto |
| `https://` | Conexión segura | ✅ Seguro |

---

## 📱 Pasos para Instalar APK en Android

### Antes de Instalar
1. ✅ Descargaste del repositorio oficial
2. ✅ Verificaste que el tamaño es razonable
3. ✅ Analizaste los permisos
4. ✅ Tienes respaldo de tu dispositivo

### Durante la Instalación
1. Ve a Ajustes > Seguridad
2. Habilita "Fuentes desconocidas"
3. Abre el archivo APK
4. Sigue las instrucciones

### Después de Instalar
1. Abre la app
2. Verifica que funciona
3. Monitorea comportamiento sospechoso
4. Si algo raro → Desinstala inmediatamente

---

## 🤖 Prompts Rápidos

### Explorar repositorio:
```
Explora el repositorio ViMusic-es-ES y dime qué hace cada carpeta
```

### Analizar seguridad:
```
Analiza la seguridad de ViMusic-es-ES y dame un informe
```

### Verificar permisos:
```
¿Los permisos de Android de ViMusic son los mínimos necesarios?
```

### Decisión de instalación:
```
¿Es seguro instalar ViMusic en mi teléfono? Dame 5 razones
```

---

## 🚨 Señales de Alarma

**NO instales la app si encuentras:**

- [ ] Permisos excesivos (ej: acceder a contactos, cámara)
- [ ] Conexiones HTTP (no HTTPS)
- [ ] API keys hardcodeadas en el código
- [ ] Código ofuscado o ilegible
- [ ] Issues reportados sobre malware
- [ ] Autor desconocido o sin historial
- [ ] Tamaño del APK sospechoso (muy grande o muy pequeño)

---

## ✅ Checklist de Seguridad

### Al Clonar Repositorios
- [ ] Verifiqué la reputación del autor
- [ ] Leí el README completamente
- [ ] Revisé los issues abiertos
- [ ] Exploré la estructura del proyecto
- [ ] Busqué palabras clave de seguridad

### Al Instalar Apps
- [ ] Descargué del repositorio oficial
- [ ] Verifiqué la integridad del archivo
- [ ] Analicé los permisos
- [ ] Tengo un respaldo del dispositivo
- [ ] Sé cómo desinstalar si algo falla

---

## 🆕 Si Te Atascas

1. **No puedo clonar** → Verifica que Git esté instalado
2. **No encuentro AndroidManifest.xml** → Busca en app/src/main/
3. **No entiendo el código** → Usa el PROMPT 2 con DeepSeek
4. **No sé si instalar** → Usa el PROMPT 4 con DeepSeek
5. **La app no funciona** → Verifica que tengas Android 6.0+

---

## 📚 Recursos

- [GitHub Docs: Cloning repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
- [Android: App permissions](https://developer.android.com/guide/topics/permissions/overview)
- [OWASP Mobile Security](https://owasp.org/www-project-mobile-top-10/)
