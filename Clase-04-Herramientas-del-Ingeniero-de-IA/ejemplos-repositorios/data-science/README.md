# Ejemplo: Data Science (Ciencia de Datos)

## ¿Qué es Data Science?

Análisis estadístico, machine learning, visualización de datos, predicciones. El objetivo es extraer información valiosa de datos para tomar decisiones informadas.

## Estructura del Repositorio

```
mi_proyecto_data_science/
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
├── GLOSSARY.md                    # ESTÁNDAR: Términos estadísticos
│
├── METHODOLOGY.md                 # NUEVO: Metodología del análisis
├── DATA_DICTIONARY.md             # NUEVO: Diccionario de datos (qué significa cada columna)
│
├── data/
│   ├── raw/                       # Datos sin procesar (NUNCA modificar)
│   │   ├── ventas_2024.csv
│   │   ├── clientes.json
│   │   └── productos.xlsx
│   ├── processed/                 # Datos limpios y transformados
│   │   ├── ventas_limpias.csv
│   │   └── clientes_normalizados.csv
│   └── external/                  # Datos de fuentes externas
│       ├── datos_mercado.csv
│       └── indicadores-economicos.json
│
├── notebooks/
│   ├── 01_exploracion.ipynb       # Análisis exploratorio (EDA)
│   ├── 02_limpieza.ipynb          # Limpieza de datos
│   ├── 03_feature_engineering.ipynb # Creación de variables
│   ├── 04_modelado.ipynb          # Creación del modelo
│   ├── 05_evaluacion.ipynb        # Evaluación de resultados
│   └── 06_visualizacion.ipynb     # Gráficos y dashboards
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py             # Carga de datos
│   ├── preprocessor.py            # Limpieza y transformación
│   ├── feature_engineering.py     # Creación de variables
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── regresion.py           # Modelos de regresión
│   │   ├── clasificacion.py       # Modelos de clasificación
│   │   ├── clustering.py          # Agrupamiento
│   │   └── pipeline.py            # Pipeline completo
│   ├── evaluacion.py              # Métricas de evaluación
│   └── visualizaciones.py         # Gráficos
│
├── models/                        # Modelos entrenados (pesados)
│   ├── modelo_regresion_v1.pkl
│   ├── modelo_clasificacion_v1.pkl
│   └── scaler.pkl
│
├── reports/
│   ├── informe_resultados.pdf
│   ├── presentacion_ejecutiva.pptx
│   └── dashboard.html
│
├── tests/
│   ├── test_data_loader.py
│   ├── test_preprocessor.py
│   └── test_modelos.py
│
├── .gitignore
├── .env
├── requirements.txt
├── setup.py
└── README.md
```

## Archivos de Configuración para IA

### CODEX.md (Para Codex/OpenAI)
```markdown
Eres un científico de datos especializado en análisis exploratorio y modelado predictivo.

REGLAS:
1. USA Python puro con pandas, numpy, scikit-learn
2. DOCUMENTA cada paso con comentarios en español
3. SEPARA datos de entrenamiento (80%) y prueba (20%)
4. NUNCA uses datos de prueba para entrenar el modelo
5. SIEMPRE calcula métricas de evaluación
6. GUARDA los modelos entrenados en la carpeta models/
7. VISUALIZA los resultados con matplotlib o seaborn
```

### CLAUDE.md (Para Claude)
```markdown
## Metodología Científica
1. **Pregunta de Investigación:** Definir claramente qué queremos responder
2. **Recolección de Datos:** Obtener datos relevantes y confiables
3. **Limpieza:** Manejar valores faltantes, duplicados, outliers
4. **Análisis Exploratorio:** Entender patrones y relaciones
5. **Modelado:** Crear modelos predictivos o descriptivos
6. **Evaluación:** Validar con datos no vistos
7. **Comunicación:** Presentar resultados de forma clara

## Reglas de Código
- Usa type hints en todas las funciones
- Documenta con docstrings estilo NumPy
- Separa el código en módulos reutilizables
- Incluye pruebas unitarias para funciones críticas
- Usa virtual environments para dependencias

## Ética en Datos
- NUNCA uses datos personales sin consentimiento
- SIEMPRE anonimiza datos sensibles
- DOCUMENTA las fuentes de datos
- RESPETA la privacidad de los individuos
```

