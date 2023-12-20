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
            
        }