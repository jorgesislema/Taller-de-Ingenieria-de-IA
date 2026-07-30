# Ejemplos de Repositorios por Tipo de Proyecto

> Cómo se ve la estructura de carpetas y los archivos `.md` de configuración para IA según el tipo de proyecto que estés construyendo.

---

## Tabla de Equivalencias: Nombres de Archivos `.md` por Plataforma

**IMPORTANTE:** Cada plataforma de IA tiene su propio nombre "secreto" para el archivo de configuración. Si usas el estándar (RULES.md, CONTEXT.md), funciona en todas. Pero si quieres que la IA lea automáticamente sin que se lo pidas, usa el nombre correcto para cada plataforma.

| Concepto Genérico | Codex (OpenAI) | GitHub Copilot | Claude | Gemini | GLM (ChatGLM) | DeepSeek | Qwen | Z.ai (Zhipu) | Grok (xAI) | OpenCode |
|-------------------|----------------|----------------|--------|--------|---------------|----------|------|--------------|------------|----------|
| **Reglas y Comportamiento** | `CODEX.md` | `.github/copilot-instructions.md` | `CLAUDE.md` | `.gemini/instructions.md` | `GLM.md` | `RULES.md` | `RULES.md` | `ZAI.md` | `GROK.md` | `RULES.md` |
| **Contexto y Arquitectura** | Dentro de `CODEX.md` | Al final de instrucciones | Dentro de `CLAUDE.md` | En `.gemini/instructions.md` | Dentro de `GLM.md` | `CONTEXT.md` | `CONTEXT.md` | Dentro de `ZAI.md` | Dentro de `GROK.md` | `CONTEXT.md` |
| **Seguridad** | Dentro de `CODEX.md` | En instrucciones | Dentro de `CLAUDE.md` | En instrucciones | Dentro de `GLM.md` | `SECURITY.md` | `SECURITY.md` | Dentro de `ZAI.md` | Dentro de `GROK.md` | `SECURITY.md` |
| **Glosario** | Dentro de `CODEX.md` | En instrucciones | Dentro de `CLAUDE.md` | En instrucciones | Dentro de `GLM.md` | `GLOSSARY.md` | `GLOSSARY.md` | Dentro de `ZAI.md` | Dentro de `GROK.md` | `GLOSSARY.md` |

### Explicación Rápida

**¿Por qué hay tantos nombres diferentes?**

Cada empresa que creó una IA quiso que su herramienta fuera "la mejor". Para mejorar la experiencia del usuario, programaron sus herramientas para que, al abrir un proyecto, buscaran automáticamente un archivo con **su nombre especial** en la carpeta raíz.

**Analogía:** Es como si cada empleado llegara y buscara su nombre en la puerta de la oficina. Si no encuentra su nombre, no sabe dónde sentarse.

**La solución inteligente:** Si tú creas tus archivos con los nombres estándar (`RULES.md`, `CONTEXT.md`, `SECURITY.md`), **funcionan en todas las plataformas**. Luego, si usas una plataforma específica, solo haces un "copiar y pegar" al nombre correcto.

---

## Ejemplos por Tipo de Proyecto

### 1. Chat de IA (Chatbot)

**¿Qué es?** Un programa que conversa con usuarios, respondiendo preguntas o dando recomendaciones.

**Archivos de configuración para cada plataforma:**

```
mi_chatbot_ia/
│
├── .github/
│   └── copilot-instructions.md    # GitHub Copilot lee esto automáticamente
│
├── .gemini/
│   └── instructions.md            # Gemini lee esto automáticamente
│
├── CODEX.md                       # Codex (OpenAI) lee esto automáticamente
├── CLAUDE.md                      # Claude lee esto automáticamente
├── GLM.md                         # ChatGLM lee esto automáticamente
├── ZAI.md                         # Z.ai (Zhipu) lee esto automáticamente
├── GROK.md                        # Grok (xAI) lee esto automáticamente
│
├── CONTEXT.md                     # ESTÁNDAR: Lo leen todas las plataformas
├── RULES.md                       # ESTÁNDAR: Lo leen todas las plataformas
├── SECURITY.md                    # ESTÁNDAR: Lo leen todas las plataformas
├── GLOSSARY.md                    # ESTÁNDAR: Lo leen todas las plataformas
│
├── data/
│   └── respuestas_ejemplo.json
│
├── src/
│   ├── chatbot.py
│   └── procesador_mensajes.py
│
├── tests/
│   └── test_chatbot.py
│
└── README.md
```

