print("==========Programa recursivo==========")
def suma(a,b):
    if b == 0:
        return a
    else:
        return suma(a + 1, b - 1)

print(suma(2,4))