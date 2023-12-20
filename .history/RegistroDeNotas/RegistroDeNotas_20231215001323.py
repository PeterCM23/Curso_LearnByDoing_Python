def agregar_estudiante(registro, nombre):
    """Agrega un estudiante al registro."""
    registro[nombre]=[]
    
def ingresar_nota(registro, nombre, nota): 
    """Ingresa una nota para un estudiante."""
    if nombre in registro:
        registro[nombre].append(nota)
    else:
        print(f"Error: El estudiante {nombre} no esta en el registro.")

def calcular_promedio(registro, nombre):
    """Calcula el promedio de las notas de un estudiante."""
    if nombre in registro and len(registro[nombre])>0:
        promedio = sum(registro[nombre]) / len(registro[nombre])
        return promedio
    else:
        print(f"Error: No hay notas registradas para el estudiante {nombre}.")
        return None
    
def main():
    # Inicializar el registro como un diccionario vacio
    registro_notas = []

    while True:
        print("\n=== Menu ===")
        print("1. Agregar estudiante")
        print("2. Ingresar nota")
        print("3. Calcular promedio")
        print("4. Salir")

        opcion = input("Selecciona una opcion (1-4):")

        if opcion == "1":
            nombre = input("Ingrese el nombre del estudiante:")
            agregar_estudiante(registro_notas, nombre)
            print(f"Estudiante {nombre} agregado al registro.")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del estudiante:")
            nota = float(input("Ingrese la nota del estudiante:"))
            ingresar_nota(registro_notas, nombre, nota )
            print(f"Nota {nota} ingresada para el estudiante {nombre}.")

        elif opcion == "3":
            nombre = input("Ingrese el nombre del estudiante:")
            promedio = calcular_promedio(registro_notas, nombre)
            if promedio is not None:
                print(f"El promedio de {nombre} es: {promedio:}")
