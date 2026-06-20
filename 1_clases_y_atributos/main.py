import Paciente

# CREACION DE OBJETOS, PASANDO LOS ARGUMENTOS NECESARIOS PARA EL CONSTRUCTOR
lista_pacientes = [
    Paciente.Paciente("Esteban", "Gómez", 27, "Esguince de tobillo"),
    Paciente.Paciente("María", "López", 35, "Esguince de rodilla"),
    Paciente.Paciente("Carlos", "Pérez", 42, "Esguince de muñeca")
]

# LLAMADA AL METODO DE INSTANCIA
for paciente in lista_pacientes:
    print("=========================================")
    print("Información del paciente:")
    paciente.mostrar_informacion()
    paciente.asistir_cita()

# ACTUALIZAR EL DIAGNOSTICO DE MARIA LOPEZ
for paciente_modificado in lista_pacientes:
    if paciente_modificado.nombre == "María" and paciente_modificado.apellido == "López":
        paciente_modificado.actualizar_diagnostico("Rotura de ligamento cruzado")

# MOSTRAR LA INFORMACION ACTUALIZADA DE LOS PACIENTES
for paciente in lista_pacientes:
    print("=========================================")
    print("\nInformación actualizada del paciente:")
    paciente.mostrar_informacion()