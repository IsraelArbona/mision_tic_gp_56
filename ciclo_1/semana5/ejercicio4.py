# libreria pandas - leer archivo excel

import pandas as pd

ruta = r'C:\Users\israelarbonaguerrero\Desktop\RUTA2_MISIONTIC_2022\grupo_56\ciclo_1\semana5\archivo.xlsx'

datosDataFrame = pd.read_excel(ruta,sheet_name='personas')
print(datosDataFrame)
print()

datosDataFrame = pd.read_excel(ruta,sheet_name='personas', header=None, skiprows=1)
print(datosDataFrame)
print()

datosDataFrame = pd.read_excel(ruta,sheet_name='personas', header=None, skiprows=1,
                                names=['Id','Pr Nombre','Sg Nombre','Edad','Salario 1','Salario 2'])
print(datosDataFrame)
print()