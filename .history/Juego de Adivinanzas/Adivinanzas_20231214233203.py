import random   

def jugar_adivinanzas():
    print("¡Bienvenido al Juego de Adivinanzas!")

    #Generar un numero aleatorio entre 1 y 100
    numero_secreto = random.randint(1,100)

    intentos=0

    while True:
        #Obtener el intento del usuario 
        intento_usuario = int(input("Adivina el numero (entre 1 y 100):"))

        #Incrementar el contador de intentos 
        intentos += 1

        #Comparar el intento del usuario con el numero secreto
        if intento_usuario < numero_secreto