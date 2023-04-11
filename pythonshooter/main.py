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

#Boucle de jeu

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        try:
            # détecte si une touche est enfoncée
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("La touche espace est enfoncée")
                elif event.key == pygame.K_z or event.key == pygame.K_UP:
                    print("La touche z ou flèche du haut est enfoncée")
                elif event.key == pygame.K_q or event.key == pygame.K_LEFT:
                    print("La touche z ou flèche du haut est enfoncée")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    print("La touche z ou flèche du haut est enfoncée")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    print("La touche z ou flèche du haut est enfoncée")


            # détecte si une touche est relâchée
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    print("La touche espace est relâchée")
                elif event.key == pygame.K_z or event.key == pygame.K_UP:
                    print("La touche z ou flèche du haut est relâchée")
                elif event.key == pygame.K_q or event.key == pygame.K_LEFT:
                    print("La touche z ou flèche du haut est relâchée")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    print("La touche z ou flèche du haut est relâchée")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    print("La touche z ou flèche du haut est relâchée")

        
        except AttributeError:
            # ignore tous les événements qui ne sont pas liés aux touches
            pass

    #Dessin de la fenêtre
    pygame.display.flip()
