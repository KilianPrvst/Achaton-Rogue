from random import randint
import pygame as pg

taille = 20


class Salle:
    def __init__(self, x0, y0, longueur, hauteur, portes=[], attributs=[]):
        self.x0 = x0
        self.y0 = y0
        self.longueur = longueur
        self.hauteur = hauteur
        self.portes = portes
        self.attributs = attributs

    def choix_porte(self):
        x0, y0 = self.origine
        pos = randint(0, 2 *
                      self.longueur + 2*self.hauteur)
        booleen = True
        while booleen:
            if pos < self.longueur:
                x_porte = x0 + pos
                y_porte = y0
            if pos >= self.longueur and pos < self.longueur + self.hauteur:
                x_porte = x0 + self.longueur
                y_porte = y0 + pos - self.longueur
            if pos >= self.longueur + self.hauteur and pos < 2*self.longueur + self.hauteur:
                x_porte = x0 + pos - self.longueur - self.hauteur
                y_porte = y0 - self.hauteur
            if pos >= 2*self.longueur + self.hauteur:
                x_porte = x0
                y_porte = y0 + pos - 2*self.longueur - self.hauteur
            if (x_porte, y_porte) not in self.position_porte:
                booleen = False
        self.position_porte.append((x_porte, y_porte))

    def dans_salle(self, x, y):
        return (x < self.x0 + self.longueur) and (x >= self.x0) and (y < self.y0 + self.hauteur) and (y >= self.y0)

    def dans_porte(self, x, y):
        return (x, y) in self.portes

    def affiche(self, screen):
        rect1 = pg.Rect(taille*(self.x0 - 1), taille(self.y0-1),
                        taille*self.longueur, taille*self.hauteur)
        rect2 = pg.Rect(self.x0*taille, self.y0*taille, taille *
                        (self.longueur + 2), taille*(self.hauteur + 2))
        pg.draw.rect(screen, (255, 0, 0), rect1)
        pg.draw.rect(screen, (0, 255, 0), rect2)


salle = Salle(0, 0, 10, 10, [])
print(salle.dans_salle(9, 9))


class Niveau:
    def __init__(self, liste_origines, nb_salles):
        self.origines = liste_origines
        self.nb_salles = nb_salles

    def creation_salle(nb_salles):


class Couloir:
    def __init__(self, x0, y0, x1, y1, longueur_1, hauteur_1, longueur_0, hauteur_0, portes=[], attributs=[]):
        self.salle_1 = Salle(x1, y1, longueur_1, hauteur_1, portes, attributs)
        self.salle_0 = Salle(x0, y0, longueur_0, hauteur_0, portes, attributs)

    def couloir(self):
