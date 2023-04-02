print("CURSO FUNDAMENTOS DE PYTHON")
print("Carlos Astudillo")
print("30/3/2023\n")
valor_1=int(input("valor 1 = "))
valor_2=int(input("valor 2 = "))
valor_3= valor_1 + valor_2
valor_4= valor_1 - valor_2
valor_5= valor_1*valor_2
print("Presione 1 para sumar")
print("Presione 2 para restar")
print("Presione 3 para multiplicar")
opción= input("Que opción desea:")
if opción=="1":
    print("La suma de los valores es", valor_3)
elif opción=="2":
    print("La resta de los valores es", valor_4 )
elif opción=="3":
    print("La multiplicación es", valor_5)
else:
    print("No es correcta la opcion")