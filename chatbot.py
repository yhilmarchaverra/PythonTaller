# Recibir mensajes desde la terminal y permitir la interacción con el usuario.
# Responder con frases predefinidas según la entrada del usuario.
# Personalizar respuestas leyendo variables de entorno.
# Registrar todas las interacciones en un archivo de logs usando logging - OPCIONAL 
# Permitir la ejecución de comandos del sistema si el usuario lo solicita. 


import os
import logging
import subprocess

def load_environment_variables():
    return {
        "USER_NAME":os.getenv("USER_NAME", "Usuario")
    }

def setup_logging():
    logging.basicConfig(
        filename="logs_chatbot.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def execute_command(command):
    try: 
        result = subprocess.run(
            ["cmd","/c", command],
            capture_output=True,
            text=True
        )
        return result.stdout if result.stdout else "Comando {command} ejecutado sin salida"
    
    except Exception as e:
        return f"Error ejecutando el comando '{command}' {e}"


def chatbot():
    setup_logging()
    env_vars = load_environment_variables()

    predefined_response = {
        "hola": f"Hola {env_vars["USER_NAME"]}! ¿En qué puedo ayudarte? ",
        "adios": "Hasta luego, que tengas un buen día! ",
        "comando": "Dime qué comando del sistema quieres ejecutar:"
    }

    while True:
        user_input = input("Chatbot iniciado. Escribe 'salir' para terminar. ").strip().lower()
        logging.info(f"Usuario: {user_input}")
        if user_input == "salir":
            break
        elif user_input == "comando":
            command = input("Escribe el comando que deseas ejecutar: ")
            response = execute_command(command)
        else:
            response = predefined_response.get(user_input, "No entiendo esa orden. ")
        
        logging.info(f"Chatbot: {response}")
        print(response)

chatbot()