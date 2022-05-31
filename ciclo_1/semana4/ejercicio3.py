# Funciones Anónimas (lambda)

#def sumar(val1 = 0, val2 = 0):
#    return val1 + val2

'''
sumar = lambda val1 = 0, val2 = 0 : val1 + val2

print(sumar(5 + 10))

operacion = lambda operacion, val1 = 0, val2 = 0 : operacion(val1,val2)

resultado = operacion(sumar,43,77)
print(resultado)
'''

# Funciones anónimas sin parametros de entrada.

'''
sin_parametros = lambda : True
print(sin_parametros() == True)
'''

# Funciones anónimas con varios argumentos.
# *args -> significa que cero o mas argumentos que se almacenan en un tupla

'''
con_valores = lambda val, val1= 0, val2= 0 : val + val1 + val2
resultado = con_valores(13,43,25)
print(resultado) 
'''

'''
con_asteristo = lambda *args : args[2]
lista = [1,2,3,4,5,6,7,8,9]

resultado = con_asteristo(*lista)
print(resultado)


def suma(*valor):
    return sum(valor)

resultado = suma(1,2,3,4,5,6,7,8,9)
print(resultado)
'''



# **kwargs -> crea es un diccionario.

'''
diccionario = {
    '0' : 1,
    '1' : 2,
    '2' : 4,
    '3' : 5
}

con_doble_asterisco = lambda **kwargs : kwargs['2']

resultado = con_doble_asterisco(**diccionario)
print(resultado)
'''

lista = [1,2,3,4,5,6,7,8,9]

diccionario = {
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5 
}

con_asteriscos = lambda *args, **kwargs : sum(args) + sum(kwargs.values())

resultado = con_asteriscos(*lista,**diccionario)
print(resultado)
