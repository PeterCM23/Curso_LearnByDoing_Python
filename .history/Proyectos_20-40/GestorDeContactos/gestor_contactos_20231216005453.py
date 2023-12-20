class Contacto:
    def __init__(self,nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

class GestionContactos:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self,contacto):
        self.contactos.append(contacto)

    def eliminar_contacto(self, nombre):
        self.contactos = [c for c in self.contactos if c.nombre != nombre]

    def buscar_contacto (self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                return contacto
            return None
        
#Menu de la app
        
def menu():
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Salir")

if __name__ == "__main__":
    gestion = GestionContactos()

    while True:
        menu()
        opcion = input("Selecciona una opcion")

        if opcion == "1":
            nombre = input("Nombre del contacto: ")
            telefono = input("Telefono del contacto: ")
            nuevo_contacto = Contacto(nombre, telefono)
            gestion.agregar_contacto(nuevo_contacto)
            print("Contacto agregado con exito.")

        elif opcion == "2":
            nombre =input("Nombre del contacto a eliminar: ")
            gestion.eliminar_contacto(nombre)
            print("Contacto eliminado exitosamente.")

        elif opcion == "3":
            nombre =input("nombre del contacto a buscar: ")
            contacto_encontrado = gestion.buscar_contacto(nombre)
            if contacto_encontrado:
                print(f"Contacto encontrado - Nombre: {contacto_encontrado.nombre}, Telefono")