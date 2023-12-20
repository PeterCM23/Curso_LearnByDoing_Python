from flask import Flask, render_template, request
import requests
import hashlib
import time

app = Flask(__name__)

# Reemplaza con tu clave publica y privada de Marvel
PUBLIC_KEY = "c7986e132ccd493ad27683ea0eb26d88"
PRIVATE_KEY = "2e83e786832c98823bf274fbea506ad84ec3fc11"

# Funcion para obtener el hash MD5 necesario para la autenticacion
def generate_hash(ts):
    hash_input = f"{ts}{PRIVATE_KEY}{PUBLIC_KEY}"
    hash_output = hashlib.md5(hash_input.encode('utf-8')).hexdigest()
    return hash_output

# Ruta Principal
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # Obtener la marca de tiempo actual
        ts = str(int(time.time()))

        # Crear el hash necesario para la autenticacion
        hash_value = generate_hash(ts)

        # Obtener el nombre del personaje ingresado por el usuario
        character_name = request.form['character_name']

        # Construir la URL de la API de Marvel
        base_url = "https://gateway.marvel.com/v1/public/characters"
        params = {
            'apikey': PUBLIC_KEY,
            'ts': ts,
            'hash': hash_value,
            'name': character_name
         }

        # Hacer la solicitud a la API de Marvel
        response = requests.get(base_url, params=params)
        data = response.json()
        
        # Obtener la lista de personajes que coinciden con el nombre
        characters = data['data']['results']

    else:
        characters=[]

    # Renderizar la plantilla con los datos de la API
    return render_template('index.html', characters=characters)

if __name__== '__main__':
    app.run(debug=True)