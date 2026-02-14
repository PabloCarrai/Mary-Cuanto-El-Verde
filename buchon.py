import os
from dotenv import load_dotenv
import requests

#   Cargo las variables del archivo .env
load_dotenv()


def enviarMensajes(token, chat, mensaje):
    """
    enviarMensajes; Envia mensaje a bot de telegrams

    :param token: Tu token de telegram
    :param chat: Tu id de chat de telegram
    :param mensaje: Tu mensaje a enviar
    """
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    parametros = {"chat": chat, "mensaje": mensaje, "parse_mode": "Markdown"}
    try:
        response = requests.get(url, params=parametros)
        response.raise_for_status()
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ocurrio un error: {e}")
        return None


#  Asigno los valores de las variables del .env a una variable interna
token = os.environ.get("TOKEN")
chat = os.environ.get("ID")
enviarMensajes(token, chat, "Putooooo")
