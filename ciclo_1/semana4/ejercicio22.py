# libreria pandas

import pandas as pd

'''
d = {'a': 1, 'b':2, 'c':3}
serie = pd.Series(data=d,index=['a','b','c'])
print(serie)
'''

'''
ventas1 = pd.Series([12,43,25])
print(ventas1)
'''

ventas = pd.Series([12,43,25], index=['Ene','Feb','Mar'])

'''
print(ventas)
print(ventas[0])
print(ventas['Ene'])
print(ventas.dtype)

print(ventas.index)
print(ventas.values)
'''

ventas.name = 'Ventas 2022'
ventas.index.name = 'Meses'

print(ventas)
print(ventas.axes)
print(ventas.shape)