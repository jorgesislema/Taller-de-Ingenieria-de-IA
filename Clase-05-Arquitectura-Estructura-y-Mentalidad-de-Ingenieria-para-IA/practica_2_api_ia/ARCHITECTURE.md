# Arquitectura del Proyecto

## Estructura de carpetas

```
practica_2_api_ia/
│
├── .vscode/                 # Configuracion de VS Code (se comparte)
│   └── settings.json        # Activa el .venv automaticamente
│
├── data/                    # (VACIA) Aqui irian datos de entrada si los hubiera
│
├── src/                     # (VACIA) Aqui iria el codigo fuente de un proyecto real
│
├── docs/                    # Documentacion
│   ├── guia_practica.md     # Guia paso a paso para alumnos
│   └── notas_seguridad.md   # Reglas de seguridad para llaves API
│
├── tests/                   # (VACIA) Aqui irian las pruebas unitarias
│
├── scripts/                 # Los scripts de esta practica
│   ├── script_google_gemini.py
│   ├── script_deepseek.py
│   ├── script_openrouter.py
│   ├── script_openai_gpt.py
│   └── script_claude.py
│
├── .env.example             # Plantilla de llaves (sin valores reales)
├── .gitignore               # Lista negra de archivos que NO suben a GitHub
├── requirements.txt         # Librerias necesarias
├── CONTEXT.md               # Quienes somos y que hacemos
├── RULES.md                 # Reglas de codigo y comportamiento
├── SECURITY.md              # Lineas rojas de seguridad
├── ARCHITECTURE.md          # Este archivo
└── README.md                # Resumen del proyecto
```

## Relacion entre carpetas

| Carpeta | Propiedad | Quien la lee |
|---------|-----------|--------------|
| `scripts/` | Codigo ejecutable | Python / Terminal |
| `docs/` | Documentacion para humanos | Humanos / IA |
| `.vscode/` | Configuracion del editor | VS Code |
| `data/` | Datos de entrada | Los scripts |
| `src/` | Codigo fuente principal | Python |
| `tests/` | Pruebas | Python |

## Flujo de datos

```
Terminal (humano) 
    ↓ escribe pregunta
Script (Python)
    ↓ envia a la API
Proveedor de IA (Google, DeepSeek, etc.)
    ↓ responde
Script (Python)
    ↓ muestra respuesta
Terminal (humano)
```

## Reglas de la arquitectura

1. **Los scripts NUNCA guardan llaves.** Las leen de `.env`.
2. **El archivo `.env` NUNCA se sube a GitHub.** Esta en `.gitignore`.
3. **Cada script es independiente.** No dependen entre si.
4. **Los archivos `.md` se comparten.** Son la documentacion del proyecto.
5. **La carpeta `.vscode/` se comparte.** Configura el entorno para todos.
