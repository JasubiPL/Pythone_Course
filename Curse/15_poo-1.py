#Clases

class Coche():

  #Propiedades Iniciales
  largoChasis = 250
  anchoChasis = 120
  ruedas = 4
  enmarcha = False

  #Metodos de la clase
  def arrancar(self):
    self.enmarcha = True

  def estado(self):
    if(self.enmarcha):
      return "El coche esta en marcha"
    else:
      return "El coche esta parado"

#creamos una instacia de la clase Coche
mercedes = Coche()

#cambiando el valor inicial de las propiedades de la clase
mercedes.largoChasis = 300

#Accedemos al metodo "arrancar"
mercedes.arrancar()

print(f"El largo del chasisi es de {mercedes.largoChasis}")
print(mercedes.estado())
