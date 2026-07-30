# Ejemplo: Páginas Web con IA

## ¿Qué es una Página Web con IA?

Una página web que integra inteligencia artificial: chatbots en el sitio, recomendaciones personalizadas, generación de contenido, análisis de comportamiento del usuario.

## Estructura del Repositorio

```
mi_pagina_web_ia/
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
│
├── DESIGN.md                      # NUEVO: Guía de diseño visual (colores, fuentes, estilos)
│
├── public/                        # Archivos estáticos (CSS, JS, imágenes)
│   ├── index.html
│   ├── css/
│   │   ├── estilos.css
│   │   └── responsive.css
│   ├── js/
│   │   ├── chat_widget.js         # Widget del chatbot
│   │   ├── recomendaciones.js     # Sistema de recomendaciones
│   │   └── analytics.js           # Análisis de comportamiento
│   └── img/
│       ├── logo.png
│       └── avatares/
│
├── src/
│   ├── servidor.py                # Servidor principal
│   ├── api/
│   │   ├── __init__.py
│   │   ├── chat.py                # Endpoint del chatbot
│   │   ├── recomendaciones.py     # Endpoint de recomendaciones
│   │   └── usuarios.py            # Gestión de usuarios
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── chatbot.py             # Lógica del chatbot
│   │   ├── recomendador.py        # Sistema de recomendaciones
│   │   └── analizador.py          # Análisis de comportamiento
│   └── utilidades/
│       ├── __init__.py
│       ├── validador.py           # Validación de entradas
│       └── logger.py              # Registro de actividad
│
├── data/
│   ├── productos.json             # Catálogo de productos
│   ├── preguntas_frecuentes.json  # FAQ para el chatbot
│   └── usuarios_ejemplo.json      # Datos de prueba
│
├── tests/
│   ├── test_api.py
│   ├── test_chatbot.py
│   └── test_recomendaciones.py
│
├── .gitignore
├── .env
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Archivos de Configuración para IA

### CODEX.md (Para Codex/OpenAI)
```markdown
Eres un desarrollador web especializado en integrar IA en páginas web.

REGLAS:
1. Usa HTML5, CSS3 y JavaScript moderno (ES6+)
2. El backend siempre es Python (Flask o FastAPI)
3. NUNCA expongas API keys en el frontend
4. SIEMPRE valida las entradas del usuario
5. Implementa CSRF protection en todos los formularios
6. Usa HTTPS para todas las comunicaciones
7. Optimiza para móviles (responsive design)
```

### CLAUDE.md (Para Claude)
```markdown
## Identidad del Proyecto
Creamos páginas web inteligentes que integran IA para mejorar la experiencia del usuario.

## Tecnologías
- **Frontend:** HTML5, CSS3, JavaScript (ES6+)
- **Backend:** Python 3.8+ con FastAPI
- **IA:** APIs de OpenAI, Claude, modelos open source
- **Base de Datos:** SQLite (desarrollo), PostgreSQL (producción)
- **Despliegue:** Docker + Nginx

## Reglas de Diseño
1. **Responsive:** La página debe funcionar en móvil, tablet y desktop
2. **Accesible:** Cumple con WCAG 2.1 nivel AA
3. **Rápida:** Carga máxima de 3 segundos
4. **Segura:** HTTPS, CSP headers, sanitización de entradas

## Reglas de Código
1. **Frontend:** Modulariza el JavaScript en archivos separados
2. **Backend:** Usa arquitectura de capas (API → Lógica → Datos)
3. **IA:** Implementa fallback si la API de IA falla
4. **Logs:** Registra todos los errores y eventos importantes
```

### DESIGN.md (Nuevo: Guía de Diseño)
```markdown
# Guía de Diseño Visual

## Paleta de Colores
- **Primario:** #2563eb (azul)
- **Secundario:** #10b981 (verde)
- **Acento:** #f59e0b (amarillo)
- **Texto:** #1f2937 (gris oscuro)
- **Fondo:** #ffffff (blanco)
- **Error:** #ef4444 (rojo)

## Tipografía
- **Títulos:** Inter, Bold, 24-32px
- **Cuerpo:** Inter, Regular, 16px
- **Código:** Fira Code, 14px

## Espaciado
- **Margen externo:** 16px
- **Padding interno:** 24px
- **Espacio entre elementos:** 12px

## Bordes y Sombras
- **Bordes:** 8px de radio
- **Sombras:** 0 4px 6px rgba(0, 0, 0, 0.1)

## Componentes del Chatbot
- **Ventana del chat:** 350px ancho, 500px alto
- **Burbujas de usuario:** Azul (#2563eb)
- **Burbujas del bot:** Gris claro (#f3f4f6)
- **Botón de envío:** Verde (#10b981)
```

## Ejemplo de Uso

```
Usuario abre la página web →
1. Se carga el HTML, CSS y JavaScript
2. Se inicializa el widget del chatbot (chat_widget.js)
3. El usuario escribe un mensaje
4. chat_widget.js envía el mensaje a api/chat.py
5. api/chat.py procesa con chatbot.py
6. La respuesta se muestra en la ventana del chat
7. Se registra la conversación en logs/
```

## Nota para el Instructor

Las páginas web con IA son el tipo de proyecto más visible para los alumnos. Es importante enseñar:

1. **Separación de responsabilidades:** Frontend ≠ Backend ≠ IA
2. **Seguridad:** Nunca exponer API keys en el navegador
3. **Experiencia de usuario:** El chatbot debe ser fácil de usar
4. **Rendimiento:** Las respuestas de IA pueden ser lentas, usar loading states
5. **Fallback:** Si la IA falla, mostrar un mensaje amigable