# Imports
import numpy as np
import pygame as pg
from random import randint
import interface
from interface import *
from functions import *

# Initialisation
pg.init()
screen = pg.display.set_mode((1000, 1000))
clock = pg.time.Clock()
knight = [5, 8]
#salle = Salle(1, 7, 10, 10, [(2,6)], [])
#monster = [salle.x0 + salle.longueur//2, salle.y0 + salle.hauteur//2]
niveau = Niveau(1)
niveau.creer_salles(5)
salle = niveau.salles[0]
salle.choix_portes()


# Movements
running = True
while running:
    clock.tick(5)
    # Mise en place des salles
    for i in range(50):
        for j in range(50):
            x = i*20
            y = j*20
            rect = pg.Rect(x, y, 20, 20)
            if (i+j) % 2 == 0:
                color = (200, 200, 200)
            else:
                color = (200, 200, 200)
            pg.draw.rect(screen, color, rect)

    for event in pg.event.get():

        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
            # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if True:
                x_new, y_new = knight[0], knight[1]
                if event.key == pg.K_q:
                    running = False
                elif event.key == pg.K_UP and (salle.dans_salle(knight[0], knight[1] - 1) or (salle.dans_porte(knight[0], knight[1] - 1))):
                    knight[1] -= 1
                elif event.key == pg.K_DOWN and (salle.dans_salle(knight[0], knight[1] + 1) or (salle.dans_porte(knight[0], knight[1] + 1))):
                    knight[1] += 1
                elif event.key == pg.K_RIGHT and (salle.dans_salle(knight[0] + 1, knight[1]) or (salle.dans_porte(knight[0]+1, knight[1]))):
                    knight[0] += 1
                elif event.key == pg.K_LEFT and (salle.dans_salle(knight[0] - 1, knight[1]) or (salle.dans_porte(knight[0]-1, knight[1]))):
                    knight[0] -= 1

    niveau.affiche_niveau(screen)
    # les coordonnées de rectangle que l'on dessine
    x = 20*knight[0]  # coordonnée x (colonnes) en pixels
    y = 20*knight[1]  # coordonnée y (lignes) en pixels
    width = 20  # largeur du rectangle en pixels
    height = 20  # hauteur du rectangle en pixels
    rect = pg.Rect(x, y, width, height)
    # appel à la méthode draw.rect()
    color = (0, 0, 0)  # couleur rouge
    pg.draw.rect(screen, color, rect)
    pg.display.update()


# Conclusion
pg.quit()
