print("==========Programa recursivo==========")
def potencia(base, expontente):
    if expontente == 0:
      return 1
    elif expontente % 2 == 0:
      return potencia(base, expontente//2)**2
    else:
      return base*potencia(base,expontente-1)

print(potencia(2,3))
print(potencia(2,4))