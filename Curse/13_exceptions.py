def divide():
  try:
    op1 = (float(input("Introduce el primer numero: ")))
    op2 = (float(input("Introduce el segundo numero: ")))

    print("La divicion es: " + str(op1/op2))

  #Manejo de excepciones especificas
  except ValueError:
    print("El valor introducido es erroneo")
  
  except ZeroDivisionError:
    print("No se puede dividir entre 0!")

  #Manejo de error generico
  except:
    print("A ocurrido un error")
  
  print("Calculo finalizado")

divide()