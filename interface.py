import pygame as pg
from random import randint


liste_origines = [(100, 100)]


class Niveau:
    def __init__(self, liste_origine):
        self.origine = liste_origine[0]


class Salles(Niveau):
    def __init__(self, liste_origine, longueur, hauteur):
        super().__init__(liste_origine)
        self.x0, self.y0 = self.origine
        self.longueur = longueur
        self.hauteur = hauteur


class Couloir(Salles):
    def __init__(self, liste_origine, longueur, hauteur):
        super().__init__(liste_origine, longueur, hauteur)
        self.position_porte = []

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
        return x_porte, y_porte


def couloir():
