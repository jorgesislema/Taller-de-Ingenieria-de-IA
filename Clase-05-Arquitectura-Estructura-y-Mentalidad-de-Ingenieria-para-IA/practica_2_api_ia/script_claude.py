"""
============================================
SCRIPT DE EJEMPLO — Chat con Claude
============================================

Claude es la IA de Anthropic. Es conocida por ser
muy precisa y segura. Usa su propia libreria "anthropic".

Costos (aproximados):
- Claude 3 Haiku: $0.25 / millon de tokens (rapido y barato)
- Claude 3.5 Sonnet: $3 / millon de tokens (potente)

COMO OBTENER LA LLAVE:
1. Ve a https://console.anthropic.com
2. Crea una cuenta
3. Ve a "API Keys"
4. Crea una nueva llave
5. Pegala en .env como: ANTHROPIC_API_KEY=tu_llave
"""

import os
import sys

try:
    import anthropic
except ImportError:
    print("ERROR: No tienes instalada la libreria anthropic.")
    print("Ejecuta: pip install anthropic")
    sys.exit(1)

try:
    from dotenv import load_dotenv
except ImportError:
    print("ERROR: No tienes instalada python-dotenv.")
    print("Ejecuta: pip install python-dotenv")
    sys.exit(1)


# Cargar llaves
load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    print("=" * 60)
    print("ERROR: No se encontro la llave de Anthropic (Claude).")
    print("=" * 60)
    print()
    print("Pasos:")
    print("1. Ve a https://console.anthropic.com")
    print("2. Crea una cuenta")
    print("3. Ve a API Keys")
    print("4. Crea una nueva llave")
    print("5. Pegala en .env como: ANTHROPIC_API_KEY=tu_llave")
    print()
    sys.exit(1)


# Claude usa su propia libreria (NO es compatible con OpenAI)
cliente = anthropic.Anthropic(api_key=api_key)


def hacer_pregunta(pregunta, historial):
    """
    Envia una pregunta a Claude.
    
    NOTA: Claude usa un formato diferente a OpenAI.
    No usa "messages" como lista, sino que el historial
    se maneja de forma diferente.
    """
    
    # Agregamos la pregunta al historial
    historial.append({"role": "user", "content": pregunta})
    
    try:
        # Claude requiere que le digamos el "max_tokens" siempre
        respuesta = cliente.messages.create(
            model="claude-3-haiku-20240307",  # Modelo barato y rapido
            max_tokens=2000,
            messages=historial
        )
        
        # El texto esta en respuesta.content[0].text
        texto = respuesta.content[0].text
        
        # Agregamos la respuesta al historial
        historial.append({"role": "assistant", "content": texto})
        
        return texto
    
    except Exception as e:
        return f"Error: {e}"


def main():
    """Funcion principal."""
    
    print()
    print("=" * 60)
    print("  CHAT CON CLAUDE (Anthropic)")
    print("=" * 60)
    print()
    print("  Usa el modelo: Claude 3 Haiku (rapido y barato)")
    print("  Para salir, escribe 'salir'.")
    print()
    print("  NOTA: Cada pregunta cuesta dinero (~$0.0005 por pregunta)")
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
            print("  Claude esta pensando...")
            print()
            
            respuesta = hacer_pregunta(pregunta, historial)
            
            print("  Claude:")
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
