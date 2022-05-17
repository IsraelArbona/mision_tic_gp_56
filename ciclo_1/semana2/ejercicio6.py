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
