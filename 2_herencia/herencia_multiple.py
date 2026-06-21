# HERENCIA MÚLTIPLE
# Es posible que una clase herede de múltiples clases base. Esto se conoce como herencia múltiple.
# En Python, esto se logra simplemente listando las clases base entre paréntesis al definir la clase derivada.

# CLASE BASE 1
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método específico de la clase Persona
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# CLASE BASE 2
class Trabajador:
    def __init__(self, puesto):
        self.puesto = puesto

    # Método específico de la clase Trabajador
    def trabajar(self): 
        print(f"Estoy trabajando como {self.puesto}.")

# CLASE DERIVADA QUE HEREDA DE AMBAS CLASES BASE
class Empleado(Persona, Trabajador):
    def __init__(self, nombre, edad, puesto):
        Persona.__init__(self, nombre, edad)  # Llamada al constructor de la clase Persona
        Trabajador.__init__(self, puesto)      # Llamada al constructor de la clase Trabajador

    def presentarse(self):
        Persona.presentarse(self)
        self.trabajar()

# CREACION DE UN OBJETO DE LA CLASE EMPLEADO
empleado1 = Empleado("Laura", 28, "Diseñadora Gráfica")
# LLAMADA AL METODO DE LA CLASE EMPLEADO, QUE A SU VEZ LLAMA A LOS METODOS DE AMBAS CLASES BASE
empleado1.presentarse()


# VERIFICAR LA HERENCIA Y LA INSTANCIA DE LOS OBJETOS USANDO LAS FUNCIONES BUILT-IN issubclass() E isinstance().
hereda = issubclass(Empleado, Persona)  # Verificar si Empleado hereda de Persona
print(f"\n¿Empleado hereda de Persona? {hereda}")

hereda_trabajador = issubclass(Empleado, Trabajador)  # Verificar si Empleado hereda de Trabajador
print(f"¿Empleado hereda de Trabajador? {hereda_trabajador}")

es_instancia = isinstance(empleado1, Empleado)  # Verificar si empleado1 es una instancia de Empleado
print(f"\n¿empleado1 es una instancia de Empleado? {es_instancia}")

es_instancia_persona = isinstance(empleado1, Persona)  # Verificar si empleado1 es una instancia de Persona
print(f"¿empleado1 es una instancia de Persona? {es_instancia_persona}")

es_instancia_trabajador = isinstance(empleado1, Trabajador)  # Verificar si empleado1 es una instancia de Trabajador
print(f"¿empleado1 es una instancia de Trabajador? {es_instancia_trabajador}")
