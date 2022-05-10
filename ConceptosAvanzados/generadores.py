def tablaDeMultiplicar(numero,maximo=12):
    for posicion in range(1,maximo+1):
        yield posicion * numero, numero, posicion

for resultado,numero,posicion in tablaDeMultiplicar(7,12):
    print(numero,"*",posicion,"=",resultado)