**Ver ejemplo completo:** [chat-ia/](chat-ia/)

---

### 2. Agentes de IA

**¿Qué es?** Un programa que no solo conversa, sino que **ejecuta acciones**: busca en internet, genera archivos, conecta con otras herramientas.

**Archivos de configuración para cada plataforma:**

```
mi_agente_ia/
│
├── .github/
│   └── copilot-instructions.md    # GitHub Copilot
│
├── .gemini/
│   └── instructions.md            # Gemini
│
├── CODEX.md                       # Codex
├── CLAUDE.md                      # Claude
├── GLM.md                         # ChatGLM
├── ZAI.md                         # Z.ai
├── GROK.md                        # Grok
│
├── CONTEXT.md                     # ESTÁNDAR
├── RULES.md                       # ESTÁNDAR
├── SECURITY.md                    # ESTÁNDAR
├── GLOSSARY.md                    # ESTÁNDAR
│
├── TOOLS.md                       # NUEVO: Lista de herramientas que puede usar el agente
├── MEMORY.md                      # NUEVO: Cómo el agente recuerda conversaciones
│
├── data/
│   └── historial_conversaciones.json
│
├── src/
│   ├── agente_principal.py
│   ├── herramientas/
│   │   ├── buscador_web.py
│   │   ├── generador_archivos.py
│   │   └── conexion_api.py
│   └── memoria.py
│
├── audits/
│   └── auditoria_agente.md
│
├── tests/
│   └── test_agente.py
│
└── README.md
```

**Ver ejemplo completo:** [agentes-ia/](agentes-ia/)

---

### 3. Páginas Web con IA

**¿Qué es?** Una página web que integra inteligencia artificial: chatbots en el sitio, recomendaciones, generación de contenido.

**Archivos de configuración para cada plataforma:**

```
mi_pagina_web_ia/
│
├── .github/
│   └── copilot-instructions.md    # GitHub Copilot
│
├── .gemini/
│   └── instructions.md            # Gemini
│
├── CODEX.md                       # Codex
├── CLAUDE.md                      # Claude
├── GLM.md                         # ChatGLM
├── ZAI.md                         # Z.ai
├── GROK.md                        # Grok
│
├── CONTEXT.md                     # ESTÁNDAR
├── RULES.md                       # ESTÁNDAR
├── SECURITY.md                    # ESTÁNDAR
│
├── DESIGN.md                      # NUEVO: Guía de diseño visual (colores, fuentes, estilos)
│
├── public/
│   ├── index.html
│   ├── css/
│   │   └── estilos.css
│   └── js/
│       └── chat_widget.js
│
├── src/
│   ├── servidor.py
│   ├── api_chat.py
│   └── modelos/
│       └── recomendador.py
│
├── data/
│   └── productos.json
│
├── tests/
│   └── test_api.py
│
└── README.md
```

**Ver ejemplo completo:** [paginas-web-ia/](paginas-web-ia/)

---

### 4. Data Science (Ciencia de Datos)

**¿Qué es?** Análisis estadístico, machine learning, visualización de datos, predicciones.

**Archivos de configuración para cada plataforma:**

