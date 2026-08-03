# 🎓 Laboratorio 2: Vibe Check IA

## Analizador de Sentimientos para Tweets

---

## 🎯 ¿Qué vamos a hacer?

Crear un programa que:
- 📖 Lee tweets de un dataset en español
- 🤖 Usa IA (Google Gemini) para analizar sentimientos
- 📊 Muestra 3 gráficos interactivos:
  - 🥧 Pastel (distribución)
  - 📊 Barras (conteo)
  - 📈 Línea de tiempo (evolución)

---

## 🧠 Diferencia con el Laboratorio 1

| Antes (Lab 1) | Ahora (Lab 2) |
|---------------|---------------|
| Clonar repositorio | Crear desde cero |
| Copiar código | Diseñar con IA |
| Encontrar errores | Definir soluciones |
| Observador | Constructor |

---

## 📋 Los 4 Pasos

| # | Paso | Qué hacemos |
|---|------|-------------|
| 1 | Lógica | Definimos QUÉ hace el programa |
| 2 | Estructura | Definimos DÓNDE va cada cosa |
| 3 | Tests | Definimos CÓMO probamos la calidad |
| 4 | Código | Recién aquí escribimos el código |

---

## 📁 Estructura del Proyecto

```
vibe_check_ia/
├── app.py                    → Dashboard Streamlit
├── src/
│   ├── analizador.py         → Lógica con Gemini
│   ├── datos.py              → Lectura de CSV
│   └── graficos.py           → 3 gráficos Plotly
├── tests/                    → Tests automáticos
├── data/
│   └── tweets_espanol.csv    → 15 tweets de ejemplo
└── Documentación (.md)
```

---

## 🔑 Regla de Oro

> **"Primero pensamos, después programamos"**

No copiamos código sin entenderlo.

---

## 🛠️ Herramientas

| Herramienta | Para qué |
|-------------|----------|
| IA (Gemini/ChatGPT) | Compañero de diseño |
| VS Code | Editor de código |
| Python | Lenguaje de programación |
| Streamlit | Dashboard web |
| Plotly | Gráficos interactivos |
| Google Gemini | API de IA para análisis |

---

## 📊 Métricas de Éxito

- ✅ 90% cobertura de código
- ✅ 90% tests aprobados
- ✅ App funcionando
- ✅ 3 gráficos grandes y en vertical
- ✅ Entender cada línea de código

---

## 🚀 ¿Listos para crear?

**¡Empezamos con el Paso 1!**
