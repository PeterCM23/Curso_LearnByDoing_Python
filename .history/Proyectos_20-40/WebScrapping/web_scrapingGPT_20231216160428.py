import requests
from bs4 import BeautifulSoup

def obtener_titulos_de_noticias(url):
    # Realizar una solicitud GET a la URL
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtener el contenido HTML de la página
        html = response.text

        # Crear un objeto BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')

        # Encontrar todos los elementos HTML que contienen los títulos de las noticias
        titulos = soup.find_all('h2', class_='headline')  # Esto es un ejemplo, ajusta según la estructura HTML de la página

        # Imprimir los títulos obtenidos
        for titulo in titulos:
            print(titulo.text)
    else:
        print(f"Error al obtener la página. Código de estado: {response.status_code}")

if __name__ == "__main__":
    # URL de ejemplo de una página de noticias
    url_noticias = 'https://www.ejemplonoticias.com'
    
    # Llamar a la función para obtener los títulos de las noticias
    obtener_titulos_de_noticias(url_noticias)
