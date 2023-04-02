print("CURSO FUNDAMENTOS DE PYTHON")
print("Carlos Astudillo")
print("30/3/2023\n")
letra=input("Ingrese su letra: ")
letra=letra.lower()
if len(letra) !=1:
    print("No de puede proceder el dato, debe ingresar una sola letra")
elif letra in ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    print("Es una letra del avecedario")
else:
    print("No es una letra del avecedario")