# Definir funciones para operaciones básicas
def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    # Manejar el caso de división por cero
    if y != 0:
        return x / y
    else:
        return "Error: No se puede dividir por cero"

# Obtener número del usuario
def obtener_numero():
    while True:
        try:
            # Intentar convertir la entrada del usuario a un número
            return float(input("Ingresa un número: "))
        except ValueError:
            # Manejar excepción si la entrada no es un número
            print("Por favor, ingresa un número válido.")

# Obtener operación del usuario
def obtener_operacion():
    # Definir operaciones válidas
    operaciones_validas = ['+', '-', '*', '/']
    while True:
        # Pedir al usuario que ingrese una operación
        operacion = input("Ingresa una operación (+, -, *, /): ")
        if operacion in operaciones_validas:
            return operacion
        else:
            # Mostrar mensaje si la operación no es válida
            print("Operación no válida. Inténtalo de nuevo.")

# Realizar la operación seleccionada
def calcular():
    while True:
        # Obtener dos números y la operación del usuario
        num1 = obtener_numero()
        operacion = obtener_operacion()
        num2 = obtener_numero()

        # Realizar la operación seleccionada
        if operacion == '+':
            resultado = sumar(num1, num2)
        elif operacion == '-':
            resultado = restar(num1, num2)
        elif operacion == '*':
            resultado = multiplicar(num1, num2)
        elif operacion == '/':
            resultado = dividir(num1, num2)

        # Mostrar el resultado al usuario
        print(f"Resultado: {resultado}")

        # Preguntar al usuario si quiere realizar otra operación
        continuar = input("¿Quieres realizar otra operación? (s/n): ")
        if continuar.lower() != 's':
            # Salir del bucle si el usuario no quiere continuar
            break

# Verificar si el script se ejecuta directamente (no se importa como módulo)
if __name__ == "__main__":
    # Iniciar la calculadora
    calcular()
