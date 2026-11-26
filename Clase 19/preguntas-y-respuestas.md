# Clase 28 · Preguntas y respuestas del profesor

Cada pregunta tiene **respuesta corta** (para decirla en clase) y **respuesta profunda** (para cuando insistan).
Marcas: ✅ verificado · ⚠️ por verificar. Fecha: 2026-11-18.

---

**1. ¿Cuántos casos de prueba necesito?**
- **Corta:** Para empezar, entre 12 y 20. Crece cuando aparecen errores nuevos.
- **Profunda:** No hay un número universal ⚠️. Lo que importa es la **variedad de riesgos**, no la cantidad. Con riesgo alto (dinero, salud, datos personales) se necesitan más casos en esas áreas. Cada error real en producción debe convertirse en un caso nuevo.

**2. ¿Por qué no basta con probar el bot "a mano" conversando?**
- **Corta:** Porque no puedes repetirlo igual ni comparar versiones.
- **Profunda:** Probar conversando sirve para explorar (es el "chat sirve para pensar"). Pero sin casos fijos no sabes si v2 es mejor o si tuviste suerte. Además, tu cerebro recuerda los éxitos y olvida los fallos.

**3. ¿Qué diferencia hay entre prueba y eval?**
- **Corta:** La prueba tiene una respuesta exacta. El eval mide calidad con una rúbrica.
- **Profunda:** En la práctica se mezclan. Una buena estrategia usa pruebas exactas para todo lo que se pueda, y evals solo para lo abierto. El motivo: lo exacto es barato, rápido y sin discusión.

**4. ¿Puedo confiar en que un juez de IA califique bien?**
- **Corta:** A veces. Hay que calibrarlo y conocer sus sesgos.
- **Profunda:** El trabajo de Zheng y otros (2023) mostró que un juez fuerte coincide con las preferencias humanas en más del 80 % de los casos, un nivel parecido al de dos personas entre sí ✅. También documentó sesgos de posición, longitud y autopreferencia, y razonamiento limitado ✅. Por eso: rúbrica de sí/no, orden invertido, juez distinto del bot y muestra revisada por una persona.

**5. ¿Por qué el juez no debe ser el mismo modelo que el bot?**
- **Corta:** Porque tiende a preferir lo que se parece a su propio estilo.
- **Profunda:** Es la autopreferencia ✅. No siempre se puede usar otro modelo (planes gratis y límites). En ese caso, hay que compensar con más muestra humana. No hay garantía de que usar otro modelo elimine el problema: dos modelos pueden compartir los mismos puntos ciegos.

**6. ¿Qué es el sesgo de posición?**
- **Corta:** El juez prefiere la respuesta que aparece primero (o segunda), sin importar su contenido.
- **Profunda:** Se detecta con una prueba simple: pides comparar A contra B, y luego B contra A. Si el ganador cambia con el orden, ese veredicto no es fiable. Un estudio con 12 jueces y más de 100.000 evaluaciones lo midió ✅. El tamaño del efecto depende del juez y de la tarea, así que no des un porcentaje ⚠️.

**7. Si pongo temperatura 0, ¿ya no hay variación?**
- **Corta:** Hay menos, pero puede seguir habiendo.
- **Profunda:** Un análisis técnico de 2025 explicó que el resultado puede depender de cuántas peticiones procesa el servidor a la vez y del orden en que se suman los decimales ✅. En los chats gratis normalmente no puedes fijar la temperatura de todos modos ⚠️. Por eso se corre cada caso 3 veces.

**8. ¿Por qué correr cada caso 3 veces y no 1?**
- **Corta:** Para ver si el resultado es estable.
- **Profunda:** Una corrida te da una foto. Tres te dicen si el caso es estable (3/3), falla (0/3) o es inestable (1/3 o 2/3). Los inestables son los más peligrosos. Tres es una regla práctica del curso, no una ley; con riesgo alto, más.

**9. v2 mejora el promedio pero rompe un caso grave. ¿Qué hago?**
- **Corta:** No cambias. Arreglas v2 y vuelves a probar.
- **Profunda:** Por eso se escribe la regla de decisión **antes** y se mira por gravedad. Un total mejor puede esconder una pérdida seria (el ejemplo de alergias). Es la lección de la actualización de GPT-4o de 2025: mejorar agrado y empeorar honestidad ✅.

