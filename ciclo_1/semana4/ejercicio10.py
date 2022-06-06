uids = ['B1CD102354','B1CDEF2354','MST213112','B1RJSO12$']

for uid in uids:
    cond = list()
    print(cond)
    # Por lo menos dos letras mayúsculas en el alfabeto ingle
    cond.append(len(list(filter(lambda x : x.isupper(),list(uid)))) >= 2)
    # Por lo menos tiene tres digitos
    cond.append(len(list(filter(lambda x : x.isdigit(),list(uid)))) >= 3)
    # Solo digitos alfanuméricos
    cond.append(len(list(filter(lambda x : not(x.isalnum()), list(uid)))) == 0)
    # Que no existan repeticiones
    cond.append(len(uid) == len(set(uid)))
    # Exactamente que contenga 10 caracteres
    cond.append(len(uid) == 10)

    print(cond) 
    print('Válido' if all(cond) else 'Inválido')