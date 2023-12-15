#con yield from entramos al elemnto y recorremos los sub elemento
#El primer elemento seria MADRID y los sub elemento son las letras que conforman la palabra

def devuelve_ciudades(*ciudades):
  for elemento in ciudades:
    
    yield from elemento

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))