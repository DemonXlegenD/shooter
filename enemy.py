import pygame
import random

#Classe des ennemis
class Enemy(pygame.sprite.Sprite):

    def __init__(self, game, max_hp, speed, attack):
        super().__init__()
        self.game = game

        self.hp = max_hp
        self.speed = speed
        self.attack = attack
        self.image = pygame.image.load('PygameAssets/button-settings.png')
        # self.image = pygame.transform.scale(self.image, (1200,1200))
        self.image = pygame.transform.scale(self.image, (200,200))
        self.rect = self.image.get_rect()
        self.projectileHit = 0

        self.rect.x = 1600
        self.rect.y = random.randint(100, 800)

        # self.origine_image = self.image
        # self.angle = 0

    def remove(self):
        self.game.all_enemy.remove(self)

    # def rotation(self):
    #     self.angle -= 5
    #     self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
    #     self.rect = self.image.get_rect(center=self.rect.center)

    def damage(self, amount):
        if (self.hp - amount > amount) :
            self.hp -= amount
        else:
            self.remove()

    def forward(self):
        # self.rotation()
        #le deplacement s'arrete si collision
        if self.game.check_collision(self, self.game.all_players):
            self.remove()
            self.game.player.damage(self.attack)
        else:
            self.rect.x -= self.speed

        if self.game.check_collision(self, self.game.player.all_projectile):
            self.damage(self.game.player.attack)
            print(self.hp)










    