```
mi_proyecto_data_science/
│
├── .github/
│   └── copilot-instructions.md    # GitHub Copilot
│
├── .gemini/
│   └── instructions.md            # Gemini
│
├── CODEX.md                       # Codex
├── CLAUDE.md                      # Claude
├── GLM.md                         # ChatGLM
├── ZAI.md                         # Z.ai
├── GROK.md                        # Grok
│
├── CONTEXT.md                     # ESTÁNDAR
├── RULES.md                       # ESTÁNDAR
├── SECURITY.md                    # ESTÁNDAR
├── GLOSSARY.md                    # ESTÁNDAR: Términos estadísticos
│
├── METHODOLOGY.md                 # NUEVO: Metodología del análisis
├── DATA_DICTIONARY.md             # NUEVO: Diccionario de datos (qué significa cada columna)
│
├── data/
│   ├── raw/                       # Datos sin procesar (NUNCA modificar)
│   ├── processed/                 # Datos limpios
│   └── external/                  # Datos de fuentes externas
│
├── notebooks/
│   ├── 01_exploracion.ipynb       # Análisis exploratorio
│   ├── 02_limpieza.ipynb          # Limpieza de datos
│   ├── 03_modelado.ipynb          # Creación del modelo
│   └── 04_evaluacion.ipynb        # Evaluación de resultados
│
├── src/
│   ├── data_loader.py
│   ├── feature_engineering.py
│   ├── modelos/
│   │   ├── regresion.py
│   │   └── clasificacion.py
│   └── visualizaciones.py
│
├── models/                       # Modelos entrenados (pesados, no subir a GitHub)
│   └── modelo_v1.pkl
│
├── reports/
│   └── informe_resultados.pdf
│
├── tests/
│   └── test_modelos.py
│
└── README.md
```

**Ver ejemplo completo:** [data-science/](data-science/)

---

### 5. Análisis de Datos

**¿Qué es?** Extraer información de bases de datos, generar reportes, dashboards, KPIs.

**Archivos de configuración para cada plataforma:**

```
mi_analisis_datos/
│
├── .github/
│   └── copilot-instructions.md    # GitHub Copilot
│
├── .gemini/
│   └── instructions.md            # Gemini
│
├── CODEX.md                       # Codex
├── CLAUDE.md                      # Claude
├── GLM.md                         # ChatGLM
├── ZAI.md                         # Z.ai
├── GROK.md                        # Grok
│
├── CONTEXT.md                     # ESTÁNDAR
├── RULES.md                       # ESTÁNDAR
├── SECURITY.md                    # ESTÁNDAR
│
├── BUSINESS_CONTEXT.md            # NUEVO: Contexto del negocio (qué miden los KPIs)
├── DATA_SOURCES.md                # NUEVO: De dónde vienen los datos
│
├── data/
│   ├── input/                     # Datos de entrada
│   ├── output/                    # Reportes generados
│   └── queries/                   # Consultas SQL guardadas
│
├── src/
│   ├── extraccion_datos.py
│   ├── transformacion.py
│   ├── carga_reportes.py
│   └── dashboards/
│       ├── ventas.py
│       └── marketing.py
│
├── reports/
│   ├── reporte_ventas_2024.xlsx
│   └── dashboardmarketing.html
│
├── tests/
│   └── test_transformaciones.py
│
└── README.md
```

**Ver ejemplo completo:** [analisis-datos/](analisis-datos/)

---

### 6. Bases de Datos

**¿Qué es?** Sistemas para almacenar, organizar y consultar información de forma estructurada.

**Archivos de configuración para cada plataforma:**

```
mi_base_datos_ia/
│
├── .github/
│   └── copilot-instructions.md    # GitHub Copilot
│
├── .gemini/
│   └── instructions.md            # Gemini
│
├── CODEX.md                       # Codex
├── CLAUDE.md                      # Claude
├── GLM.md                         # ChatGLM
├── ZAI.md                         # Z.ai
├── GROK.md                        # Grok
│
├── CONTEXT.md                     # ESTÁNDAR
├── RULES.md                       # ESTÁNDAR
├── SECURITY.md                    # ESTÁNDAR: CRÍTICO para bases de datos
│
├── SCHEMA.md                      # NUEVO: Diagrama de la estructura de tablas
├── MIGRATIONS.md                  # NUEVO: Historial de cambios en la estructura
│
├── data/
│   ├── schema/
│   │   ├── crear_tablas.sql
│   │   └── datos_iniciales.sql
│   └── backups/
│       └── backup_2024_01_15.sql
│
├── src/
│   ├── conexion.py
│   ├── modelos/
│   │   ├── usuario.py
│   │   ├── producto.py
│   │   └── transaccion.py
│   ├── consultas/
│   │   ├── busqueda.py
│   │   └── reportes.py
│   └── utilidades/
│       ├── validacion.py
│       └── encriptacion.py
│
├── migrations/                    # Cambios en la estructura de la BD
│   ├── 001_crear_tabla_usuarios.py
│   └── 002_agregar_columna_email.py
│
├── tests/
│   ├── test_consultas.py
│   └── test_modelos.py
│
└── README.md
```

