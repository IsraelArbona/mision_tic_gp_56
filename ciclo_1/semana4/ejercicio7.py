# Función filter

# filtramos los elementos según la condición

'''
def mayor_a_cinco(elemento):
    return elemento > 5


tupla = (5,2,6,7,8,10,77,55,2,1,30,4,21,4,32,5)

print('Número de elementos de la tupla original: ', len(tupla))
resultado = tuple( filter(mayor_a_cinco,tupla) )
print('Número de elementos de la tupla filtrada: ', len(resultado))
print(resultado)

resultado = list( filter( lambda elemento: elemento >= 5, tupla) )
print(resultado)
'''

pares = list()
for i in range(100):
    if i% 2 == 0:
        pares.append(i)

print(pares)

tupla = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print('\n', tupla)

resultado = list( filter( lambda elemento: elemento % 2 == 0, tupla ) )
print('Números pares: ', resultado)

resultado = list( filter( lambda elem: elem % 2, tupla ) )
print('Número Impares: ', resultado)

'''
resultado = list( map( lambda elemento: elemento % 2 if elemento % 2 == 0 else 'Impar', tupla ) )
print('map pares ', resultado)

resultado = list( map( lambda elemento: elemento % 2 if elemento % 2 else 'par', tupla ) )
print('map impares ', resultado)
'''