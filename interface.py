import pygame as pg
from random import randint
import random  as rd
import numpy as np
taille =20
class Niveau:
    pass   
class Salle:

    def __init__(self, x0, y0, longueur, hauteur, portes):
        self.x0 = x0
        self.y0 = y0
        self.longueur = longueur
        self.hauteur = hauteur
        self.portes = portes
    
    def dans_salle(self, x, y):
        return (x<self.x0 + self.longueur ) and (x>self.x0) and (y<self.y0 + self.hauteur) and (y>self.y0 )
    

    def dans_porte(self, x, y):
        return (x,y) in self.portes
    

    
    def salle(self, screen):
        rect1 = pg.Rect(self.x0, self.y0, 20*self.longueur, 20*self.hauteur)
        rect2 = pg.Rect(self.x0, self.y0, 20*(self.longueur -1), 20*(self.hauteur -1))
        pg.draw.rect(screen, (255,0,0), rect1 )
        pg.draw.rect(screen, (0,255,0), rect2 )


    

salle = Salle(0,0,10,10,[])
print(salle.dans_salle(9,9))
