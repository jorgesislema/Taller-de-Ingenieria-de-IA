"""
============================================
SCRIPT PRINCIPAL - Chat con Google Gemini
============================================

Este script te permite hacer preguntas a la IA de Google (Gemini)
directamente desde la terminal de tu computadora.

REQUISITOS:
1. Tener Python 3.10 o superior instalado
2. Haber creado un entorno virtual (.venv)
3. Haber instalado las dependencias: pip install -r requirements.txt
4. Tener una llave de API de Google (GRATIS)

COMO OBTENER LA LLAVE GRATIS:
1. Ve a https://aistudio.google.com/apikey
2. Inicia sesion con tu cuenta de Google (Gmail)
3. Haz clic en "Create API Key"
4. Copia la llave y pegala en tu archivo .env

COMO EJECUTAR:
1. Abre la terminal
2. Entra a la carpeta de esta practica
3. Activa el entorno virtual: .venv\\Scripts\\activate (Windows)
                                  source .venv/bin/activate (Mac/Linux)
4. Ejecuta: python script_google_gemini.py
5. Escribe tu pregunta y presiona Enter
6. Para salir, escribe "salir" o "exit"
"""

# ============================================
# IMPORTACIONES
# ============================================
# os: Para leer variables de entorno (nuestras llaves)
import os

# sys: Para cerrar el programa limpiamente
import sys

# google.generativeai: La libreria de Google para usar Gemini
# Si no la tienes instalada, ejecuta: pip install google-generativeai
try:
    import google.generativeai as genai
except ImportError:
    print("ERROR: No tienes instalada la libreria de Google Gemini.")
    print("Ejecuta: pip install google-generativeai")
    sys.exit(1)

# dotenv: Para cargar las variables desde el archivo .env
# Si no la tienes instalada, ejecuta: pip install python-dotenv
try:
    from dotenv import load_dotenv
except ImportError:
    print("ERROR: No tienes instalada la libreria python-dotenv.")
    print("Ejecuta: pip install python-dotenv")
    sys.exit(1)


# ============================================
# PASO 1: Cargar la llave de API desde .env
# ============================================

# load_dotenv() busca el archivo .env en la misma carpeta que este script
# Esto asegura que funcione sin importar desde donde lo ejecutes
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

# Ahora podemos leer la llave con os.getenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Verificamos que la llave exista
if not api_key:
    print("=" * 60)
    print("ERROR: No se encontro la llave de API de Google.")
    print("=" * 60)
    print()
    print("PASOS PARA ARREGLARLO:")
    print("1. Abre el archivo .env en esta carpeta")
    print("2. Busca la linea: GOOGLE_API_KEY=tu_llave_de_google_aqui")
    print("3. Reemplaza 'tu_llave_de_google_aqui' con tu llave real")
    print("4. Guarda el archivo")
    print("5. Vuelve a ejecutar este script")
    print()
    print("¿No tienes llave? Obtene una GRATIS aqui:")
    print("https://aistudio.google.com/apikey")
    print()
    sys.exit(1)


# ============================================
# PASO 2: Configurar la conexion con Gemini
# ============================================

# Le decimos a la libreria que use nuestra llave
genai.configure(api_key=api_key)

# Seleccionamos el modelo de IA que vamos a usar
# "gemini-flash-latest" es el modelo que funciona con tu llave
# Si en el futuro quieres otro modelo, busca en:
# https://ai.google.dev/gemini-api/docs/models/gemini
model = genai.GenerativeModel("gemini-flash-latest")


# ============================================
# PASO 3: Crear el historial de conversacion
# ============================================

# Un historial permite que la IA recuerde lo que le preguntamos antes
# Sin esto, cada pregunta seria como hablar con alguien que tiene amnesia
chat = model.start_chat(history=[])


# ============================================
# PASO 4: El bucle principal (el chat)
# ============================================

def mostrar_bienvenida():
    """Muestra el mensaje de bienvenida del chat."""
    print()
    print("=" * 60)
    print("  CHAT CON GOOGLE GEMINI (IA de Google)")
    print("=" * 60)
    print()
    print("  Escribe tu pregunta y presiona Enter.")
    print("  Para salir, escribe 'salir' o 'exit'.")
    print("  Para borrar el historial, escribe 'limpiar'.")
    print()
    print("-" * 60)
    print()


def hacer_pregunta(pregunta):
    """
    Envia una pregunta a Gemini y devuelve la respuesta.
    
    Args:
        pregunta (str): La pregunta que le hacemos a la IA
        
    Returns:
        str: La respuesta de la IA
    """
    try:
        # send_message() envia la pregunta y espera la respuesta
        respuesta = chat.send_message(pregunta)
        # El texto de la respuesta esta en respuesta.text
        return respuesta.text
    except Exception as e:
        return f"Error al conectar con Gemini: {e}"


def main():
    """Funcion principal que ejecuta el chat."""
    
    # Mostramos la bienvenida
    mostrar_bienvenida()
    
    # Bucle infinito (solo se detiene con "salir")
    while True:
        try:
            # Pedimos al usuario que escriba su pregunta
            pregunta = input("Tu pregunta: ").strip()
            
            # Si esta vacia, ignoramos
            if not pregunta:
                continue
            
            # Si escribe "salir", terminamos
            if pregunta.lower() in ["salir", "exit", "quit", "q"]:
                print()
                print("¡Hasta luego! Gracias por usar Gemini.")
                print()
                break
            
            # Si escribe "limpiar", borramos el historial
            if pregunta.lower() in ["limpiar", "clear", "reset"]:
                chat.history.clear()
                print("  [Historial borrado. La IA ya no recuerda preguntas anteriores.]")
                print()
                continue
            
            # Mostramos que estamos procesando
            print()
            print("  Pensando...")
            print()
            
            # Hacemos la pregunta a la IA
            respuesta = hacer_pregunta(pregunta)
            
            # Mostramos la respuesta
            print("  Gemini:")
            print("-" * 40)
            print(respuesta)
            print("-" * 40)
            print()
        
        # Si el usuario presiona Ctrl+C, cerramos limpiamente
        except KeyboardInterrupt:
            print()
            print("  [Programa interrumpido por el usuario]")
            print("  ¡Hasta luego!")
            print()
            break


# ============================================
# PASO 5: Ejecutar el script
# ============================================

# Este codigo solo se ejecuta si corres este archivo directamente
# (no si lo importas desde otro archivo)
if __name__ == "__main__":
    main()
