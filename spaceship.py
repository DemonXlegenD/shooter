import pygame
import time
from projectile import Projectile
from particules import Smart_bomb
import animation
#Classe du vaiseau du joueur
class Spaceship(animation.AnimateSprite):

    
    def __init__(self, game, max_hp, velocity, attack):
        self.game = game
        self.hp = max_hp
        self.max_hp = max_hp
        self.velocity = velocity
        self.upgrade = 1
        self.attack = attack * (self.upgrade/2)
        self.ult = False
        self.smart_bomb_count = 5
        
        self.killed = 0

        # Animation
        self.first_frame = True
        self.wait_anim = time.time()


        if self.upgrade == 1:
            super().__init__('spaceship1_')

        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200

        self.all_projectile = pygame.sprite.Group()
        self.all_upgrades = pygame.sprite.Group()
        self.all_smart_bomb = pygame.sprite.Group()

    def update_animation(self):
        self.animate(500, False)
        self.first_frame = False


    def update_health_bar(self, surface):
        #definir la couleur de la jauge de vie
        bar_color = (0, 255, 0) #vert
        #definir une couleur pour l'arriere plan de la jauge
        back_bar_color = (60, 60, 60)

        #definir la position de la jauge de vie + largeur+ epaisseur
        hp = (self.hp / self.max_hp) * 200
        bar_position = [self.rect.x, self.rect.y - 20, hp, 10]
        #definir la positiond e l'arrere plan de la jauge
        back_bar_position = [self.rect.x, self.rect.y - 20, 200, 10]

        #dessine la bar de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)



    def launch_projectile(self):
        self.all_projectile.add(Projectile(self, 0, 0, self.upgrade)) # les 0 signifient que le projectile est lancé par le joueur
        self.start_animation()

    def ultimate(self, ultime):
        if self.ult == True:
            for enemy in self.game.all_enemy:
                enemy.remove(True)
            ultime.percent = 0
            self.ult = False
            print(self.ult)

    def smart_bomb(self):
        if self.smart_bomb_count != 0:
            for enemy in self.game.all_enemy:
                for proj in enemy.all_projectile:
                    proj.remove()
                    self.smart_bomb_count -= 1
            self.all_smart_bomb.add(Smart_bomb(self.rect.x, self.rect.y, self))
                        # Réparer la smart bomb : lag + problemes d'agrandissment + empecher de tirer apres quelques secondes
            self.smart_bomb_count -= 1
                    
    def get_health(hp, max_hp, heal):
        if hp+heal <= max_hp:
            hp += heal
        else:
            hp = max_hp 

    def damage(self, amount, ultime):
        if (self.hp - amount <= 0) :
            self.game.test_score()
            #si le joueur n'a plus de point de vie
            self.game.game_over()
            ultime.percent = 0
        else:
            self.hp -= amount
            
            

    
    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
    
    def move_down(self):
        self.rect.y += self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def upgrade_ship(self):
        if self.upgrade == 2:
            # self.image = pygame.image.load('PygameAssets/spaceship2_.png')
            super().__init__('spaceship2_')
        elif self.upgrade == 3:
            # self.image = pygame.image.load('PygameAssets/spaceship3_.png')
            super().__init__('spaceship3_')
        elif self.upgrade == 4:
            # self.image = pygame.image.load('PygameAssets/spaceship4_.png')
            super().__init__('spaceship4_')
        elif self.upgrade == 5:
            # self.image = pygame.image.load('PygameAssets/spaceship5_.png')
            super().__init__('spaceship5_')
        elif self.upgrade == 6:
            # self.image = pygame.image.load('PygameAssets/spaceship6_.png')
            super().__init__('spaceship6_')
        self.attack = self.attack + 2*self.upgrade
        self.image = pygame.transform.scale(self.image, (200, 150))

        if self.game.score > 500:
            self.game.test_score()
            #si le joueur n'a plus de point de vie
            self.game.game_over()