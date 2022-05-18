# Bucle for
# range(start, stop, step)
# range(inicio, fin, contador)

'''
for x in range(0,4):
    print('Estamos en la iteración', x)
'''

# contador de dos en dos

'''
for x in range(0, 10, 2):
    print('Estamos en la iteración: ' + str(x))
'''

'''
for x in range(10, 0, -2):
    print('Estamos en la iteración: ', x)


for x in range(10, 0, -2):
    if x == 6:
        break
    print(x)
'''

# ejercicio 1

'''
oracion = 'Mary entiende muy bien Python'
frases = oracion.split() # Convertir a una lista cada palabra

print(type(frases))
print(frases)
print(len(frases))
print('La oración analizada es: ', oracion,'\n')

for palabra in range(len(frases)):
    print('Palabra: {}, en la frase su posición es: {}'.format(frases[palabra], palabra))

'''

# ejercicio 2
# Bucle for else

db_connection = '127.0.0.1','5432','root','nomina'
print(db_connection)

for parametro in db_connection:
    print(parametro)

print('El comando de postgreSQL es : -h {} -p {} -u {} -d {}'
.format(db_connection[0], db_connection[1], db_connection[2], db_connection[3]))    