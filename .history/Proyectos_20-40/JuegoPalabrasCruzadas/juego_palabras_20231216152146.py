import random

def generar_tablero(palabras):
    # Crea un tablero de 10x10 lleno de espacios en blanco
    tablero = [['' for _ in range(10)]for _ in range(10)]
    
    #Coloca cada palabra en el tablero de manera aleatoria
    for palabra in palabras:
        # Elige aleatoriamente la direccion de la palabra (horizontal o vertical)
        direccion = random.choice(['horizontal',"vertical"])
        x = random.randint(0,9)
        y=random.randint(0,9)
        
        # Busca una posicion valida para la palabra en el tablero
        while not es_posicion_valida(tablero, palabra, x, y, direccion):
            x = random.randint(0,9)
            y = random.randint(0,9)
            
        # Coloca la palabra en el tablero
        colocar_palabra(tablero, palabra, x, y, direccion)
        
    return tablero

def es_posicion_valida(tablero, palabra, x, y, direccion):
    # Verifica si la posicion y direccion elegidas son validas para colocar la palabra
    if direccion == 'horizontal' and y + len (palabra) <= 10:
        for i in range(len(palabra)):
            #Verifica si hay alguna colision con otra palabra ya colocada
            if tablero[x][y + i] != ' ' and tablero[]