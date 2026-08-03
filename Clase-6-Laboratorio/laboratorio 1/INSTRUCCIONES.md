# 🧪 Clase 6: Laboratorio de Reconocimiento de Repositorio

## 🎯 Objetivo
Aprender a reconocer la estructura de un repositorio de software, identificar la función de cada archivo y detectar errores usando IA.

---

## 📋 Requisitos Previos
- Python 3.10 o superior instalado
- Git instalado
- VS Code o editor de código
- Acceso a una IA (ChatGPT, Gemini, etc.)

---

## 🔧 Fase 1: Preparación (5 min)

### Paso 1.1: Verificar Python
Abre la terminal y ejecuta:
```bash
python --version
```
Deberías ver algo como: `Python 3.10.x`

### Paso 1.2: Verificar Git
```bash
git --version
```
Deberías ver: `git version 2.x.x`

---

## 📥 Fase 2: Clonar el Repositorio (5 min)

### Paso 2.1: Clonar desde GitHub
```bash
git clone https://github.com/jorgesislema/El-Chatbot-de-Consola-Integracion-de-API-real.git
```

### Paso 2.2: Entrar a la carpeta
```bash
cd El-Chatbot-de-Consola-Integracion-de-API-real
```

### Paso 2.3: Ver la estructura
**En Windows:**
```bash
dir
```

**En Mac/Linux:**
```bash
ls -la
```

---

## 🔍 Fase 3: Reconocimiento del Repositorio (15 min)

### Paso 3.1: Leer el README
Abre el archivo `README.md` y responde:
1. ¿Qué es este proyecto?
2. ¿Qué dos chatbots incluye?
3. ¿Qué librerías necesita?

### Paso 3.2: Identificar cada archivo
Completa esta tabla en tu cuaderno:

| Archivo | Tipo | Función |
|---------|------|---------|
| `chatbot.py` | | |
| `deepseek_chatbot.py` | | |
| `test_chatbot.py` | | |
| `test_deepseek_chatbot.py` | | |
| `requirements.txt` | | |
| `context.md` | | |
| `arquitectura.md` | | |
| `README.md` | | |

### Paso 3.3: Abrir los archivos de código
Abre `chatbot.py` y `deepseek_chatbot.py` en VS Code.

**Pregunta para reflexionar:**
¿Qué diferencias ves entre ambos archivos?

---

## 🤖 Fase 4: Análisis con IA (15 min)

### Paso 4.1: Copiar el código
Copia el contenido completo de `deepseek_chatbot.py`

### Paso 4.2: Usar este prompt con tu IA

```
Actúa como un profesor de programación para principiantes.

Revisa el siguiente código Python que es un chatbot que usa la API de DeepSeek.

Explica:
1. Qué hace cada función
2. Qué librerías importa y para qué sirven
3. Cómo funciona el bucle principal
4. Si hay algún error, indícalo y explica por qué es un error

CÓDIGO:
[PEGA AQUÍ EL CÓDIGO DE deepseek_chatbot.py]
```

### Paso 4.3: Anotar los hallazgos
Escribe en tu cuaderno:
- Función principal del archivo:
- Librerías que usa:
- Errores encontrados:

---

## 🐛 Fase 5: Encontrar el Error (15 min)

### Paso 5.1: Ejecutar el chatbot (opcional)
Si tienes las API keys configuradas:
```bash
python deepseek_chatbot.py
```

**¿Qué error ves?**

### Paso 5.2: Usar este prompt con tu IA

```
Revisa el siguiente código que debería conectar con la API de DeepSeek.

El archivo se llama deepseek_chatbot.py pero tiene un error que impide 
que funcione correctamente con DeepSeek.

Encuentra el error y explícalo paso a paso.

CÓDIGO:
[PEGA AQUÍ EL CÓDIGO DE deepseek_chatbot.py]
```

### Paso 5.3: Identificar el error
El error está en la función `cargar_api_key()`. 

**Pista:** Compara qué API key busca el código vs cuál debería buscar.

| Lo que dice el código | Lo que debería decir |
|----------------------|---------------------|
| `os.getenv("GEMINI_API_KEY")` | `os.getenv("DEEPSEEK_API_KEY")` |

### Preguntas de reflexión:
1. ¿Por qué es incorrecto usar `GEMINI_API_KEY` en un archivo que usa DeepSeek?
2. ¿Qué pasaría si ambas variables existen en el `.env`?
3. ¿Cómo previene este tipo de errores el uso de variables de entorno?

---

## ✏️ Fase 6: Corregir el Error (10 min)

### Paso 6.1: Corregir manualmente
Abre `deepseek_chatbot.py` y cambia la línea 23:

**ANTES (con error):**
```python
clave = os.getenv("GEMINI_API_KEY")
```

**DESPUÉS (corregido):**
```python
clave = os.getenv("DEEPSEEK_API_KEY")
```

### Paso 6.2: Verificar la corrección
Puedes pedir a la IA que verifique:

```
¿Está correcto el siguiente código ahora? Verifica que use 
la variable de entorno correcta para DeepSeek.

def cargar_api_key():
    """Lee la llave secreta (API Key) desde el archivo .env."""
    load_dotenv()
    clave = os.getenv("DEEPSEEK_API_KEY")
    return clave
```

---

## 📝 Fase 7: Cierre y Reflexión (10 min)

### Responde estas preguntas en tu cuaderno:

1. **¿Cuántos archivos tiene el repositorio?**
   __________

2. **¿Cuál es la diferencia principal entre chatbot.py y deepseek_chatbot.py?**
   __________

3. **¿Qué error se encontró y por qué es grave?**
   __________

4. **¿Qué aprendiste sobre el uso de IA para encontrar errores?**
   __________

5. **¿Por qué es importante no subir el archivo .env a GitHub?**
   __________

---

## 🏆 Criterios de Éxito

Marca con ✓ cuando completés:
- [ ] Cloné el repositorio exitosamente
- [ ] Puedo explicar qué hace al menos 5 archivos
- [ ] Identifiqué el error en deepseek_chatbot.py
- [ ] Entiendo por qué usar DEEPSEEK_API_KEY es correcto
- [ ] Usé IA para ayudarme a encontrar el error
- [ ] Corregí el error correctamente

---

## 📚 Recursos Adicionales

- [Documentación de DeepSeek API](https://platform.deepseek.com/api_keys)
- [Documentación de Google Gemini](https://ai.google.dev/)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)

---

**⏱ Tiempo total estimado: 80 minutos**
https://drive.google.com/drive/u/2/folders/1ORi48lTXyRGp8lBcvZSqarpk59JvIzaI