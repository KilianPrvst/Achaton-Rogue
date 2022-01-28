from os import lseek
from zipfile import LargeZipFile
import pygame as pg
from random import randint
import random  as rd
import numpy as np
taille =20
liste_origines = [(100, 100)]





    


taille = 20


class Salle:
    def __init__(self, x0, y0, longueur, hauteur, portes=[], attributs=[]):
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
        return (x,y) in self.portes
    
    def affiche(self, screen):
        rect1 = pg.Rect(taille*(self.x0 -1), taille*(self.y0-1), taille*(self.longueur +2), taille*(self.hauteur +2))
        rect2 = pg.Rect(self.x0*taille, self.y0*taille, taille*self.longueur, taille*self.hauteur )
        pg.draw.rect(screen, (206,206,206), rect1 )
        pg.draw.rect(screen, (179,139,109), rect2 )
        for x,y in self.portes:
            rect = pg.Rect(x*taille, y*taille, taille, taille )
            pg.draw.rect(screen, (64,224,208), rect )

    def choix_porte(self):
        x0, y0 = self.x0, self.y0
        pos = randint(0, 2 *
                      self.longueur + 2*self.hauteur)
        booleen = True
        while booleen:
            if pos < self.longueur :
                x_porte = x0 + pos 
                y_porte = y0
            elif pos > self.longueur  and pos < self.longueur + self.hauteur -1 :
                x_porte = x0 + self.longueur 
                y_porte = y0 + pos - self.longueur
            elif pos > self.longueur + self.hauteur -1 and pos < 2*self.longueur + self.hauteur -2:
                x_porte = x0 + pos - self.longueur - self.hauteur
                y_porte = y0 + self.hauteur 
            elif pos > 2*self.longueur + self.hauteur -3:
                x_porte = x0
                y_porte = y0 + pos - 2*self.longueur - self.hauteur
            
            if (x_porte, y_porte) not in self.portes :
                booleen = False
        self.portes.append((x_porte - 1, y_porte - 1))

    def dans_salle(self, x, y):
        return (x < self.x0 + self.longueur) and (x >= self.x0) and (y < self.y0 + self.hauteur) and (y >= self.y0)

    def dans_porte(self, x, y):
        return (x, y) in self.portes

    def affiche(self, screen):
        rect1 = pg.Rect(taille*(self.x0 - 1), taille*(self.y0-1),
                        taille*(self.longueur + 2), taille*(self.hauteur + 2))
        rect2 = pg.Rect(self.x0*taille, self.y0*taille,
                        taille*self.longueur, taille*self.hauteur)
        pg.draw.rect(screen, (255, 0, 0), rect1)
        pg.draw.rect(screen, (0, 255, 0), rect2)
        for x, y in self.portes:
            rect = pg.Rect(x*taille, y*taille, taille, taille)
            pg.draw.rect(screen, (0, 0, 255), rect)

    
class Niveau:
    def __init__(self, numero, escaliers=[], salles=[], couloirs=[]):
        self.numero = numero
        self.escaliers = escaliers
        self.salles = salles
        self.couloirs = couloirs
    
    def pas_dans_salles(self, s):
        bol = True
        for salle in self.salles:
            bol = bol and ( s.x0>salle.x0 + salle.longueur or s.x0 + s.longueur <salle.x0 or s.y0>salle.y0+salle.hauteur or s.y0 + s.hauteur<salle.y0)
        return bol 


    def creer_salles(self, nombre_salles):
        while len(self.salles)<nombre_salles:
            x = randint(1, 43)
            y = randint(4, 43)
            hauteur = randint(4,6)
            longueur = randint(4,6)
            salle = Salle(x,y,hauteur,longueur)
            salle.choix_porte()
            if self.pas_dans_salles(salle):
                self.salles.append(salle)
    
    def affiche_niveau(self, screen):
        for salle in self.salles:
            salle.affiche(screen)
        


# class Couloir:
#     def __init__(self):
#         self.coordonnees = []

#     def couloir(self, salle_1, salle_2):
#         porte_1 = salle_1.portes[0]
#         porte_2 = salle_2.portes[0]
#         origine_1 = salle_1.x0, salle_1.y0
#         origine_2 = salle_2.x0, salle_2.y0
#         longueur_1 = salle_1.longueur
#         hauteur_1 = salle_1.hauteur
#         hauteur_2 = salle_2.hauteur
#         longueur_2 = salle_2.longueur
#         x1, y1 = porte_1
#         self.coordonnees.append(x1, y1)
#         x2, y2 = porte_2
#         if x1 == origine_1[0]:

#         if y1 == origine_1[1]:
#         if x1 == origine_1[0] + longueur_1:
#         if y1 == origine_1[1] + hauteur_1
#         self.coordonnees.append(x, y)


salle = Salle(0, 0, 10, 10, [(1, 0)])
print(salle.dans_porte(1, 0))
