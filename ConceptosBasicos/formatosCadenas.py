# cadena = '   este es un curso de Python,curso ,curso ,curso    '
# resultadoCadena= cadena.capitalize()
# resultadoCadena = cadena.swapcase()
# resultadoCadena = cadena.upper()
# resultadoCadena = cadena.lower()
# resultadoCadena = cadena.title()
# resultadoCadena = cadena.replace('curso','Especializacion',1)
# resultadoCadena = cadena.strip()
# print(cadena)
# print(resultadoCadena.isupper())
# print(resultadoCadena.islower())
cadenaNueva= 'Curso'
cadenaDos= 'Python 3'

# cadenaFinal= 'Bienvenidos al %s de %s' %(cadenaDos,cadenaNueva)
cadenaFinal = 'Bienvenidos al {c2} de {c1}'.format(c1=cadenaNueva,c2=cadenaDos)
print(cadenaFinal)