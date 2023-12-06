#funciones sin Parametros
def mensaje():
  print("Mi primer ejersicio")

#mensaje()
#mensaje()

#funciones con Parametros
def suma(n1, n2):
  print(n1+n2)

#suma(3,4)
#suma(8,23)

#funciones con Retorno
def suma2(n1, n2):
  resultado = n1+n2
  return resultado

almacena_resultado = suma2(5,8)

print(almacena_resultado)
print(suma2(3,4))