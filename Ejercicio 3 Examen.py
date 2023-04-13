#Dado el siguiente diccionario:
personas = {"Juan": 28, "María": 20, "Pedro": 32, "Ana": 25}
#a) Imprime la edad de Juan.
print(personas["Juan"]["edad"])
#b) Agrega un nuevo elemento al diccionario con la clave "Luis" y la edad 18.
personas["Luis"]={"edad":18}
#c) Elimina el elemento con la clave "Pedro".
personas.pop("Pedro")
print(personas)