'''
    Método clear()
    Este método remueve o elimina todos los elementos (items) de un diccionario.
'''

diccionario = {
    'Cedula': 1021100,
    'Nombre': 'Juan',
    'Apellido': 'Diaz',
    'Correo': 'jdiaz@micorreo.com'
}

print(diccionario)
diccionario.clear()
print(diccionario)

'''
    Método copy()
    Este método devuelve una copia del diccionario.
'''

diccionario2 = {
    'Cedula': 1021100,
    'Nombre': 'Juan',
    'Apellido': 'Diaz',
    'Correo': 'jdiaz@micorreo.com'
}

print()
print('Diccionario2 : ',diccionario2)
nuevoDiccionario2 = diccionario2.copy()
print('nuevoDiccionario2 ',nuevoDiccionario2)

'''
    fromkeys
    Este método crea un nuevo diccionario con la clave a partid de un tipo de dato secuencia.
    El valor de value por defecto es el tipo None.
'''

lista_tupla = ('python','zope','plone')

versiones = dict.fromkeys(lista_tupla)
print('Nuevo diccionario: %s' % str(versiones))

diccionario3 = {
    'Cedula': 1021100,
    'Nombre': 'Juan',
    'Apellido': 'Diaz',
    'Correo': 'jdiaz@micorreo.com'
}

nuevoDiccionario3 = dict.fromkeys(diccionario3)
print('nuevo diccionario3: %s' % str(nuevoDiccionario3))

nuevoDiccionario3 = dict.fromkeys(diccionario3,0.5)
print('nuevo diccionario3: %s' % str(nuevoDiccionario3))

'''
    Método get()
    Devuelve el valor de una clave seleccionada, sino la encuentra devuelve None.
'''

diccionario4 = {
    'Cedula': 1021100,
    'Nombre': 'Juan',
    'Apellido': 'Diaz',
    'Correo': 'jdiaz@micorreo.com'
}

print()
print(diccionario4.get('Nombre'))
print(diccionario4.get('correo'))
#print(diccionario4['correo'])

'''
    Método items()
    Devuelve una lista de pares de diccionario (clave,valor), como una tupla

    [                                       -> lista
        ('Cedula', 1021100),                -> tupla
        ('Nombre', 'Juan'),                 -> tupla
        ('Apellido', 'Diaz'),               -> tupla
        ('Correo', 'jdiaz@micorreo.com')    -> tupla
    ]
'''

diccionario5 = {
    'Cedula': 1021100,
    'Nombre': 'Juan',
    'Apellido': 'Diaz',
    'Correo': 'jdiaz@micorreo.com'
}

print()
print(diccionario5.items())

'''
    Método pop()
    Remover o eliminar específicamente una clave del diccionario 
    y devolver el valor correspondiente, lanza una excepción KeyError si la
    clave no es encontrada.
'''

diccionario6 = {
    'Cedula': 1021100,
    'Nombre': 'Juan',
    'Apellido': 'Diaz',
    'Correo': 'jdiaz@micorreo.com'
}

print('diccionario6: ', diccionario6)
print()
valor_eliminado = diccionario6.pop('Apellido')
print('valor eliminado: ', valor_eliminado)
print('diccionario6: ', diccionario6)

'''
    Método update()
    Actuliza un diccionario agregando nuevos pares (clave-valor).
    se llama el update() sin pasar parametros, el diccionario permanece sin cambio.
'''

diccionario7 = {
    'Cedula': 1021100,
    'Nombre': 'Juan',
    'Apellido': 'Diaz',
    'Correo': 'jdiaz@micorreo.com'
}

print('\nDiccionario original: ', diccionario7)

nuevoDiccionario7 = ({'Telefono' : 6019435459})
print('nuevoDiccionario7 - complemento', nuevoDiccionario7)

diccionario7.update(nuevoDiccionario7)
print('\n Diccionario actulizado', diccionario7)


# ejercicio 8

usuario_1 = {
    'Cedula': 1021100,
    'Nombre': 'Juan',
    'Apellido': 'Diaz',
    'Correo': 'jdiaz@micorreo.com'
}

usuario_2 = {
    'Cedula': 2301223,
    'Nombre': 'Carlos',
    'Apellido': 'Marin',
    'Correo': 'cmarin@micorreo.com'
}

print('Cliente 1 \n', usuario_1)
print('Cliente 2 \n', usuario_2)

usuario_1.update(usuario_2)

print('Usuario 1 actulizado: \n', usuario_1)


# ejercicio 9

datos = {
    'nombre': 'Andres',
    'apellido': 'Pizarro',
    'cedula': 19343222
}

for k in datos.keys():
    print('{} = {}'.format(k,datos[k]))

datos_add = {
    'cuenta_ahorro': 203249344,
    'saldo': 10000
}

print('\nNumero de items: ', len(datos))
datos.update(datos_add)
print('Numero de items actulizados: ', len(datos))
print('\n', datos)


# ejercicio 10
# Método keys() y sorted()
# Retorna una lista de todas las claves dentro del diccionario ascendentemente

datos10 = {
    'nombre': 'Andres',
    'apellido': 'Pizarro',
    'cedula': 19343222
}

print()

for key in sorted(datos10.keys()):
    # print(key)
    print(key, " -> ", datos10[key])


# ejercicio 11
# Método items() retorna lista de tuplas

datos11 = {
    'nombre': 'Andres',
    'apellido': 'Pizarro',
    'cedula': 19343222
}

print()
for k, valor in datos11.items():
    print(k, ' = ', valor)

# Ejecicio 12
# Comparaciones de nombre de los estudiantes.

informacion = { 
    'alumno1':{
        'nombre': 'David',
        'edad': 13,
        'estatura': 1.60,
        'grado':'Junior'
    },
    'alumno2':{
        'nombre': 'Juan',
        'edad': 16,
        'estatura': 1.70,
        'grado':'Master'
    } 
}

print('\n', informacion, '\n')

# comparación de los Nombres de cada alumno

if informacion['alumno1']['nombre'] == informacion['alumno2']['nombre']:
    print('\n' + str(informacion['alumno1']['nombre']) +
    ' es igual a '+ str(informacion['alumno2']['nombre']) + '\n')
else:
    print('\n' + str(informacion['alumno1']['nombre']) +
    ' es diferente a '+ str(informacion['alumno2']['nombre']) + '\n')


# ejercicio 13

diccionario13 = {
    'gato': 'chat',
    'perro': 'chiel',
    'caballo': 'cheval'
}

nuevo = ['gato','leon','caballo']

for n in nuevo:
    if n in diccionario13:
        print(n, ' -> ', diccionario13[n])
    else:
        print(n, ' no esta en el diccionario13')

