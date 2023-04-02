print("CURSO FUNDAMENTOS DE PYTHON")
print("Carlos Astudillo")
print("30/3/2023\n")
nombre=input("igresar su nombre: ")
edad=int(input("ingresar su edad "))
if edad>=18:
    print(nombre, "es mayor de edad")
elif edad<18:
    print(nombre, "es menor de edad")