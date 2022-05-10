# Formas de clasificación de condiciones

'''
# condiciín simple
if:

if: 
else:


horaDelDia = 7

if horaDelDia >= 12:
    print("PM")
else:
    print("AM")
'''

'''
# condiciones secuenciales

if:
if:
if:
if:

resultadoDelExamen = 78

if resultadoDelExamen > 60:
    print("aprobado")
if resultadoDelExamen > 90:
    print("Excelente trabajo")
'''

'''
num = input('Por favor, digite un numero entero: ')
num = int(num)

if num < 0:
    num = num * ( -1 )

if (num >= 1) and (num <= 9):
    print("El número tiene 1 dígito")
else:
    if num >= 10 and num <= 99:
        print("El número tiene 2 dígitos")
    else:
        if num >= 100 and num <= 999:
            print("El número tiene 3 dígitos")
        else:
            if num >= 10000 and num <= 9999:
                print("El número tiene 4 dígitos")
            else:
                print("El número tienas mas de 4 dígitos")


if num < 0:
    num *= -1

if num > 0 and num < 10:
    print("El número tiene 1 dígito")
elif num > 9 and num < 100:
    print("El número tiene 2 dígitos")
elif num > 99 and num < 1000:
    print("El número tiene 3 dígitos")
elif num > 999 and num < 10000:
    print("El número tiene 4 dígitos")
else:
    print("El número tiene mas de 4 dígitos")
'''


num = int(input('Digite un número entero: '))

if num > 0:
    if num > 9 and num < 100:
        print('El número es positivo y tiene dos dígitos')
    else:
        print('El número es positivo no tiene dos dígitos')
else:
    if num > -1000 and num < -99:
        print('El número es negativo y tiene tres dígitos')
    else:
        if num == 0:
            print('Número invalido!')
        else:
            print('El número es negativo no tiene tres dígitos')
    

