#Veamos los casos posibles de que el robot pueda caminar
#1 metro -> ([1]) 1 forma de caminar
#2 metros -> ([1,1] [2]) 2 formas de caminar
#3 metros -> ([1, 1, 1], [1, 2], [2, 1], [3]) 4 formas de caminar
#4 metros -> ([1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2], [1, 3], [3, 1]) 7 formas de caminar

from PIL import Image
print("==========Formas de caminar de un robot==========")
print("Veamos los valores de a, b y c")
imagen = Image.open('EJERCICIO7_img.jpg')
imagen.show()

def formas_de_caminar(x):
    a=1/2
    b=-1/2
    c=1
    if x == 0:
        return 0
    else:
        return int((x**2)*(a) + (x)*(b) + c)

print(formas_de_caminar(0))
print(formas_de_caminar(1))
print(formas_de_caminar(2))
print(formas_de_caminar(3))
print(formas_de_caminar(4))