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
        self.contactos = [c for c in self.contactos if c.nombre !]