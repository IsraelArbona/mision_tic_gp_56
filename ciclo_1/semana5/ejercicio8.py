import json
ruta = r'C:\Users\israelarbonaguerrero\Desktop\RUTA2_MISIONTIC_2022\grupo_56\ciclo_1\semana5\archivo.json'

with open(ruta) as file:

    archivo = json.load(file)

    for client in archivo['clients']:
        print('First name:', client['first_name'])
        print('Last name:', client['last_name'])
        print('Age:', client['age'])
        print('Amount:', client['amount'])
        print('')