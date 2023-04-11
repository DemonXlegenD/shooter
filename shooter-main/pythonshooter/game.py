import pygame
from spaceship import Spaceship
#créer une classe qui va représenter notre jeu
class Game:

    def __init__(self):
        #définir si notre jeu a commencé ou non
        self.is_playing = False
        #générer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Spaceship(self)

        #groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        #mettre le score a 0
        self.score = 0
        self.font = pygame.font.Font("robot/RobotoCondensed-Bold.ttf", 25)
        #gérer le son
        # self.sound_manager = SoundManager()

    def start(self):
        self.is_playing = True


    def game_over(self):
        #remettre le jeu à neuf, retirer les monstres, remettre les joueurs à 100 de vie, jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.Score = 0

    def add_score(self, points = 10):
        self.score += points