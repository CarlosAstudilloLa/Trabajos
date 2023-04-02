print("FUNDAMENTOS DE PROGRAMACION DE PYTHON")
print("Carlos Astudillo")
print("30/03/2023")
renta=float(input("El valor de la renta "))
tax=0
if renta <10000:
    tax=5/100
elif renta>=10000 and renta <=20000:
    tax=10/100
elif renta>=20000 and renta <=35000:
    tax=15/100
elif renta>=35000 and renta <=60000:
    tax=20/100
elif renta >60000:
    tax=30/100
print("El valor de la renta total es "+ str(tax) + "%")