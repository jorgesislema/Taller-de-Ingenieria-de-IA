# GLOSSARY.md - Glosario del Proyecto

## Términos Técnicos

| Término | Definición | Ejemplo de Uso |
|---------|------------|----------------|
| **Chatbot** | Programa que simula conversación humana | "El chatbot respondió en 2 segundos" |
| **API** | Interfaz para conectar sistemas | "La API de OpenAI procesa los prompts" |
| **Prompt** | Instrucción que se le da a la IA | "Mejora tu prompt para obtener mejores resultados" |
| **Token** | Unidad de texto que procesa la IA | "Cuesta $0.002 por 1000 tokens" |
| **Embedding** | Representación numérica del texto | "Los embeddings capturan el significado" |
| **Fine-tuning** | Entrenar un modelo con datos específicos | "Hicimos fine-tuning con 1000 ejemplos" |
| **RAG** | Retrieval-Augmented Generation | "Usamos RAG para buscar en documentos" |
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

## Nuestros Módulos Internos

| Módulo | Función | Archivos Principales |
|--------|---------|---------------------|
| **Procesador de Mensajes** | Analiza y genera respuestas | `procesador.py`, `generador.py` |
| **Gestor de Contexto** | Recuerda conversaciones anteriores | `memoria.py`, `historial.py` |
| **Conector de APIs** | Se conecta a servicios externos | `conector.py`, `cliente_api.py` |
| **Validador de Entradas** | Verifica datos del usuario | `validador.py`, `sanitizador.py` |
| **Generador de Logs** | Registra actividad del sistema | `logger.py`, `reportero.py` |