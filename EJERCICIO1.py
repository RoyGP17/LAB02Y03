import random
print("==========Algoritmo para desordenar==========")
def desordenar():
    L = [1, 2, 3, 4, 5]
    for i in range(len(L)):
        indice_al_azar = random.randint(i, len(L) - 1)
        L[i], L[indice_al_azar] = L[indice_al_azar], L[i]
    print(L)

def desordenar():
    L = [1,2,3,4,5]
    for i in range(len(L)):
        indice_al_azar = random.randint(i, len(L)-1)
        L[i], L[indice_al_azar] = L[indice_al_azar], L[i]
    print(L)

desordenar()