# Ejercicio 1

# Diccionario vacio
diccionario = {}

print(diccionario)
print(type(diccionario))

# Diccionario vacio usando el constructor de dict()
diccionario2 = dict()

print(diccionario2)

# Si necesitamos almacenar nuevo valores basta con separarlos mediante coma.

diccionario2 = {
    "total"     : 50,
    "descuento" : True,
    "subtotal"  : 13.435242,
    "cliente"   : "Marlon"
}

print(diccionario2)


# ejercicio 3

# Argumentos con nombre
diccionario3 = dict(uno = 1, dos = 2, tres = 3)
print(diccionario3)

diccionario3 = dict({'cinco': 5,'seis': 6, 'siete': 7})
print(diccionario3)


# ejercicio 4

diccionario4 = {
    "gato" : "chat",
    "perro": "chien",
    "caballo": "cheval"
}

numTelefonico = {
    'jefe' : '+57 34224343',
    'secretaria' : '+57 32324422'
}

print(numTelefonico['secretaria'])


# Ejercicio 5

usuario = {
    'nombre' : 'Juan',
    'edad' : 24,
    'curso': 'Curso de Python',
    'skills': {
        'programacion': True,
        'base_de_datos': False
    },
    'no_medallas' : 10
}

print(usuario)

# Agregar, obtener y modificar algún valor del diccionario, 
# hay que hacer uso de corchetes

usuario['activo'] = True
print(usuario)
print(usuario['activo'])
usuario['nombre'] = 'Carlos'
print(usuario['nombre'])
print(usuario)

# ejercicio 6

'''
    Podemos obtener todas las llaves de nuestro diccionario utilizando
    el método keys, de igual forma podemos obtener todos los valores
    del diccionario con el método values.
'''

diccionario6 = {
#   clave      : valor 
    'Eduardo'  : 1, 
    'Jose'     : 2, 
    'Fernando' : 3, 
    'Juan'     : 4
    }

print(diccionario6.keys())
print(diccionario6.values())

# Ejercicio 7

diccionario7 = {
    "Nombre" : "Sixto Manuel",
    "Apellido": 'García',
    "Cedula": 65493000,
    "Dirección": "Calle 10 # 11-23",
    "Telefono": 54332322,
    "Titulo": "Ingeniero",
    "Ciudad": "Cali",
    "Trabajo":"Independiente"
}

print()
print("Cantidad de datos: ", len(diccionario7), "\n")
print(diccionario7, "\n")
print(diccionario7.keys(), "\n")
print(diccionario7.values(), "\n")

print(f'Numero de datos: {len(diccionario7)}')

for clave in diccionario7.keys():
    print(f'{clave} = {diccionario7[clave]}')


# ejercicio 8

datos = dict(
    id = '329323232',
    nombre = 'Mauro',
    apellido = 'Plata',
    email = 'mplata@micorreo.com',
    telefono = 7954343,
    direccion = 'Cll 32 # 4029',
    ciudad = 'Armenia',
    departamento = 'Risaralda',
    pais = 'Colombia'
)

print('Cantidad de datps: ', len(datos))
print(datos)
print()
print(datos.keys())
print()
print(datos.values())
