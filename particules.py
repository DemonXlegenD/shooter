import pygame
import animation
import time

class Explosion(animation.AnimateSprite):

    def __init__(self, x, y, game, bigger):
        super().__init__('explosion')

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.game = game
        self.bigger = bigger
        self.remove_time = time.time()
        self.wait_anim = time.time()
        self.first = True

        self.start_animation()



    def remove(self):
        self.game.all_explo.remove(self)

    def update_animation(self):
        self.animate(None, self.bigger)
        self.first = False


class Smart_bomb(pygame.sprite.Sprite):

    def __init__(self, x, y, player):
        super().__init__()

        self.image = pygame.image.load('PygameAssets/wave.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.player = player
        self.size = 500
        self.growtime = time.time()

    def remove(self):
        self.player.all_smart_bomb.remove(self)

    def growing(self, size):
        self.size += size
        self.rect.x -= size/2
        self.rect.y -= size/2

        self.image = pygame.transform.scale(self.image, (self.size, self.size))

        for enemy in self.player.game.all_enemy:
            for proj in self.player.game.check_collision(self, enemy.all_projectile):
                proj.remove()

        if self.size > 2000:
            self.remove()