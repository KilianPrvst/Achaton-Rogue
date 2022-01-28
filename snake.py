# v1 : pareil mais au moins on peut sortir du programme
# avec la touche 'q', ou avec la souris en fermant la fenêtre

import pygame as pg
from random import randint

pg.init()
screen = pg.display.set_mode((600, 600))
color=(255,255,255)
for i in range(15):
    for j in range(30):
        
        rect=pg.Rect(i*40+20*(j%2),j*20,20,20)
        pg.draw.rect(screen,color,rect)
snake = [
    (10, 15),
    (5, 15),
    (0, 15),
]
for i in range(len(snake)):
        pg.draw.rect(screen,(255,0,0),pg.Rect(snake[i][0],snake[i][1],5,5))
clock = pg.time.Clock()
direction=(0,0)
# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
while running:
    clock.tick(1)
    
    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_DOWN:
                direction=(0,5)
            if event.key == pg.K_UP:
                direction = (0,-5)
            if event.key == pg.K_RIGHT:
                direction = (5,0)
            if event.key == pg.K_LEFT:
                direction = (-5,0)
            if event.key == pg.K_q:
                running = False
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    x=snake[-1]
    for i in range(len(snake)-1):
        snake[i+1]=snake[i]
    snake[0]=direction[0]+snake[0][0],direction[1]+snake[0][1]
    for i in range(len(snake)):
        pg.draw.rect(screen,(255,0,0),pg.Rect(snake[i][0],snake[i][1],5,5))
    pg.draw.rect(screen,(0,0,0),pg.Rect(x[0],x[1],5,5))
    pg.display.update()

# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()