print("CURSO FUNDAMENTOS DE PYTHON")
print("Carlos Astudillo")
print("30/3/2023\n")
calificacion  = float(input("Ingrese su calificacion: "))
if 0 <= calificacion <= 10:
    if calificacion >= 0 and calificacion < 4:
            print(f"Su nota de: {calificacion} \nequivalencia de DEFICIENTE")
    elif calificacion >= 4 and  calificacion < 7:
            print(f"Su nota de: {calificacion} \nequivalencia de REGULAR")
    elif calificacion >= 7 and calificacion < 8.5:
            print(f"Su nota de: {calificacion} \nequivalencia de BUENO")
    elif calificacion >= 8.5 and calificacion < 9.5:
            print(f"Su nota de: {calificacion} \nequivalencia de MUY BUENO")
    else:
        calificacion >= 9.5
        print(f"Su nota de: {calificacion} \nequivalencia de EXCELENTE ")
else:
       print(f"Su nota de: {calificacion} \nno esta dentro del rango de las CALIFICACIONES")