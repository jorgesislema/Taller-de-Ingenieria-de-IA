# CLAUDE.md - Configuración para Claude

## Objetivo del Análisis
Proporcionar insights accionables para la toma de decisiones de negocio.

## KPIs Principales
1. **Ventas Totales:** Suma de todas las ventas por período
2. **Ticket Promedio:** Ventas totales / Número de transacciones
3. **Tasa de Conversión:** Clientes que compran / Visitantes totales
4. **Churn Rate:** Clientes que se van / Total de clientes
5. **ROI:** (Ganancia - Inversión) / Inversión

## Fuentes de Datos
- **ventas_raw.csv:** Exportación del sistema de ventas
- **marketing_raw.csv:** Datos de campañas de marketing
- **inventario_raw.xlsx:** Estado actual del inventario

## Reglas de Análisis
1. NUNCA uses datos sin verificar su integridad
2. SIEMPRE incluye una descripción de la metodología
3. DOCUMENTA las suposiciones del análisis
4. PRESENTA los resultados de forma visual (gráficos)
5. INCLUYE recomendaciones accionables

## Reglas Técnicas
- Python 3.8+ con pandas, matplotlib, seaborn
- Usa type hints en todas las funciones
- Documenta con docstrings descriptivos
- Genera reportes en Excel y HTML
- Usa consultas SQL optimizadas

## Lo que NO debes hacer
- NO modifiques los datos originales
- NO publiques datos personales sin anonimizar
- NO hagas análisis sin verificar la calidad
- NO presentes gráficos sin etiquetas
- NO saques conclusiones sin evidencia