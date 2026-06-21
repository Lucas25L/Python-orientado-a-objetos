# MRO es el orden de resolución de métodos, que determina el orden en el que se buscan los métodos en una jerarquía de clases.
# En Python, el MRO se calcula utilizando el algoritmo C3 linearization, que garantiza un orden consistente y predecible para la resolución de métodos en presencia de herencia múltiple.

class A:
    def metodo(self):
        print("Método de la clase A")

class B(A):
    def metodo(self):
        print("Método de la clase B")

class C(A):
    def metodo(self):
        print("Método de la clase C")

class D(B, C):
    pass

# CREACION DE UN OBJETO DE LA CLASE D
d = D()
# LLAMADA AL METODO DE LA CLASE D, QUE A SU VEZ LLAMA AL METODO DE LA CLASE B, YA QUE B APARECE ANTES QUE C EN LA DEFINICION DE LA CLASE D
d.metodo()
# MOSTRAR EL MRO DE LA CLASE D
print("\nMRO de la clase D:", D.mro())