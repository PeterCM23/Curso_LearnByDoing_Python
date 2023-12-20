import random   

def jugar_adivinanzas():
    print("¡Bienvenido al Juego de Adivinanzas!")

    #Generar un numero aleatorio entre 1 y 100
    numero_secreto = random.randint(1,100)

    intentos=0

    while