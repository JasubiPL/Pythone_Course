#instruccion "continue"
#Esta instruccion hace que cuendo la condicion se cumpla, ignore el resto de codigo probocando que se vuelva a ejecutar el bucle
# Osea, ignora el print de ese ciclo
for letra in "Pythone":
  if letra =="h":
    continue

  print(f"Viendo la letra {letra}")