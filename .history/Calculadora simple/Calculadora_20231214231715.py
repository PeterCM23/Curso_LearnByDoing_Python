def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: No se puede dividir por cero"


def obtener_numero():
    while True:
        try:
            return float(input("Ingresa un número: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")

def obtener_operacion():
    operaciones_validas = ['+', '-', '*', '/']
    while True:
        operacion = input("Ingresa una operación (+, -, *, /): ")
        if operacion in operaciones_validas:
            return operacion
        else:
            print("Operación no válida. Inténtalo de nuevo.")
