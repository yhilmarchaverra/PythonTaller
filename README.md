# Chatbot en Python

## Descripción
Este proyecto consiste en la creación de un chatbot en Python que interactúa con el usuario desde la terminal. El chatbot puede responder con frases predefinidas, personalizar respuestas según variables de entorno, registrar interacciones en un archivo de logs y ejecutar comandos del sistema cuando el usuario lo solicite.

## Objetivos
- Recibir mensajes desde la terminal y permitir la interacción con el usuario.
- Responder con frases predefinidas según la entrada del usuario.
- Personalizar respuestas leyendo variables de entorno.
- **(Opcional)** Registrar todas las interacciones en un archivo de logs usando `logging`.
- Permitir la ejecución de comandos del sistema si el usuario lo solicita.

## Requisitos Técnicos
Para completar este reto, se deben utilizar las siguientes librerías de Python:

- `os` y `sys`: Para interactuar con el sistema operativo.
- `subprocess`: Para ejecutar comandos del sistema.
- `logging`: Para registrar mensajes en un archivo de log.

## Lo que Aprenderás
- Usar las librerías `os` y `sys` para manejar el sistema operativo.
- Ejecutar comandos del sistema con `subprocess`.
- Leer variables de entorno con `os.getenv()`.
- Registrar eventos en un archivo de logs con `logging`.
- Construir un chatbot funcional en Python que interactúe en la terminal.

## Instalación y Uso
### Requisitos Previos
- Tener instalado Python 3.x en el sistema.

### Instalación
1. Clona este repositorio o descarga los archivos del proyecto.
2. Asegúrate de que tienes Python instalado en tu sistema.

### Ejecución
Para ejecutar el chatbot, abre una terminal y corre el siguiente comando:
```sh
python chatbot.py
```

### Uso
- Escribe un mensaje y presiona `Enter` para interactuar con el chatbot.
- Usa comandos predefinidos para recibir respuestas específicas.
- Introduce comandos del sistema (si está habilitado) para ejecutarlos directamente desde el chatbot.

## Registro de Interacciones (Opcional)
Si se habilita el registro de interacciones, el chatbot almacenará todas las conversaciones en un archivo de log. Esto es útil para auditoría y depuración.

