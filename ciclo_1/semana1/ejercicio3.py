# Creación de funciones
def imprime_Cosas():
    print("La clase esta genial")
    print("Python es lo mmáximo")
    #print("continuar..")

def repetir_funciones():
    print("\n")
    imprime_Cosas()
    imprime_Cosas()

#repetir_funciones()

# Llamar la funcion imprime_Cosas
#imprime_Cosas()




# Creamos la función operacionSuma de dos variables
def operacionSuma():
    a = 45
    b = 15
    suma = a + b
    return "La suma de " + str(a) + " + " + str(b) + " es igual a: " + str(suma)
    #return "La suma de ",a," + ",b," es igual a: ",suma

resultado = operacionSuma()
#print(type(resultado))
#print(resultado)
#print(operacionSuma())

def operacionSumaP():
    a = 3
    b = 7
    suma = a + b
    print("La suma de",a,"+",b, "es igual a:",suma)

#operacionSumaP()

def sumarDosnumeros():
    num1 = float(input("Ingrese el numero 1 : "))
    num2 = float(input("Ingrese el numero 2 : ")) 
    print("la suma de", int(num1),"+", int(num2),"es igual a",int(num1 + num2))

# sumarDosnumeros()

def raizCuadrada():
    valor = float(input("Por favor, introduzca un numero a calcular la raiz cuadrada "))
    raiz = valor ** 0.5
    return print("La raiz cuadrada del valor : ", valor, "es",raiz)

raizCuadrada()