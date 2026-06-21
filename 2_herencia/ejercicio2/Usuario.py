class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre} \nApellido: {self.apellido}")