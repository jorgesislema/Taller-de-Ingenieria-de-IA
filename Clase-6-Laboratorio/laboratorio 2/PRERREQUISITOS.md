# ✅ Verificación de Prerrequisitos - Laboratorio 2

## Antes de empezar, verifica que tengas todo listo:

---

## 1. Software Necesario

### Python 3.10+
```bash
python --version
```
✅ Deberías ver: `Python 3.10.x` o superior

### Git
```bash
git --version
```
✅ Deberías ver: `git version 2.x.x`

### VS Code
- [ ] Está instalado
- [ ] Puedes abrirlo

---

## 2. Cuenta de Google AI Studio

### Obtener API Key:
1. Ve a [https://aistudio.google.com/](https://aistudio.google.com/)
2. Inicia sesión con tu cuenta de Google
3. Haz clic en "Get API Key"
4. Copia la API key

### Verificar que la tienes:
- [ ] Tengo una API key de Google Gemini
- [ ] La guardé en un lugar seguro

---

## 3. Carpeta del Proyecto

### Crear carpeta:
```bash
mkdir vibe_check_ia
cd vibe_check_ia
```

### Verificar estructura:
```
vibe_check_ia/
├── data/
│   └── comentarios_ficticios.csv
├── INSTRUCCIONES.md
├── PROMPTS.md
└── GUIA_RAPIDA.md
```

---

## 4. Entorno Virtual

### Crear:
```bash
python -m venv venv
```

### Activar (Windows):
```bash
venv\Scripts\activate
```

### Activar (Mac/Linux):
```bash
source venv/bin/activate
```

### Verificar:
```bash
which python
```
✅ Deberías ver la ruta al entorno virtual

---

## 5. Archivo .env

### Crear archivo `.env` en la raíz:
```
GEMINI_API_KEY=tu_api_key_aquí
```

### ⚠️ IMPORTANTE:
- [ ] El archivo se llama `.env` (con punto al inicio)
- [ ] No tiene extensión `.txt`
- [ ] Está en la carpeta raíz del proyecto
- [ ] NO lo subas a GitHub

---

## 6. Conexión a Internet

### Verificar:
```bash
ping google.com
```
✅ Deberías ver respuestas

---

## 7. Dependencias

### Crear `requirements.txt`:
```
streamlit>=1.28.0
plotly>=5.18.0
google-generativeai>=0.3.0
pandas>=2.1.0
python-dotenv>=1.0.0
pytest>=7.4.0
pytest-cov>=4.1.0
```

### Instalar:
```bash
pip install -r requirements.txt
```

---

## 📋 Checklist Final

- [ ] Python 3.10+ instalado
- [ ] Git instalado
- [ ] VS Code instalado
- [ ] API Key de Google Gemini
- [ ] Carpeta del proyecto creada
- [ ] Entorno virtual activado
- [ ] Archivo .env configurado
- [ ] Conexión a internet
- [ ] Dependencias instaladas

---

## 🆕 Si Algo No Funciona

| Problema | Solución |
|----------|----------|
| Python no se reconoce | Reinstalar marcando "Add to PATH" |
| Git no se reconoce | Reinstalar Git |
| API key no funciona | Verificar que esté en .env correctamente |
| pip no funciona | Usar `python -m pip install` |
| Entorno virtual no activa | Verificar ruta correcta |

---

**✅ ¿Todo listo? ¡Empezamos con el Paso 1!**
