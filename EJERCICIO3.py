print("==========Programa seleccion=========")
def seleccion(lista):
  if len(lista)<=1:
    return lista

  minimo = 0
  for i in range(1, len(lista)):
    if lista[i] <lista[minimo]:
      minimo = i

  lista[0], lista[minimo] = lista[minimo], lista[0]
  return [lista[0]] + seleccion(lista[1:])

print(seleccion([1,4,2,6,7]))