# GLOSSARY.md - Glosario del Proyecto

## Términos Técnicos

| Término | Definición | Ejemplo de Uso |
|---------|------------|----------------|
| **Agente** | Programa de IA que ejecuta acciones autónomas | "El agente buscó información y creó el reporte" |
| **API** | Interfaz para conectar sistemas | "La API de OpenAI procesa los prompts" |
| **Prompt** | Instrucción que se le da a la IA | "Mejora tu prompt para obtener mejores resultados" |
| **Token** | Unidad de texto que procesa la IA | "Cuesta $0.002 por 1000 tokens" |
| **Sandbox** | Entorno aislado para ejecutar código | "El código se ejecuta en sandbox por seguridad" |
| **Tool** | Herramienta que puede usar el agente | "El agente tiene acceso a la herramienta de búsqueda" |
| **Memory** | Sistema de memoria del agente | "El agente recuerda conversaciones anteriores" |
| **Hallucination** | Cuando la IA inventa información | "El modelo alucinó datos que no existían" |
| **Temperature** | Controla la creatividad de la IA | "Temperature 0 = más preciso, 1 = más creativo" |
| **Context window** | Memoria máxima del modelo | "GPT-4 tiene 128k tokens de contexto" |

## Términos del Negocio

| Término | Definición | Equivalente |
|---------|------------|-------------|
| **MVP** | Producto Mínimo Viable | Primera versión funcional |
| **SaaS** | Software como Servicio | Aplicación web por suscripción |
| **KPI** | Indicador Clave de Rendimiento | Métrica importante del negocio |
| **Churn** | Tasa de cancelación de clientes | Porcentaje de usuarios que se van |
| **ARR** | Ingresos Anuales Recurrentes | Dinero que entra cada año |
| **CAC** | Costo de Adquisición de Cliente | Cuánto cuesta conseguir un cliente |
| **LTV** | Valor de Vida del Cliente | Cuánto dinero genera un cliente en total |

## Siglas del Proyecto

| Sigla | Significado | Contexto |
|-------|-------------|----------|
| **NLP** | Procesamiento de Lenguaje Natural | Campo de la IA que entiende texto |
| **LLM** | Large Language Model | Modelos como GPT, Claude, etc. |
| **API** | Application Programming Interface | Para conectar sistemas |
| **SQL** | Structured Query Language | Para bases de datos relacionales |
| **JSON** | JavaScript Object Notation | Formato de intercambio de datos |
| **REST** | Representational State Transfer | Estilo de arquitectura de APIs |
| **Docker** | Plataforma de contenedores | Para despliegue de aplicaciones |
| **CI/CD** | Continuous Integration/Deployment | Automatización de despliegue |

## Herramientas del Agente

| Herramienta | Función | Límites |
|-------------|---------|---------|
| **busqueda_web** | Buscar información en internet | No buscar información personal |
| **crear_archivo** | Crear archivos de texto o código | Solo crear en carpetas permitidas |
| **conexion_api** | Conectar con servicios externos | Solo servicios aprobados |
| **ejecutar_codigo** | Ejecutar Python en sandbox | Tiempo máximo 30 segundos |
| **leer_archivo** | Leer contenido de archivos | Solo archivos del proyecto |
| **modificar_archivo** | Editar archivos existentes | Solo con confirmación del usuario |