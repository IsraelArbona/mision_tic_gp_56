# Función map
# map: función que toma dos argumentos.
# map: función secuencial, donde secuencia puede ser cualquier estructura.

'''
def cuadrado(elemento = 0):
    return elemento * elemento

lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)

resultado = list(map(cuadrado, lista))
print(resultado)

resultado2 = list( map(lambda ele = 0 : ele * ele,lista) )
print(resultado2)
'''

def factorial(numero = 0):
    contar = 2
    resultado = 1
    while contar <= numero:
        resultado *= contar
        contar += 1
    return resultado

# print(factorial(3))

lista = [2,4,6,8,10]
resultado = list( map(factorial,lista) )
print(resultado)