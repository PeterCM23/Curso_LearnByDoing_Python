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