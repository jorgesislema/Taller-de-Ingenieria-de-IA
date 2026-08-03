# 🤖 Guía de Prompts para el Laboratorio 3: ViMusic

## 📋 PROMPTS PRINCIPALES (5 Fases)

---

### 🔍 FASE 1: Exploración del Repositorio

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

### 📥 FASE 2: Análisis de Código Clonado

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

### 🔒 FASE 3: Auditoría de Seguridad Profunda

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

### 📱 FASE 4: Verificación de Seguridad Pre-instalación

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

### 💡 FASE 5: Reflexión y Aprendizaje

```
He completado un laboratorio de ciberseguridad donde:
1. Cloné el repositorio ViMusic-es-ES
2. Analicé el código fuente
3. Identifiqué permisos de Android
4. Evalué riesgos de seguridad
5. Instalé la app (opcional)

Ayúdame a reflexionar:
1. ¿Qué aprendí sobre ciberseguridad hoy?
2. ¿Qué haría diferente la próxima vez que clone un repositorio?
3. ¿Cómo aplico esto en mi vida diaria con apps móviles?
4. ¿Cuáles son las 5 reglas de oro que debo recordar siempre?

Resumen cada punto en una oración simple y clara.
```

---

## 🤖 PROMPTS ADICIONALES PARA MOMENTOS ESPECÍFICOS

---

### 📄 Cuando no entiendes un archivo

```
No entiendo qué hace este archivo en el proyecto ViMusic-es-ES:

[PEGA EL CONTENIDO DEL ARCHIVO O SU RUTA]

Explícame:
1. Para qué sirve
2. Qué relación tiene con el resto del proyecto
3. Si tiene implicaciones de seguridad
```

---

### 🐛 Cuando encuentras algo sospechoso

```
Encontré este código en el repositorio ViMusic-es-ES que me parece 
sospechoso:

[PEGA EL CÓDIGO O DESCRIBE LO QUE ENCONTRASTE]

Archivo: [NOMBRE DEL ARCHIVO]
Línea: [NÚMERO DE LÍNEA]

¿Es esto un problema de seguridad? Explícalo como si tuviera 10 años.
```

---

### 🔍 Cuando quieres analizar un permiso específico

```
El permiso [NOMBRE_DEL_PERMISO] aparece en el AndroidManifest.xml 
de ViMusic-es-ES.

Explícame:
1. ¿Qué permite hacer a la app?
2. ¿Es necesario para un reproductor de música?
3. ¿Qué riesgos tiene?
4. ¿Lo quitarías? ¿Por qué sí o por qué no?
```

---

### 📊 Cuando necesitas comparar con otra app

```
Quiero comparar la seguridad de ViMusic-es-ES con otra app de 
música de código abierto.

ViMusic tiene estos permisos: [LISTA DE PERMISOS]

¿Cómo se compara esto con apps similares? ¿Es más seguro o menos?
¿Qué permisos debería tener un reproductor de música ideal?
```

---

### 🛡️ Cuando quieres crear tu propia lista de verificación

```
Basado en mi experiencia analizando ViMusic-es-ES, ayúdame a crear 
una lista de verificación de seguridad que pueda usar siempre que:

1. Clone un repositorio de GitHub
2. Instale una app de fuente desconocida
3. Ejecute código de internet

Para cada punto, dame una acción específica y fácil de recordar.
```

---

### 📱 Cuando tienes dudas sobre instalar

```
Estoy en dudas sobre instalar ViMusic-es-ES en mi teléfono.

Factores que me preocupan:
- [LO QUE TE PREOCUPA]

Factores positivos:
- [LO QUE TE GUSTA]

Ayúdame a tomar una decisión informada. ¿Los beneficios superan 
los riesgos? ¿Qué hago si igual quiero probarla?
```

---

## 💡 Consejos para Usar los Prompts

1. **Sé específico**: "El permiso WAKE_LOCK en la línea 45" vs "un permiso"
2. **Da contexto**: "He clonado ViMusic y encontré..." vs "Hay algo raro"
3. **Pide explicaciones**: "Explícame por qué es un riesgo"
4. **Verifica siempre**: La IA a veces se equivoca
5. **Guarda los prompts** que te funcionaron

---

## 🔄 Flujo de Conversación Efectiva

```
TÚ: [Prompt inicial]
IA: [Respuesta]
TÚ: "¿Por qué ese permiso es riesgoso?"
IA: [Explicación]
TÚ: "¿Qué pasaría si no lo instalo?"
IA: [Alternativas]
TÚ: "¿Cómo verifico que el APK es seguro?"
IA: [Pasos de verificación]
TÚ: "Gracias, ya entiendo"
```

---

## 🚫 Evita Esto

| ❌ No hagas | ✅ Mejor haz |
|-------------|-------------|
| Instalar sin analizar | Primero analiza, luego decide |
| Copiar sin entender | Lee y comprende cada línea |
| Ignorar permisos | Evalúa si son necesarios |
| No verificar integridad | Siempre verifica antes de instalar |
| Confiar ciegamente en la IA | Verifica con otras fuentes |
