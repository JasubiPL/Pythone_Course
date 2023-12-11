print("Asignaturas Optativas año 2023")
print("Asiganaturas Optatvivas: Informatica - Soporte - Fisica")
opcionSeleccionada = input("Escribe la asignatura escogida: ")

asignatura =  opcionSeleccionada.lower()
if asignatura in ("informatica", "soporte", "fisica"):
  print("Asigantura elegida " + asignatura)
else:
  print("La asignatura escogida no esta contemplada")