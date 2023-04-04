print("CURSO FUNDAMENTOS DE PYTHON")
print("Carlos Astudillo")
print("30/3/2023\n")
cantidad  = float(input("Ingrese una cantidad de días: "))
if 0 <= cantidad <= 10:
    if cantidad >= 0 and cantidad < 4:
            print(f"Cantidad de días: {cantidad} \nequivalencia de HORAS")
    elif cantidad >= 4 and  cantidad < 7:
            print(f"Cantidad de días: {cantidad} \nequivalencia de MINUTOS")
    elif cantidad >= 7 and cantidad < 8:
            print(f"Cantidad de días: {cantidad} \nequivalencia de SEGUNDOS")
    else:
        cantidad >= 9
        print(f"Cantidad de días: {cantidad} \nequivalencia de EXCELENTE ")
else:
       print(f"Cantidad de días: {cantidad} \nno esta dentro del rango de DIAS")