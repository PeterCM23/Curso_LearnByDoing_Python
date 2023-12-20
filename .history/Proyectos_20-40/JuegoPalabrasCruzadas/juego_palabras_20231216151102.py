import random

def generar_tablero(palabras):
    # Crea un tablero de 10x10 lleno de espacios en blanco
    tablero = [['' for _ in range(10)]for _ in range(10)]
    
    #Coloca cada palabra en el tablero de manera aleatoria
    for palabra in palabras:
        # Elige aleatoriamente la direccion de la palabra (horizontal o vertical)