# leer o escribir en archivo txt
 
datos = ['linea 1','linea 2','linea 3','linea 4','linea 5']

ruta = r'C:\Users\israelarbonaguerrero\Desktop\RUTA2_MISIONTIC_2022\grupo_56\ciclo_1\semana5\archivo.txt'
fichero = open(ruta,'w')

for i in range(1001):
    for li in datos:
        var = str(i) + ', ' + li
        fichero.write(var)
    fichero.write('\n')
    
fichero.close()