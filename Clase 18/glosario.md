# Clase 27 · Glosario

| Término | Qué es | Analogía | 🎓 Trampa |
|---|---|---|---|
| Arquitectura | Cómo se conectan las piezas de un sistema | Plano de una cocina | Se dibuja lo que existe, no lo ideal |
| Harness (arnés, orquestador) | Programa que rodea al modelo, ejecuta el ciclo y hace cumplir reglas | Jefe de turno de la cocina | También se usa para "conjunto de pruebas" ⚠️ aclarar |
| Canal | Por donde el cliente habla con el bot | Mostrador o teléfono | Cada canal trae sus propios mensajes y límites |
| Orquestador | Pieza que decide qué se llama y cuándo | Director de orquesta | Si es el modelo quien orquesta, hay más riesgo |
| Herramienta | Función que el sistema ejecuta a pedido del modelo | Llave de una puerta | El modelo pide; el sistema ejecuta |
| Integración | Conexión con otro servicio | Teléfono con el proveedor | Cada integración puede fallar |
| API | Forma de pedir algo a otro sistema y esperar respuesta | Llamar por teléfono | Puede fallar o tardar |
| Evento | Aviso de que algo ocurrió | Mensaje en el buzón | Puede llegar repetido o tarde |
| Webhook | Evento que otro servicio envía a una dirección tuya | El proveedor te toca el timbre | Hay que verificar la firma y responder rápido |
| Cola de mensajes | Buzón que guarda eventos para procesarlos a ritmo propio | Fila del mostrador | Puede crecer sin control si no se vigila |
| Estado | Lo que el sistema recuerda de cada pedido | Libreta del encargo | El modelo no lo recuerda por sí solo |
| Máquina de estados | Lista de estados y saltos válidos | Mapa de caminos permitidos | Evita estados imposibles |
| Permiso | Qué puede hacer una pieza o persona | Llaves de cada empleado | Permisos amplios multiplican el daño |
| Mínimo privilegio | Dar solo el poder necesario | Llave de bodega, no de caja fuerte | Se aplica a herramientas y credenciales |
| Validación | Comprobar datos o acciones antes de aceptarlos | Pesar la masa antes de hornear | El modelo no valida |
| Registro (log) | Bitácora de lo que pasa | Cuaderno de la cocina | Sin lectura ni alertas no sirve |
| Traza | Registro de todos los pasos de una solicitud | Recorrido de una comanda | Útil para reproducir fallos |
| Alerta | Aviso que obliga a actuar | Alarma de humo | Alertas sin responsable se ignoran |
| Error temporal | Fallo que puede pasar solo | Línea ocupada | Se reintenta |
| Error permanente | Fallo que no se arregla reintentando | Número inexistente | No se reintenta |
| Reintento | Volver a intentar | Llamar de nuevo | Sin tope es un bucle |
| Espera exponencial | Cada espera es el doble de la anterior | Esperar 1, 2, 4, 8 segundos | Con tope y con azar |
| Tope de espera | Máximo tiempo de espera entre reintentos | Límite del reloj | Sin tope, esperas eternas |
| Jitter (aleatoriedad) | Azar sumado a la espera para repartir los reintentos | Desfase al salir del cine | Sin él, los reintentos golpean juntos |
| Tiempo máximo (timeout) | Cuánto se espera una respuesta antes de rendirse | Reloj de arena | Muy alto o muy bajo, ambos dañan |
| Corte de circuito | Dejar de llamar un rato a un servicio que falla seguido ⚠️ | Fusible | Hay que definir cuándo se reabre |
| Idempotencia | Repetir una operación da el mismo resultado que hacerla una vez | Interruptor de "encender" | No todo es idempotente por sí solo |
| Clave de idempotencia | Código único que identifica un intento | Número de comanda | Debe ser único por operación |
| "Al menos una vez" | Garantía de entrega: nunca se pierde, puede repetirse | Carta certificada que puede llegar dos veces | Hay que diseñar para duplicados |
| Duplicado | El mismo evento recibido más de una vez | Misma comanda dos veces | Se detecta por el ID |
| Fuera de orden | Un evento llega antes que otro anterior | Carta del martes antes que la del lunes | No ordenar por hora de llegada |
| Registro de eventos procesados | Lista de IDs ya tratados | Lista de comandas despachadas | Debe guardarse de forma duradera |
| Mermaid | Texto que se convierte en diagrama | Plano dibujado con palabras | El diagrama puede mostrar lo que no existe |
| Diagrama de flujo / de secuencia / de estados | Tres tipos de dibujo para ver piezas, mensajes y estados | Mapa, guion y semáforo | Elegir el tipo según la pregunta |
| Contingencia | Plan para cuando algo cae | Generador eléctrico | Se practica antes (Clase 30) |
