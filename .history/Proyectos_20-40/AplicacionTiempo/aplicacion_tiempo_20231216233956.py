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
        
def mostrar_informacion_clima(datos_clima):
    if datos_clima:
        # Extraer informacion relevante del objeto JSON
        nombre_ciudad = datos_clima['name']
        temperatura = datos_clima['main']['temp']
        descripcion_clima = datos_clima['weather'][0]['description']
        
        # Mostrar la informacion del clima
        print(f"Informacion del clima en {nombre_ciudad}: ")
        print(f"Temperatura: {temperatura}ºC")
        print(f"Descripcion del clima :{ descripcion_clima}")
    else:
        print("No se pudo obtener la informacion del clima.")
        
if __name__ == "__main__":
    # Configuracion
    ciudad = input()