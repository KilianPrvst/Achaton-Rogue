#Imports
import numpy as np
import pygame as pg
from random import randint
import interface
from interface import *
from functions import *

#Initialisation
pg.init()
counter = 1
screen = pg.display.set_mode((1000, 1000))
clock = pg.time.Clock()
knight = [25, 20]
salle = Salle(1, 7, 30, 30, [(2,6)], [])
#monster = [salle.x0 + salle.longueur//2, salle.y0 + salle.hauteur//2]
monster = [2, 8]

#Movements
running = True
while running:
    clock.tick(10)
    #Mise en place des salles
    for i in range(50):
        for j in range(50):
            x=i*20
            y=j*20
            rect = pg.Rect(x, y, 20, 20)
            if (i+j)%2==0:
                color = (0, 0, 0)
            else:
                color = (0, 0, 0)
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
                elif event.key == pg.K_RIGHT and (salle.dans_salle(knight[0] + 1, knight[1]) or (salle.dans_porte(knight[0]+1, knight[1] ))):
                    knight[0] += 1
                elif event.key == pg.K_LEFT and (salle.dans_salle(knight[0] - 1, knight[1]) or (salle.dans_porte(knight[0]-1, knight[1] ))):
                    knight[0] -= 1
        

        distance = np.sqrt((knight[0] - monster[0])**2 + (knight[1] - monster[1])**2)  
        if distance <= 30 and distance != 1 and counter %2 == 0:        
            if np.abs(knight[0] - monster[0]) <= np.abs(knight[1] - monster[1]) and knight[1] - monster[1] > 0 and (salle.dans_salle(monster[0], monster[1] + 1)) or (salle.dans_porte(monster[0], monster[1] + 1)):
                monster[1] += 1
            elif np.abs(knight[0] - monster[0]) <= np.abs(knight[1] - monster[1]) and knight[1] - monster[1] <= 0 and (salle.dans_salle(monster[0], monster[1] - 1)) or (salle.dans_porte(monster[0], monster[1] - 1)):
                monster[1] -= 1
            elif np.abs(knight[0] - monster[0]) > np.abs(knight[1] - monster[1]) and knight[0] - monster[0] > 0 and (salle.dans_salle(monster[0], monster[1] + 1)) or (salle.dans_porte(monster[0], monster[1] + 1)):
                monster[0] += 1
            elif np.abs(knight[0] - monster[0]) > np.abs(knight[1] - monster[1]) and knight[0] - monster[0] <= 0 and (salle.dans_salle(monster[0], monster[1] - 1)) or (salle.dans_porte(monster[0], monster[1] - 1)):
                monster[0] -= 1

       # if knight[0] == surprise[0] and knight[1] == surprise[1]:
       #     surprise[0], surprise[1] = randint(0, 49), randint(0, 49)

                

    salle.affiche(screen)
    x= 20*surprise[0]
    y= 20*surprise[1]
    rect = pg.Rect(x, y, 20, 20)
    color = (255, 127, 0)
    pg.draw.rect(screen, color, rect)
    x = 20*monster[0] # coordonnée x (colonnes) en pixels
    y = 20*monster[1] # coordonnée y (lignes) en pixels
    width = 20 # largeur du rectangle en pixels
    height = 20 # hauteur du rectangle en pixels
    rect = pg.Rect(x, y, width, height)
    # appel à la méthode draw.rect()
    color = (255, 0, 0) # couleur rouge
    pg.draw.rect(screen, color, rect)
    # les coordonnées de rectangle que l'on dessine
    x = 20*knight[0] # coordonnée x (colonnes) en pixels
    y = 20*knight[1] # coordonnée y (lignes) en pixels
    width = 20 # largeur du rectangle en pixels
    height = 20 # hauteur du rectangle en pixels
    rect = pg.Rect(x, y, width, height)
    # appel à la méthode draw.rect()
    color = (0, 0, 0) # couleur rouge
    pg.draw.rect(screen, color, rect)
    counter += 1
    pg.display.update()


#Conclusion
pg.quit()