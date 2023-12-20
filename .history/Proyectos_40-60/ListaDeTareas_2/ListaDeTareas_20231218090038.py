from datetime import datetime

class Tarea:
    def __init__(self, descripcion, completada=False, recordatorio=None, fecha_vencimiento=None):
        self.descripcion = descripcion
        self.completada = completada 
        self.recordatorio = recordatorio
        self.fecha_vencimiento = fecha_vencimiento

def agregar_tarea(lista_tareas, descripcion, recordatorio=None, fecha_vencimiento=None):
        """Agrega una tarea a la lista."""
        nueva_tarea = Tarea(descripcion, recordatorio=recordatorio, fecha_vencimiento=fecha_vencimiento)
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
                recordatorio = f"Recordatorio: {tarea.recordatorio}" if tarea.recordatorio else "Sin recordatorio"
                fecha_vencimiento = f"Fecha de vencimiento: {tarea.fecha_vencimiento}" if tarea.fecha_vencimiento else "Sin fecha de vencimiento"
                print(f"{i}. {tarea.descripcion} - {estado} - ")

def marcar_completada(lista_tareas,numero_tarea):
        """Marca una tarea como completada."""
        if 1 <= numero_tarea <= len(lista_tareas):
            tarea = lista_tareas[numero_tarea - 1]
            tarea.completada = True
            print(f'Tarea "{tarea.descripcion}" marcada como completada.')
        else:
            print("Numero de tarea invalido.")
            
def eliminar_tarea(lista_tareas, numero_tarea):
        """Elimina una tarea de la lista."""
        if 1 <= numero_tarea <= len(lista_tareas):
            tarea_eliminada = lista_tareas.pop(numero_tarea - 1)
            print(f'Tarea "{tarea_eliminada.descripcion}" eliminada.')
        else:
            print("Número de tarea inválido.")


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

        elif opcion == "2":
            ver_tareas(lista_tareas)

        elif opcion == "3":
            ver_tareas(lista_tareas)
            numero_tarea = int(input("Ingrese el numero de la tarea completada:"))
            marcar_completada(lista_tareas, numero_tarea)

        elif opcion == "4":
            ver_tareas(lista_tareas)
            numero_tarea = int(input("Ingrese el numero de la tarea a eliminar:"))
            eliminar_tarea(lista_tareas, numero_tarea)

        elif opcion == "5":
            print("Saliendo del programa.")
            break



        else:
            print("Opcion no valida. Intentalo de nuevo.")

if __name__ == "__main__":
    main()
        
