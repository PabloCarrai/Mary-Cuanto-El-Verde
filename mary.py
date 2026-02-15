import requests


def cotizacion_Blue():
    try:
        url = "https://api.bluelytics.com.ar/v2/latest"
        response = requests.get(url)
        data = response.json()
        dolar_blue = data["oficial"]["value_sell"]
        return f"Cotizacion Dolar: ${dolar_blue}"
    except Exception as e:
        print(f"Error al obtener el dolar: {e}")
