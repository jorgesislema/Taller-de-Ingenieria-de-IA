# Contexto del Proyecto: Vibe Check IA

## ¿Qué es este proyecto?

Es un **analizador de sentimientos** que usa inteligencia artificial para 
clasificar tweets en español como **Positivos**, **Negativos**, **Neutrales** 
y otras emociones. Los resultados se muestran en un **dashboard interactivo** 
con 3 gráficos interactivos.

---

## ¿Para qué sirve?

- **Influencers**: Saber si su audiencia reacciona bien o mal
- **Empresas**: Medir satisfacción de clientes
- **Marcas**: Evaluar reputación online
- **Estudiantes**: Aprender a combinar IA con visualización de datos

---

## ¿Cómo funciona?

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  ARCHIVO    │     │    IA DE     │     │  GRÁFICOS   │
│  CSV        │ ──► │  GEMINI      │ ──► │INTERACTIVOS │
│ (tweets)    │     │ (análisis)   │     │(3 tipos)    │
└─────────────┘     └─────────────┘     └─────────────┘
```

1. **Lee** un archivo CSV con tweets en español
2. **Envía** cada tweet a la IA de Google Gemini
3. **Recibe** la clasificación: Positivo/Negativo/Neutral/Otra emoción
4. **Cuenta** cuántos hay de cada tipo
5. **Muestra** 3 gráficos interactivos

---

## Los 3 Gráficos

| Gráfico | Tipo | Qué muestra |
|---------|------|-------------|
| 🥧 Pastel | Pie Chart | Distribución porcentual de sentimientos |
| 📊 Barras | Bar Chart | Conteo exacto por cada emoción |
| 📈 Línea | Line Chart | Evolución temporal de sentimientos |

---

## ¿Qué aprende el estudiante?

### Habilidades Técnicas
- Conversar con IA de forma estructurada
- Organizar proyectos de software profesionalmente
- Crear dashboards interactivos con Streamlit
- Generar gráficos profesionales con Plotly
- Escribir tests automáticos con cobertura
- Manipular datos con Pandas

### Habilidades Blandas
- Pensamiento crítico
- Resolución de problemas
- Comunicación efectiva con IA
- Documentación técnica

---

## Datos de Ejemplo

El proyecto usa un archivo CSV ficticio con 15 tweets sobre el 
influencer "NeoMax". Los tweets tienen sentimientos variados:
- **Positivos**: "Eres el mejor", "Me encanta"
- **Negativos**: "No me gustó", "Decepcionado"
- **Neutrales**: "Buen contenido pero largo"
- **Otras emociones**: Sorprendido, Confundido, Asustado

---

## Tecnologías Usadas

| Tecnología | Para qué |
|------------|----------|
| Python | Lenguaje de programación |
| Google Gemini | API de IA para análisis de sentimientos |
| Streamlit | Dashboard web interactivo |
| Plotly | Gráficos interactivos (pastel, barras, línea) |
| Pandas | Manipulación y lectura de datos |
| Pytest | Tests automáticos |
| Mocks | Simular respuestas de IA sin gastar tokens |

---

## Requisitos

- Python 3.10 o superior
- API Key de Google Gemini (gratis)
- Conexión a internet
- VS Code o editor de código

---

## Documentación del Proyecto

- **context.md** → Este archivo (qué es y para qué sirve)
- **arquitectura.md** → Cómo está construido internamente
- **estado.md** → Versión actual y próximos pasos
- **README.md** → Instrucciones de instalación y uso
