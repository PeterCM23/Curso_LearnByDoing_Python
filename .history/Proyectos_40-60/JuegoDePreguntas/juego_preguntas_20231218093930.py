import random 

class Pregunta:
    def __init__(self, enunciado, opciones, respuesta_correcta):
        self.enunciado = enunciado
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta
        
    def seleccionar_pregunta(categoria, nivel):
        preguntas = {
            'Matematicas':{
                'Facil': [Pregunta("¿Cuanto es 2 + 2?",['3','4','5'], '4')],
                'Dificil': [Pregunta("¿Cual es la raiz cuadrada de 81?",['9','8','7'],'9')]
            },
            'Ciencia':{
                'Facil': [Pregunta("¿Cual es el simbolo quimico del agua?",['H2O','CO2','O2'], 'H2O')],
                'Dificil': [Pregunta("¿Cual es la velocidad de la luz en el vacio?",['300,000 km/s', '500,000 km/s', '200,000 km/s'], '300,000 km/s')]
            }
        }
        
        return random.choice(preguntas.get(categoria, {}).get(nivel, []))
    
    def jugar():
        categorias = ['Matematicas', 'Ciencia']
        niveles = ['Facil', 'Dificil']
        
        while True:
            print("\n=== Juego de Preguntas y Respuestas ===")
            print("1. Jugar")
            print("2. Salir")
            
            opcion = input("Selecciona una opcion (1-2): ")
            
            if opcion == "1":
                categoria =random.choice(categorias)
                nivel = random.choice(niveles)
                
                pregunta = seleccionar_pregunta(categoria, nivel)
                
                print(f"\nCategoria: {categoria} - ")
            