# Calculo de grado celsius a fahrenheit

'''
c = [39.2,36.4,38,39.1]
f = list( map(lambda x: (float(9)/5)*(x+32),c) )

print('Grados celsius: ', c)
print('Conversión a grados fahrenheit: ', f)
'''

# Calculo de grado fahrenheit a celsius.

'''
f = [39.2,36.4,38,39.1]
c = list( map(lambda x: (float(9)/5)*(x-32),f) )

print('\nGrados fahrenheit: ', f)
print('Conversión a grados celsius: ', c)
'''

# Sumar tres listas.

lista1 = [1,2,3,4]
lista2 = [12,10,15,13]
lista3 = [-2,-3,4,8]

'''
resultado = list( map( lambda x,y,z : x+y+z , lista1,lista2,lista3 ) )
print(resultado)

# Sumar dos listas
resultado2 = list( map( lambda x,y : x+y , lista1,lista2 ) )
print(resultado2)
'''

# Operacion adicional
resultado3 = list( map( lambda a,b,c : ((2.3*a)+(2*b)-c) , lista1,lista2,lista3) )
print(resultado3)

