
""" # a(b)->c

def evaluar(funcion):
    def verificar():
        print("Estamos abriendo la base de datos")
        funcion()
        print("Estamos cerrando la base de datos")
    return verificar

@evaluar
def ejecutar():
    print("Estamos creando un usuario")

# funcion que he ejecutado
ejecutar() """


