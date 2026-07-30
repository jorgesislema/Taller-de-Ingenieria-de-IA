# METHODOLOGY.md - Metodología del Análisis

## Enfoque: CRISP-DM

Este proyecto sigue la metodología CRISP-DM (Cross-Industry Standard Process for Data Mining).

### Fase 1: Comprensión del Negocio
- **Objetivo:** Predecir ventas del próximo trimestre
- **Métrica de éxito:** RMSE < 10% del promedio de ventas
- **Contexto:** Empresa de retail con 5 años de datos históricos
- **Preguntas clave:** ¿Qué factores influyen más en las ventas?

### Fase 2: Comprensión de los Datos
- **Fuente:** Sistema de ventas interno
- **Período:** Enero 2023 - Diciembre 2024
- **Variables:**
  - Fecha de venta
  - ID del producto
  - Cantidad vendida
  - Precio unitario
  - ID del cliente
  - Región geográfica
  - Canal de venta (online/físico)

### Fase 3: Preparación de los Datos
1. **Limpieza:**
   - Manejo de valores faltantes (imputación con mediana)
   - Eliminación de duplicados
   - Detección y tratamiento de outliers
2. **Transformación:**
   - Codificación de variables categóricas (one-hot encoding)
   - Escalado de variables numéricas (StandardScaler)
   - Creación de nuevas variables (día de la semana, mes, trimestre)
3. **Validación:**
   - Verificación de integridad de datos
   - Pruebas de consistencia

### Fase 4: Modelado
- **Modelos candidatos:**
  - Regresión Lineal (baseline)
  - Random Forest
  - XGBoost
  - LightGBM
- **Validación:** 5-fold cross-validation
- **Optimización:** Grid Search con hiperparámetros

### Fase 5: Evaluación
- **Métricas principales:**
  - RMSE (Root Mean Squared Error)
  - MAE (Mean Absolute Error)
  - R² (Coefficient of Determination)
- **Validación temporal:** Entrenar con 2023-2024, predecir 2025
- **Comparación:** Benchmarking con modelo baseline

### Fase 6: Despliegue
- **Formato:** API REST con FastAPI
- **Frecuencia de actualización:** Mensual
- **Monitoreo:** Alertas si RMSE > 15%
- **Documentación:** Guía de uso y mantenimiento