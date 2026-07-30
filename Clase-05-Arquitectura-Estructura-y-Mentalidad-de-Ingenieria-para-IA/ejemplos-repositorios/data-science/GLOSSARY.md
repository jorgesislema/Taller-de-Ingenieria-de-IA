# GLOSSARY.md - Glosario de Data Science

## Términos Estadísticos

| Término | Definición | Ejemplo |
|---------|------------|---------|
| **Media** | Promedio de todos los valores | Media de edad: 35 años |
| **Mediana** | Valor central de los datos | Mediana de ingresos: $50,000 |
| **Moda** | Valor que más se repite | Moda de compra: $25 |
| **Desviación Estándar** | Qué tan dispersos están los datos | DS de precios: $10 |
| **Correlación** | Relación entre dos variables | Correlación entre precio y ventas |
| **Sesgo** | Distorsión en los datos | Sesgo de selección en encuestas |

## Términos de Machine Learning

| Término | Definición | Ejemplo |
|---------|------------|---------|
| **Supervisado** | Aprende con datos etiquetados | Predecir precios de casas |
| **No supervisado** | Encuentra patrones sin etiquetas | Agrupar clientes por comportamiento |
| **Entrenamiento** | Aprende de los datos | Entrenar modelo con datos históricos |
| **Prueba** | Evalúa el modelo | Probar con datos no vistos |
| **Overfitting** | Memoriza en lugar de aprender | Modelo perfecto en entrenamiento, malo en prueba |
| **Underfitting** | No aprende lo suficiente | Modelo demasiado simple |
| **Feature** | Variable predictora | Precio, cantidad, región |
| **Label** | Variable objetivo | Total de ventas |
| **Pipeline** | Serie de pasos de procesamiento | Limpieza → Transformación → Modelo |

## Métricas de Evaluación

### Regresión
| Métrica | Qué mide | Cuándo usarla |
|---------|----------|---------------|
| **RMSE** | Error promedio al cuadrado | Cuando errores grandes son peores |
| **MAE** | Error promedio absoluto | Cuando todos los errores pesan igual |
| **R²** | Porcentaje de varianza explicada | Para entender qué tan bien explica el modelo |

### Clasificación
| Métrica | Qué mide | Cuándo usarla |
|---------|----------|---------------|
| **Accuracy** | Porcentaje de aciertos | Cuando las clases están balanceadas |
| **Precision** | De los positivos, cuántos son correctos | Cuando los falsos positivos son costosos |
| **Recall** | De los reales, cuántos detectó | Cuando los falsos negativos son costosos |
| **F1-Score** | Balance entre precision y recall | Cuando necesitas equilibrio |

## Herramientas

| Herramienta | Para qué sirve |
|-------------|----------------|
| **pandas** | Manipulación y análisis de datos |
| **numpy** | Cálculos numéricos |
| **scikit-learn** | Machine learning |
| **matplotlib** | Visualización básica |
| **seaborn** | Visualización estadística |
| **jupyter** | Notebooks interactivos |
| **xgboost** | Modelos boosteados |
| **tensorflow** | Deep learning |
| **pytorch** | Deep learning |

## Términos del Negocio

| Término | Definición | Equivalente |
|---------|------------|-------------|
| **KPI** | Indicador Clave de Rendimiento | Métrica importante |
| **ROI** | Retorno de Inversión | Ganancia / Inversión |
| **Cohorte** | Grupo de usuarios con características comunes | Usuarios que llegaron en enero |
| **Churn** | Tasa de cancelación | Porcentaje de usuarios que se van |
| **LTV** | Valor de vida del cliente | Cuánto dinero genera un cliente |
| **CAC** | Costo de adquisición de cliente | Cuánto cuesta conseguir un cliente |