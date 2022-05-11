# sobre una función validar si un numero es positivo y tiene dos digitos o 
# si es negativo si tiene tres digitos 
# si es cero indicar que es invalido!

def testNumero():
    entero = int(input('Digite el número: '))

    if entero == 0:
        return 'El numero es invalido o no puede ser cero'
    elif entero > 0:
        if len(str(entero)) == 2:
            return 'El número es positivo y tiene dos dígitos'
        else:
            return 'El número es positivo no tiene dos dígitos'
    else:
        if len(str(entero)) -1 == 3:
            return 'El número es negativo y tiene tres dígitos'
        else:
            return 'El número es negativo no tiene tres dígitos'

#print(testNumero())          

def testNumero2():
    numCadena = input('Digite el numero: ')

    if numCadena == '0':
         return 'El numero es invalido o no puede ser cero'
    
    elif numCadena.startswith('-'):
        if len(numCadena)-1 == 3:
            return 'El número es negativo y tiene tres dígitos'
        else:
            return 'El número es negativo no tiene tres dígitos'
    else:
        if len(numCadena) == 2:
            return 'El número es positivo y tiene dos dígitos'
        else:
            return 'El número es positivo no tiene dos dígitos'


print(testNumero2())
