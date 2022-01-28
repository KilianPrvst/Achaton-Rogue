import pygame as pg
import random as rd
from random import randint

x = 400
y = 300



def salle(x,y):
    """IN : point en haut à gauche"""
    pg.init()
    screen = pg.display.set_mode((x, y))

    taille  = (np.rd.randint(x), np.rd.randint(y))
    surface = pygame.display.set_mode((taille[0],taille[1]))

    screen.fill((255,255,255))
    pg.draw.rect(screen,(255,0,0),surface)



    pg.display.update()

    # Enfin on rajoute un appel à pg.quit()
    # Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
    pg.quit()
