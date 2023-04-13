print("CURSO FUNDAMENTOS DE PYTHON")
print("Carlos Astudillo")
print("5/4/2023\n")
#Crear una lista de ventas
listas=[10,20,30,40,50,60,70,80]
print("Imprimir",[listas])
#Remplazar el valor
listas[4]=100
print(listas)
#Agregar valores append
listas.append(120)
#Ingresar listas con bucle for
for e in listas:
    print(e)
#Ordenar las listas
listas.sort()
print(listas)
#Agregar comando len
print(len(listas))
#Verificar si estan en el comando listas
print("Imprimir",listas.count(120),"Imprimir")
#Ejercicio
numeros=[]
for e in range(5):
    print("Muestras los numeros",(numeros))
#Muestra los nombres de tus amigos
llaves=["Sandro","Sebastian","Ariel","Bruce","Paul","Jhonatan"]
print("Imprimir el primer ", llaves[0])
#Crear una lista de nnumeros pares
numeros1=[1,2,3,4,5,6,7,8,9,10]
for e in numeros1:
    if e % 2 == 0:
        print(f"El numeros es par: {e} ")
#Eliminar le ultimo elemento de la lista de amigos
print("Imprimir el ultimo",llaves[-1])
#Añade un nuevo amigo
llaves=["Sandro","Sebastian","Ariel","Bruce","Paul","Jhonatan"]
llaves.insert(2,"Adri")
print(llaves)
#Muestra el primer y ultimo
numeros=[1,2,3,4,5,6,7,8,9,10]
print(f"El primer elemento de la lista es: {numeros[1]} \n\t y el ultimo elemento es: {numeros[-1]}")
#Contar los valores de los nombres
llaves=["Sandro","Sebastian","Ariel","Bruce","Paul","Jhonatan"]
print("Imprimir los numeros",len(llaves))
#Realizar la suma de los numeros
numeros=[1,2,3,4,5,6,7,8,9,10]
suma=0
for e in numeros:
    suma = e + suma
print(suma)