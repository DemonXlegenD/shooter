import pygame
from spaceship import Spaceship

class UltimateCharging():
    def __init__(self, difficulty):
        self.percent = 0
        self.percent_speed = 1 / difficulty

    def add_percent(self):
        self.percent += self.percent_speed / 100


    # def reset_percent(self):
    #     self.percent = 0
            

    def update_bar(self, surface, Player):
        # ajouter %
        self.add_percent()

        if self.percent >= 100 and Player.ult == False:
            Player.ult = True
            print(Player.ult)


        #barre en arriere plan (grise)
        pygame.draw.rect(surface, (114, 101, 98), [
            0, # X
            surface.get_height()-40, # Y
            surface.get_width(), #longueur de la fenetre
            20 #epaisseur
        ])

        # barre bleu foncé : jauge d'ult
        pygame.draw.rect(surface, (0, 90, 211), [
            0, # X
            surface.get_height()-40, # Y
            (surface.get_width() /100) * self.percent, #longueur de la fenetre
            20 #epaisseur
        ])