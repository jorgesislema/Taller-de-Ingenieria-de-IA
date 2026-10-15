# Skill: Consultar precios y descuentos

## Cuándo usarla
Cuando ya sabes el tipo de cliente y necesitas calcular el precio.

## Entradas necesarias
- Tipo de cliente (Persona o Empresa).
- Lista de productos con cantidades.
- Archivo de precios (`datos/precios.md`).

## Pasos
1. Lee el archivo de precios.
2. Si el cliente es persona, usa precios unitarios.
3. Si el cliente es empresa, usa precios al por mayor.
4. Aplica descuentos por cantidad según la tabla.
5. Si el total supera $200 o $500, aplica descuento adicional.
6. Calcula subtotal, descuento y total.

## Formato de salida
```text
| Producto | Cantidad | Precio unitario | Subtotal |
|---|---|---|---|
| Pan francés | 300 | $0.40 | $120.00 |
| Pastel chocolate | 20 | $9.50 | $190.00 |
| **Subtotal** | | | $310.00 |
| **Descuento por cantidad** | | | -$62.00 |
| **Descuento adicional** | | | -$15.50 |
| **Total** | | | $232.50 |
Criterios de calidad
Los cálculos deben ser correctos.

Los descuentos deben aplicarse según las reglas.

No inventar precios.

Ejemplo
Entrada: Empresa, 300 panes franceses, 20 pasteles de chocolate.
Salida: Tabla con cálculos y total.

Errores comunes
Aplicar descuento de persona a empresa.

No aplicar descuento adicional cuando corresponde.

Límites
No modifica precios.

No inventa productos que no están en la lista.

```