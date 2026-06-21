from Administrador import Administrador
from Bibliotecario import Bibliotecario
from AdministradorBibliotecario import AdministradorBibliotecario

soy_un_administrador = Administrador("Lucas", "Lopez")
soy_un_bibliotecario = Bibliotecario("Gonzalo", "Montiel")
soy_un_administrador_bibliotecario = AdministradorBibliotecario("Maravilla", "Martinez")

print("-------- ADMINISTRADOR ----------------------")
soy_un_administrador.mostrar_datos()
soy_un_administrador.crear_usuario()
print("---------------------------------------------")
print("-------- BIBLIOTECARIO ----------------------")
soy_un_bibliotecario.mostrar_datos()
soy_un_bibliotecario.registrar_prestamo()
print("---------------------------------------------")
print("-------- ADMINISTRADOR BIBLIOTECARIO --------")
soy_un_administrador_bibliotecario.mostrar_datos()
soy_un_administrador_bibliotecario.crear_usuario()
soy_un_administrador_bibliotecario.registrar_prestamo()
print("---------------------------------------------")

print(AdministradorBibliotecario.mro())