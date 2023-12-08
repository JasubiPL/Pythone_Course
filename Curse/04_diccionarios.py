miDiccionario = {
  "Alemania":"Berlin",
  "Francia":"Paris",
  "Reino Unido":"Londres",
  "España":"Madrid"
}

print("La capital de España es " + miDiccionario["España"])

#Añadir un nuevo elemento
miDiccionario["Italia"]="Lisboa"
print("======================================")
print(miDiccionario)

#Modificar un elemento
miDiccionario["Italia"]="Roma"
print("======================================")
print(miDiccionario)

#Eliminar un elemento
del miDiccionario["Reino Unido"]
print("======================================")
print(miDiccionario)

#Saber las Keys de un diccionario
print("======================================")
print(miDiccionario.keys())

#Saber el Valor de un diccionario
print("======================================")
print(miDiccionario.values())

#Saber la longitud
print("======================================")
print(len(miDiccionario))