import os
import logging
import subprocess
import platform

# Configurar logs
logging.basicConfig(
    filename="logs_chatbot.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    encoding="utf-8"
)

USER_NAME = os.environ.get("USER_NAME", "Usuario")

RESPUESTAS = {
    "hola": f"Hola {USER_NAME}! ¿En qué puedo ayudarte?",
    "adios": "Hasta luego, que tengas un buen día!",
    "comando": "Dime qué comando del sistema quieres ejecutar:"
}

def responder_chatbot(mensaje: str):
    mensaje = mensaje.strip().lower()
    logging.info(f"Usuario: {mensaje}")

    if mensaje in ["salir", "adios"]:
        respuesta = RESPUESTAS["adios"]
    elif mensaje == "hola":
        respuesta = RESPUESTAS["hola"]
    elif mensaje == "comando":
        respuesta = RESPUESTAS["comando"]
    else:
        respuesta = RESPUESTAS.get(mensaje, "No entiendo esa orden.")

    logging.info(f"Chatbot: {respuesta}")
    return respuesta

def ejecutar_comando_directo(comando: str):
    try:
        sistema = platform.system()
        if sistema == "Windows":
            result = subprocess.run(["cmd", "/c", comando], capture_output=True, text=True)
        else:
            result = subprocess.run(comando, shell=True, capture_output=True, text=True)

        salida = result.stdout if result.stdout else "Comando ejecutado sin salida."
        logging.info(f"Comando ejecutado: {comando}")
        logging.info(f"Salida del comando: {salida}")
        return salida
    except Exception as e:
        return f"Error ejecutando el comando: {str(e)}"

