import requests
from bs4 import BeautifulSoup

def obtener_titulos_de_noticias(url)
    # Realizar una solicitud GET a la URL
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa (codigo de estado 200)
    if response.status_code == 200:
        #Obtener el contenido HTML de la pagina
        html = response.text
        
        # Crear un objeto BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        
        # Encontrar todos los elementos HTML que contienen los titulos de las noticias
        titulos = soup.find_all('h2', class_='titulo-noticia') 
        
        # Imprimir los titulos obtenidos
        for titulo in titulos:
            print(titulo.text)
            
    else: 
        print(f"Error al obtener la pagina. Codigo de estado: {response.status_code}")
        
if __name__ == "__main__":
    #URL de una pagina de noticias
    url_noticias = ''
    
    # Llamar a la funcion para obtener los titulos de las noticias
    obtener_titulos_de_noticias