#veamos lo casos posibles de que el robot pueda caminar
#1 metro -> ([1]) 1 forma de caminar
#2 metros -> ([1,1] [2]) 2 formas de caminar
#3 metros -> ([1,1,1] [2,1] [1,2]) 3 formas de caminar
#4 metros -> ([1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]) 5 formas de caminar

print("==========Formas de caminar de un robot==========")
def formas_de_caminar(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        return formas_de_caminar(x-1) + formas_de_caminar(x-2)

print(formas_de_caminar(1))
print(formas_de_caminar(2))
print(formas_de_caminar(3))
print(formas_de_caminar(5))