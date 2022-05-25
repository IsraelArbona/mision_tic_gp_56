# Conversión entre contenedores.
#conversión de cadenas

# cadena -> lista (str - list)

'''
cadena = 'grupo_56'
lista = list(cadena)
print(lista)
'''

# cadena -> tupla (str - tuple)

'''
cadena1 = 'hola'
cadena2 = 'adios'
numero = 18
tupla = tuple(cadena1)
tuplaGeneral = (tupla,numero,tuple(cadena2))
print(tupla)
print(tuplaGeneral)
'''

# cadena -> conjunto (str - set)

'''
cadena = 'hhola'
conjunto = set(cadena)
print(conjunto)
'''

# lista -> cadena (list - str)

'''
lista = ['h','o','l','a', (1,2,3)]

try:
    cadena = ''.join(lista)
    print(cadena)
except:
    print('No se puede concatenar tipo de datos diferentes ha String.')

convertirCadena = ''
for elemento in lista:
    convertirCadena = convertirCadena + str(elemento)

print(convertirCadena)
'''

# lista -> tupla (list - tuple)

'''
lista = ['h','o','l','a',123, [1,2,3]]
tupla = tuple(lista)
print(tupla)
'''

# lista -> conjunto (list - set)

'''
lista = ['h','o','l','a',1,1,2,2,3]
conjunto = set(lista)
print(conjunto)
'''

# tupla -> cadena (tuple - str)

'''
tupla = ('h','o','l','a')
cadena = ''.join(tupla)

print(cadena)
'''

# tupla -> lista (tuple - list)

'''
tupla = ('hola',123,'mundo')
lista = list(tupla)

print(lista)
'''

# tupla -> conjunto (tuple - set)

'''
tupla = ('hola',111,'mundo', 'hola')
conjunto = set(tupla)

print(conjunto)
'''

# conjunto -> cadena (set - str)

'''
conjunto = {'h','o','l','a'}
cadena = ''.join(conjunto)

print(cadena)
'''

# conjunto -> tupla (set - tuple)

'''
conjunto = {'h','o','l','a'}
tupla = tuple(conjunto)

print(tupla)
'''

# conjunto -> lista (set - list)

'''
conjunto = {'h','o','l','a'}
lista = list(conjunto)

print(lista)
'''

# conversión a diccionario

# cadena -> diccionario (str - dict)

'''
cadena = 'grupo_56'

diccionario = dict()
for posicion in range(len(cadena)):
    diccionario[posicion] = cadena[posicion]

print(diccionario)

diccionarioZip = dict(zip(range(len(cadena)),cadena))
print(diccionarioZip)
'''

# lista -> diccionario (list - dict)

'''
lista = ['h','0','l','a']

diccionarioZip = dict( zip( range( len(lista) ), lista ) ) 
print(diccionarioZip)
'''

# tupla -> diccionario (tuple - dict)

'''
tupla = ('h','o','l','a')
diccionarioZip = dict(zip(range(len(tupla)),tupla))

print(diccionarioZip)
'''

# conjunto -> diccionario (set - dict)

conjunto = {'h','o','l','a'}
diccionarioZip = dict(zip(range(len(conjunto)), conjunto))

print(diccionarioZip)