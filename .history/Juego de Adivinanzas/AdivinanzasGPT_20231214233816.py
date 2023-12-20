import random  # Importar el módulo random para generar números aleatorios

def jugar_adivinanza():
    print("¡Bienvenido al Juego de Adivinanzas!")
    
    # Generar un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    
    intentos = 0

    while True:
        # Obtener el intento del usuario
        intento_usuario = int(input("Adivina el número (entre 1 y 100): "))
        
        # Incrementar el contador de intentos
        intentos += 1

        # Comparar el intento del usuario con el número secreto
        if intento_usuario < numero_secreto:
            print("Demasiado bajo. ¡Intenta de nuevo!")
        elif intento_usuario > numero_secreto:
            print("Demasiado alto. ¡Intenta de nuevo!")
        else:
            print(f"¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
            break

if __name__ == "__main__":
    jugar_adivinanza()
