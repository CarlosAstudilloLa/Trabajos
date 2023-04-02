print("CURSO FUNDAMENTOS DE PYTHON")
print("Carlos Astudillo")
print("30/3/2023\n")
a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
c=int(input("Ingrese el terser numero: "))
if a>b and a >c :
    print ("El numero ",a ," es mayor al segundo y tercer numero")
elif b>a and b >c :
    print ("El numero ",b ," es mayor al primer y tercer numero")
elif c>b and c >a :
    print ("El numero ",c ," es mayor al primer y segundo numero")
else :
    print ("Ninguno es mayor ")