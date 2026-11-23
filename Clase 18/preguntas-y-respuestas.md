# Clase 27 · Preguntas y respuestas

---

### 1. ¿Qué es un harness, en palabras simples?
**Corta:** el programa que rodea al modelo y hace cumplir las reglas.
**Profunda:** recibe la petición, arma lo que ve el modelo, llama al modelo, valida y ejecuta las herramientas, guarda estado y registro, y aplica los topes de la Clase 26. ⚠️ El término no tiene definición única; en pruebas también se habla de "test harness".

### 2. ¿Por qué no dejo que el modelo se conecte directo a la base de datos?
**Corta:** porque su salida puede ser equivocada o manipulada.
**Profunda:** el modelo genera texto probable. Con acceso directo, un error o una instrucción escondida se convierte en cambio de datos. Entre ambos se ponen validación, permisos mínimos y registro. Es el principio de "agencia excesiva" ✅ (OWASP).

### 3. ¿Necesito todas las piezas del diagrama en mi chatbot?
**Corta:** no. Dibuja las que existen.
**Profunda:** un bot de preguntas sin acciones no necesita estado de pedidos ni herramientas de escritura. Sobredibujar da falsa seguridad. Lo que no existe se marca como "futuro".

### 4. ¿Qué es el estado y por qué el modelo no lo guarda?
**Corta:** es en qué punto va cada pedido; el modelo no recuerda entre llamadas.
**Profunda:** el modelo recibe lo que se le manda en cada llamada (Clase 22). El estado se guarda en el sistema y se le vuelve a entregar lo necesario. Así un reinicio no pierde el pedido.

### 5. ¿Qué se registra y qué no?
**Corta:** pasos, herramientas, resultados, tiempos y costos; no claves ni datos personales de más.
**Profunda:** hay que equilibrar auditoría y privacidad. Se registran seudónimos y se enmascaran datos. Un registro con claves es una fuga en espera. Y se define quién lo revisa y qué alertas produce ✅ (caso Knight).

### 6. ¿Cuándo reintento y cuándo no?
**Corta:** reintento errores temporales y de límite de uso; no los del cliente ni de permisos.
**Profunda:** un error de datos no se arregla repitiéndolo. ⚠️ Cómo se clasifica cada código de error depende del proveedor; hay que leer su documentación. Las acciones con efecto se reintentan solo si son idempotentes.

### 7. ¿Qué es la espera exponencial?
**Corta:** esperar cada vez el doble: 1, 2, 4, 8 segundos, con un tope.
**Profunda:** da tiempo al servicio para recuperarse y reduce la carga. Se le suma azar para que muchos clientes no reintenten sincronizados ✅ (Amazon). Los topes de espera y de intentos son parte del diseño.

### 8. ¿Por qué el azar ayuda?
**Corta:** reparte los reintentos en el tiempo.
**Profunda:** si mil clientes fallaron al mismo tiempo y todos reintentan exactamente a los 1, 2, 4 segundos, producen oleadas sincronizadas. Con azar, la carga se reparte ✅ (guía de Amazon).

### 9. ¿Puede reintentar empeorar una caída?
**Corta:** sí.
**Profunda:** cada reintento es carga extra. En el incidente de AWS de octubre de 2025 un subsistema quedó en colapso por congestión y se recuperó limitando el trabajo entrante ✅. Por eso los reintentos tienen tope y los sistemas tienen límites de entrada.

### 10. ¿Qué es la idempotencia?
**Corta:** hacerlo varias veces da el mismo resultado que una.
**Profunda:** se logra con una clave única por operación o con una comprobación previa ("¿ya existe el borrador del pedido P-101?"). Stripe documenta una cabecera de clave de idempotencia para reintentar sin duplicar ✅. No todas las operaciones lo son por sí solas.

### 11. ¿Por qué puede llegar un mensaje duplicado?
**Corta:** porque el emisor no recibió la confirmación a tiempo y lo reenvía.
**Profunda:** los proveedores suelen garantizar que el mensaje llegue "al menos una vez" y reintentan ✅. También hay fallos de red y de recuperación. No es un error del proveedor: es el contrato.

### 12. ¿Por qué puede llegar fuera de orden?
**Corta:** porque la entrega no garantiza el orden.
**Profunda:** Stripe lo dice de forma explícita ✅. Hay reintentos, rutas distintas y procesamiento en paralelo. No se debe ordenar por la hora de llegada ni por la hora de creación.

### 13. ¿Cómo manejo un evento que llega antes de tiempo?
**Corta:** lo dejo en espera o consulto el estado actual.
**Profunda:** con una máquina de estados, si el salto no es válido se pone en cola y se reprocesa cuando llega el evento anterior. Alternativa: pedir a la fuente el estado actual del objeto ✅ (Stripe lo recomienda).

### 14. ¿Qué hago si llega una cancelación después de un pago?
**Corta:** aplico la cancelación y aviso a una persona para el reembolso.
**Profunda:** el reembolso es una acción de dinero (herramienta roja de la Clase 26). El sistema detecta la situación y escala; no la resuelve solo.

### 15. ¿Qué es Mermaid y por qué usarlo?
**Corta:** texto que se convierte en diagrama, dentro de un archivo Markdown.
**Profunda:** GitHub lo muestra en sus documentos ✅. Como es texto, se versiona con Git y se ve qué cambió. Para no programadores, se le pide a un asistente y se revisa a ojo. ⚠️ Comprobar la vista previa en VSCode y en el repositorio del curso.

### 16. ¿Un diagrama generado por IA es confiable?
**Corta:** solo si lo comparas con tu sistema.
**Profunda:** puede añadir cajas que no existen o quitar controles. Se revisa con la lista de control: permisos, validación, estado, registros, persona, qué pasa si cada caja falla.

### 17. ¿MCP es parte de la arquitectura?
**Corta:** es una forma estándar de conectar herramientas a una aplicación de IA.
**Profunda:** MCP es un estándar abierto para conectar aplicaciones de IA con sistemas externos ✅. Cada conexión agrega poder: se aplican permisos mínimos y validación igual que con cualquier herramienta. ⚠️ La especificación cambia; revisar versión vigente.

### 18. ¿Esto lo hago yo o lo hace un programador?
**Corta:** tú diseñas, decides y revisas; un programador o un asistente lo construye.
**Profunda:** el Ing. de IA dibuja la arquitectura, define permisos, topes y casos de prueba, y verifica que lo construido los cumple. Saber leer el diagrama y el registro es la habilidad central.

---

## Preguntas trampa

| Pregunta trampa | Qué buscar en la respuesta | Respuesta que se espera |
|---|---|---|
| "Mi proveedor no repite mensajes, ¿verdad?" | Que no lo asuma | Lee el contrato; lo habitual es "al menos una vez" ✅ |
| "Reintento siempre hasta que funcione" | Tope, espera, idempotencia | Con tope y solo lo temporal |
| "Ordeno los eventos por la hora" | Que dude | No es fiable ✅ |
| "El log guarda todo, también las claves" | Que lo vea como riesgo | No se guardan claves |
| "El modelo valida los datos" | Que lo corrija | El modelo genera texto; valida el sistema |
| "Con más agentes no necesito harness" | Que vea que cada agente necesita control | El harness es el que aplica los límites |
| "El diagrama bonito prueba que funciona" | Que dude | Solo describe |
| "El caso Knight es de un bot de IA" | Que distinga | No: es un sistema automático de trading; las lecciones de ingeniería aplican |
