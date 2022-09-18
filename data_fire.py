from time import sleep
from random import randint

def Create_matriz(x , y):
    matriz = []
    for a in range(0,x*y):
        matriz.append(0)
    return matriz

def Show_Matriz(matriz):
    a = 0
    for u in range(0,x):
        for i in range(0,y):
            if matriz[a] < 10:
                print(f' 0{matriz[a]} ', end='')
            else:
                print(f' {matriz[a]} ', end='')
            a += 1
        print()

def Create_fireSorce(matriz, x):
    for v in range(len(matriz)-x, len(matriz)):
        matriz[v] = 36

def Calculate_fire(matriz,x,y):
    coluna = -1
    linha = -1
    for v in range(0,x):
        coluna += 1
        for i in range(0,y):
            decay = randint(0, 3)
            decay2 = randint(0, 1)
            linha += 1
            pos = linha + (coluna * y)
            below = pos + x + decay2
            if below >= x * y:
                return
            if matriz[below]-decay >= 0:
                matriz[pos] = matriz[below]-decay
            else:
                decay = 0
                matriz[pos] = matriz[below] - decay

        linha = -1


if __name__ == '__main__':
    x = 20
    y = 20
    matriz = Create_matriz(x,y)
    Create_fireSorce(matriz, x)
    while True:
        sleep(1)
        Calculate_fire(matriz,x,y)
        Show_Matriz(matriz)


