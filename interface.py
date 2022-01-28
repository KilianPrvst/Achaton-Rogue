from random import randint
import pygame as pg
from random import randint
import random  as rd
import numpy as np
taille =20
liste_origines = [(100, 100)]

class Niveau:
    pass   

class Salle:

    def __init__(self, x0, y0, longueur, hauteur, portes, attributs):
        self.x0 = x0
        self.y0 = y0
        self.longueur = longueur
        self.hauteur = hauteur
        self.portes = portes
        self.attributs = attributs
        self.position_porte = []
    
    def dans_salle(self, x, y):
        return (x<self.x0 + self.longueur ) and (x>=self.x0) and (y<self.y0 + self.hauteur ) and (y>=self.y0 )
    
    def dans_porte(self, x, y):
        return (x,y) in self.position_porte
    
    def affiche(self, screen):
        rect1 = pg.Rect(taille*(self.x0 -1), taille*(self.y0-1), taille*(self.longueur +2), taille*(self.hauteur +2))
        rect2 = pg.Rect(self.x0*taille, self.y0*taille, taille*self.longueur, taille*self.hauteur )
        pg.draw.rect(screen, (255,0,0), rect1 )
        pg.draw.rect(screen, (0,255,0), rect2 )

    def choix_porte(self):
        x0, y0 = self.origine
        pos = randint(self.origine, self.origine + 2 *
                      self.longueur + 2*self.hauteur)
        booleen = True
        while booleen:
            if pos < self.origine + self.longueur:
                x_porte = x0 + pos
                y_porte = y0
            if pos >= self.origine + self.longueur and pos < self.origine + self.longueur + self.hauteur:
                x_porte = x0 + self.longueur
                y_porte = y0 + pos - self.longueur
            if pos >= self.origine + self.longueur + self.hauteur and pos < self.origine + 2*self.longueur + self.hauteur:
                x_porte = x0 + pos - self.longueur - self.hauteur
                y_porte = y0 - self.hauteur
            if pos >= self.origine + 2*self.longueur + self.hauteur:
                x_porte = x0
                y_porte = y0 + pos - 2*self.longueur - self.hauteur
            if (x_porte, y_porte) not in self.position_porte:
                booleen = False
        return self.position_porte.append(x_porte, y_porte)


class Couloir:
    def __init__(self, x0, y0, x1, y1, longueur_1, hauteur_1, longueur_2, hauteur_2):
        self.position_porte = []
        self.origine_1 = x1, y1
        self.origine_0 = x0, y0
        self.longueur_1, self.hauteur_1 = longueur_1, hauteur_1
        self.longueur_2, self.hauteur_2 = longueur_2, hauteur_2

    

#salle = Salle(0,0,10,10,[])
#print(salle.dans_salle(9,9))
