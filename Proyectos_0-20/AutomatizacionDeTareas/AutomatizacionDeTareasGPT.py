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
        shutil.move(origen, destino)
        print(f"Archivo movido de '{origen}' a '{destino}'.")
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en '{origen}'.")

def listar_contenido_directorio(ruta):
    """Lista el contenido de un directorio."""
    try:
        contenido = os.listdir(ruta)
        print(f"Contenido de '{ruta}':")
        for elemento in contenido:
            print(f"- {elemento}")
    except FileNotFoundError:
        print(f"Error: Directorio no encontrado en '{ruta}'.")

def eliminar_archivo(ruta):
    """Elimina un archivo."""
    try:
        os.remove(ruta)
        print(f"Archivo '{ruta}' eliminado.")
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en '{ruta}'.")

def main():
    while True:
        print("\n=== Menú ===")
        print("1. Copiar archivo")
        print("2. Mover archivo")
        print("3. Listar contenido de directorio")
        print("4. Eliminar archivo")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            origen = input("Ingrese la ruta del archivo de origen: ")
            destino = input("Ingrese la ruta del archivo de destino: ")
            copiar_archivo(origen, destino)

        elif opcion == "2":
            origen = input("Ingrese la ruta del archivo de origen: ")
            destino = input("Ingrese la ruta del archivo de destino: ")
            mover_archivo(origen, destino)

        elif opcion == "3":
            ruta = input("Ingrese la ruta del directorio: ")
            listar_contenido_directorio(ruta)

        elif opcion == "4":
            ruta = input("Ingrese la ruta del archivo a eliminar: ")
            eliminar_archivo(ruta)

        elif opcion == "5":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
