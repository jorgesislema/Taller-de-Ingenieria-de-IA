"""
============================================
SCRIPT DE EJEMPLO — Chat con OpenAI GPT
============================================

OpenAI es la empresa que creo ChatGPT.
Su API es la mas conocida pero tambien la mas cara.

Costos (aproximados):
- GPT-4o-mini: $0.15 / millon de tokens (barato)
- GPT-4o: $2.50 / millon de tokens (potente)

COMO OBTENER LA LLAVE:
1. Ve a https://platform.openai.com/api-keys
2. Crea una cuenta
3. Agrega credito de pago (minimo $5)
4. Crea una API key
5. Pegala en .env como: OPENAI_API_KEY=tu_llave
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

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("=" * 60)
    print("ERROR: No se encontro la llave de OpenAI.")
    print("=" * 60)
    print()
    print("Pasos:")
    print("1. Ve a https://platform.openai.com/api-keys")
    print("2. Crea una cuenta")
    print("3. Agrega credito (minimo $5 USD)")
    print("4. Crea una API key")
    print("5. Pegala en .env como: OPENAI_API_KEY=tu_llave")
    print()
    print("NOTA: OpenAI NO tiene modelo gratuito.")
    print()
    sys.exit(1)


# OpenAI es el cliente por defecto (no necesita URL base)
cliente = OpenAI(api_key=api_key)


def hacer_pregunta(pregunta, historial):
    """Envia una pregunta a GPT y devuelve la respuesta."""
    
    historial.append({"role": "user", "content": pregunta})
    
    try:
        respuesta = cliente.chat.completions.create(
            model="gpt-4o-mini",  # Modelo barato. Cambia a "gpt-4o" para mas potencia
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
    print("  CHAT CON OPENAI GPT (ChatGPT)")
    print("=" * 60)
    print()
    print("  Usa el modelo: gpt-4o-mini (barato)")
    print("  Para salir, escribe 'salir'.")
    print()
    print("  NOTA: Cada pregunta cuesta dinero (~$0.001 por pregunta)")
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
            print("  GPT esta pensando...")
            print()
            
            respuesta = hacer_pregunta(pregunta, historial)
            
            print("  GPT:")
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
