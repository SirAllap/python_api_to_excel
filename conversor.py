import requests

api_url = "http://localhost:5001/products"

def get_api_data():
    response = requests.get(api_url)
    if response.status_code != 200:
        raise Exception(f"Error al obtener datos de la API. Código de estado: {response.status_code}")
    print(f"Código de estado: {response.status_code}")
    return response.json()

print(get_api_data())