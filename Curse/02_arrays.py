miLista = ["Maria",5, True, "Antonio"]

#print(miLista[:])
#print(miLista[3])
#print(miLista[-2])
#print(miLista[0:3])
#print(miLista[1:3])

#añadir un elemento al final de la lista
miLista.append("Sandra")

print(miLista[:])

#añadir varios Elementos al final de la lista
miLista.extend(["Samuel", "Ana", "Gerardo"])

print(miLista[:])

#Saber el indice de un elemento
print(miLista.index("Samuel"))

#Saber si el elemento existe en la lista
print("Pepe" in miLista)

#Eliminar un elemento del array
miLista.remove("Antonio")

print(miLista[:])

#Eliminar ultimo elemento del array
miLista.pop()

print(miLista[:])

#Unir arrays
miLista2 = ["Jasubi", "Piñeyro"]

miLista3 = miLista+miLista2

print(miLista3[:])