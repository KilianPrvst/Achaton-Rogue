import pygame as pg
from random import randint

class Niveau:
    pass   
class Salle:

    def __init__(self, x0, y0, longueur, hauteur):
        self.x0 = x0
        self.y0 = y0
        self.longueur = longueur
        self.hauteur = hauteur
    
    def dans_salle(self, x, y):
        if x<
