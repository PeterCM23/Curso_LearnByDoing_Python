import requests 

def obtener_clima(ciudad, clave_api):
    # URL de la API de OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={clave_api}"
    
    
    # Realiza la solicitud a la API
    respuesta = requests.get(url)
    
    # 