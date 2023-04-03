print("CURSO FUNDAMENTOS DE PYTHON")
print("Carlos Astudillo")
print("30/3/2023\n")
palabra = input("Ingrese la palabra a comprobar: ")
if str(palabra) == str(palabra)[::-1]:
    print(f"La palabra ingresada {palabra},si es un Palindromo")
else:
    print(f"La palabra ingresada {palabra},no es Palindromo")