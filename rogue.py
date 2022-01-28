#Imports
import pygame as pg
from random import randint

#Initialisation
pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
knight = [11, 10]

#Movements
running = True
while running:
    clock.tick(5)
    #Mise en place des salles
    for i in range(30):
        for j in range(30):
            x=i*20
            y=j*20
            rect = pg.Rect(x, y, 20, 20)
            if (i+j)%2==0:
                color = (200, 200, 200)
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
                if event.key == pg.K_q:
                    running = False
                elif event.key == pg.K_UP:
                    knight[1] -= 1
                elif event.key == pg.K_DOWN:
                    knight[1] += 1
                elif event.key == pg.K_RIGHT:
                    knight[0] += 1
                elif event.key == pg.K_LEFT:
                    knight[0] -= 1

    # les coordonnées de rectangle que l'on dessine
    x = 20*knight[0] # coordonnée x (colonnes) en pixels
    y = 20*knight[1] # coordonnée y (lignes) en pixels
    width = 20 # largeur du rectangle en pixels
    height = 20 # hauteur du rectangle en pixels
    rect = pg.Rect(x, y, width, height)
    # appel à la méthode draw.rect()
    color = (253, 108, 158) # couleur rouge
    pg.draw.rect(screen, color, rect)
    pg.display.update()


#Conclusion
pg.quit()