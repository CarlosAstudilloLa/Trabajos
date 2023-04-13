#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE DICCIONARIOS
#1.Crea un diccionario vacío y agrega tres elementos de la siguiente forma: "clave": valor
personas={}
personas=dict()
#2.Dado el siguiente diccionario:
personas = {"Juan": 28, "María": 20, "Pedro": 32, "Ana": 25}
#a) Imprime la edad de Juan.
print(personas.get)
#b) Agrega un nuevo elemento al diccionario con la clave "Luis" y la edad 18.
personas["Luis"]="18"
print(personas)
#c) Elimina el elemento con la clave "Pedro".
personas.pop("Pedro")
print(personas)
#3.Dado el siguiente diccionario:
ventas = {"manzanas": 10, "naranjas": 5, "peras": 8}
#a) Imprime la cantidad de manzanas vendidas.
print(ventas["manzanas"])
#b) Agrega 3 elementos más al diccionario: "limones": 12, "sandías": 3, "melones": 5.
print(ventas["limones":12])
print(ventas["sandias":3])
print(ventas["melones":5])
#c) Imprime las claves del diccionario.
print(ventas.keys())
#4. Dado el siguiente diccionario:
alumnos = {"Juan": {"edad": 22, "promedio": 8.5}, "María": {"edad": 20, "promedio": 9.0}, "Pedro": {"edad": 25, "promedio": 7.5}}
#a) Imprime la edad de Juan.
print(alumnos["Juan"]["edad"])
#b) Imprime el promedio de María.
print(alumnos["Maria"]["promedio"])
#c) Agrega un nuevo elemento al diccionario con la clave "Ana" y los valores "edad": 19 y "promedio": 8.0.
alumnos["Ana"]={"edad":19,"promedio":9}
#5. Dado el siguiente diccionario:
empleados = {"Juan": {"departamento": "Ventas", "sueldo": 1500}, "María": {"departamento": "Contabilidad", "sueldo": 1800}, "Pedro": {"departamento": "Ventas", "sueldo": 1700}, "Ana": {"departamento": "Recursos Humanos", "sueldo": 1900}}
#a) Imprime el sueldo de Pedro.
print(empleados["sueldo"])
#b) Cambia el sueldo de Ana a 2000.
empleados.pop("sueldo")
print("Ana")
print(empleados.get("1900","No se encuentra en el diccionario"))
empleados["2000"]="Ana"
print(empleados)
#c) Crea un nuevo diccionario con los empleados del departamento de Ventas.
empleados = {"Juan":{"departamento":"Ventas", "sueldo": 1500},"Pedro": {"departamento": "Ventas", "sueldo": 1700}}
#6.Dado el siguiente diccionario:
cursos = {"Pedro": ["Matemáticas", "Biología", "Historia"], "María": ["Física", "Química", "Literatura"]}
#a) Imprime las materias en las que está inscrito Pedro.
print(cursos["Pedro"]["matematicas"]["computacion"]["Biologia"]["Calculo"])
#b) Agrega una materia más a la lista de materias de María: "Programación".
cursos["Programacion"]="Maria"
print(cursos)
#c) Crea un nuevo diccionario con los estudiantes que están inscritos en la materia de Biología.
cursos = {"Biologia":{"Pedro", "Maria"}}
#7. Dado el siguiente diccionario:
precio = {"manzanas": 10, "naranjas": 5, "peras": 8}
#a) Imprime el precio de las naranjas.
print(precio["naranjas"])
#b) Cambia el stock de peras a 12.
precio.pop("stock")
print("peras")
print(precio.get("8","No se encuentra en el diccionario"))
precio["12"]="peras"
print(precio)
#c) Crea una función que calcule el valor total de los productos en el diccionario.
