def CDT(usuario: str, capital: int, tiempo: int):
    porcentaje_interes = 0.03
    porcentaje_aperder = 0.02

    if tiempo > 2:
        valor_inte = (capital * porcentaje_interes * tiempo) / 12
        valor_total = valor_inte + capital
    else:
        valor_aperder = capital * porcentaje_aperder
        valor_total = capital - valor_aperder
    
    resultado  = "Para el usuario " + str(usuario)
    resultado += " La cantidad de dinero a recibir, según el monto inicial " + str(capital)
    resultado += " para un tiempo de " + str(tiempo) 
    resultado += " meses es: " + str(valor_total)    

    return resultado

# Recordar que el bot de la plataforma no se debe hacer impresiones (print), 
# ni llamar la función
# print(CDT("AB1012",1000000,3))