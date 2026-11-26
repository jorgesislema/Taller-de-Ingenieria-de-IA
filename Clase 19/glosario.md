# Clase 28 · Glosario del profesor

Cada término: **qué es** (palabras simples) · **analogía** · 🎓 **trampa** (dónde se confunde).

| # | Término | Qué es | Analogía | 🎓 Trampa |
|---|---|---|---|---|
| 1 | Prueba (test) | Comprobación con resultado exacto: pasa o no pasa | La balanza: 100 g o no | Sirve solo si hay una respuesta correcta definida |
| 2 | Eval (evaluación) | Medir la calidad de una respuesta abierta con una rúbrica | La cata de pan | No es una prueba exacta: depende de quién califica |
| 3 | Caso de prueba | Ficha con entrada, esperado, criterio y gravedad | Una orden de pedido de prueba | Sin "esperado" escrito antes, no es caso, es opinión |
| 4 | Conjunto dorado (golden set) | Lista pequeña y congelada de casos representativos | Los panes de referencia de la panadería | "Dorado" no significa perfecto, significa fijo |
| 5 | Resultado esperado | Lo que debe ocurrir, definido antes de correr | La receta con su foto final | Escribirlo después del resultado invalida la prueba |
| 6 | Criterio de aprobación | La regla que decide pasa o falla | "Debe contener $1,73" | Criterios vagos ("que suene bien") dan resultados distintos por persona |
| 7 | Rúbrica | Lista de criterios para calificar | Hoja de cata con casillas | Escala de 1 a 10 es menos estable que sí/no |
| 8 | Regresión | Algo que funcionaba y dejó de funcionar tras un cambio | Cambiar la harina y que el pan de yema ya no suba | Mejorar un caso y romper otro es lo normal, no raro |
| 9 | Prueba de reglas | Prueba exacta de algo cerrado (precio, formato) | Pesar el pan | No cubre lo abierto (tono, honestidad) |
| 10 | Prueba de integración | Prueba de que las piezas funcionan juntas | Probar que el pedido llega de la caja al horno | Una pieza sana no garantiza una conexión sana |
| 11 | Juez de IA (LLM-as-a-judge) | Un modelo que califica respuestas con una rúbrica | Un catador automático | Tiene sesgos y puede equivocarse con seguridad |
| 12 | Sesgo de posición | El juez prefiere la respuesta que aparece primero (o segunda) | Elegir siempre la primera bandeja | Se detecta intercambiando el orden |
| 13 | Sesgo de longitud (verbosidad) | El juez premia lo más largo | Creer que el pan más grande es el mejor | Una respuesta larga no es una mejor respuesta |
| 14 | Autopreferencia | Un modelo califica mejor lo que se parece a su propio estilo | El panadero que siempre prefiere su receta | Usar un juez distinto del bot lo reduce, no lo elimina |
| 15 | Calibrar al juez | Comparar sus notas con las de una persona en una muestra | Ajustar la balanza con una pesa conocida | Si coinciden poco, el juez no sirve para esa rúbrica |
| 16 | Variación entre corridas | La misma entrada puede dar salidas distintas | Dos panes del mismo lote nunca son idénticos | Temperatura 0 reduce, no garantiza ✅ |
| 17 | Temperatura | Perilla de cuánto riesgo toma el modelo al elegir | Cuánto se aparta el panadero de la receta | En chats gratis rara vez se puede fijar |
| 18 | Caso estable / inestable | Estable: pasa siempre. Inestable: pasa a veces | Un horno que a veces falla | El inestable es más peligroso que el que siempre falla |
| 19 | Gravedad | Cuánto daño hace que un caso falle | Una moneda de $0,05 vs una alergia | El promedio ignora la gravedad |
| 20 | Sobreajuste (a los casos) | Ajustar el prompt hasta que pase justo esos casos | Estudiar solo las preguntas del examen pasado | Se evita con casos reservados |
| 21 | Casos reservados | Casos que no miras mientras mejoras | El examen sorpresa | Si los usas para ajustar, dejan de ser reservados |
| 22 | Versionar | Guardar cada versión con un nombre y fecha | Numerar las recetas | Versionar el prompt y olvidar el modelo y el catálogo |
| 23 | Línea base | La versión actual contra la que se compara | La receta de siempre | Sin línea base no se puede decir "mejoró" |
| 24 | Deriva (drift) | El comportamiento cambia con el tiempo sin que tú cambies nada | El horno que se desregula | Pasa por actualizaciones del proveedor ✅ |
| 25 | Cobertura | Qué riesgos cubren los casos | Revisar todas las puertas, no solo la principal | No es cantidad de casos, es variedad de riesgos |
| 26 | Prueba adversaria | Caso diseñado para engañar o romper al bot | El cliente que intenta pagar menos | Se hacen con permiso y sobre sistemas propios |
