# TOOLS.md - Herramientas del Agente

## Herramientas Disponibles

### 1. Búsqueda Web
- **nombre:** busqueda_web
- **descripción:** Busca información en internet
- **parámetros:** query (string), num_results (int)
- **retorno:** lista de URLs y fragmentos de texto
- **restricciones:** No buscar información personal, no acceder a sitios maliciosos
- **ejemplo:** `busqueda_web("inteligencia artificial 2024", 5)`

### 2. Crear Archivo
- **nombre:** crear_archivo
- **descripción:** Crea un archivo de texto o código
- **parámetros:** nombre_archivo (string), contenido (string), ruta (string)
- **retorno:** Boolean (True si se creó correctamente)
- **restricciones:** Solo crear en carpetas permitidas, no sobrescribir sin permiso
- **ejemplo:** `crear_archivo("reporte.md", "# Reporte\n...", "docs/")`

### 3. Conexión API
- **nombre:** conectar_api
- **descripción:** Se conecta con un servicio externo
- **parámetros:** servicio (string), endpoint (string), datos (dict)
- **retorno:** JSON con la respuesta
- **restricciones:** Solo servicios aprobados, nunca enviar credenciales
- **ejemplo:** `conectar_api("github", "/repos/usuario/repo", {})`

### 4. Ejecución de Código
- **nombre:** ejecutar_codigo
- **descripción:** Ejecuta código Python de forma aislada
- **parámetros:** codigo (string), timeout (int)
- **retorno:** stdout, stderr, exit_code
- **restricciones:** Sandbox obligatorio, tiempo máximo 30 segundos, sin acceso a red
- **ejemplo:** `ejecutar_codigo("print('Hola')", 10)`

### 5. Leer Archivo
- **nombre:** leer_archivo
- **descripción:** Lee el contenido de un archivo
- **parámetros:** ruta (string)
- **retorno:** String con el contenido del archivo
- **restricciones:** Solo archivos del proyecto, no archivos sensibles
- **ejemplo:** `leer_archivo("data/datos.csv")`

### 6. Modificar Archivo
- **nombre:** modificar_archivo
- **descripción:** Edita el contenido de un archivo existente
- **parámetros:** ruta (string), contenido_nuevo (string), modo (string)
- **retorno:** Boolean (True si se modificó correctamente)
- **restricciones:** Solo con confirmación del usuario, no archivos sensibles
- **ejemplo:** `modificar_archivo("README.md", "# Nuevo título", "reemplazar")`

## Límites de Seguridad

1. **Tiempo máximo de ejecución:** 30 segundos por tarea
2. **Tamaño máximo de archivo:** 10 MB
3. **Acceso a red:** Solo para búsqueda web y APIs aprobadas
4. **Modificación de archivos:** Solo en carpetas src/, data/, docs/, audits/
5. **Ejecución de código:** Siempre en sandbox, nunca en el sistema principal

## Flujo de Uso

1. El usuario pide una tarea al agente
2. El agente consulta TOOLS.md para saber qué herramientas tiene
3. El agente selecciona la herramienta adecuada
4. El agente ejecuta la herramienta con los parámetros correctos
5. El agente registra la acción en auditoria_seguridad.md
6. El agente entrega el resultado al usuario