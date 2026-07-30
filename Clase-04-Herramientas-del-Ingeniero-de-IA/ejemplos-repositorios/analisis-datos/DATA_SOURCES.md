# DATA_SOURCES.md - Fuentes de Datos

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
| Fuente | Completitud | Duplicados | Errores |
|--------|-------------|------------|---------|
| ventas_raw.csv | 99.5% | 0.1% | 0.4% |
| marketing_raw.csv | 95% | 0.5% | 4.5% |
| inventario_raw.xlsx | 100% | 0% | 0% |

## Acceso a Datos
1. **Lectura:** SELECT permitido en todas las tablas
2. **Escritura:** Solo en tablas de staging
3. **Eliminación:** PROHIBIDA sin aprobación
4. **Backup:** Diario automático a las 2:00 AM

## Políticas de Retención
- **Datos en bruto:** 2 años
- **Datos procesados:** 5 años
- **Reportes:** Permanente
- **Logs de acceso:** 1 año

## Fuentes Externas
| Fuente | Tipo | Frecuencia | Costo |
|--------|------|------------|-------|
| Google Analytics | API | Diaria | Gratis |
| Stripe | API | Tiempo real | 2.9% por transacción |
| Mailchimp | API | Semanal | $20/mes |
| Meteorología | CSV | Diaria | Gratis |