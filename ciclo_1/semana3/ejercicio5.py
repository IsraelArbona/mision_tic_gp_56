# Creación de conjuntos

'''
s = {1,2,3,4,5}

print(type(s))
print(s)
'''
# Al igual que otras colecciones, sus elementos pueden ser de diverso tipo de datos.

'''
s = {True, 3.14,None,False,'Hola grupo 56',(5,6)}
print(s)
'''

# Un conjunto no puede incluir objetos mutables.

'''
s = {[1,2,3]}
'''

# Python distingue este tipo de operación de la creación de un diccionario.

'''
s = {}
'''

# para generar un conjunto vacio, la clase set

'''
s = set()
print(s)
'''

# podemos obtener un conjunto a partir de cualquier objeto iterable

'''
s1 = set([1,2,3,4,5])
s2 = set(range(20))

print(s1)
print(s2)
'''

# en los conjuntos los elementos no se repiten.

'''
c = {1,3,2,9,3,1}
print(c)

a = set('Hola grupo 56')
print(a)
'''


# realizar un recorrido por los elementos de un conjunto.

'''
conjunto = {1,3,2,9,3,1}

for numero in conjunto:
    print(numero)
'''

# Método de tipo de dato conjunto (Set)

# add() -> agrega un elemento aun conjunto.

'''
setMutable = set([4,3,11,7,5,2,1,4])
print(setMutable)
setMutable.add(23.55555)
setMutable.add(9)
setMutable.add(9)
print(setMutable)
'''

# clear() -> remover o eliminar todos los elementos de un conjunto.

'''
setMutable = set([4,3,11,7,5,2,1,4])
print(setMutable)
setMutable.clear()
print(setMutable)
'''

# copy() -> devuelve un copia de tipo conjunto.

'''
setMutable = set([4.0,'Carro',True,12,0,'Grupo 56'])
print(setMutable)
setMutableCopy = setMutable.copy()
print(setMutableCopy)

print(setMutable == setMutableCopy)
'''

# difference -> devuelve la diferencia entre dos conjuntos.

'''
setMutable1 = set([4,3,11,7,5,2,1,4])
setMutable2 = set([11,5,9,2,4,8])

print(setMutable1)
print(setMutable2)

print(setMutable1.difference(setMutable2))
print(setMutable2.difference(setMutable1))
'''

# difference_update() -> actuliza el conjunto, con la diferencia de los conjuntos.

'''
conj1 = {'python','Zope2','ZODB3','pytz'}
conj2 = {'python','Plone','diazo'}

print(conj1)
print(conj2)

conj1.difference_update(conj2)
print(conj1)
'''

# discard() -> remueve un elemento desde un conjunto.

'''
paquetes = {'python','zope','plone','django'}
print(paquetes)
paquetes.discard('django')
print(paquetes)
'''

# intersection() -> devuelve la intersección entre los conjuntos.

'''
setMutable1 = set([4,3,11,7,5,2,1,4])
setMutable2 = set([11,5,9,2,4,8])

print(setMutable1)
print(setMutable2)

print(setMutable1.intersection(setMutable2))
print(setMutable2.intersection(setMutable1))
'''

# intersection_update() -> actuliza el conjunto 
# con la intersección de ese mismo y otro.

'''
conj1 = {'python','Zope2','ZODB3','pytz'}
conj2 = {'python','Plone','diazo'}
conj3 = {'python','django','django-filter'}

print(conj1)
print(conj2)
print(conj3)

conj3.intersection_update(conj1,conj2)

print(conj3)
'''

# isdisjoint() -> devuelve verdadero si no hay elemento comunes entre los conjuntos.

'''
setMutable1 = set([4,3,11,7,5,2,1,4])
setMutable2 = set([11,5,9,2,4,8])
setMutable3 = set([11,5,2,4])

print(setMutable1)
print(setMutable2)
print(setMutable3)

print(setMutable2.isdisjoint(setMutable1))
'''

# pop() -> elimina y devuelve un elemento aleatorio de un conjunto

'''
conj1 = {'python','Zope2','ZODB3','pytz'}
print(conj1)
print('Valor aleatorio devuelto es: ', conj1.pop())
print('Valor aleatorio devuelto es: ', conj1.pop())
print('Valor aleatorio devuelto es: ', conj1.pop())
print(conj1)
'''

# remove() -> busca y elimina un elemento de un conjunto mutable.


paquete = {'python','zope','plone','django'}
print(paquete)
paquete.remove('django')
print(paquete)

print(dir(paquete))


