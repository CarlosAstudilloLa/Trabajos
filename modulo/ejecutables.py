from Funciones import*
from paquete.metodos import*
opcion=0
while opcion>=0 and opcion<=10:
    print("Menu de opciones")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicacion")
    print("4.Divicion")
    print("5.Suma")
    print("0.Salida")
    opcion=int(input("Ingrese una opcion: "))
    if opcion==0:
        print("Ha seleccionado la opcion salir")
        break
    elif opcion==1:
        a=int(input("Ingrese el primer numero: "))
        b=int(input("Ingrese el segundo numero: "))
        print("la suma es: ", a+b)
    elif opcion==2:
        a=int(input("Ingrese el primer numero: "))
        b=int(input("Ingrese el segundo numero: "))
        print("la resta es: ", a-b)