def saludo(a: str) -> str:
    """
    Función que devuelve un saludo
    :param nombre: Nombre del usuario
    :return: Saludo
    """
    return "Hola " + a
resultado = saludo("Frank");
print(resultado)
def cazar(usuario:str)->None:
    print("Hola estoy cazando a " + usuario)
# cazar("Frank")