**Ver ejemplo completo:** [bases-datos/](bases-datos/)

---

### 7. Programas Python

**¿Qué es?** Scripts y herramientas en Python: automatizaciones, procesamiento de archivos, utilidades.

**Archivos de configuración para cada plataforma:**

```
mi_programa_python/
│
├── .github/
│   └── copilot-instructions.md    # GitHub Copilot
│
├── .gemini/
│   └── instructions.md            # Gemini
│
├── CODEX.md                       # Codex
├── CLAUDE.md                      # Claude
├── GLM.md                         # ChatGLM
├── ZAI.md                         # Z.ai
├── GROK.md                        # Grok
│
├── CONTEXT.md                     # ESTÁNDAR
├── RULES.md                       # ESTÁNDAR
├── SECURITY.md                    # ESTÁNDAR
│
├── .env                           # Variables de entorno (NUNCA subir a GitHub)
├── .gitignore                     # Lista de archivos ignorados
├── requirements.txt               # Lista de dependencias
│
├── src/
│   ├── __init__.py
│   ├── main.py                    # Punto de entrada del programa
│   ├── modulos/
│   │   ├── __init__.py
│   │   ├── procesador.py
│   │   └── utilidades.py
│   └── configuracion.py
│
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_procesador.py
│
├── docs/
│   ├── guia_instalacion.md
│   └── ejemplos_uso.md
│
├── scripts/                       # Scripts de automatización
│   ├── ejecutar_analisis.sh
│   └── generar_reporte.py
│
└── README.md
```

**Ver ejemplo completo:** [programas-python/](programas-python/)

---

## ¿Cómo elegir qué archivos `.md` crear?

### Regla del 80/20

**El 20% de los archivos cubre el 80% de los casos de uso:**

1. **CONTEXT.md** → ¿Quiénes somos? (Siempre necesario)
2. **RULES.md** → ¿Cómo debe comportarse la IA? (Siempre necesario)
3. **SECURITY.md** → ¿Qué NO debe hacer? (Siempre necesario)

**El otro 80% depende de tu proyecto:**

- ¿Manejas datos sensibles? → Agrega `SECURITY.md` detallado
- ¿Tienes términos raros? → Agrega `GLOSSARY.md`
- ¿Es un equipo grande? → Agrega `ARCHITECTURE.md` y `DECISIONES.md`
- ¿Usas múltiples IAs? → Agrega `RULES_CODER.md` y `RULES_AUDITOR.md`

### Flujo de Decisión

```
¿Tu proyecto es simple (un chatbot básico)?
  → Solo crea: CONTEXT.md, RULES.md, SECURITY.md

¿Tu proyecto maneja datos sensibles (médicos, financieros)?
  → Agrega: SECURITY.md detallado, AUDIT_LOG.md

¿Tu proyecto tiene múltiples desarrolladores?
  → Agrega: ARCHITECTURE.md, DECISIONES.md, CONTRIBUTING.md

¿Usas IA para generar Y auditar código?
  → Agrega: RULES_CODER.md, RULES_AUDITOR.md, carpeta audits/
```

---

## Nota para el Instructor

Estos ejemplos son **plantillas de partida**. Cada proyecto real será diferente. Lo importante es que los alumnos entiendan:

1. **La estructura base** siempre es la misma (data/, src/, docs/, tests/)
2. **Los archivos .md estándar** funcionan en todas las plataformas
3. **Los archivos específicos** de cada plataforma son solo "atajos" para que la IA lea automáticamente
4. **Lo más importante** es el CONTENIDO de los archivos, no el nombre

**Consejo:** Pide a los alumnos que elijan UN tipo de proyecto que les interese y creen su propia estructura basándose en el ejemplo. Luego, comparen con sus compañeros para ver las diferencias.