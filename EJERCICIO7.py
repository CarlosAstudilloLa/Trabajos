print("CURSO FUNDAMENTOS DE PYTHON")
print("Carlos Astudillo")
print("30/3/2023\n")
print("Bienvenido a la pizzeria La Carroza, Tipo1 Familiar - Tipo2 Mediana")
tipo=input("Ingrese el tipo de pizza que desea: ")
if tipo=="1":
    print("Ingrese ingredientes de pizza familiar, 1-Jamon - Chorizo, 2-Salami - Salchicha")
ingredientes=input("Ingrese el tipo de ingredientes que quiere")
if ingredientes=="1":
    print("Jamon - Chorizo")
if ingredientes=="2":
    print("Salami - Salchicha")
else:
    print("Nada solo Queso")