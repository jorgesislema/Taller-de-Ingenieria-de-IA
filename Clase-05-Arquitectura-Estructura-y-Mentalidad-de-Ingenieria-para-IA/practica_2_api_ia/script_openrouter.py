"""
============================================
SCRIPT DE EJEMPLO — Chat con OpenRouter
============================================

OpenRouter es un "agregador" de IAs. Con UNA sola llave,
puedes acceder a multiples modelos:
- GPT-4o (OpenAI)
- Claude (Anthropic)
- Llama (Meta)
- Gemini (Google)
- Y muchos mas...

Algunos modelos tienen opciones GRATUITAS.

COMO OBTENER LA LLAVE:
1. Ve a https://openrouter.ai
2. Crea una cuenta
3. Ve a "Keys" y crea una nueva
4. Pegala en .env como: OPENROUTER_API_KEY=tu_llave
"""

import os
import sys

try:
    from openai import OpenAI
except ImportError:
    print("ERROR: No tienes instalada la libreria openai.")
    print("Ejecuta: pip install openai")
    sys.exit(1)

try:
    from dotenv import load_dotenv
except ImportError:
    print("ERROR: No tienes instalada python-dotenv.")
    print("Ejecuta: pip install python-dotenv")
    sys.exit(1)


# Cargar llaves
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    print("=" * 60)
    print("ERROR: No se encontro la llave de OpenRouter.")
    print("=" * 60)
    print()
    print("Pasos:")
    print("1. Ve a https://openrouter.ai")
    print("2. Crea una cuenta")
    print("3. Ve a Keys y crea una nueva")
    print("4. Pegala en .env como: OPENROUTER_API_KEY=tu_llave")
    print()
    sys.exit(1)


# OpenRouter tambien es compatible con la libreria de OpenAI
# pero con una URL base diferente
cliente = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)


# Modelos disponibles en OpenRouter
# Puedes cambiar "model" por cualquiera de estos:
MODELOS_DISPONIBLES = {
    "1": "google/gemini-2.0-flash-001",           # Gratis
    "2": "deepseek/deepseek-chat",                 # Muy barato
    "3": "meta-llama/llama-3.1-8b-instruct:free", # Gratis
    "4": "openai/gpt-4o-mini",                     # Barato
    "5": "anthropic/claude-3-haiku",               # Rapido
}


def hacer_pregunta(pregunta, historial, modelo):
    """Envia una pregunta al modelo seleccionado."""
    
    historial.append({"role": "user", "content": pregunta})
    
    try:
        respuesta = cliente.chat.completions.create(
            model=modelo,
            messages=historial,
            max_tokens=2000,
            temperature=0.7
        )
        
        texto = respuesta.choices[0].message.content
        historial.append({"role": "assistant", "content": texto})
        
        return texto
    
    except Exception as e:
        return f"Error: {e}"


def main():
    """Funcion principal."""
    
    print()
    print("=" * 60)
    print("  CHAT CON OPENROUTER (Multiples IAs)")
    print("=" * 60)
    print()
    print("  Modelos disponibles:")
    for clave, modelo in MODELOS_DISPONIBLES.items():
        etiqueta = "(GRATIS)" if "free" in modelo or "gemini" in modelo else ""
        print(f"    {clave}. {modelo} {etiqueta}")
    print()
    
    opcion = input("  Elige un modelo (1-5, o Enter para 1): ").strip()
    if opcion not in MODELOS_DISPONIBLES:
        opcion = "1"
    
    modelo_elegido = MODELOS_DISPONIBLES[opcion]
    print(f"  Usando modelo: {modelo_elegido}")
    print()
    print("  Para salir, escribe 'salir'.")
    print("-" * 60)
    print()
    
    historial = []
    
    while True:
        try:
            pregunta = input("Tu pregunta: ").strip()
            
            if not pregunta:
                continue
            
            if pregunta.lower() in ["salir", "exit", "quit"]:
                print()
                print("¡Hasta luego!")
                print()
                break
            
            print()
            print("  Pensando...")
            print()
            
            respuesta = hacer_pregunta(pregunta, historial, modelo_elegido)
            
            print("  Respuesta:")
            print("-" * 40)
            print(respuesta)
            print("-" * 40)
            print()
        
        except KeyboardInterrupt:
            print()
            print("  ¡Hasta luego!")
            print()
            break


if __name__ == "__main__":
    main()
