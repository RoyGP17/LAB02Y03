import time
print("===========Programa recursivo=========")
def factorial_num(n):
    if n == 1:
        return 1
    return  n * factorial(n - 1)
#print(factorial_num(4))

print("==========Programa no recursivo==========")
def factorial(n):
    respuesta = 1
    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta
#print(factorial(4))

print("==========Tiempo de ejecucion==========")
if __name__ == '__main__':
    n = 20000

    print("Recursivo")
    comienzo = time.time()
    factorial_num(n)
    final = time.time()
    print(final - comienzo)

    print("No recursivo")
    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)