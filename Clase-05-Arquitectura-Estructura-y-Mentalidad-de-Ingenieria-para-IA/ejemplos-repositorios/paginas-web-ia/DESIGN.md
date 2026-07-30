# DESIGN.md - Guía de Diseño Visual

## Paleta de Colores

### Colores Principales
- **Primario:** #2563eb (azul) - Botones principales, enlaces
- **Secundario:** #10b981 (verde) - Éxito, confirmaciones
- **Acento:** #f59e0b (amarillo) - Advertencias, elementos destacados

### Colores de Texto
- **Texto principal:** #1f2937 (gris oscuro)
- **Texto secundario:** #6b7280 (gris medio)
- **Texto en fondo oscuro:** #ffffff (blanco)

### Colores de Fondo
- **Fondo principal:** #ffffff (blanco)
- **Fondo secundario:** #f9fafb (gris claro)
- **Fondo del chat:** #f3f4f6 (gris claro)

### Colores de Estado
- **Éxito:** #10b981 (verde)
- **Error:** #ef4444 (rojo)
- **Advertencia:** #f59e0b (amarillo)
- **Info:** #3b82f6 (azul)

## Tipografía

### Fuentes
- **Principal:** Inter (para todo el texto)
- **Código:** Fira Code (para bloques de código)

### Tamaños
- **Títulos:** 24-32px, Bold
- **Subtítulos:** 18-20px, Semi-bold
- **Cuerpo:** 16px, Regular
- **Pequeño:** 14px, Regular
- **Muy pequeño:** 12px, Regular

## Espaciado

### Unidades
- **XS:** 4px
- **SM:** 8px
- **MD:** 16px
- **LG:** 24px
- **XL:** 32px
- **XXL:** 48px

### Márgenes y Paddings
- **Margen externo:** 16px
- **Padding interno:** 24px
- **Espacio entre elementos:** 12px
- **Espacio entre secciones:** 32px

## Bordes y Sombras

### Bordes
- **Radio de bordes:** 8px
- **Borde de inputs:** 1px solid #d1d5db
- **Borde de focus:** 2px solid #2563eb

### Sombras
- **Sombra suave:** 0 1px 3px rgba(0, 0, 0, 0.1)
- **Sombra media:** 0 4px 6px rgba(0, 0, 0, 0.1)
- **Sombra fuerte:** 0 10px 15px rgba(0, 0, 0, 0.1)

## Componentes del Chatbot

### Ventana del Chat
- **Ancho:** 350px
- **Alto:** 500px
- **Posición:** Esquina inferior derecha
- **Borde:** 8px radio
- **Sombra:** 0 4px 6px rgba(0, 0, 0, 0.1)

### Burbujas de Mensaje
- **Usuario:** Azul (#2563eb) con texto blanco
- **Bot:** Gris claro (#f3f4f6) con texto oscuro
- **Radio:** 16px (esquinas redondeadas)
- **Padding:** 12px 16px
- **Máximo ancho:** 80% del chat

### Botones
- **Primario:** Fondo azul (#2563eb), texto blanco
- **Secundario:** Fondo blanco, borde azul
- **Hover:** Oscurecer 10%
- **Radio:** 8px
- **Padding:** 12px 24px

### Input de Mensaje
- **Alto:** 48px
- **Borde:** 1px solid #d1d5db
- **Radio:** 24px (completamente redondeado)
- **Padding:** 12px 16px
- **Focus:** Borde azul (#2563eb)

## Iconos
- **Envío:** Icono de avión de papel
- **Adjuntar:** Icono de clip
- **Cerrar:** Icono de X
- **Mínizar:** Icono de guion

## Animaciones
- **Transición de hover:** 0.2s ease
- **Aparición de mensajes:** 0.3s ease
- **Apertura del chat:** 0.3s ease-out

## Responsive

### Móvil (< 640px)
- **Chat:** Ancho completo, alto completo
- **Posición:** Pantalla completa
- **Botón flotante:** Oculto (el chat se abre automáticamente)

### Tablet (640px - 1024px)
- **Chat:** 400px ancho, 600px alto
- **Posición:** Esquina inferior derecha

### Desktop (> 1024px)
- **Chat:** 350px ancho, 500px alto
- **Posición:** Esquina inferior derecha