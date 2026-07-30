# Ejemplo: Programas Python

## ¿Qué es un Programa Python?

Scripts y herramientas en Python: automatizaciones, procesamiento de archivos, utilidades, APIs, análisis de datos. Python es el lenguaje más usado en IA y ciencia de datos.

## Estructura del Repositorio

```
mi_programa_python/
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
├── .env                           # Variables de entorno (NUNCA subir a GitHub)
├── .gitignore                     # Lista de archivos ignorados
├── requirements.txt               # Lista de dependencias
├── setup.py                       # Script de instalación
├── pyproject.toml                 # Configuración moderna de Python
│
├── src/
│   ├── __init__.py
│   ├── main.py                    # Punto de entrada del programa
│   ├── configuracion.py           # Carga variables de entorno
│   ├── modulos/
│   │   ├── __init__.py
│   │   ├── procesador.py          # Procesamiento principal
│   │   ├── utilidades.py          # Funciones auxiliares
│   │   └── validador.py           # Validación de entradas
│   └── modelos/
│       ├── __init__.py
│       ├── usuario.py             # Modelo de datos
│       └── producto.py            # Modelo de datos
│
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_procesador.py
│   ├── test_utilidades.py
│   └── fixtures/                  # Datos de prueba
│       ├── datos_entrada.json
│       └── datos_esperados.json
│
├── docs/
│   ├── guia_instalacion.md
│   ├── ejemplos_uso.md
│   ├── arquitectura.md
│   └── changelog.md
│
├── scripts/                       # Scripts de automatización
│   ├── ejecutar_analisis.sh
│   ├── generar_reporte.py
│   ├── deploy.sh
│   └── backup.sh
│
├── data/
│   ├── input/                     # Datos de entrada
│   ├── output/                    # Datos procesados
│   └── logs/                      # Archivos de registro
│       └── app.log
│
├── Dockerfile
├── docker-compose.yml
├── Makefile
└── README.md
```

## Archivos de Configuración para IA

### CODEX.md (Para Codex/OpenAI)
```markdown
Eres un desarrollador Python senior. Genera código limpio, seguro y mantenible.

REGLAS:
1. USA Python 3.8+ con type hints
2. Sigue PEP 8 (guía de estilo)
3. Escribe docstrings en todas las funciones públicas
4. USA virtual environments para dependencias
5. NUNCA guardes contraseñas en el código
6. SIEMPRE maneja excepciones específicas
7. USA logging en lugar de print()
8. Escribe pruebas unitarias para cada módulo
9. USA context managers para archivos y conexiones
10. Documenta el código en español
```

### CLAUDE.md (Para Claude)
```markdown
## Arquitectura del Proyecto
- **Patrón:** MVC (Model-View-Controller)
- **Dependencias:** Inyección de dependencias
- **Configuración:** Variables de entorno (.env)
- **Logging:** Python logging module
- **Testing:** pytest con fixtures

## Reglas de Código
1. **Funciones:** Máximo 20 líneas, una responsabilidad
2. **Clases:** Máximo 5 métodos públicos
3. **Archivos:** Máximo 300 líneas
4. **Imports:** Ordenados (stdlib → third-party → local)
5. **Nombres:** Descriptivos, snake_case, sin abreviaciones

## Seguridad
1. **Dependencias:** Usa pip-audit para escanear vulnerabilidades
2. **Entradas:** Valida y sanitiza todo input del usuario
3. **Salidas:** Escapa HTML para prevenir XSS
4. **Credenciales:** Usa vault o variables de entorno
5. **Logs:** Nunca loguees datos sensibles

## Testing
1. **Cobertura:** Mínimo 80% del código
2. **Unitarias:** Para cada función aislada
3. **Integración:** Para endpoints de API
4. **E2E:** Para flujos críticos del usuario
5. **Mocks:** Para servicios externos
```

## Ejemplo de Estructura de Código

### src/main.py
```python
"""
Punto de entrada del programa.
Este módulo coordina la ejecución principal.
"""

import logging
from configuracion import Configuracion
from modulos.procesador import Procesador
from modulos.utilidades import cargar_datos, guardar_resultados

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Función principal del programa."""
    try:
        # Cargar configuración
        config = Configuracion()
        logger.info("Configuración cargada correctamente")
        
        # Cargar datos de entrada
        datos = cargar_datos(config.ruta_entrada)
        logger.info(f"Cargados {len(datos)} registros")
        
        # Procesar datos
        procesador = Procesador(config)
        resultados = procesador.procesar(datos)
        logger.info(f"Procesados {len(resultados)} resultados")
        
        # Guardar resultados
        guardar_resultados(resultados, config.ruta_salida)
        logger.info("Resultados guardados correctamente")
        
    except Exception as e:
        logger.error(f"Error en la ejecución: {e}")
        raise

if __name__ == "__main__":
    main()
```

### src/configuracion.py
```python
"""
Módulo de configuración.
Carga variables de entorno y configura el programa.
"""

import os
from dataclasses import dataclass
from dotenv import load_dotenv

@dataclass
class Configuracion:
    """Clase que almacena la configuración del programa."""
    
    ruta_entrada: str
    ruta_salida: str
    api_key: str
    modo_debug: bool = False
    
    def __init__(self):
        """Inicializa la configuración desde variables de entorno."""
        load_dotenv()
        
        self.ruta_entrada = os.getenv("RUTA_ENTRADA", "data/input/")
        self.ruta_salida = os.getenv("RUTA_SALIDA", "data/output/")
        self.api_key = os.getenv("API_KEY", "")
        self.modo_debug = os.getenv("MODO_DEBUG", "False").lower() == "true"
        
        if not self.api_key:
            raise ValueError("API_KEY no está configurada en .env")
```

## Ejemplo de Uso

```bash
# Instalación
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
pip install -r requirements.txt

# Ejecución
python src/main.py

# Testing
pytest tests/ -v

# Linting
flake8 src/
mypy src/
```

## .gitignore para Python

```gitignore
# Byte-compiled / optimized
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
.env
.venv/
venv/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Testing
.coverage
htmlcov/
.pytest_cache/

# MyPy
.mypy_cache/

# Logs
*.log
```

## Nota para el Instructor

Python es el lenguaje perfecto para empezar porque:
1. **Sintaxis simple:** Se parece al pseudocódigo
2. **Comunidad gigantesca:** Miles de tutoriales y librerías
3. **Versátil:** Sirve para web, IA, automatización, análisis
4. **Demandado:** Es el #1 en ofertas de trabajo de IA

Enseñar buenas prácticas desde el principio evita malos hábitos difíciles de corregir después.