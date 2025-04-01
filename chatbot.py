# Recibir mensajes desde la terminal y permitir la interacción con el usuario.
# Responder con frases predefinidas según la entrada del usuario.
# Personalizar respuestas leyendo variables de entorno.
# Registrar todas las interacciones en un archivo de logs usando logging - OPCIONAL 
# Permitir la ejecución de comandos del sistema si el usuario lo solicita. 

import os
import logging
import subprocess

# Configuración de logs
logging.basicConfig(
    filename="logs_chatbot.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    encoding="utf-8"
)

# Obtener el nombre del usuario desde variables de entorno
USER_NAME = os.environ.get("USER_NAME", "Usuario")

# Respuestas predefinidas
RESPUESTAS = {
    "hola": f"Hola {USER_NAME}! ¿En qué puedo ayudarte?",
    "adios": "Hasta luego, que tengas un buen día!",
    "comando": "Dime qué comando del sistema quieres ejecutar:"
}

def ejecutar_comando():
    while True:
        comando = input(f"{RESPUESTAS['comando']} -> ").strip()
        if comando == "salir":
            print("Saliendo del modo de comandos. ")
            break
        result = subprocess.run(["cmd", "/c", comando], capture_output=True, text=True)
        print(result.stdout if result.stdout else f"Comando '{comando}' ejecutado sin salida.")
        logging.info(f"Comando ejecutado: {comando}")
        logging.info(f"Salida del comando: {result.stdout}")

def chatbot():
    print("Bienvenido al chatbot! Escribe 'salir' para terminar.")
    
    while True:
        try:
            entrada = input("-> ").strip().lower()
            logging.info(f"Usuario: {entrada}")

            if entrada in ["salir", "adios"]:
                print(RESPUESTAS["adios"])
                break
            elif entrada == "comando":
                ejecutar_comando()
            else:
                respuesta = RESPUESTAS.get(entrada, "No entiendo esa orden.")

            if (entrada != "comando"):
                logging.info(f"Chatbot: {respuesta}")
                print(respuesta)
        except KeyboardInterrupt:
            print("\n", RESPUESTAS["adios"])
            break

if __name__ == "__main__":
    chatbot()
