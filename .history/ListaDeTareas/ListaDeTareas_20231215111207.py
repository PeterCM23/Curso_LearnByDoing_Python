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