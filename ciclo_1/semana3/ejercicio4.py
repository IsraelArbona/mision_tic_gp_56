# lista paralelas

'''
nombres = list() # nombres = []
edades = list()  # edades = []

for x in range(5):
    nombre = input('Digite el nombre de la persona. ')
    nombres.append(nombre)
    edad = int(input('Digite la edad de la persona. '))
    edades.append(edad)

print('Nombre de las personas mayores de edad.')
print(' --------- ')

for x in range(5):
    if edades[x] >= 18:
        print('Nombre ', nombres[x], ' edad -> ', edades[x])
'''

# lista compuestas

lista = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

'''
print(lista)
print(lista[0])
print(lista[0][0])
'''

'''
for x in range(len(lista[0])):
    print(lista[0][x])
'''


'''
for x in range(len(lista)):
    for k in range(len(lista[x])):
        print(lista[x][k])
'''

# Ejercicio 2

'''
lista = [[1,3,5,7,9],[2,4,6,8,10]]

for x in range(len(lista)):
    resultado = 0
    for k in range(len(lista[x])):
        resultado = resultado + lista[x][k]
    print(resultado)
'''

# Ejercicio 3

'''
lista = [[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5]]

resultado = 0
for x in range(len(lista)):
    for k in range(len(lista[x])):
        resultado += lista[x][k]
print(resultado)
'''

# Ejercicio 4

padres = list()
hijos = list()

for x in range(3):
    pa = input('Ingrese el nombre del padre. ')
    ma = input('Ingrese el nombre de la madre.')
    padres.append([pa,ma])

    cantidad = int(input('Cantidad de hijos en la familia. '))
    hijos.append([])
    for k in range(cantidad):
        hi = input('Ingrese el nombre del hij@. ')
        hijos[x].append(hi)


print('\nListado de padre, madre e hijos\n')

for x in range(len(padres)):
    print('Padre: ',padres[x][0])
    print('Madre: ',padres[x][1])
    for k in range(len(hijos[x])):
        print('Hij@ : ',hijos[x][k])

print('\nListado de padre con la cantidad de hijos \n')

for x in range(len(padres)):
    print('Padre : ', padres[x][0])
    print('Hijos : ', len(hijos[x]))