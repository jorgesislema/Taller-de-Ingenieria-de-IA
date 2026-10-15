# Ejemplo de estructura para la práctica de Agentes y Skills

## Objetivo
Este ejemplo muestra la estructura básica que usarás en la práctica de la Clase 12.

## Estructura esperada

```text
mi-proyecto/
│
├── .venv/          # Entorno virtual (no versionar - .gignore)
├── .gignore        # Archivo para ignorar carpetas y archivos
├── example/        # Ejemplo o configuración inicial
│   └── agente-inicial.md
│
├── agents/
│   ├── agente-principal.md
│   └── skills/
│       ├── skill-1.md
│       └── skill-2.md
│
├── datos/
│   └── precios.md
│
└── pruebas/
    ├── caso-persona.md
    └── caso-empresa.md
```

## Pasos para comenzar

1. Clona o crea tu carpeta de trabajo
2. Ejecuta `python -m venv .venv` para crear el entorno virtual
3. Actívalo: `.venv\Scripts\activate` (Windows) o `source .venv/bin/activate` (Mac/Linux)
4. Copia los archivos de la práctica (agente, skills, datos)
5. Abre Google AI Studio en aistudio.google.com
6. Pega el agente y las skills
7. Prueba con los casos de práctica

## Recursos

- Google AI Studio: aistudio.google.com
- VS Code: code.visualstudio.com
- Documentación práctica: revisa la Clase 12 completa