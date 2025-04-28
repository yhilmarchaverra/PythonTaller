import os
import json
import logging
import subprocess
import platform
from dotenv import load_dotenv

# Configurar logs
logging.basicConfig(
    filename="logs_chatbot.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    encoding="utf-8"
)

def read_name():
    # Cargar variables de entorno desde .env si existe
    load_dotenv()
    return os.environ.get("USERNAME", "Usuario")

def cargar_respuestas():
    try:
        ruta = os.path.join("static", "database.json")
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Error cargando respuestas: {e}")
        return {}

def responder_chatbot(mensaje: str):
    mensaje = mensaje.strip().lower()
    respuestas = cargar_respuestas()
    username = read_name()
    
    logging.info(f"Usuario: {mensaje}")
    
    if mensaje in ["salir", "adios"]:
        plantilla = respuestas.get("adios", "Hasta luego.")
    elif mensaje == "hola":
        plantilla = respuestas.get("hola", "Hola.")
    elif mensaje == "comando":
        plantilla = respuestas.get("comando", "Escribe un comando.")
    else:
        plantilla = respuestas.get(mensaje, "No entiendo esa orden.")
    
    # Insertar el nombre del usuario si está en la plantilla
    respuesta = plantilla.format(USERNAME=username)
    
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
        logging.error(f"Error ejecutando el comando: {str(e)}")
        return f"Error ejecutando el comando: {str(e)}"
