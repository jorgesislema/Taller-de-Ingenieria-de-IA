# Ejemplo: Análisis de Datos

## ¿Qué es Análisis de Datos?

Extraer información de bases de datos, generar reportes, dashboards, KPIs. Se enfoca en entender "qué pasó" y "por qué pasó", no en predecir el futuro.

## Estructura del Repositorio

```
mi_analisis_datos/
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
│
├── BUSINESS_CONTEXT.md            # NUEVO: Contexto del negocio (qué miden los KPIs)
├── DATA_SOURCES.md                # NUEVO: De dónde vienen los datos
│
├── data/
│   ├── input/                     # Datos de entrada
│   │   ├── ventas_raw.csv
│   │   ├── marketing_raw.csv
│   │   └── inventario_raw.xlsx
│   ├── output/                    # Reportes generados
│   │   ├── reporte_ventas_2024.xlsx
│   │   ├── dashboard_marketing.html
│   │   └── kpis_trimestrales.pdf
│   └── queries/                   # Consultas SQL guardadas
│       ├── ventas_por_region.sql
│   │   ├── productos_top.sql
│   │   └── clientes_frecuentes.sql
│
├── src/
│   ├── __init__.py
│   ├── extraccion_datos.py        # Conecta con bases de datos
│   ├── transformacion.py          # Limpia y transforma datos
│   ├── carga_reportes.py          # Genera reportes automáticos
│   ├── dashboards/
│   │   ├── __init__.py
│   │   ├── ventas.py              # Dashboard de ventas
│   │   ├── marketing.py           # Dashboard de marketing
│   │   └── inventario.py          # Dashboard de inventario
│   └── utilidades/
│       ├── __init__.py
│       ├── conexion_bd.py         # Conexión a bases de datos
│       └── formateador.py         # Formatea números y fechas
│
├── reports/
│   ├── plantillas/
│   │   ├── reporte_ventas.xlsx
│   │   └── presentacion_ejecutiva.pptx
│   ├── generados/
│   │   ├── reporte_enero_2024.xlsx
│   │   └── reporte_febrero_2024.xlsx
│   └── dashboards/
│       ├── ventas_interactivo.html
│       └── kpis_en_tiempo_real.html
│
├── tests/
│   ├── test_extraccion.py
│   ├── test_transformacion.py
│   └── test_reportes.py
│
├── .gitignore
├── .env
├── requirements.txt
└── README.md
```

## Archivos de Configuración para IA

### CODEX.md (Para Codex/OpenAI)
```markdown
Eres un analista de datos especializado en reportes y dashboards.

REGLAS:
1. USA pandas para manipulación de datos
2. USA matplotlib/seaborn para visualizaciones
3. GENERA reportes en Excel y HTML
4. CALCULA KPIs automáticos
5. NUNCA modifiques los datos originales en data/input/
6. SIEMPRE guarda los resultados en data/output/
7. USA consultas SQL optimizadas
```

### CLAUDE.md (Para Claude)
```markdown
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
```

### BUSINESS_CONTEXT.md (Nuevo: Contexto del Negocio)
```markdown
# Contexto del Negocio

## Empresa
**TechStore** - Tienda de tecnología con 5 años en el mercado

## Objetivos Estratégicos
1. Aumentar ventas un 20% este año
2. Reducir churn de clientes al 5% mensual
3. Mejorar el ticket promedio en $50

## Preguntas Clave del Negocio
- ¿Qué productos se venden más en cada región?
- ¿Qué canales de venta generan más ingresos?
- ¿Cuáles son los mejores meses para promociones?
- ¿Qué clientes son los más valiosos?

## Decisiones que Tomamos con Estos Datos
1. **Inventario:** Cuánto stock comprar de cada producto
2. **Marketing:** Dónde invertir en publicidad
3. **Precios:** Cuándo hacer descuentos
4. **Personal:** Cuántos empleados necesitamos por sucursal
```

### DATA_SOURCES.md (Nuevo: Fuentes de Datos)
```markdown
# Fuentes de Datos

## Base de Datos Principal
- **Tipo:** PostgreSQL
- **Conexión:** Variables de entorno (DB_HOST, DB_USER, DB_PASSWORD)
- **Frecuencia de actualización:** Diaria

## Archivos de Exportación
| Archivo | Fuente | Frecuencia | Última Actualización |
|---------|--------|------------|---------------------|
| ventas_raw.csv | Sistema de ventas | Diaria | 2024-01-15 |
| marketing_raw.csv | Google Ads + Meta | Semanal | 2024-01-10 |
| inventario_raw.xlsx | Sistema de inventario | Semanal | 2024-01-12 |

## API Externas
- **Google Analytics:** Tráfico web
- **Stripe:** Pagos procesados
- **Mailchimp:** Email marketing

## Calidad de Datos
- **ventas_raw.csv:** 99.5% completo, 0.1% duplicados
- **marketing_raw.csv:** 95% completo (faltan algunos IDs de campaña)
- **inventario_raw.xlsx:** 100% completo
```

## Ejemplo de Uso

```
Analista de Datos →
1. Extracción: extraccion_datos.py conecta con la BD
2. Transformación: transformacion.py limpia y formatea
3. Análisis: Consultas SQL en data/queries/
4. Visualización: dashboards/ genera gráficos interactivos
5. Reporte: carga_reportes.py genera Excel y PDF
6. Distribución: Se envía por email a los directivos
```

## Nota para el Instructor

El análisis de datos es diferente a Data Science:
- **Análisis de Datos:** ¿Qué pasó? ¿Por qué? (Historia)
- **Data Science:** ¿Qué va a pasar? ¿Cómo lo evitamos? (Predicción)

Enseñar a los alumnos a diferenciar entre ambos campos y cuándo usar cada uno.