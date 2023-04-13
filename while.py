###CURSO DE FUNDAMENTOS DE PYTHON
###Carlos Astudillo
###11/04/2023
#Trabajar los ejercicios con funciones, para llamarlos deberá de crear un menu en el que le permitira seleccionar al usuario que ejercicios ejecutar.
#1.Contador ascendente: # Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, cuente desde cero hasta ese número, imprimiendo cada número en la pantalla.
def contador_Ascendente(num):
    cadena=""
    contador=0
    while contador <=num:
        cadena=cadena+str(contador)+"\n"
        contador+=1
    return cadena
num=int(input("Ingrese un numero: "))
print(contador_Ascendente(num))
#2.Contador descendente: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, cuente desde ese número hasta cero, imprimiendo cada número en la pantalla.
def contador_Descendente(num):
    cont=num
    while cont>=0:
        print(cont)
        cont-=1
num=int(input("Ingrese un numero: "))
contador_Descendente(num)
#3.Suma de números: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule la suma de todos los números desde cero hasta ese número y lo imprima en la pantalla.
def sumanumeros(num):
    cont=0
    suma=0
    while cont <=num:
        cont+=1
        suma+=cont
    return suma-(num+1)
num=int(input("Ingrese un numero: "))
print(sumanumeros(num))
#4.Factorial: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule el factorial de ese número y lo imprima en la pantalla. El factorial de un número n se define como el producto de todos los números enteros desde 1 hasta n.
def factorial(num):
    cont=0
    mul=0
    while cont<=num:
        cont+=1
        mul=cont*mul
    return mul
num=int(input("Ingrese un numero: "))
print(factorial(num))
#5.Adivinar un número: Escribe un programa en Python que genere un número aleatorio entre 1 y 100, y pida al usuario que adivine ese número. Si el usuario ingresa un número mayor al número generado, el programa debe imprimir "El número que buscas es menor". Si el usuario ingresa un número menor al número generado, el programa debe imprimir "El número que buscas es mayor". Si el usuario adivina el número, el programa debe imprimir "¡Felicitaciones, adivinaste el número!" y terminar.
import random
def adivinar_numero(num_generado):
    adivinanza=0
    while adivinanza!=num_generado:
        adivinanza=int(input("Adivina el numero entre el 1 y 100: "))
        if adivinanza>num_generado:
            print("El numero que buscas es menor")
        if adivinanza<num_generado:
            print("El numero que buscas es mayor")
        else:
            print("¡Felicitaciones, adivinastes el numero!")
num_generado=random.randint(1,100)
print("El numero que se genero es: ",str(num_generado))
adivinar_numero(num_generado)
#6.Contador de vocales: Escribe un programa en Python que pida al usuario una cadena de texto y, utilizando un bucle while, cuente la cantidad de vocales que tiene esa cadena. Para simplificar el problema, puedes considerar que la cadena solo contiene letras minúsculas.
def contador_vocales(letra):
    if letra in "aeiouAEIOU":
        print("Es vocal")
    else:
        print("No es una vocal")
#7.Suma de números pares: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule la suma de todos los números pares desde cero hasta ese número y lo imprima en la pantalla.
def suma_Pares(num):
    print("Ingree el numero inicial")
    i=int(input())
    print("Ingrese el numero final")
    f=int(input())
    suma=0
    print("Los numeros pares del rango")
    while i <= f:
        if i % 2 == 0:
            print(i)
            suma=suma+i
        i+=1
    print("La suma de los numeros es: ",suma)
#8.Cálculo de potencia: Escribe un programa en Python que pida al usuario dos números enteros positivos: una base y un exponente. Utilizando un bucle while, calcule la potencia de la base elevada al exponente y lo imprima en la pantalla.
def potencia(numero,exponente):
    resultado=1
    cont=1
    while cont<=exponente:
        resultado=resultado*numero
        cont+=1
    print(resultado)
#9.Cálculo de promedio: Escribe un programa en Python que pida al usuario una lista de números y, utilizando un bucle while, calcule el promedio de esos números y lo imprima en la pantalla.
def promedio(lista_numeros):
    numeros=[]
    print("Cuantos numeros ingresara")
    n=int(input())
    i=0
    while i < n:
        print("Valor numero: ",i+1)
        val=float(input())
        num.append(val)
        i+=1
    promedio=sum(num)/len(num)
    print("El promerdio es: ",promedio)
#10.Contador de palabras: Escribe un programa en Python que pida al usuario una cadena de texto y, utilizando un bucle while, cuente la cantidad de palabras que tiene esa cadena. Para simplificar el problema, puedes considerar que las palabras están separadas por espacios en blanco.
def contador_Palabras(cadena):
    contador=0
    indice=0
    while indice<len(cadena):
        if cadena[indice]=="":
            contador+=1
            indice+=1
    print("La cadena de texto tiene",contador,"palabras.")
    if len(cadena)==0:
        contador=0
    else:
        contador=1
####MENU DE OPCIONES####
opcion=1
while opcion>=0 and opcion<=10:
    print("######Menu de Opciones######")
    print("1. Contador Ascendente")
    print("2. Contador Descendente")
    print("3. Suma de numeros")
    print("4. Factorial")
    print("5. Adivinar un numero")
    print("6. Contador de vocales")
    print("7. Suma de numeros pares")
    print("8. Calculo de potencia")
    print("9. Calculo de promedio")
    print("10. Contador de palabras")
    print("0. Salir")
    opcion=int(input("Ingrese una opcion: "))
    if opcion==0:
        print("Ha seleccionado salir")
        break
    elif opcion==1:
        num=int(input("Ingrese un numero entero positivo: "))
        contador_Ascendente(num)
    elif opcion==2:
        num=int(input("Ingrese un numero entero positivo: "))
        contador_Descendente(num)
    elif opcion==3:
        num=int(input("Ingrese un numero entero positivo: "))
        sumanumeros(num)
    elif opcion==4:
        num=int(input("Ingrese un numero entero positivo: "))
        factorial(num)
    elif opcion==5:
        import random
        num_generado=random.randint(1, 100)
        adivinar_numero(num_generado)
    elif opcion==6:
        num=int(input("Ingrese un numero entero positivo: "))
        contador_vocales(cadena)
    elif opcion==7:
        num=int(input("Ingrese un numero entero positivo: "))
        suma_Pares(num)
    elif opcion==8:
        base=int(input("Ingrese la base: "))
        exp=int(input("Ingrese el exponente: "))
        potencia(base,exp)
    elif opcion==9:
        numeros=input("Ingrese una lista de numeros separados por comas: ")
        promedio(numeros)
    elif opcion==10:
        cadena=input("Ingrese una cadena de texto: ")
        contador_Palabras(cadena)
    else:
        print("Ha ingresado un valor diferente del menu")