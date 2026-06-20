class Paciente():
    # METODO CONSTRUCTOR
    def __init__(self, nombre, apellido, edad, diagnostico): # SELF ES UNA REFERENCIA A LA PROPIA CLASE, SE USA PARA ACCEDER A LOS ATRIBUTOS Y METODOS DE LA CLASE
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.diagnostico = diagnostico

    # METODO DE INSTANCIA
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}") # SE USA EL SELF PARA ACCEDER A LOS ATRIBUTOS DE LA CLASE
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Diagnóstico: {self.diagnostico}")
    
    def asistir_cita(self):
        print(f"\n{self.nombre} {self.apellido} ha asistido a su cita médica.")
    
    def actualizar_diagnostico(self, nuevo_diagnostico):
        self.diagnostico = nuevo_diagnostico
        print("\nDiagnóstico actualizado exitosamente.")