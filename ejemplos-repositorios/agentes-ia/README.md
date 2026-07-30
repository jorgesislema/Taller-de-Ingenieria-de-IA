# Ejemplo: Agentes de IA

## ¿Qué es un Agente de IA?

Un agente de IA no solo conversa, sino que **ejecuta acciones**: busca en internet, genera archivos, conecta con otras herramientas, toma decisiones y aprende de sus errores.

## Estructura del Repositorio

```
mi_agente_ia/
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
├── GLOSSARY.md                    # ESTÁNDAR: Lo leen todas las plataformas
│
├── TOOLS.md                       # NUEVO: Lista de herramientas que puede usar el agente
├── MEMORY.md                      # NUEVO: Cómo el agente recuerda conversaciones
│
├── data/
│   ├── historial_conversaciones.json
│   ├── herramientas_disponibles.json
│   └── config_agente.json
│
├── src/
│   ├── agente_principal.py        # El cerebro del agente
│   ├── herramientas/
│   │   ├── __init__.py
│   │   ├── buscador_web.py        # Busca información en internet
│   │   ├── generador_archivos.py  # Crea documentos y archivos
│   │   ├── conexion_api.py        # Se conecta con servicios externos
│   │   └── ejecutor_codigo.py     # Ejecuta código de forma segura
│   ├── memoria/
│   │   ├── __init__.py
│   │   ├── corto_plazo.py         # Recuerda la conversación actual
│   │   └── largo_plazo.py         # Recuerda conversaciones anteriores
│   └── utilidades/
│       ├── __init__.py
│       ├── validador.py           # Verifica que las acciones sean seguras
│       └── logger.py              # Registra todo lo que hace el agente
│
├── audits/
│   ├── auditoria_seguridad.md     # Auditoría de seguridad del agente
│   ├── historial_acciones.md      # Registro de todas las acciones ejecutadas
│   └── errores_aprendidos.md      # Errores que el agente debe evitar
│
├── tests/
│   ├── test_agente.py
│   ├── test_herramientas.py
│   └── test_memoria.py
│
├── .gitignore
├── .env
├── requirements.txt
└── README.md
```

## Archivos de Configuración para IA

### CODEX.md (Para Codex/OpenAI)
```markdown
Eres un agente de IA autónomo que puede ejecutar acciones. Tus herramientas incluyen:
- Buscar en internet
- Crear archivos
- Conectar con APIs
- Ejecutar código Python

REGLAS:
1. NUNCA ejecutes código sin verificación previa
2. NUNCA modifiques archivos sensibles (.env, .gitignore)
3. SIEMPRE registra cada acción en auditoria_seguridad.md
4. SIEMPRE pregunta antes de acciones destructivas (borrar, modificar)
5. Si algo falla, repórtalo en errores_aprendidos.md
```

### CLAUDE.md (Para Claude)
```markdown
## Identidad del Agente
Eres un asistente autónomo que ayuda a los usuarios a completar tareas complejas.
Puedes buscar información, crear archivos y conectar con servicios externos.

## Capacidades
1. **Búsqueda Web:** Encuentra información actualizada
2. **Generación de Archivos:** Crea documentos, código, reportes
3. **Conexión de APIs:** Se conecta con servicios como Google, Twitter, etc.
4. **Ejecución de Código:** Ejecuta Python de forma aislada

## Restricciones
- NO ejecutes código que pueda dañar el sistema
- NO accedas a archivos fuera del proyecto
- NO compartas información sensible
- SIEMPRE confirma antes de acciones irreversibles
```

### TOOLS.md (Nuevo: Lista de Herramientas)
```markdown
# Herramientas Disponibles para el Agente

## Búsqueda Web
- **nombre:** busqueda_web
- **descripción:** Busca información en internet
- **parámetros:** query (string), num_results (int)
- **retorno:** lista de URLs y fragmentos de texto
- **restricciones:** No buscar información personal, no acceder a sitios maliciosos

## Generación de Archivos
- **nombre:** crear_archivo
- **descripción:** Crea un archivo de texto o código
- **parámetros:** nombre_archivo (string), contenido (string), ruta (string)
- **retorno:** Boolean (True si se creó correctamente)
- **restricciones:** Solo crear en carpetas permitidas, no sobrescribir sin permiso

## Conexión API
- **nombre:** conectar_api
- **descripción:** Se conecta con un servicio externo
- **parámetros:** servicio (string), endpoint (string), datos (dict)
- **retorno:** JSON con la respuesta
- **restricciones:** Solo servicios aprobados, nunca enviar credenciales

## Ejecución de Código
- **nombre:** ejecutar_codigo
- **descripción:** Ejecuta código Python de forma aislada
- **parámetros:** codigo (string), timeout (int)
- **retorno:** stdout, stderr, exit_code
- **restricciones:** Sandbox obligatorio, tiempo máximo 30 segundos, sin acceso a red
```

## Ejemplo de Uso

```
Usuario: "Crea un reporte de ventas del último trimestre"

Agente:
1. Lee TOOLS.md para saber qué herramientas tiene disponibles
2. Usa "conexion_api" para conectarse a la base de datos de ventas
3. Usa "ejecutar_codigo" para procesar los datos
4. Usa "crear_archivo" para generar el reporte en PDF
5. Registra la acción en auditoria_seguridad.md
6. Entrega el archivo al usuario
```

## Nota para el Instructor

Los agentes de IA son más complejos que los chatbots porque **ejecutan acciones**. Es fundamental enseñar a los alumnos:

1. **Seguridad:** Los agentes pueden causar daños reales si no se les ponen límites
2. **Transparencia:** Cada acción debe quedar registrada para auditoría
3. **Confirmación:** Antes de acciones destructivas, SIEMPRE preguntar al usuario
4. **Aprendizaje:** Los errores deben documentarse para no repetirlos