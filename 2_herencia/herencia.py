# HERENCIA
# CLASE PADRE O BASE
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# CLASE HIJA O DERIVADA
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.carrera = carrera # Atributo específico de la clase Estudiante

    def presentarse(self):
        super().presentarse()  # Llamada al método de la clase base
        print(f"Estoy estudiando {self.carrera}.")

class Empleado(Persona):
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.puesto = puesto # Atributo específico de la clase Empleado
    
    def presentarse(self):
        super().presentarse()  # Llamada al método de la clase base
        print(f"Trabajo como {self.puesto}.")


# CREACION DE UN OBJETO DE LA CLASE ESTUDIANTE
estudiante1 = Estudiante("Ana", 22, "Ingeniería Informática")
# LLAMADA AL METODO DE LA CLASE ESTUDIANTE, QUE A SU VEZ LLAMA AL METODO DE LA CLASE BASE
estudiante1.presentarse()

print("\n---------------------------------\n")

# CREACION DE UN OBJETO DE LA CLASE EMPLEADO
empleado1 = Empleado("Juan", 30, "Ingeniero de Software")
# LLAMADA AL METODO DE LA CLASE EMPLEADO, QUE A SU VEZ LLAMA AL METODO DE LA CLASE BASE
empleado1.presentarse()