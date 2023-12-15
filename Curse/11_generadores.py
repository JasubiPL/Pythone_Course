#Los generadores sirven para crear listas iterables con mayos eficiencia en tiempo y recursos

def generaPares(limite):

  num = 1

  while num < limite:

    yield num*2

    num = num + 1

devuelvePares = generaPares(10)

print(next(devuelvePares))
print("Puede ir mas codigo aqui")
print(next(devuelvePares))
print("Puede ir mas codigo aqui")
print(next(devuelvePares))
print("Puede ir mas codigo aqui")
