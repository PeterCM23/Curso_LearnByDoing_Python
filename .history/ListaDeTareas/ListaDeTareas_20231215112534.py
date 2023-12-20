class Tarea:
    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion
        self.completada = completada 

    def agregar_tarea(lista_tareas, descripcion):
        """Agrega una tarea a la lista."""
        nueva_tarea = Tarea(descripcion)
        lista_tareas.append(nueva_tarea)
        print(f'Tarea "{descripcion}" agregada.')

    def ver_tareas(lista_tareas):
        """Muestra todas las tareas en la lista."""
        if not lista_tareas:
            print("No hay tareas pendientes.")
        else:
            print("Tareas Pendientes:")
            for i, tarea in enumerate(lista_tareas, 1):
                estado = "Completada" if tarea.completada else "Pendiente"
                print(f"{i}. {tarea.descripcion} - {estado}")

    def marcar_completada(lista_tareas,numero_tarea):
        """Marca una tarea como completada."""
        if 1 <= numero_tarea <= len(lista_tareas):
            tarea = lista_tareas[numero_tarea - 1]
            tarea.completada = True
            print(f'Tarea "{tarea.descripcion}" marcada como completada.')
        else:
            print("Numero de tarea invalido.")


    def main():
        lista_tareas = []

        while True:
            print("\n=== Menu ===")
            print("1. Agregar Tarea")
            print("2. Ver Tareas")
            print("3. Marcar tarea como completada")
            print("4. Eliminar tarea")
            print("5. Salir")

            opcion =input("Selecciona una opcion (1-5):")

            if opcion == "1":
                descripcion = input("Ingrese la descripcion de la tarea:")
                agregar_tarea(lista_tareas, descripcion)

            elif opcion == ""

            elif opcion == ""

            elif opcion == ""

            elif opcion == ""
