# 🏠 Laboratorio 2: Vibe Check IA

## 📂 Estructura del Material

```
laboratorio 2/
│
├── 📄 INSTRUCCIONES.md      ← Guía principal para el alumno
│   Los 4 pasos para crear el proyecto con IA
│
├── 📄 PROMPTS.md            ← Prompts listos para usar
│   Prompts para cada momento de la clase
│
├── 📄 GUIA_RAPIDA.md        ← Referencia de comandos
│   Comandos, estructura y errores comunes
│
├── 📄 EVALUACION.md         ← Autoevaluación
│   Preguntas y calificación (20 puntos)
│
├── 📄 NOTAS_PROFESOR.md     ← Guía del profesor
│   Cronograma, puntos clave, extensiones
│
├── 📄 PRESENTACION.md       ← Diapositivas
│   Material para proyectar al inicio
│
├── 📄 RESUMEN.md            ← Resumen ejecutivo
│   Vista rápida de todo
│
├── 📄 PRERREQUISITOS.md     ← Verificación antes de empezar
│   Checklist de software necesario
│
├── 📄 EJEMPLO_CONVERSACION.md ← Ejemplos de conversación
│   Cómo hablar efectivamente con IA
│
├── 📄 README.md             ← Documentación del proyecto
│   Instrucciones de instalación y uso
│
├── 📄 context.md            ← Qué es el proyecto
│   Documentación para el alumno
│
├── 📄 arquitectura.md       ← Cómo está construido
│   Diagramas Mermaid incluidos
│
├── 📄 estado.md             ← Estado del proyecto
│   Versión, pendientes, métricas
│
└── 📄 data/
    └── tweets_espanol.csv   ← 15 tweets de ejemplo
        Sentimientos: positivo, negativo, neutral,
        sorprendido, confundido, asustado
```

---

## 🎯 Flujo de Uso

### Para el Profesor:
1. **Antes:** Leer `NOTAS_PROFESOR.md`
2. **Inicio:** Proyectar `PRESENTACION.md`
3. **Durante:** Guiar con `INSTRUCCIONES.md`
4. **Dudas:** Dirigir a `PROMPTS.md`
5. **Final:** Entregar `EVALUACION.md`

### Para el Alumno:
1. **Inicio:** Abrir `INSTRUCCIONES.md`
2. **Paso 1:** Copiar Prompt 1 en la IA
3. **Leer** la respuesta de la IA
4. **Preguntar** si no entiende
5. **Repetir** para cada paso
6. **Final:** Completar `EVALUACION.md`

---

## 🔑 Los 4 Pasos Clave

| Paso | Prompt | Qué se logra |
|------|--------|--------------|
| 1 | "Define la lógica" | Entender QUÉ hace el programa |
| 2 | "Organiza el proyecto" | Saber DÓNDE va cada cosa |
| 3 | "Define los tests" | Establecer CÓMO medimos calidad |
| 4 | "Escribe el código" | Crear el programa ENTENDIÉNDOLO |

---

## 📁 Estructura del Proyecto que Crearán

```
vibe_check_ia/
├── app.py                    → Dashboard Streamlit
├── src/
│   ├── __init__.py
│   ├── analizador.py         → Lógica con Gemini
│   ├── datos.py              → Lectura de CSV
│   └── graficos.py           → 3 gráficos Plotly
├── tests/
│   ├── __init__.py
│   ├── test_analizador.py
│   ├── test_datos.py
│   └── test_graficos.py
├── data/
│   └── tweets_espanol.csv
├── requirements.txt
├── .env
├── .gitignore
├── README.md
├── context.md
├── arquitectura.md
└── estado.md
```

---

## 📊 Los 3 Gráficos

| Gráfico | Tipo | Qué muestra |
|---------|------|-------------|
| 🥧 Pastel | Pie Chart | Distribución porcentual |
| 📊 Barras | Bar Chart | Conteo exacto por emoción |
| 📈 Línea | Line Chart | Evolución temporal |

**Importante:** Deben ser GRANDES (height=600, width=800) y en VERTICAL

---

## 📊 Comparación con Laboratorio 1

| Aspecto | Laboratorio 1 | Laboratorio 2 |
|---------|---------------|---------------|
| Enfoque | Reconocer | Crear |
| Rol del alumno | Observador | Diseñador |
| IA como... | Buscador | Compañero |
| Código | Existe | Se crea |
| Error | Se encuentra | Se previene |
| Estructura | Simple | Profesional |

---

## 💡 Diferencia Clave

> **Laboratorio 1:** "¿Qué hace este código?"
> **Laboratorio 2:** "¿Qué quiero que haga mi código?"

---

## 🚀 Listo para Empezar

1. Abrir `INSTRUCCIONES.md`
2. Seguir el Paso 1
3. Conversar con la IA
4. ¡Crear tu app!

---

## 📦 Repositorio de Referencia

El resultado final debe ser similar a:
https://github.com/jorgesislema/programa_analisis_sentimientos_influenser
