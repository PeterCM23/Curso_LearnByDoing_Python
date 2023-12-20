def agregar_estudiante(registro, nombre):
    """Agrega un estudiante al registro."""
    registro[nombre]=[]
    
def ingresar_nota(registro, nombre, nota): 
    """Ingresa una nota para un estudiante."""
    if nombre in registro:
        registro[nombre].append(nota)
    else:
        print(f"Error: El estudiante {nombre} no esta en el registro.")
.
def calcular_promedio(registro, nombre)