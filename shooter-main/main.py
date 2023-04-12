import pygame
import sys
import math
import time

from game import Game
from settings import Settings
#import the class Enemy from the file enemy.py
from enemy import Enemy
#import the class Spaceship from the file spaceship.py
from spaceship import Spaceship

#définir une clock
clock = pygame.time.Clock()
FPS = 100


#Initialisation des dimensions de la fenêtre
largeur = 1920
hauteur = 1080

#Initialize Pygame
pygame.init()

#Création de la fenêtre en passant ses dimensions en pixel sous forme d'un tuple
pygame.display.set_caption("Shoot'em up")
screen = pygame.display.set_mode((largeur,hauteur))

#importer de charger l'arrière plan de notre jeu
background = pygame.image.load('PygameAssets/bgspace.jpg').convert()
bg_largeur = 1920
bg_hauteur = 1080
background = pygame.transform.scale(background, (bg_largeur, bg_hauteur))

#importer charger notre bannière
banner = pygame.image.load('PygameAssets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/3)

#importer charger notre bouton pour lancer la partie 
play_button = pygame.image.load('PygameAssets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/2.7)
play_button_rect.y = math.ceil(screen.get_height()/1.7)

#importer charger notre bouton pour lancer les settings
settings_button = pygame.image.load('PygameAssets/button-settings.png')
settings_button = pygame.transform.scale(settings_button, (50, 50))
settings_button_rect = settings_button.get_rect()
settings_button_rect.x = math.ceil(screen.get_width()/100)
settings_button_rect.y = math.ceil(screen.get_height()/100)


#=====================================================================================================================#
#------------------------------------------------------SETTINGS-------------------------------------------------------#
#=====================================================================================================================#

#gameplay pas selectionné
Gameplay_button = pygame.image.load('PygameAssets/Gameplay.png')
Gameplay_button = pygame.transform.scale(Gameplay_button, (200, 150))
Gameplay_button_rect = Gameplay_button.get_rect()
Gameplay_button_rect.x = math.ceil(screen.get_width()/10.15)
Gameplay_button_rect.y = math.ceil(screen.get_height()/4)
#audio pas selectionné
audio_button = pygame.image.load('PygameAssets/audio.png')
audio_button = pygame.transform.scale(audio_button, (200, 150))
audio_button_rect = audio_button.get_rect()
audio_button_rect.x = math.ceil(screen.get_width()/2.25)
audio_button_rect.y = math.ceil(screen.get_height()/4)
#commandes pas selectionné
controle_button = pygame.image.load('PygameAssets/controle.png')
controle_button = pygame.transform.scale(controle_button, (200, 150))
controle_button_rect = controle_button.get_rect()
controle_button_rect.x = math.ceil(screen.get_width()/1.3)
controle_button_rect.y = math.ceil(screen.get_height()/4)
#bouton retour
return_button = pygame.image.load('PygameAssets/retour.png')
return_button = pygame.transform.scale(return_button, (100, 5))
return_button_rect = return_button.get_rect()
return_button_rect.x = math.ceil(screen.get_width()/100)
return_button_rect.y = math.ceil(screen.get_height()/100)
#gameplay pas selectionné
Gameplay_underline_button = pygame.image.load('PygameAssets/Gameplay_underline.png')
Gameplay_underline_button = pygame.transform.scale(Gameplay_underline_button, (200, 150))
Gameplay_underline_button_rect = Gameplay_underline_button.get_rect()
Gameplay_underline_button_rect.x = math.ceil(screen.get_width()/10.15)
Gameplay_underline_button_rect.y = math.ceil(screen.get_height()/4)
#audio pas selectionné
audio_underline_button = pygame.image.load('PygameAssets/audio_underline.png')
audio_underline_button = pygame.transform.scale(audio_underline_button, (200, 150))
audio_underline_button_rect = audio_underline_button.get_rect()
audio_underline_button_rect.x = math.ceil(screen.get_width()/2.25)
audio_underline_button_rect.y = math.ceil(screen.get_height()/4)
#commandes pas selectionné
controle_underline_button = pygame.image.load('PygameAssets/controle_underline.png')
controle_underline_button = pygame.transform.scale(controle_underline_button, (200, 150))
controle_underline_button_rect = controle_underline_button.get_rect()
controle_underline_button_rect.x = math.ceil(screen.get_width()/1.3)
controle_underline_button_rect.y = math.ceil(screen.get_height()/4)


#=====================================================================================================================#
#------------------------------------------------------PLANETES-------------------------------------------------------#
#=====================================================================================================================#

#importer charger notre bouton pour lancer la planète terre
terre_button = pygame.image.load('PygameAssets/terre.png')
terre_button = pygame.transform.scale(terre_button, (300, 300))
terre_button_rect = terre_button.get_rect()
terre_button_rect.x = math.ceil(screen.get_width()/1.5)
terre_button_rect.y = math.ceil(screen.get_height()/2.50)

#importer charger notre bouton pour lancer la planète 1
planete1_button = pygame.image.load('PygameAssets/planete1.png')
planete1_button = pygame.transform.scale(planete1_button, (200, 200))
planete1_button_rect = planete1_button.get_rect()
planete1_button_rect.x = math.ceil(screen.get_width()/2)
planete1_button_rect.y = math.ceil(screen.get_height()/1.5)

#importer charger notre bouton pour lancer la planète 2
planete2_button = pygame.image.load('PygameAssets/planete2.png')
planete2_button = pygame.transform.scale(planete2_button, (250, 250))
planete2_button_rect = planete2_button.get_rect()
planete2_button_rect.x = math.ceil(screen.get_width()/1.80)
planete2_button_rect.y = math.ceil(screen.get_height()/7.5)

#importer charger notre bouton pour lancer la planète 3
planete3_button = pygame.image.load('PygameAssets/planete3.png')
planete3_button = pygame.transform.scale(planete3_button, (200, 200))
planete3_button_rect = planete3_button.get_rect()
planete3_button_rect.x = math.ceil(screen.get_width()/2.5)
planete3_button_rect.y = math.ceil(screen.get_height()/3)

#importer charger notre bouton pour lancer la planète 4
planete4_button = pygame.image.load('PygameAssets/planete4.png')
planete4_button = pygame.transform.scale(planete4_button, (450, 300))
planete4_button_rect = planete4_button.get_rect()
planete4_button_rect.x = math.ceil(screen.get_width()/8)
planete4_button_rect.y = math.ceil(screen.get_height()/1.5)

#importer charger notre bouton pour lancer la planète 5
planete5_button = pygame.image.load('PygameAssets/planete5.png')
planete5_button = pygame.transform.scale(planete5_button, (175, 175))
planete5_button_rect = planete5_button.get_rect()
planete5_button_rect.x = math.ceil(screen.get_width()/1.20)
planete5_button_rect.y = math.ceil(screen.get_height()/8.5)

#importer charger notre bouton pour lancer la planète 6
planete6_button = pygame.image.load('PygameAssets/planete6.png')
planete6_button = pygame.transform.scale(planete6_button, (150, 150))
planete6_button_rect = planete6_button.get_rect()
planete6_button_rect.x = math.ceil(screen.get_width()/1.25)
planete6_button_rect.y = math.ceil(screen.get_height()/1.25)


#=====================================================================================================================#
#---------------------------------------------------DIFFICULTIES------------------------------------------------------#
#=====================================================================================================================#

#importer charger notre bouton pour lancer le mode easy
easy_button = pygame.image.load('PygameAssets/easy-button.png')
easy_button = pygame.transform.scale(easy_button, (500, 150))
easy_button_rect = easy_button.get_rect()
easy_button_rect.x = math.ceil(screen.get_width()/3)
easy_button_rect.y = math.ceil(screen.get_height()/6)

#importer charger notre bouton pour lancer le mode medium
medium_button = pygame.image.load('PygameAssets/medium-button.png')
medium_button = pygame.transform.scale(medium_button, (500, 150))
medium_button_rect = medium_button.get_rect()
medium_button_rect.x = math.ceil(screen.get_width()/3)
medium_button_rect.y = math.ceil(screen.get_height()/3)

#importer charger notre bouton pour lancer le mode hard
hard_button = pygame.image.load('PygameAssets/hard-button.png')
hard_button = pygame.transform.scale(hard_button, (500, 150))
hard_button_rect = hard_button.get_rect()
hard_button_rect.x = math.ceil(screen.get_width()/3)
hard_button_rect.y = math.ceil(screen.get_height()/2)

#importer charger notre bouton pour lancer le mode hard
nightmare_button = pygame.image.load('PygameAssets/nightmare-button.png')
nightmare_button = pygame.transform.scale(nightmare_button, (500, 150))
nightmare_button_rect = nightmare_button.get_rect()
nightmare_button_rect.x = math.ceil(screen.get_width()/3)
nightmare_button_rect.y = math.ceil(screen.get_height()/1.5)

# Define game varibales
scroll = 0
tiles = math.ceil(largeur/bg_largeur) + 1
seconde = time.time()

game = Game()
settings = Settings()

#Boucle de jeu

running = True

while running:

    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(background, (i * bg_largeur + scroll, 0))

    #Scroll background
    scroll -= 2

    # reset scroll
    if abs(scroll) > bg_largeur:
        scroll = 0

    #  ------------------------------------------- Projectiles -------------------------------------------
    #recuperer les projectiles
    for projectile in game.player.all_projectile:
        projectile.move()

    # appliquer l'ensemble des image de mon groupe de projectile
    game.player.all_projectile.draw(screen)

    #  ------------------------------------------- Enemy -------------------------------------------
    #recuperer les ennemy
    for enemy in game.all_enemy:
        enemy.forward()

    # appliquer l'ensemble des image de mon groupe de mosntres
    game.all_enemy.draw(screen)


     #  ------------------------------------------- Game Related -------------------------------------------
    #vérifier si le jeu a commencé ou non
    if (game.is_playing and game.mode_is_choose):
        #déclencher les isntructions de la partie
        game.update(screen, seconde)
    #---------settings--------#
    elif(settings.is_settings):
        screen.blit(Gameplay_button, Gameplay_button_rect)
        screen.blit(audio_button, audio_button_rect)
        screen.blit(controle_button, controle_button_rect)
        screen.blit(return_button, return_button_rect)
    #verifier quelles sont les settings lancés
    elif(settings.is_gameplay):
        screen.blit(Gameplay_underline_button, Gameplay_underline_button_rect)
        screen.blit(audio_button, audio_button_rect)
        screen.blit(controle_button, controle_button_rect)
        screen.blit(return_button, return_button_rect)
    elif(settings.is_audio):
        screen.blit(Gameplay_button, Gameplay_underline_button_rect)
        screen.blit(audio_underline_button, audio_button_rect)
        screen.blit(controle_button, controle_button_rect)
        screen.blit(return_button, return_button_rect)
    elif(settings.is_commandes):
        screen.blit(Gameplay_button, Gameplay_underline_button_rect)
        screen.blit(audio_button, audio_button_rect)
        screen.blit(controle_underline_button, controle_button_rect)
        screen.blit(return_button, return_button_rect)
    elif(not settings.is_settings and settings.is_audio and settings.is_commandes and settings.is_gameplay):
        #ajouter mon écran de bienvenue 
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)
        screen.blit(settings_button, settings_button_rect)
        
    #Show the screen with the difficulties
    elif(not game.is_playing and not game.mode_is_choose and game.planete_is_choose):
        screen.blit(terre_button, terre_button_rect)
        screen.blit(planete1_button, planete1_button_rect)
        screen.blit(planete2_button, planete2_button_rect)
        screen.blit(planete3_button, planete3_button_rect)
        screen.blit(planete4_button, planete4_button_rect)
        screen.blit(planete5_button, planete5_button_rect)
        screen.blit(planete6_button, planete6_button_rect)

    #vérifier si notre jeu n'a pas commencé
    #Show the screen with the difficulties
    elif(not game.is_playing and game.mode_is_choose):
        screen.blit(easy_button, easy_button_rect)
        screen.blit(medium_button, medium_button_rect)
        screen.blit(hard_button, hard_button_rect)
        screen.blit(nightmare_button, nightmare_button_rect)
    #vérifier si notre jeu n'a pas commencé
    else:
        #ajouter mon écran de bienvenue 
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)
        screen.blit(settings_button, settings_button_rect)

    #Dessin de la fenêtre
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Fermeture du jeu")
            sys.exit()
            
            
        # Faire spawn des ennemis
        if game.is_playing == True:
            
            if time.time() > seconde + 3:
                game.spawn_monster()
                seconde = time.time()

        if event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #détecter si la touche espace est enclenchée pour lance notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif (event.type == pygame.MOUSEBUTTONDOWN):

            #vérification pour svaoir si la souris est en collision avec le bouton
            if (play_button_rect.collidepoint(event.pos)):

                game.show_planetes()

            #vérification pour svaoir si la souris est en collision avec le bouton
            elif (settings_button_rect.collidepoint(event.pos)):
                settings.show_settings()
            elif(Gameplay_button_rect.collidepoint(event.pos)):
                settings.show_gameplay()
            elif(audio_button_rect.collidepoint(event.pos)):
                settings.show_audio()
            elif(controle_button_rect.collidepoint(event.pos)):
                settings.show_commandes()
            elif(return_button_rect.collidepoint(event.pos)):
                settings.back_settings()
            
            elif (terre_button_rect.collidepoint(event.pos)):
                game.show_game_modes()
            elif (planete1_button_rect.collidepoint(event.pos)):
                game.show_game_modes()
            elif (planete2_button_rect.collidepoint(event.pos)):
                game.show_game_modes()
            elif (planete3_button_rect.collidepoint(event.pos)):
                game.show_game_modes()
            elif (planete4_button_rect.collidepoint(event.pos)):
                game.show_game_modes()
            elif (planete5_button_rect.collidepoint(event.pos)):
                game.show_game_modes()
            elif (planete6_button_rect.collidepoint(event.pos)):
                game.show_game_modes()
            
            elif (easy_button_rect.collidepoint(event.pos)):
                game.create_player(1)
                game.start()

            elif (medium_button_rect.collidepoint(event.pos)):
                game.create_player(1.5)

                game.start()
            elif (hard_button_rect.collidepoint(event.pos)):
                game.create_player(2)

                game.start()
            elif (nightmare_button_rect.collidepoint(event.pos)):
                game.create_player(3)

                game.start()
                
                #mettre le jeu en monde "lancé"
                

           
    #fixer le nombre de fps sur ma clock
    clock.tick(FPS)  
