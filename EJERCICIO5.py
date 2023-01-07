import time
print("==========Programa recursivo==========")
def fibonacci(x):
    if x==0:
        return 0
    if x==1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)
print(fibonacci(2))

print("==========Programa no recursivo==========")
def fibonacci_n(x):
    a, b = 0, 1
    for i in range(x):
        a, b = b, a + b
    return a
print(fibonacci_n(2))

print("==========Tiempo de ejecucion==========")
if __name__ == '__main__':
    n = 40

    print("Recursivo")
    comienzo = time.time()
    fibonacci(n)
    final = time.time()
    print(final - comienzo)

    print("No recursivo")
    comienzo = time.time()
    fibonacci_n(n)
    final = time.time()
    print(final - comienzo)