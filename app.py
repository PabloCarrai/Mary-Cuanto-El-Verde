import asyncio
import os
from dotenv import load_dotenv
from buchon import enviarMensajes
from mary import cotizacion_Blue as cb

#   Cargo las variables del archivo .env
load_dotenv()


async def main(mensaje):
    #  Asigno los valores de las variables del .env a una variable interna
    token = os.environ.get("TOKEN")
    chat = os.environ.get("ID")
    await enviarMensajes(token=token, chat=chat, mensaje=mensaje)


if __name__ == "__main__":
    asyncio.run(main(cb()))
