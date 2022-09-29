def calculo_salario(horas,tarifa):
    MAXH = 40
    if(horas > MAXH):
        horas_extra = int(horas) - MAXH
    else:
        horas_extra = 0
    calculo = (int(horas)* int(tarifa)) + (horas_extra * (int(tarifa)/2))
    return calculo
print("este programa tiene el fin de calcular su salario a partir de horas semanales de trabajo")
horas = float(input("ingrese las horas trabajadas: "))
tarifa = float(input("ingrese tarifa: "))
pago = calculo_salario(horas, tarifa)
print(pago)
