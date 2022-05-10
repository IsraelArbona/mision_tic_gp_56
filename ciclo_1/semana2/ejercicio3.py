
# Acceder a los caracteres de uno en uno en la cadena (String)

# ejercicio 1
fruta = 'fresa'
letra = fruta[1]
print(letra)

fruta = 'banana'
letra = fruta[0]
print(letra)

# Conseguir la longitud de una cadena

fruta = 'banana'
print(len(fruta))

longitud = len(fruta)
ultimo = fruta[longitud-1]
print(ultimo)

frase = 'grupo 56 python fundamentos de programación'
print(len(frase))
print(frase[-1])
print(frase[-43])

# Rebanadas de una cadena

# ejercicio 4
s = 'Monty_Python'

print(s[0:6])
print(s[6:12])

fruta = 'banana'
#        0123456
print(fruta[:4])
print(fruta[3:])
print(fruta[3:3])
print(fruta[:])


# Inmutabilidad de una cadena -- Solo es posible crear una nueva cadena
saludo = 'Hola todos'
#saludo[0] = 'j'
nuevo_saludo = 'j' + saludo[1:]
print(nuevo_saludo, saludo)

# Operador in, devuelve respuesta booleana 
# si una cadena se encuentra dentro de otra cadena

var1 = 'a'
var2 = 'banana'
print(var1 in var2)

var1 = 'ola'
var2 = 'banana'
print(var1 in var2)


# Comparacíon de cadenas (String)

palabra = 'fresa'
if palabra == 'fresa':
    print('son iguales las palabras')


palabra2 = 'perA'

if palabra2 < 'banana':
    print('Tu palabra ' + palabra2 + ' viene antes de banana')
elif palabra > 'banana':
    print('Tu palabra ' + palabra2 + ' viene despues de banana')
else:
    print('las palabras son iguales')

# Conseguir el tipo de dato de una variable 
# y los métodos asociados a ese tipo de variables

cadena = 'Grupo 56'
print(type(cadena))
# print(dir(cadena))


# Convertir una cadena en mayúsculas

palabra = 'banana'
palabra_nueva = palabra.upper()
print(palabra_nueva)

# Retornar la posición de una subcadena dentro de una cadena

palabra = 'banana'
posicion = palabra.find('a')
print(posicion)

print(palabra.find('na'))
print(palabra.find('na',3))

# Retirar espacios en blanco a los extremos de una cadena (String)

linea = '              Aquí vamos           '
print(linea)
print(linea.strip())


# Conseguir una subcadena dentro de otra cadena al inicio

linea = 'Que Tengas Un Buen Día'
print(linea.startswith('Que'))
print(linea.startswith('q'))

print(linea.lower().startswith('q'))
print(linea.lower())


# Pieza de código que permite cortar el 
# host del correo electronico e imprimirlo luego

# conseguir el @
dato = 'De stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
posicion = dato.find('@') # devuelve la posición del @
print(posicion)
espacio = dato.find(' ', posicion)
print(espacio)
host = dato[posicion+1:espacio]
print(host)

# --- Operadores de formato --- #

# %s cadena
# %d número

camellos = 42

print('%d' % camellos)

print('He visto %d camellos' % camellos)

# saltar una linea en terminal
cadena = 'Hola\nMundo'
print(cadena)

cadena = r'Hola \n Mundo'
print(cadena)


cadena = 'un uno, un dos, un tres'

# sacar 4, hay 4 "un" en la cadena
print(cadena.count('un'))

# sacar 1, hay 1 "un" a partir de la posición 10 de la cadena
print(cadena.count('un',10))

# sacar 3, si hay 3 "un" entre la posición 0 y la posición 10
print(cadena.count('un',0,10))



