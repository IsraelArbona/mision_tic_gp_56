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



'''
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
'''


def raizCuadrada():
    valor = float(input("Por favor, introduzca un numero a calcular la raiz cuadrada "))
    raiz = valor ** 0.5
    return print("La raiz cuadrada del valor : ", valor, "es",raiz)

# raizCuadrada()


b = 5
a = 15

def suma(a,b):
    return a + b

B = 30
A = 10

#print(suma(A,B))
#print(suma(a,b))

#resultado = suma(5,3)
#print(resultado)

def mi_funcion(nombre,apellido):
    miNombre = nombre + apellido
    return miNombre

# print(mi_funcion("Luis ", "Morelo"))

def saludar(nombre,mensaje = "Hola"):
    print(mensaje,nombre)

# saludar("Pepe Grillo")


def mensaje():
    print("Ingrese por favor un valor")

def sumarDosnumeros():
    mensaje()
    num1 = float(input())
    mensaje()
    num2 = float(input())
    return print("La suma de", num1,"+",num2,"es igual a:",num1 + num2)

#sumarDosnumeros()

'''
#Crear la función
def primeraFuncion(): # función externa
    print("\n \"Hola desde la función externa\" \n")
    def segundaFuncion():
        print("\n \"Hola desde la función interna\" \n")

    #Llamar la función
    segundaFuncion()

# Llamar la función
#primeraFuncion()
'''



'''
def primerNumero(x):
    def segundoNumero(y):
        return x * y
    return segundoNumero

resultado = primerNumero(2)

# print(resultado)

print(type(resultado))
print(type(resultado(5)))
print(resultado(5))
'''

def primeraFuncion():
    x = 2

    #Creando la función segundoFuncion
    def segundaFuncion(a):
        x = 6
        print(a + x)
    
    #llamamos la función
    segundaFuncion(3)
    print(x)

#llamamos la función
primeraFuncion()