# Ciclos While

'''
n = 5
while n > 0: # -> condición para realizar cada iteración
    print(n)
    n = n - 1
print('Fin')
'''

# break -> nos permite terminar el ciclo.

'''
while True:    
    numero = int(input('Ingrese un número: '))
    if numero % 2 == 0:
        print('El número es par')
        break
    else: 
        print('El número es impar')
        break
'''

'''
n = int(input('Por favor, ingresa un número mayor que cero: '))
while n > 0:
    print(n)
    print('Correcto!')
    break
'''

'''
n = int(input('Por favor, ingrese un número positivo'))

while n > 0:
    print(n)
    n = n-1
print('Finalizar') 
'''

# ejercicio 2
# Alejarse de terminación

'''
i = 1
while i > 0:
    print(i)
    i += 1
print('Terminar')
'''

# ejercicio 3
# Brincarse la meta

'''
i = 1
while i != 10:
    print(i)
    i += 2
print('Fin')
'''

# ejercicio 4
# Problemas de indentación

'''
n = 1
while n<10:
    print(n)
n = n+1
print('Finalizar')
'''

# ejercicio 5
# olvidar el avance

'''
i = 1
while i<10:
    print(i)
print('Finalizar')
'''

# ejercicio 6
# Mostrar los primero 40 número de 100

'''
n = 1
while n<=100:
    print(n)
    if n == 40:
        break
    n += 1
print('Finalizar')
'''

'''
n = 1
while n < 100:
    if n > 0 and n <= 40:
        print(n)
    else:
        break
    n = n + 1
'''

# ejercicio 7
# continue -> omitir las lineas siguientes de bloque del ciclo.

# mostrar los primero 5 número impares saltando el cuarto número.

'''
    1
    3
    5

    9
    11
'''

'''
n = -1
while n != 11:
    n = n + 2
    if n == 7:
        continue
    print(n)
'''

'''
var = -1
while var<11:
    var += 2
    if var == 7:
        continue
    print('Valor variable es: ', var)
'''

'''
i = 0 
impar = -1
while i <= 5:
    impar += 2
    i += 1
    if i == 4:
        continue
    print(impar)
'''

# ejercicio 8 
# Bucle while controlado por evento

'''
acuNotas, promedio, conNotas = 0,0.0,0

print('Introduzca la nota de un estudiante ( -1 para salir): ')
calif = int(input())

while calif != -1:
    acuNotas += calif
    conNotas += 1
    print('Introduzca la nota de un estudiante ( -1 para salir): ')
    calif = int(input())

promedio = acuNotas/conNotas
print('Promedio de notas de los estudiantes es ' + str(promedio))
'''

'''
acuNotas, promedio, conNotas = 0,0.0,0
mensaje = 'Introduzca la nota de un estudiante ( -1 para salir): '
calif = int(input(mensaje))

while calif != -1:
    acuNotas += calif
    conNotas += 1
    calif = int(input(mensaje))
else:
    if acuNotas != 0:
        promedio = round(acuNotas/conNotas,1)
        print('Promedio de notas de los estudiantes es ' + str(promedio))
    else:
        print('No existen Notas')
'''

'''
a, b = 0, 1
while b < 100:
    print(b)
    a, b = b , a + b
'''




