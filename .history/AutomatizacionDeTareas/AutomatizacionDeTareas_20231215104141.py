import os 
import shutil

def copiar_archivo(origen, destino):
    """Copia un archivo desde el origen hasta el destino."""
    try:
        shutil.copy(origen, destino)
        print(f"Archivo copiado de '{origen}' a '{destino}'.")
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en '{origen}'.")


def mover_archivo(origen, destino):
    """Mueve un archivo desde el origen hasta el destino."""
    try:
        shutil.move(origen,destino)
        print(f"Archivo movideo de '{origen}' a '{destino}'.")
    except FileNotFoundError:
        print(f"Error:Archivo no encontrado en '{origen}'.")

        