import os 
import shutil

def copiar_archivo(origen, destino):
    """Copia un archivo desde el origen hasta el destino."""
    try:
        shutil.copy(origen, destino)
        print()