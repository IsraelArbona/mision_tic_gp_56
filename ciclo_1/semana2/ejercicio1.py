# condicionales

'''
var1 = 5
var2 = 5

print(var1 > var2)
print(var1 < var2)
print(var1 != var2)
print(var1 == var2)
'''

'''
x = 10

if x > 0:
    print('x es un número positivo')
'''


'''
# determinar si un número es par o impar
x = 32
if x % 2 == 0:
    print('x es par')
else:
    print('x es impar')
'''

# dado dos variables determinar si es mayor, menor o igual

'''
x = 10
y = 20

if x < y:
    print('"x" es menor que "y"')
elif x > y:
    print('"x" es mayor a "y"')
else:
    print('"x" y "y" son iguales')
'''

'''
letra = 'a'

if letra == 'a':
    print('Mal Resultado')
elif letra == 'b':
    print('Buen Resultado')
elif letra == 'c':
    print('Cerca, pero no es correcto')
'''

x = 9
y = 32

'''
if x == y:
    print('x es igual a y')
else:
    if x > y:
        print('x es mayor a y')
    else:
        print('x es menor a y')
'''

temperatura_fahr = input('Ingrese la temperatura en grados fahr: ')

try:
    fahr = float(temperatura_fahr)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Numero invalido')