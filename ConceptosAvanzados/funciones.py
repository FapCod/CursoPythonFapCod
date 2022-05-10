# def saluda():
#     print('Hola')

# saluda()

# def saluda(nombre):
#     saludo= 'Hola {} como estas'.format(nombre)
#     return saludo

# productoterminado= saluda('Frank')
# print(productoterminado)

# def suma(number1,number2):
#     return number1 + number2

# resultado = suma(23,54)
# print(resultado)

# def resta(number1,number2,number3=4):
#     return number1 - number2 - number3

# resultado = resta(10,2)
# print(resultado)

# def crearUsuario(nombre='',apellido='',edad=0):
#     return {
#         'nombre': nombre,
#         'apellido':apellido,
#         'edad': edad,
#         'nombreCompleto': '{} {}'.format(nombre,apellido)
#     }

# usuario =crearUsuario()

# print(usuario['nombre'])
# print(usuario['apellido'])
# print(usuario['edad'])
# print(usuario['nombreCompleto'])

# def usuario(nombre,apellido):
#     return {
#         'nombre':nombre,
#         'apellido':apellido
#     }

# usuario = usuario(apellido='Lopez',nombre='Jose')
# print(usuario['nombre'])
# print(usuario['apellido'])

# def sumar(*args):
#     total = 0
#     print(args)
#     for numero in args:
#         total+= numero
#     return total

# resultado= sumar(1,2,3,4,5,1,2,1)
# print(resultado)

# def sumar(valorestatico,*args,**kwargs):
#     print(valorestatico)
#     print(args)
#     print(kwargs) 
# sumar('Hola perro',1,2,3,4,5,number1=1,number2=2,number3=3,number4=4)


# bandera= 0
# def saludar():
#     global bandera
#     bandera=1
#     print(bandera)
# saludar()
# print(bandera)

# def listarEnOrden(lista): 
#     def listarUxU():
#         for valor in lista:
#             print(valor)
#     listarUxU()
#     print(lista)


# lista=['AguaMarina','Romeo','Aventura','Ozuna','Arcangel','Banda']
# listarEnOrden(lista)

def saludar(nombre):
    nombreL=nombre
    def saludaOtro():
        print(nombreL)
    return saludaOtro
funcionRecibida=saludar('Frank')
funcionRecibida()