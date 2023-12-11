for i in [5,6,7]:
  print(i)

for j in ["Primavera","Verano", "Otoño", "Invierno"]:
  print(j)

for a in range(10):
  print(a)

#Imprimir en una sola linea con estacio
for b in range(5):
  print(b, end=" ")

print("========================================")
#comprovacion de correo electronico
email = False

for i in "juanito@gmail.com":
  if i== "@":
    email = True

if email == True:
  print("El correo es correcto")
else:
  print("Correo Erroneo")


print("========================================")
#Comprobacion con input
email2 = False

emailUsuario = input("Ingresa tu correo 📧: ")

for c in emailUsuario:
  if c == "@":
    email2 = True

if email2 == True:
  print("Correo Valido")
else:
  print("Correo Invalido")

print("========================================")
#Comprobacion con input2
contador = 0

emailUsuario2 = input("Ingresa tu correo2 📧: ")

for c in emailUsuario2:
  if c == "@" or c == ".":
    contador = contador + 1

if contador == 2:
  print("Correo Valido")
else:
  print("Correo Invalido")