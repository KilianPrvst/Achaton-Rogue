from os import lseek
from zipfile import LargeZipFile
import pygame as pg
from random import randint

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
        self.cases = []

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

    def choix_porte(self):
        x0, y0 = self.x0, self.y0
        pos = randint(0, 2 *
                      self.longueur + 2*self.hauteur)
        booleen = True
        while booleen:
            if pos < self.longueur:
                x_porte = x0 + pos
                y_porte = y0
            if pos > self.longueur and pos < self.longueur + self.hauteur:
                x_porte = x0 + self.longueur
                y_porte = y0 + pos - self.longueur
            if pos > self.longueur + self.hauteur and pos < 2*self.longueur + self.hauteur:
                x_porte = x0 + pos - self.longueur - self.hauteur
                y_porte = y0 - self.hauteur
            if pos > 2*self.longueur + self.hauteur:
                x_porte = x0
                y_porte = y0 + pos - 2*self.longueur - self.hauteur
            if (x_porte, y_porte) not in self.portes:
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

    def cases_salle(self):
        for i in range(50):
            for j in range(50):
                if self.dans_salle(i, j):
                    self.cases.append((i, j))


class Niveau:
    def __init__(self, numero, escaliers=[], salles=[], couloirs=[]):
        self.numero = numero
        self.escaliers = escaliers
        self.salles = salles
        self.couloirs = couloirs
        self.cases = []

    def pas_dans_salles(self, s):
        bol = True
        for salle in self.salles:
            bol = bol and (s.x0 > salle.x0 + salle.longueur or s.x0 + s.longueur <
                           salle.x0 or s.y0 > salle.y0+salle.hauteur or s.y0 + s.hauteur < salle.y0)
        return bol

    def creer_salles(self, nombre_salles):
        while len(self.salles) < nombre_salles:
            x = randint(0, 50)
            y = randint(0, 50)
            hauteur = randint(4, 6)
            longueur = randint(4, 6)
            salle = Salle(x, y, hauteur, longueur)
            if self.pas_dans_salles(salle):
                self.salles.append(salle)

    def affiche_niveau(self, screen):
        for salle in self.salles:
            salle.affiche(screen)

    def liste_salle(self):
        for salle in self.salles:
            for i in range(50):
                for j in range(50):
                    if salle.dans_salle(i, j):
                        self.cases.append((i, j))


class Couloir:
    def __init__(self):
        self.coordonnees = []

    def couloir(self, salle_1, salle_2, niveau):
        porte_1 = salle_1.portes[0]
        x, y = porte_1
        cases_2 = salle_2.cases()
        cases_1 = salle_1.cases()
        liste = [x, y]
        while (x, y) not in cases_2:
            bool = randint(0, 1)
            while (x, y) not in cases_1:
                if bool == 1:
                    x += 1
                else:
                    y += 1
                liste.append(x, y)
        self.coordonnees.append(x, y)


salle = Salle(0, 0, 10, 10, [(1, 0)])
print(salle.dans_porte(1, 0))
