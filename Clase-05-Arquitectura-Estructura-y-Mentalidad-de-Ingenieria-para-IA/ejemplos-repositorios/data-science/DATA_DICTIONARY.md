# DATA_DICTIONARY.md - Diccionario de Datos

## Tabla: ventas
| Columna | Tipo | Descripción | Ejemplo | Valores Faltantes |
|---------|------|-------------|---------|-------------------|
| fecha | datetime | Fecha de la venta | 2024-01-15 | 0% |
| id_producto | string | Código único del producto | PROD-001 | 0% |
| nombre_producto | string | Nombre del producto | Laptop HP | 0.5% |
| cantidad | int | Unidades vendidas | 5 | 0% |
| precio_unitario | float | Precio por unidad | 899.99 | 0% |
| total_venta | float | cantidad * precio_unitario | 4499.95 | 0% |
| id_cliente | string | Código único del cliente | CLI-123 | 2% |
| región | string | Zona geográfica | Norte | 0% |
| canal_venta | string | Canal de venta | Online | 0% |

## Tabla: clientes
| Columna | Tipo | Descripción | Ejemplo | Valores Faltantes |
|---------|------|-------------|---------|-------------------|
| id_cliente | string | Código único del cliente | CLI-123 | 0% |
| nombre | string | Nombre del cliente | Juan Pérez | 1% |
| email | string | Correo electrónico | juan@email.com | 3% |
| fecha_registro | datetime | Fecha de registro | 2023-05-20 | 0% |
| tipo_cliente | string | Regular, VIP, Corporativo | VIP | 0% |
| región | string | Zona geográfica | Norte | 0% |

## Variable Objetivo
- **total_venta:** Monto total de la venta (variable a predecir)
- **Tipo:** Numérica continua
- **Rango:** $0 - $50,000
- **Distribución:** Asimétrica a la derecha (mayoría de ventas son pequeñas)

## Variables Predictoras Numéricas
| Variable | Tipo | Rango | Correlación con Objetivo |
|----------|------|-------|--------------------------|
| cantidad | int | 1 - 100 | 0.75 |
| precio_unitario | float | $10 - $10,000 | 0.45 |

## Variables Predictoras Categóricas
| Variable | Categorías | Frecuencia |
|----------|------------|------------|
| región | Norte, Sur, Este, Oeste | 25% cada una |
| canal_venta | Online, Físico | 60%, 40% |
| tipo_cliente | Regular, VIP, Corporativo | 70%, 20%, 10% |

## Variables Derivadas
| Variable | Descripción | Fórmula |
|----------|-------------|---------|
| día_semana | Día de la semana (0-6) | fecha.dt.dayofweek |
| mes | Mes del año (1-12) | fecha.dt.month |
| trimestre | Trimestre (1-4) | fecha.dt.quarter |
| es_fin_de_semana | Si es sábado o domingo | día_semana >= 5 |

## Calidad de Datos
- **Completitud:** 97% (3% de valores faltantes en id_cliente)
- **Consistencia:** 99% (1% de registros con total_venta < 0)
- **Exactitud:** 98% (2% de registros con precio_unitario = 0)
- **Temporalidad:** 100% (todos los registros dentro del rango esperado)

## Notas para el Modelo
1. **Valores faltantes:** Imputar id_cliente con "DESCONOCIDO"
2. **Outliers:** Tratar ventas mayores a $10,000 como casos especiales
3. **Codificación:** One-hot encoding para variables categóricas
4. **Escalado:** StandardScaler para variables numéricas
5. **Feature Engineering:** Crear variables de tiempo y interacciones