import requests
from bs4 import BeautifulSoup

def obtener_titulos_de_noticias(url)
    # Realizar una solicitud GET a la URL
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa (codigo de estado 200)