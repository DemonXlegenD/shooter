import pygame

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'PygameAssets/{sprite_name}.png')
        if sprite_name == 'asteroid':
            self.image = pygame.transform.scale(self.image, (200,184))
        elif sprite_name == 'ship1_':
            self.image = pygame.transform.scale(self.image, (220,75))
        elif sprite_name == 'ship2_':
            self.image = pygame.transform.scale(self.image, (220,75))
        elif sprite_name == 'spaceship1_':
            self.image = pygame.transform.scale(self.image, (200, 150))
        elif sprite_name == 'explosion':
            self.image = pygame.transform.scale(self.image, (200, 200))

        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False

    def start_animation(self):
        self.animation = True

    def animate(self, type, bigger_explosion):

        if self.animation == True:
            self.current_image += 1

            if self.current_image >= len(self.images):
                #remettre l'anime à 0
                self.current_image = 0
                self.animation = False

            self.image = self.images[self.current_image]

            if type == 0:
                self.image = pygame.transform.scale(self.image, (200,184))
            elif type == 1:
                self.image = pygame.transform.scale(self.image, (200,75))
            elif type == 2:
                self.image = pygame.transform.scale(self.image, (200,75))
            elif type == 500:
                self.image = pygame.transform.scale(self.image, (200, 150))
            elif bigger_explosion:
                self.image = pygame.transform.scale(self.image, (300, 300))

            
            




def load_animation_images(sprite_name):
    images = []
    path = f"PygameAssets/{sprite_name}/{sprite_name}"

    for num in range(0,100):
        try:
            image_path = path + str(num) + '.png'
            images.append(pygame.image.load(image_path))
        except:
            break

    return images

# ship1_ -> [...ship1_1.png, ...ship1_2.png, ...]
# ship2_ -> [...ship2_1.png, ...ship2_2.png, ...]
# spaceship1_ -> [...spaceship1_1.png, ...spaceship1_2.png, ...]
# spaceship2_ -> [...spaceship2_1.png, ...spaceship2_2.png, ...]
# spaceship3_ -> [...spaceship3_1.png, ...spaceship3_2.png, ...]
# spaceship4_ -> [...spaceship4_1.png, ...spaceship4_2.png, ...]
# spaceship5_ -> [...spaceship5_1.png, ...spaceship5_2.png, ...]
# spaceship6_ -> [...spaceship6_1.png, ...spaceship6_2.png, ...]
# explosion -> [...explosion1.png, ...explosion2.png, ...]
animations = {
    'ship1_' : load_animation_images('ship1_'),
    'ship2_' : load_animation_images('ship2_'),
    # 'asteroid' : load_animation_images('asteroid'),
    'spaceship1_' : load_animation_images('spaceship1_'),
    'spaceship2_' : load_animation_images('spaceship2_'),
    'spaceship3_' : load_animation_images('spaceship3_'),
    'spaceship4_' : load_animation_images('spaceship4_'),
    'spaceship5_' : load_animation_images('spaceship5_'),
    'spaceship6_' : load_animation_images('spaceship6_'),
    'explosion' : load_animation_images('explosion')
}
