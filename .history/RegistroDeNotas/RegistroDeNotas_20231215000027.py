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
        