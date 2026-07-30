"""
============================================
SCRIPT DE EJEMPLO — Chat con DeepSeek
============================================

DeepSeek es una IA china muy potente y MUY BARATA.
Costo: ~$0.14 por millon de tokens (mas barato que GPT).

Este script usa la API de DeepSeek, que es compatible
con la libreria de OpenAI (por eso importamos "openai").

COMO OBTENER LA LLAVE:
1. Ve a https://platform.deepseek.com
2. Crea una cuenta
3. Ve a "API Keys" y crea una nueva
4. Copia la llave y pegala en tu archivo .env
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


# Cargar llaves desde .env
load_dotenv()

# DeepSeek usa la misma estructura que OpenAI
# pero con una URL diferente ("base_url")
api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    print("=" * 60)
    print("ERROR: No se encontro la llave de DeepSeek.")
    print("=" * 60)
    print()
    print("Pasos:")
    print("1. Ve a https://platform.deepseek.com")
    print("2. Crea una cuenta (es gratis)")
    print("3. Ve a API Keys y crea una nueva")
    print("4. Pegala en .env como: DEEPSEEK_API_KEY=tu_llave")
    print()
    sys.exit(1)


# Crear el cliente conectado a DeepSeek
# La URL base apunta a los servidores de DeepSeek
cliente = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com/v1"  # URL de DeepSeek
)


def hacer_pregunta(pregunta, historial):
    """
    Envia una pregunta a DeepSeek y devuelve la respuesta.
    
    DeepSeek usa el mismo formato que OpenAI:
    - Un lista de "mensajes" con rol ("user" o "assistant")
    - "user" = pregunta del humano
    - "assistant" = respuesta de la IA
    """
    
    # Agregamos la pregunta al historial
    historial.append({"role": "user", "content": pregunta})
    
    try:
        # Llamamos a la API de DeepSeek
        respuesta = cliente.chat.completions.create(
            model="deepseek-chat",          # Nombre del modelo
            messages=historial,              # Todo el historial
            max_tokens=2000,                 # Maximo de texto generado
            temperature=0.7                  # Creatividad (0.0 = robot, 1.0 = loco)
        )
        
        # Extraemos el texto de la respuesta
        texto = respuesta.choices[0].message.content
        
        # Agregamos la respuesta al historial
        historial.append({"role": "assistant", "content": texto})
        
        return texto
    
    except Exception as e:
        return f"Error al conectar con DeepSeek: {e}"


def main():
    """Funcion principal del chat."""
    
    print()
    print("=" * 60)
    print("  CHAT CON DEEPSEEK (IA china — muy barata)")
    print("=" * 60)
    print()
    print("  Escribe tu pregunta y presiona Enter.")
    print("  Para salir, escribe 'salir'.")
    print()
    print("-" * 60)
    print()
    
    # El historial empieza vacio
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
            print("  DeepSeek esta pensando...")
            print()
            
            respuesta = hacer_pregunta(pregunta, historial)
            
            print("  DeepSeek:")
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
