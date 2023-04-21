import pygame
import random
import time
import animation
from projectile import Projectile
from powerup import PowerUp 
from particules import Explosion

#Classe des ennemis
class Enemy(animation.AnimateSprite):

    def __init__(self, game, type, difficulty, surface):
        self.game = game
        self.type = type
        self.difficulty = difficulty

        self.spawned = False

        if type == 0:
            super().__init__("asteroid")
            self.hp = 100 * self.difficulty
            self.max_hp = 100 * self.difficulty
            self.speed = 2 * self.difficulty
            self.attack = 30 * self.difficulty
            self.image = pygame.transform.scale(self.image, (200,184))
        elif type == 1:
            super().__init__("ship1_")
            self.hp = 30 * self.difficulty
            self.max_hp = 30 * self.difficulty
            self.speed = 0 * self.difficulty
            self.attack = 200 * self.difficulty
            self.image = pygame.transform.scale(self.image, (200,75))
        elif type == 2:
            super().__init__("ship2_")
            self.hp = 25 * self.difficulty
            self.max_hp = 25 * self.difficulty
            self.speed = 0 * self.difficulty
            self.attack = 200 * self.difficulty
            self.image = pygame.transform.scale(self.image, (200,75))




        self.all_projectile = pygame.sprite.Group()
        # self.image = pygame.transform.scale(self.image, (1200,1200))
        self.rect = self.image.get_rect()
        self.projectileHit = 0
        self.destroy = time.time()

        self.rect.x = 2300
        self.rect.y = random.randint(10, surface.get_height()-250)

        self.launch = time.time()
        self.wait = time.time()
        self.nbr_max = 3
        self.nbr_actuel = 0

        self.gone_where = random.randint(-5, 5)

        # Animation
        self.first_frame = True
        self.wait_anim = time.time()


    def update_animation(self):
        self.animate(self.type, False)
        self.first_frame = False

# idée : changer la couleur de la barre en fonction de l'environnement
    def update_health_bar(self, surface):
        #definir la couleur de la jauge de vie
        bar_color = (255, 0, 0) #rouge
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
        

    def remove(self, drop, explode):
        # Est ce que drop de powerup ou non + determination de laquelle
        if drop == True:
            powerup_ornot = random.randint(0, 2*(self.difficulty*2))
            if powerup_ornot == 0:

                # Tous les bonus peuvent se drop
                powerups = [(0, True), (1, True), (2, True)]
                # heal =  0
                # upgrade = 1
                # score = 2

                #  Powerup heal desactivé
                if self.game.player.hp == self.game.player.max_hp:
                    powerups[0] = (0, False)

                # Powerup upgrade desactivé -> plus l'upgrade est haute, plus c'est difficile d'avoir de nouveaux bonus upgrade
                if self.game.player.upgrade == 6:
                    powerups[1] = (1, False)
                elif not self.game.player.upgrade == 1:
                    if random.randint(1,self.game.player.upgrade) == 1:
                        powerups[1] = (1, False)

                # Filtrer les powerups pour supprimer ceux qui sont en False
                available_powerups = list(filter(lambda x: x[1], powerups))
                    # lambda permet de vérifier le deuxieme element de chaque tuple dans powerups

                # Sélectionner un powerup de manière aléatoire parmi ceux qui sont en True
                if available_powerups:
                    selected_powerup = random.randint(0, len(available_powerups)-1)
                    powerup_value = available_powerups[selected_powerup][0]
                    self.spawnPowerup(powerup_value)


        # self.spawnPowerup(1)
        if explode:
            if self.type == 0:
                self.game.all_explo.add(Explosion(self.rect.x, self.rect.y, self.game, True))
            else:
                self.game.all_explo.add(Explosion(self.rect.x, self.rect.y, self.game, False))
            self.game.player.killed += 1
        print(self.game.player.killed)
        self.game.all_enemy.remove(self)

    def spawnPowerup(self, type):
        self.game.player.all_upgrades.add(PowerUp(self, type))


    # Spawn
    def spawn(self):
        if (self.type == 1 or self.type == 2) and self.rect.x > 1604:
            self.rect.x -= 5
        else:
            self.spawned = True
        if self.type == 0 and self.rect.x < 1900:
            self.spawned = True
        
    # Sort de l'écran apres etre trop resté
    def gone(self):
        self.rect.x += 10
        self.rect.y -= self.gone_where
        if self.rect.y < -200 or self.rect.x > 2100:
            self.remove(False, False)

    # Prend des dégâts
    def damage(self, amount, ultime):
        if (self.hp - amount < amount) :
            self.remove(True, True)
            ultime.percent += 0.5
            self.game.score += 10
        else:
            self.hp -= amount

    def launch_projectile(self):
        self.all_projectile.add(Projectile(self.game.player, self, 1, 0))
        self.start_animation()

    def forward(self, ultime):


        #mets des degats aux joueurs si collision et supprime l'ennemi
        if self.game.check_collision(self, self.game.all_players):
            self.remove(False, True)
            self.game.player.damage(self.attack, ultime)
        else:
            self.spawn()
            self.rect.x -= self.speed

        # fais disparaitre les ennemis hors de l'ecran
        if self.rect.x < -200:
            self.remove(False, False)

        # fait disparaitre les ennemis fixes
        if self.destroy + 10 < time.time() and (self.type == 1 or self.type == 2):
            self.gone()


        # Tirer des missiles pour le type 1
        if self.type == 1 and self.rect.x == 1600:
            if self.launch + 2/self.difficulty <= time.time():
                self.launch_projectile()
                self.launch = time.time()

        # Tirer des missiles pour le type 2
        if self.type == 2 and self.rect.x == 1600:
            if self.launch + 3/self.difficulty <= time.time():
                if self.nbr_actuel < self.nbr_max:
                    if self.wait + 0.5 <= time.time():
                        self.launch_projectile()
                        self.nbr_actuel += 1
                        self.wait = time.time()
                if self.nbr_actuel >= self.nbr_max:
                    self.launch = time.time()
                    self.nbr_actuel = 0
