#Las tuplas no se pueden modificar

miTupla = ("Juan", 2, 6, 1997, 2,2)
print(miTupla[2])

#convertimos la tupla en una lista
miLista =list(miTupla)

print("#######################################")
print(miTupla)
print(miLista)

#convertir una Lista en una tupla
miLista2 = ["lalo", "pedro", "octavio"]
miTupla2 = tuple(miLista2)

print("#######################################")
print(miTupla2)
print(miLista2)

#Comprobar si hay algun elemento en la tupla
print("#######################################")
print("juan" in miTupla)

#Comprobar cuantas veces hay un elemento en la tupla
print("#######################################")
print(miTupla.count(2))

#Comprobar cuantos elemento hay en la tupla
print("#######################################")
print(len(miTupla))

#Tuplas unitarias
print("#######################################")
tuplaUnitaria = ("Jasubi",)
print(len(tuplaUnitaria))

#Desempaquetado de tuplas
#Asignamos los elementos de las tuplas a variables
print("#######################################")
miTupla3 = ("Jasubi", 17, 7, 1997)
nombre, dia, mes, agno = miTupla3

print(nombre, dia, mes, agno)