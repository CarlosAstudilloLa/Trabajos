###CURSO DE FUNDAMENTOS DE PYTHON
#Trabajar los ejercicios con funciones, para llamarlos deberá de crear un menu en el que le permitira seleccionar al usuario que ejercicios ejecutar.
#1. Suma de elementos de una lista: Dada una lista de números, escribe un programa que calcule la suma de todos los elementos de la lista usando un bucle for.
suma_de_notas = 10
notas=[10,9,7,6]
for nota in notas:
    suma_de_notas  += nota

print(suma_de_notas)
#2. Contar elementos en una lista: Dada una lista de elementos, escribe un programa que cuente cuántos elementos hay en la lista usando un bucle for.
milistas=[1,2,3,4,5,6,7,8,9,10]
for i,v in enumerate(milistas):
    print(i,v)
#3. Imprimir elementos de una lista: Dada una lista de elementos, escribe un programa que imprima cada elemento de la lista en una línea separada usando un bucle for.
losdicionarios={"amarillo":"yellow","azul":"blue","verde":"green"}
for c in losdicionarios:
    print("imprime la lista de:",c)
#4. Contar caracteres en una cadena: Dada una cadena de caracteres, escribe un programa que cuente cuántos caracteres hay en la cadena usando un bucle for.
prefijos = "JKLMNOPQ"
sufijo = "ack"

for letra in prefijos:
    print (letra + sufijo)
#5. Imprimir caracteres de una cadena: Dada una cadena de caracteres, escribe un programa que imprima cada carácter de la cadena en una línea separada usando un bucle for.
print("Comienzo")
for i in [0, 1, 2]:
    print("Hola ")
print()
print("Final")
#6. Imprimir los primeros N números naturales: Dado un número entero N, escribe un programa que imprima los primeros N números naturales usando un bucle for.
for x in range(11):
    print(x)
#7. Imprimir los primeros N números pares: Dado un número entero N, escribe un programa que imprima los primeros N números pares usando un bucle for.
for num in range(0,11,2):
    print("imprimir los numeros pares",num)
#8. Imprimir los primeros N números impares: Dado un número entero N, escribe un programa que imprima los primeros N números impares usando un bucle for.
for num in range(0,11,3):
    print("imprimir los numeros impares",num)
#9. Imprimir la tabla de multiplicar de un número: Dado un número entero N, escribe un programa que imprima la tabla de multiplicar de N usando un bucle for.
#10. Imprimir los primeros N números de la serie de Fibonacci: Dado un número entero N, escribe un programa que imprima los primeros N números de la serie de Fibonacci usando un bucle for.