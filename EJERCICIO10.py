print("CURSO FUNDAMENTOS DE PYTHON")
print("Carlos Astudillo")
print("30/3/2023\n")
año =  int(input("Ingrese el año: "))

if año % 4 == 0 and año % 100 != 0:
	print(f"El año {año} si es bisiesto")
else:
    año % 100 == 0 and año % 400 != 0
    print("No es bisiesto")