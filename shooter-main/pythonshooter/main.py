import pygame
import sys

#import the class Enemy from the file enemy.py
from enemy import Enemy
#import the class Spaceship from the file spaceship.py
from spaceship import Spaceship


#Initialisation des dimensions de la fenêtre
largeur = 800
hauteur = 600

#Initialiser Pygame
pygame.init()

#Création de la fenêtre en passant ses dimensions en pixel sous forme d'un tuple
fenetre = pygame.display.set_mode((largeur,hauteur))
vaisseau = Spaceship()
#Boucle de jeu

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        

    #Dessin de la fenêtre
    pygame.display.flip()
