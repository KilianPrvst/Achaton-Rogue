import numpy as np
import pygame as pg
monster_size = (10,10)
def create_monster(x,y,salle):
    """IN : position du personnnage. OUT : Position des monstres"""
    a, b = np.random.randint(salle.longeur), np.random.randint(salle.largeur)
    while not dans_salle(x + a, y + b):
        a, b = np.random.randint(salle.longeur), np.random.randint(salle.largeur)
    
    monster = pg.rect(x + a,y + b, monster_size)

def moove_monster(salle, knight, monster):
    """IN: position monster. OUT : R"""
    a, b = np.random.randint(0,1), np.random.randint(0,1)
    while not dans_salle(pg.rect(monster.get_rect().size + (a, b), knight.get_rect().size[0], knight.get_rect().size[1])):
        a, b = np.random.randint(salle.longeur), np.random.randint(salle.largeur)
    monster = pg.rect.update(monster.get_rect().size + (a, b), knight.get_rect().size[0], knight.get_rect().size[1])
