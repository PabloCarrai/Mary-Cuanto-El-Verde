import telegram
import asyncio


async def enviarMensajes(token, chat, mensaje):
    elbot = telegram.Bot(token)
    try:
        await elbot.send_message(chat_id=chat, text=mensaje)
        print(f"Mensaje enviado a {chat}:  {mensaje}")
    except telegram.error.TelegramError as e:
        print(f"Error al enviar mensaje: {e}")
