# libreria pandas - creación de series

import pandas as pd

'''
s = pd.Series([7,5,6])
print(s)
s = pd.Series([7,6,5], index=['Ene','Feb','Mar'])
print(s)
'''

# utlizando un diccionario

'''
d = {'Ene': 7, 'Feb':5, 'Mar': 6}
s = pd.Series(d)
print(s)
s = pd.Series(d,index=['Abr','Mar','Feb','Ene'],dtype=int)
print(s)
'''

# Utilizando un escalar

s = pd.Series(8,index=['Ene','Feb','Mar'])
print(s)