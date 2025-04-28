# 🤖 Chatbot Web con FastAPI

## 🧠 Descripción

Este proyecto implementa un chatbot web interactivo usando **Python**, **FastAPI** y **HTML/CSS/JavaScript**. El chatbot puede responder a preguntas predefinidas, personalizar respuestas mediante variables de entorno, registrar las conversaciones (opcional) y ejecutar comandos del sistema desde la interfaz web.

## 🎯 Objetivos

- Permitir interacción con el chatbot desde una interfaz web tipo terminal.
- Personalizar respuestas mediante variables de entorno.
- Ejecutar comandos del sistema al escribir instrucciones específicas (`cmd`).
- (Opcional) Registrar todas las interacciones usando `logging`.

## ⚙️ Tecnologías Utilizadas

- Python 3.x
- FastAPI
- Uvicorn (servidor ASGI)
- HTML + CSS + JS
- `os`, `sys`, `subprocess`, `logging`
- Docker

## 📦 Instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/yhilmarchaverra/PythonTaller.git
cd Chatbot
```

### 2. Crea un entorno virtual

#### 🔹 En Windows:

```bash
python -m venv venv #Crea una carpeta llamada venv.
venv\Scripts\activate #"Activa" el entorno virtual.
```

#### 🔸 En Linux/macOS:

```bash
python3 -m venv venv #Crea una carpeta llamada venv.
source venv/bin/activate #"Activa" el entorno virtual.
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

## 🚀 Ejecución

### Ejecuta el servidor FastAPI con Uvicorn:

```bash
uvicorn api:app --reload
```

Esto abrirá el servidor en `http://127.0.0.1:8000`.

Abre tu navegador y accede a esa URL para comenzar a interactuar con el chatbot.

## 💬 Uso

- Escribe un mensaje en la interfaz web.
- Para ejecutar un comando del sistema, inicia el mensaje con `cmd`.  
  Ejemplos:  
  - `cmd dir` (en Windows)  
  - `cmd ls -la` (en Linux/macOS)
- Para **cerrar el servidor**, puedes escribir `salir` o `adios` en el chat.

## 📝 Registro de Interacciones (Opcional)

Si se activa, el chatbot puede guardar todas las conversaciones en un archivo `chat.log`.  
Esto es útil para auditoría o depuración.

## 📁 Estructura del Proyecto

```
├── api.py                 # Backend con FastAPI
├── chatbot.py             # Lógica del chatbot y ejecución de comandos
├── requirements.txt       # Dependencias del proyecto
└── static/
    ├── terminal.html      # Interfaz del chatbot
    └── styles.css         # Estilos personalizados
```
# Dockerizar la aplicación
## Login en Dockerhub
## Crear imagen
Para crear una imagen utilizamos la opción build de Docker con la bandera "-t" luego el nombre que le queremos poner a la imagen antes de los dos puntos, que en este caso seria chatboot y despues de los  " : " la versión de nuestra imagen que por defecto dejaremos latest finalizada por un " . " que indica el directorio actual donde se construira la imagen.
```bash
docker build -t chatboot:latest .
```
 Después de construirla, si quieres subirla (por ejemplo a DockerHub o a un ECR privado), debes:

 Etiquetarla hacia el repo de destino:
```bash
 docker tag chatboot:latest usuario-dockerhub/chatboot:latest
```
