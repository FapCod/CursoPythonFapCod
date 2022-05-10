# class Persona:
#     def __init__(self,nombre='',correo=''):
#         self.nombre=nombre
#         self.correo=correo
#     def saludar(self):
#         print("Hola soy ", self.nombre)
#     def detalles(self):
#         print(self.nombre, self.correo)

# persona1 = Persona('Frank','Frank@gmail.com')
# persona2 = Persona('Antonio','Antonio@gmail.com')

# persona1.saludar()
# persona2.saludar()
# persona1.detalles()
# persona2.detalles()

# class Triangulo:
#     @staticmethod
#     def calcularArea(base,altura):
#         return (base*altura)/2
    

# resultado = Triangulo.calcularArea(10,30)
# print(resultado)
class Circulo:
    pi= 3.14
    @classmethod
    def area(cls,radio):
        return cls.pi * radio**2 
    
resultado = Circulo.area(3)
print(resultado)

