def calcula_calificacion(nota):
    if (nota >=0.9 and nota <=1.0):
         nota = "sobresaliente"
    elif (nota >0.8 and nota <=0.9):
            nota = "notable"
    elif (nota >0.7 and nota <=0.8):
            nota = "bien"
    elif (nota >0.6 and nota <=0.7):
            nota = "suficiente"
    elif (nota <= 0.6 and nota <=0.6):
            nota = "insuficiente"
    else:
        nota = "calificacion no valida"
    return nota

try:
    calificacion = float(input("ingrese la calificacion(0.1-1.00: "))
    nota = calcula_calificacion(calificacion)
    print ("su calificacion es: " , nota)
except:
        print( "error, calificacion no valida")
