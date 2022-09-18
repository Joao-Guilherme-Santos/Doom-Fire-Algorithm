import pygame
from pygame.locals import *
from time import sleep
import data_fire

pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption('DoomFire')

models = []
pos = []
color = [(7,7,7),(31,7,7),(47,15,7),(71,15,7),(87,23,7),(103,31,7),(119,31,7),(143,39,7),(159,47,7),(175,63,7),
                    (191,71,7),(199,71,7),(223,79,7),(223,87,7),(223,87,7),(215,95,7),(215,95,7),(215,103,15),(207,111,15),(207,119,15),
                    (207,127,15),(207,135,23),(199,135,23),(199,143,23),(199,151,31),(191,159,31),(191,159,31),(191,167,39),(191,167,39),(191,175,47),
                    (183,175,47),(183,183,47),(183,183,55),(207,207,111),(223,223,159),(239,239,199),(255,255,255)]
x = y = 100
pos_x = pos_y = 0
square_size = 10

def att(matriz):
    a = -1
    for u in range(0, x):
        for i in range(0, y):
            a += 1
            model = pygame.Surface((square_size,square_size))
            model.fill((color[matriz[a]]))
            models.append(model)


for v in range(0, x):
    for i in range(0, y):
        pos.append((pos_x,pos_y))
        pos_x += square_size
    pos_y += square_size
    pos_x=0


matriz = data_fire.Create_matriz(x,y)
data_fire.Create_fireSorce(matriz, x)

while True:
    sleep(0)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    screen.fill((0,0,0))
    data_fire.Calculate_fire(matriz, x, y)
    att(matriz)

    for i,v in enumerate(models):
        screen.blit(v, pos[i])
    models = []

    pygame.display.update()
