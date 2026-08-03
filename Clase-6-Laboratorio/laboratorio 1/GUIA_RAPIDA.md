# 📌 Guía Rápida de Referencia - Clase 6

## 🗂️ Comandos de Git

| Comando | Qué hace |
|---------|----------|
| `git clone [URL]` | Descarga un repositorio de GitHub |
| `git status` | Muestra el estado de los cambios |
| `git add .` | Prepara todos los archivos para guardar |
| `git commit -m "mensaje"` | Guarda los cambios |
| `git push` | Sube los cambios a GitHub |

---

## 📁 Tipos de Archivos en el Repositorio

| Extensión | Tipo | Ejemplo |
|-----------|------|---------|
| `.py` | Código Python | chatbot.py |
| `.md` | Documentación Markdown | README.md |
| `.txt` | Texto simple | requirements.txt |
| `.env` | Variables secretas | .env (NO se sube a GitHub) |
| `.gitignore` | Lista de archivos ocultos | .gitignore |

---

## 🐍 Conceptos de Python

### Importar
```python
import os  # Abre una caja de herramientas
```

### Variable de entorno
```python
clave = os.getenv("NOMBRE_VARIABLE")  # Lee un dato secreto
```

### Función
```python
def mi_funcion():  # "def" define una función
    # código aquí
    return resultado  # Devuelve algo
```

### Bucle while
```python
while True:  # Se repite para siempre
    # código que se repite
    break  # Sale del bucle
```

### Manejo de errores
```python
try:
    # código que puede fallar
except:
    # qué hacer si falla
```

---

## 🤖 Cómo Usar IA para Encontrar Errores

### Paso 1: Copia el código
Selecciona todo el código problemático

### Paso 2: Pregunta específico
❌ "¿Qué está mal?" (muy vago)
✅ "Revisa esta función y dime si usa la variable de entorno correcta para DeepSeek"

### Paso 3: Verifica la respuesta
- ¿Tiene sentido?
- ¿Puedo probarlo?
- ¿La explicación es clara?

---

## 🐛 Error Común en Este Laboratorio

**Archivo:** deepseek_chatbot.py  
**Función:** cargar_api_key()

```python
# ❌ INCORRECTO - Usa la API key de Gemini
clave = os.getenv("GEMINI_API_KEY")

# ✅ CORRECTO - Usa la API key de DeepSeek
clave = os.getenv("DEEPSEEK_API_KEY")
```

**¿Por qué es error?**  
Porque cada servicio de IA tiene su propia llave. No puedes usar la llave de Google para entrar a DeepSeek, como no puedes usar tu llave de casa para entrar a la de un amigo.

---

## 📝 Checklist del Laboratorio

- [ ] git clone funciona
- [ ] Puedo ver los archivos con `ls` o `dir`
- [ ] Leo el README.md
- [ ] Abro chatbot.py y lo entiendo
- [ ] Abro deepseek_chatbot.py y lo entiendo
- [ ] Uso IA para explicar el código
- [ ] Encuentro el error
- [ ] Corrijo el error
- [ ] Respondo las preguntas de reflexión

---

## 🆕 Si Te Atascas

1. **No clona el repositorio** → Verifica que Git esté instalado
2. **No abre los archivos** → Usa VS Code: Archivo → Abrir carpeta
3. **No entiendes el código** → Usa el PROMPT 2 de la guía PROMPTS.md
4. **No encuentras el error** → Usa el PROMPT 3 o 4
5. **La IA no entiende** → Sé más específico en tu pregunta
