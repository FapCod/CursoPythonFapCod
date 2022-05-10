# con range siempre hay que acordarse que empieza desde el cero y el ultimo numero sera numero-1, si pones 21 entonces el ultimo numero sera el 20.

# for valor in range(1,21):
#     print(valor)


# for valor in range(1,101,2):
#     print(valor)

# lista = [1,2,3,4,5,6,7,8,9]
# for indice in range(len(lista)):
#     print("El indice es:",indice , "El valor del indice es:", lista[indice])

lista  = [1,2,3,4,5,6,7]
for indice,valor in enumerate(lista):
    print("El indice es:", indice, "El valor es:",valor)
