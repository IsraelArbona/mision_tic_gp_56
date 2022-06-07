# libreria pandas - diccionarios
import pandas as pd

unidad_2016 = {'Ag':2, 'Au':5, 'Cu':3, 'Pt':2}
unidad_2017 = {'Ag':4, 'Au':6, 'Cu':7, 'Pt':2}
unidad_2018 = {'Ag':3, 'Au':2, 'Cu':4, 'Pt':1}

unidades = pd.DataFrame([unidad_2016,unidad_2017, unidad_2018],
                        index=[2016,2017,2018])

print(unidades)