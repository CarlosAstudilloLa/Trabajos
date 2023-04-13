print("CURSO FUNDAMENTOS DE PYTHON")
print("Carlos Astudillo")
print("5/4/2023\n")
#Lista de Informacion de una persona
alumnos={"Nombre":"Juan",
         "Apellido":"Guarnizo",
         "Cedula":"0109904018",
         "Direccion":"Mexico",
         "Email":"juanguarni@gmail.com"}
print(alumnos["Cedula"])
print(alumnos["Email"])
alumnos["Cedula"]="0104006033"
alumnos["Genero"]="Masculino"
print(alumnos)

#Crear lista de Intituto
instituto={"Carreras":["Entrenamiento Deportivo","Big Data","Desarrollo de Software","Informatica,Periodismo","Gestion Patrimonio cultura"],
           "Materias":["Aprendizaje de Maquinas","Legislacion","Fundamentos de Investigacion","Base de datos","Estadistica","Python"],
           "Profesores":["Lady","Hector","Germania","Caterine","Veronica","Diana"],
           "Notas":[10,9,8,7,9,7]}
print(f"Tipos de Carreras:\n\t{instituto['Carreras']}")
print(f"Las Materias son:\n\t{instituto['Materias']}")
print(f"Los Profesores son:\n\t{instituto['Profesores']}")
print(f"Notas Finales:\n\t{instituto['Notas']}")
#Solucion 1
print(f"Solucion 1 Promedio de Big Data es:\n\t", sum(instituto["Notas"])/len(instituto["Notas"]))
#Solucion 2
suma=0
for e in instituto["Notas"]:
    suma += e
print("Solucion 2 Promedio de Big Data es:\n\t", suma/len(instituto["Notas"]))
#Solucion 3: Salga con dos decimales
print(round(suma/len(instituto["Notas"]),2))
#Nota minima con profesor y materia
nota_minima=min(instituto["Notas"])
posicion=instituto["Notas"].index(nota_minima)
print("La nota minima es: ",nota_minima)
print("Asignatura",instituto["Materias"][posicion])
print("Profesor",instituto["Profesores"][posicion])