import pygame
from pygame.locals import *
import data_fire
from time import sleep

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('DoomFire')

class Pixel:
    def __init__(self, matriz, x, y):
        self.matriz = matriz
        self.x = x
        self.y = y
        self.pos = []
        self.models = []
        self.color = [(7,7,7),(31,7,7),(47,15,7),(71,15,7),(87,23,7),(103,31,7),(119,31,7),(143,39,7),(159,47,7),(175,63,7),
                    (191,71,7),(199,71,7),(223,79,7),(223,87,7),(223,87,7),(215,95,7),(215,95,7),(215,103,15),(207,111,15),(207,119,15),
                    (207,127,15),(207,135,23),(199,135,23),(199,143,23),(199,151,31),(191,159,31),(191,159,31),(191,167,39),(191,167,39),(191,175,47),
                    (183,175,47),(183,183,47),(183,183,55),(207,207,111),(223,223,159),(239,239,199),(255,255,255)]
        for v in range(0, x*y):
            self.models.append(pygame.Surface((50,50)))



    def Create_pos_list(self):
        x = self.x
        y = self.y
        pos_x = pos_y = 0
        for v in range(0, x):
            for i in range(0, y):
                self.pos.append((pos_x,pos_y))
                pos_x+=50
            pos_x=0
            pos_y+=50



    def Paint(self):
        matriz = self.matriz
        a = 0
        for u in range(0, self.x):
            for i in range(0, self.y):
                self.models[a].fill((self.color[matriz[a]]))


    def Create(self):
        for v in range(0, self.x*self.y):
            self.models.append(pygame.Surface((50,50)))


x = 10
y = 10
matriz = data_fire.Create_matriz(x, y)
data_fire.Create_fireSorce(matriz, x)

lista = Pixel(matriz, x, y)

while True:
    sleep(1)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    data_fire.Calculate_fire(matriz, x, y)
    screen.fill((0,0,0))
    lista.Create_pos_list()
    lista.Paint()
    # print(lista.models)
    for i,v in enumerate(lista.models):
        screen.blit(v,lista.pos[i])
    pygame.display.update()
