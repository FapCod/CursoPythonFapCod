midiccionario= { 'a': 'Raul', 'b': 'Jose', 'c':'Joel' }
# elemento = midiccionario.get('z', 'No existe la key buscada')
# elemento = 'z' in midiccionario
elemento = midiccionario.setdefault('z',3)
print(elemento)
print(midiccionario)