from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from dotenv import set_key
from chatbot import responder_chatbot, ejecutar_comando_directo

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def get_login():
    with open("static/login.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/guardar_nombre")
async def guardar_nombre(request: Request):
    data = await request.json()
    nombre = data.get("username", "")
    if nombre:
        set_key(".env", "USERNAME", nombre)
    return {"ok": True}

@app.get("/terminal", response_class=HTMLResponse)
def get_terminal():
    with open("static/terminal.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/mensaje")
async def procesar_mensaje(request: Request):
    data = await request.json()
    mensaje = data.get("mensaje", "")
    
    if mensaje.strip().lower().startswith("cmd "):
        comando = mensaje[4:]
        print(comando)
        salida = ejecutar_comando_directo(comando)
        return {"respuesta": salida}
    else:
        respuesta = responder_chatbot(mensaje)
        return {"respuesta": respuesta}
