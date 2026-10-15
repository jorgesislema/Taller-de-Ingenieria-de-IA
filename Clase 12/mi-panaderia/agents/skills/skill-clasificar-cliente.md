# Skill: Clasificar cliente

## Cuándo usarla
Cuando llega un pedido y necesitas saber si el cliente es persona o empresa.

## Entradas necesarias
- Nombre del cliente o razón social.
- Cantidades solicitadas.
- Si el cliente indica que es una empresa, negocio o institución.

## Pasos
1. Revisa si el cliente menciona ser empresa, negocio, institución o mayorista.
2. Revisa si las cantidades son altas (más de 100 panes o más de 10 pasteles).
3. Si hay duda, pregunta al usuario: "¿El pedido es para una empresa o para uso personal?"
4. Clasifica como:
   - **Persona:** pedido individual, cantidades pequeñas.
   - **Empresa:** pedido para negocio, cantidades grandes.

## Formato de salida
```text
Tipo de cliente: [Persona / Empresa]
Justificación: [Breve explicación]
Criterios de calidad
La clasificación debe ser coherente con las cantidades.

Si no hay información suficiente, debe preguntar.

No asumir sin evidencia.

Ejemplo
Entrada: "Quiero 40 bocadillos para una fiesta familiar."
Salida:

text
Tipo de cliente: Persona
Justificación: Cantidad moderada, uso personal.
```