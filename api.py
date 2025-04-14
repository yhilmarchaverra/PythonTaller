from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from chatbot import responder_chatbot, ejecutar_comando_directo

app = FastAPI()

# Montar archivos estáticos (HTML)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def get_terminal():
    with open("static/terminal.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/mensaje")
async def procesar_mensaje(request: Request):
    data = await request.json()
    mensaje = data.get("mensaje", "")
    
    if mensaje.strip().lower().startswith("cmd "):
        comando = mensaje[4:]
        salida = ejecutar_comando_directo(comando)
        return {"respuesta": salida}
    else:
        respuesta = responder_chatbot(mensaje)
        return {"respuesta": respuesta}
