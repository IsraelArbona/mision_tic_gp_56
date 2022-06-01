# Función reduce (importante importar)
from functools import reduce

lista = [1,2,3,4,5,6,7,8,9]

acumulador = 0
for elemento in lista:
    acumulador += elemento

print(acumulador)

resultado = sum(lista)
print(resultado)

def funcion_acumular(acumulador = 0, elemento = 0):
    return acumulador + elemento

# print(funcion_acumular(10,5))

resultado = reduce(funcion_acumular, lista)
print(type(resultado))
print(resultado)

resultado = reduce( lambda acumulador=0, elemento=0: acumulador + elemento, lista)
print(resultado)