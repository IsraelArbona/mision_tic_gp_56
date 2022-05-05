# crear función
def nombre_genero(letraGenero):
    pass # no se va a realizar ninguna secuencia en el función
    # return letraGenero

# print(nombre_genero("m"))

# realizar una función que permita obtener el primedio de cuatro notas
# y que el resultado sea un numero entero

nota1 = 3.7
nota2 = 2.4
nota3 = 4.7
nota4 = 3.2

def calcularPromedio1(a,b,c,d):
    resultado = (a + b + c + d)/4
    return resultado

# print(int(calcularPromedio1(nota1, nota2, nota3, nota4)))

def calcularPromedio2(nota1,nota2,nota3,nota4):
    promNotas = (nota1 + nota2 + nota3 + nota4)/4
    return int(promNotas)

# print(calcularPromedio2(nota1, nota2, nota3, nota4))

def calcularPromedio3(nt1,nt2,nt3,nt4):
    result = (nt1+nt2+nt3+nt4)/4
    return round(result)

# print(calcularPromedio3(nota1, nota2, nota3, nota4))


# crear función con sum(), len() para calcular el promedio
def cal_promedio(lista_notas):
    result = (sum(lista_notas)/len(lista_notas))
    return int(result)

notas = (3.7,2.4,4.7,3.2)
notas2 = (3.7,4.5,2.5,3,4,1.6,1)

'''
print(type(notas))
print(cal_promedio(notas))
print(cal_promedio(notas2))
'''