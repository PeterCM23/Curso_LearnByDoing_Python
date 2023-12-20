import requests 

def obtener_clima(ciudad, clave_api):
    # URL de la API de OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={clave_api}"
    
    
    # Realiza la solicitud a la API
    respuesta = requests.get(url)
    
    # Verificar si la solicitud fue exitosa (codigo 200)
    if respuesta.status_code == 200:
        datos_clima = respuesta.json()
        return datos_clima
    else:
        print(f"Error al obtener datos del clima. Código de estado: {respuesta.status_code}")
        
def mostrar_informacion_clima(datos_clima)