### METHODOLOGY.md (Nuevo: Metodología)
```markdown
# Metodología del Análisis

## Enfoque
Este proyecto sigue la metodología CRISP-DM (Cross-Industry Standard Process for Data Mining):

1. **Comprensión del Negocio**
   - Objetivo: Predecir ventas del próximo trimestre
   - Métrica de éxito: RMSE < 10% del promedio de ventas

2. **Comprensión de los Datos**
   - Fuente: Sistema de ventas interno
   - Período: Enero 2023 - Diciembre 2024
   - Variables: Fecha, producto, cantidad, precio, cliente, región

3. **Preparación de los Datos**
   - Manejo de valores faltantes: Imputación con mediana
   - Codificación: One-hot encoding para variables categóricas
   - Escalado: StandardScaler para variables numéricas

4. **Modelado**
   - Modelos candidatos: Regresión Lineal, Random Forest, XGBoost
   - Validación: 5-fold cross-validation
   - Optimización: Grid Search con hiperparámetros

5. **Evaluación**
   - Métricas: RMSE, MAE, R²
   - Validación temporal: Entrenar con 2023-2024, predecir 2025

6. **Despliegue**
   - Formato: API REST con FastAPI
   - Frecuencia de actualización: Mensual
   - Monitoreo: Alertas si RMSE > 15%
```

### DATA_DICTIONARY.md (Nuevo: Diccionario de Datos)
```markdown
# Diccionario de Datos

## Tabla: ventas
| Columna | Tipo | Descripción | Ejemplo |
|---------|------|-------------|---------|
| fecha | datetime | Fecha de la venta | 2024-01-15 |
| id_producto | string | Código único del producto | PROD-001 |
| nombre_producto | string | Nombre del producto | Laptop HP |
| cantidad | int | Unidades vendidas | 5 |
| precio_unitario | float | Precio por unidad | 899.99 |
| total_venta | float | cantidad * precio_unitario | 4499.95 |
| id_cliente | string | Código único del cliente | CLI-123 |
| región | string | Zona geográfica | Norte |
| canal_venta | string | Canal de venta | Online |

## Tabla: clientes
| Columna | Tipo | Descripción | Ejemplo |
|---------|------|-------------|---------|
| id_cliente | string | Código único del cliente | CLI-123 |
| nombre | string | Nombre del cliente | Juan Pérez |
| email | string | Correo electrónico | juan@email.com |
| fecha_registro | datetime | Fecha de registro | 2023-05-20 |
| tipo_cliente | string | Regular, VIP, Corporativo | VIP |
| región | string | Zona geográfica | Norte |

## Variable Objetivo
- **total_venta**: Monto total de la venta (variable a predecir)

## Variables Predictoras
- **cantidad**: Unidades vendidas (numérica)
- **precio_unitario**: Precio por unidad (numérica)
- **región**: Zona geográfica (categórica)
- **canal_venta**: Canal de venta (categórica)
- **tipo_cliente**: Tipo de cliente (categórica)
```

## Ejemplo de Uso

```
Científico de Datos →
1. Carga datos con data_loader.py
2. Limpia con preprocessor.py
3. Crea variables con feature_engineering.py
4. Entrena modelos con modelos/pipeline.py
5. Evalúa con evaluacion.py
6. Visualiza con visualizaciones.py
7. Genera reporte en reports/
```

## Nota para el Instructor

Data Science es el campo donde más se usa la IA actualmente. Es importante enseñar:

1. **Metodología:** No es solo "correr un modelo", es un proceso científico
2. **Datos sucios:** El 80% del tiempo es limpiar datos
3. **Overfitting:** El modelo puede memorizar en lugar de aprender
4. **Ética:** Los datos personales deben protegerse
5. **Comunicación:** Los resultados sin interpretación no sirven