# Clase 27 · Fuentes

**Fecha de consulta:** 2026-11-18
**Confianza:** alta = fuente primaria u oficial · media = prensa o análisis serio · baja = blog o resumen, solo pista.

## Fuentes consultadas

| # | Tema | Qué respalda | Enlace | Confianza | Revisar de nuevo |
|---|---|---|---|---|---|
| 1 | Knight Capital | 4 millones de órdenes en 45 min por 212 de clientes; 397 millones de acciones; pérdida > 460 millones; 97 correos no atendidos; controles insuficientes; multa de 12 millones | [SEC, comunicado 2013-222](https://www.sec.gov/newsroom/press-releases/2013-222) | Alta | No vence |
| 2 | Knight Capital | Orden administrativa de la SEC | [SEC, orden 34-70694 (PDF)](https://www.sec.gov/files/litigation/admin/2013/34-70694.pdf) | Alta | Leer completa antes de dar más detalle |
| 3 | AWS octubre 2025 | Causa raíz (condición de carrera en el DNS de DynamoDB), plan viejo sobre plan nuevo, colapso por congestión en EC2, medidas | [AWS, Post-Event Summary](https://aws.amazon.com/message/101925) | Alta (informe de la propia empresa) | No vence |
| 4 | Reintentos | Tiempos de espera, reintentos y espera con aleatoriedad | [Amazon Builders' Library](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) | Alta | Revisar si se actualiza |
| 5 | Reintentos | Valores de tiempo de espera demasiado altos o bajos | [AWS Well-Architected: timeouts del cliente](https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_mitigate_interaction_failure_client_timeouts.html) | Alta | Revisar versión vigente |
| 6 | Webhooks | Duplicados, desorden, reintentos hasta 3 días con espera exponencial, cola asíncrona, firma, no usar la hora para ordenar | [Stripe: webhooks](https://docs.stripe.com/webhooks) | Alta (proveedor) | Revisar plazos en 6 meses |
| 7 | Idempotencia | Clave de idempotencia para reintentar sin efectos duplicados | [Stripe: solicitudes idempotentes](https://docs.stripe.com/api/idempotent_requests) | Alta (proveedor) | Revisar plazos de la clave |
| 8 | CrowdStrike | Análisis de causa raíz del archivo de canal 291 | [CrowdStrike RCA (PDF)](https://www.crowdstrike.com/wp-content/uploads/2024/08/Channel-File-291-Incident-Root-Cause-Analysis-08.06.2024.pdf) | Alta (**no se pudo leer en esta consulta**) | Leerlo antes de clase |
| 9 | CrowdStrike | Resumen técnico: 21 vs 20 campos; ~8,5 millones de equipos (estimación de Microsoft) | [arXiv 2610.32078](https://arxiv.org/html/2610.32078) y [The Hacker News](https://thehackernews.com/2024/08/crowdstrike-reveals-root-cause-of.html) | Media | Confirmar con el PDF |
| 10 | Mermaid | Mermaid renderiza texto en diagramas (flujo, secuencia…) en Markdown de GitHub | [GitHub Docs: creating diagrams](https://docs.github.com/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) | Alta | Probar el diagrama en el repositorio del curso |
| 11 | Agencia excesiva | Marco para permisos y autonomía | [OWASP LLM06](https://owasp.org/www-project-top-10-for-large-language-model-applications/2_0_vulns/LLM06_ExcessiveAgency.html) | Alta | Revisar si hay edición nueva |
| 12 | MCP | Estándar abierto para conectar aplicaciones de IA con sistemas externos | [modelcontextprotocol.io](https://modelcontextprotocol.io/) | Alta | Revisar versión de la especificación |

## Datos de memoria o sin fuente firme ⚠️

| Dato | Qué hay que buscar |
|---|---|
| Que la guía de Amazon describe los reintentos como "egoístas" (piden más recursos a una dependencia en dificultades) | Leer la guía original; la frase se vio citada en un blog |
| Forma exacta de la espera con aleatoriedad (por ejemplo "full jitter") | Artículo de arquitectura de AWS sobre espera exponencial y jitter |
| Corte de circuito (circuit breaker) y servicio de respaldo | Una fuente primaria (documentación de arquitectura de nube) |
| Detalles del defecto de validación de CrowdStrike | Leer el PDF del análisis de causa raíz |
| Qué medidas anunció CrowdStrike (despliegue gradual) | PDF del análisis |
| Sectores afectados por CrowdStrike | Fuente concreta de prensa o informe gubernamental |
| Cifra de pérdida de Knight (440 vs 460 millones) | Usar "más de 460 millones" (SEC); revisar cifra de 440 |
| Definición única de "harness" | No existe; revisar el uso en la documentación de cada herramienta |
| Que "al menos una vez" es lo habitual en otros proveedores | Documentación de cada proveedor usado en clase |
| Herramientas gratuitas para vista previa de Mermaid (VSCode, GitHub) | Confirmar extensión y plan gratis vigentes |
| Que GitHub rinde el diagrama dentro del README del curso | Probarlo en el repositorio del curso antes de clase |

## Reglas de uso

- Lo marcado ⚠️ se dice como "se cuenta que" hasta confirmarlo.
- Las cifras de tiempo, tablas de eventos y datos de la panadería son 🧪 inventados.
- No se leyó ningún archivo `.env`. Los materiales opcionales de otros talleres no se copiaron.
