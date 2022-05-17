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


# ejercicio 9

diccionario9 = {
    'clave1': 598,
    'clave2': True,
    'clave3': 'Armando'
}


print(diccionario9)
print(type(diccionario9))

print(diccionario9['clave1'])
print(type(diccionario9['clave1']))
print(diccionario9['clave2'])
print(type(diccionario9['clave2']))
print(diccionario9['clave3'])
print(type(diccionario9['clave3']))
print()


# Encapsulamiento con diccionarios.

def promedioNotas2(dicNotas):
    sumatoria = 0
    sumatoria += dicNotas['Nota1']
    sumatoria += dicNotas['Nota2']
    sumatoria += dicNotas['Nota3']
    sumatoria += dicNotas['Nota4']

    promedio = round(sumatoria/4, 2)
    return promedio

dicNotas = {}
dicNotas['Nota1'] = 4.5
dicNotas['Nota2'] = 3
dicNotas['Nota3'] = 3.5
dicNotas['Nota4'] = 1

print('El promedio es de: ', promedioNotas2(dicNotas))


def promedioNotas3(dicNotas):
    sumatoria = 0
    sumatoria += dicNotas['Nota1']
    sumatoria += dicNotas['Nota2']
    sumatoria += dicNotas['Nota3']
    sumatoria += dicNotas['Nota4']

    promedio = round(sumatoria/4, 2)
    return promedio

dicNotas3 = {
    'Nota1' : 3.5,
    'Nota2' : 4.0,
    'Nota3' : 2,
    'Nota4' : 4.7
}

print('El promedio es de: ', promedioNotas3(dicNotas3))


# Paso entre funciones

def reportePromedio(dicReporte):
    return dicReporte['estudiante'] + " = " + str(dicReporte['promedio'])

def generarReporteNotas(dicNotas):
    sumatoria = 0
    sumatoria += dicNotas['Nota1']
    sumatoria += dicNotas['Nota2']
    sumatoria += dicNotas['Nota3']
    sumatoria += dicNotas['Nota4']

    promedio = round(sumatoria/4, 2)

    reporteNotas = {
        'promedio': promedio,
        'estudiante': dicNotas['estudiante']
    }

    return reporteNotas

dicNotas4 = {
    'estudiante': 'Beneficiario Rodriguez',
    'Nota1' : 3.5,
    'Nota2' : 4.0,
    'Nota3' : 2,
    'Nota4' : 4.7
}

print(reportePromedio(generarReporteNotas(dicNotas4)))
