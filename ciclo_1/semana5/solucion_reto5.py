import pandas as pd

rutaFileCsv = 'https://raw.githubusercontent.com/luisguillermomolero/MisionTIC2022_2/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv'

def listaPeliculas(rutaFileCsv: str)->str:
    # print(rutaFileCsv.split('.')[-1])
    
    #validar extensión csv
    if rutaFileCsv.split('.')[-1] == 'csv':
        try:
            # Leer el archivo csv
            arcCsv = pd.read_csv(rutaFileCsv)
            #print(arcCsv)

            # Se crea un subconjunto con las columnas 'Country','Language' e 'Gross Earnings'.
            subGrupoPeliculas = arcCsv[['Country','Language','Gross Earnings']]
            #print(subGrupoPeliculas) 

            # Se usa las columnas 'Country' y 'Language' como índice para la tabla dinamica y 'Gross Earnings' como tabla de resumen
            gananciaPaisLenguaje = subGrupoPeliculas.pivot_table( index=['Country','Language'])
            
            return gananciaPaisLenguaje.head(10)

        except:
            print('Error al leer el archivo de datos.')
    else:
        print('Extensión inválida.')


print(listaPeliculas(rutaFileCsv))
