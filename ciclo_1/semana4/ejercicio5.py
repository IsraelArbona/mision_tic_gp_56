# importar pow
from math import pow

# función pow toma dos argumentos y nos permite obtener la potencia.
#print(pow(2,3))

# si tenemos las siguientes listas.
numero   = [2,3,4,5,6,7,8,9]
potencia = [3,2,4,3,2,4,3,2]

resultado = list( map(pow,numero,potencia) )
print(resultado)