**10. ¿Qué es el sobreajuste a los casos?**
- **Corta:** Ajustar el prompt hasta que pase justo esos casos.
- **Profunda:** Es como estudiar solo el examen del año pasado. El prompt "aprende" a pasar los casos pero falla con casos nuevos. Se evita con casos reservados: un grupo que no miras mientras mejoras (idea de la Clase 21).

**11. ¿Mi bot puede cambiar si yo no toqué nada?**
- **Corta:** Sí.
- **Profunda:** El proveedor puede actualizar el modelo, o puede haber errores de infraestructura. Pasó entre marzo y junio de 2023 ✅ y de agosto a septiembre de 2025 ✅. Por eso las pruebas se corren con regularidad. Con una API a veces puedes fijar la versión del modelo; en un chat gratis, no ⚠️.

**12. ¿Cada cuánto debo correr las pruebas?**
- **Corta:** Cada vez que cambies algo y cada cierto tiempo aunque no cambies nada.
- **Profunda:** No hay una frecuencia oficial ⚠️. Regla del curso: antes de cada cambio, después de cada cambio, y semanal si el bot está en uso. En la Clase 30 se ve cómo automatizar avisos.

**13. ¿Esto no es "cosa de programadores"?**
- **Corta:** No. Escribir casos y rúbricas lo hace quien conoce el negocio.
- **Profunda:** El código solo ayuda a correr los casos en lote. Pero **qué** probar, **qué** es una respuesta aceptable y **qué** gravedad tiene un fallo lo decide la persona que conoce al cliente. En el curso se hace sin código, con tablas y prompts.

**14. ¿Qué herramientas gratis hay para esto?**
- **Corta:** Una tabla en Markdown, el chat y VSCode con asistente.
- **Profunda:** Existe Promptfoo, abierto con licencia MIT ✅, pero requiere línea de comandos y OpenAI anunció su adquisición en marzo de 2026, con la promesa de mantenerlo abierto ✅ ⚠️ (revisar antes de mencionarlo). Hay otras herramientas con planes gratis cuyos límites cambian ⚠️; el curso no depende de ellas.

**15. ¿Puede un bot "pasar todas las pruebas" y aun así fallar?**
- **Corta:** Sí.
- **Profunda:** Las pruebas solo ven lo que alguien pensó. Un cliente hará algo nuevo. Y el servicio puede degradarse sin caerse (caso Anthropic 2025 ✅). Por eso se suman la revisión humana (Clase 29) y la observabilidad en producción (Clase 30).

**16. ¿Quién es responsable si el bot dice algo falso?**
- **Corta:** La empresa que lo publica.
- **Profunda:** En el caso Moffatt contra Air Canada (2024), el tribunal rechazó que el bot fuera una entidad aparte y responsabilizó a la aerolínea ✅. Es una decisión de un tribunal de reclamos menores en Canadá: señal fuerte, no regla universal. Para Ecuador, consultar a un abogado ⚠️ (no es asesoría legal).

---

## Preguntas trampa

| Pregunta trampa | Por qué es trampa | Cómo responder |
|---|---|---|
| "El juez de IA dio 9/10, ¿ya está listo?" | Mide al juez tanto como al bot | "¿Calibraste al juez con una muestra humana? ¿Y las cuentas, las probaste con reglas?" |
| "Pasó 11 de 12, es 92 %. ¿Ya?" | Ignora gravedad y variación | "¿Cuál falló? ¿Cuántas veces lo corriste?" |
| "Si temperatura 0 es siempre igual, con una corrida alcanza" | Falso ✅ | "Casi igual no es igual. Corramos 3 veces" |
| "Cambié el prompt solo un poquito" | Cambios chicos causan regresiones grandes | "Corre el conjunto completo" |
| "El modelo nuevo es mejor en los benchmarks, cámbialo" | Un benchmark general no prueba tu caso (Clase 13) | "¿Pasó tu conjunto dorado?" |
| "Usemos el mismo modelo de juez y de bot, es más simple" | Autopreferencia ✅ | "Compensemos con muestra humana" |
