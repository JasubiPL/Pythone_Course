i = 1

while i <= 10:
  print(f"Ejecucion numero {i}")
  i = i+1

print("Termino la ejecucion")

print("===================================")

edad = int(input("Cual es tu edad: "))

while edad < 0 or edad > 100:
  print("Edad erronea")
  edad = int(input("Cual es tu edad: "))

print(f"Edad aceptada, tu edad es: { edad }")