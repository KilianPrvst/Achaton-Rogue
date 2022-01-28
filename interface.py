from random import randint
import pygame as pg
<< << << < HEAD


liste_origines = [(100, 100)]


class Niveau:
    def __init__(self, liste_origine):
        self.origine = liste_origine[0]


class Salle:
    def __init__(self, x0, y0, longueur, hauteur):
        self.x0, self.y0 = x0, y0
        self.longueur = longueur
        self.hauteur = hauteur

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


class Couloir:
    def __init__(self, x0, y0, x1, y1, longueur_1, hauteur_1, longueur_2, hauteur_2):
        self.position_porte = []
        self.origine_1 = x1, y1
        self.origine_0 = x0, y0
        self.longueur_1, self.hauteur_1 = longueur_1, hauteur_1
        self.longueur_2, self.hauteur_2 = longueur_2, hauteur_2

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


== == == =

>>>>>> > pierre
