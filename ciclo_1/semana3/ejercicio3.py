# Listas 

# parentesis ()
# corchetes []
# llaves {}

'''
lista = [1, 2.5, 'DevCode', [5,6], 4]

print(lista[0]) # 1
print(lista[1]) # 2.5
print(lista[2]) # DevCode
print(lista[3]) # [5,6]
print(lista[3][0]) # 5
print(lista[3][1]) # 6
print(lista[1:3]) # [2.5, DevCode]
print(lista[1:6]) # [2.5, DevCode, [5,6],4]
print(lista[1:6:2]) # [2.5, [5,6]]
'''

# ejercicio 2
# list vacia

lista2 = []

# ejercicio 3

'''
nombre = 'Juan'
edad = 23
lista3 = [nombre,edad]
print(lista3)
'''

# ejercicio 4

'''
nombres = ['Juan','Marcos']
edades = [32,27]
lista4 = [nombres, edades]
print(lista4)
'''

# agregar elemento a la lista

'''
nombres += ['Cristian']
print(lista4)
'''

# ejercicio 5

'''
factura = ['pan','huevos', 500, 700]
print(len(factura))
'''

# modificar un elemento de la lista

'''
factura[1] = 'carne'
print(factura)
'''

# ejercicio 6
# Método append()
# Este método agrega un elemento al final de la lista.

'''
versiones_plone = [2.5, 3.6, 4, 5]
print(versiones_plone)

versiones_plone.append(6)
print(versiones_plone)
'''

# ejercicio 7
# Método count()
# Este método recibe un elemento como argumento 
# y cuenta la cantidad de veces que aprece en la lista.

'''
versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]

print('6 -> ', versiones_plone.count(6))
print('5 -> ', versiones_plone.count(5))
print('2.5 -> ', versiones_plone.count(2.5))
'''

# ejercicio 8
# Método extend()
# Este método extiende una lista agregando una iteración al final

'''
versiones_plone = [2.1, 2.5, 3.6]
print(versiones_plone)
versiones_plone.extend([6])
print(versiones_plone)
versiones_plone.extend(range(5,10))
print(versiones_plone)
'''

# ejercicio 9
# Método index()
# Este método recibir un elemento como argumento 
# y devuelve el índice de su primera aparición ne la lista.

'''
versiones_plone = [2.1, 2.5, 3.6 ,4, 5, 6, 4]
print(versiones_plone)
print(versiones_plone.index(4))

print(versiones_plone.index(4,5))
'''

# ejercicio 10
# Método insert()
# Este método inserta el elemento x en la lista, en el índice i.

'''
versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
print(versiones_plone)

versiones_plone.insert(2, 4.7)
print(versiones_plone)

versiones_plone.insert(4,[9,6,7,8,5])
print(versiones_plone)
versiones_plone.insert(1, 'lista')
print(versiones_plone)
'''

# ejercicio 11
# Método pop()
# Este método devuelve el último elemento de la lista y lo borra de la misma.

'''
versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
print(versiones_plone)
print(versiones_plone.pop())
print(versiones_plone)
'''

# Opcionamente puede recibir un argumento numerico entero, 
# que funciona como índice del elemento (por defecto -1).

'''
print(versiones_plone.pop(2))
print(versiones_plone)
'''

# ejercicio 12
# Método remove()
# Este método recibe como argumento un elemento y borra su primera aparición en la lista.

'''
versiones_plone = [2.1, 2.5, 3.6, 4, 5,6]
print(versiones_plone)
versiones_plone.remove(2.5)
print(versiones_plone)
'''

# ejercicio 13
# Método reverse()
# Este método invierte el orden de los elementos de la lista.

'''
versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
print(versiones_plone)

versiones_plone.reverse()
print(versiones_plone)
'''

# ejercicio 14
# Método sort()
# Este método nos permite ordenar los elementos de una lista.

versiones_plone = [2.1, 4, 2.7, 6, 1.3, 5, 7, 4]
print(versiones_plone)

versiones_plone.sort()
print(versiones_plone)

# el método sort() admite la opción reverse, por defecto con valor False.
# de tener el valor True, el ordenamiento se hace en sentido invertido.

versiones_plone.sort(reverse= True)
print(versiones_plone)
