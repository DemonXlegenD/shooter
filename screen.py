import pygame
import math
import time

class Screen:
    def __init__(self, w, h):
        #Width, height of the screen and of the background
        self.width = w
        self.height = h
        self.bg_width = w
        self.bg_height = h 
        
        #State of the screen
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.scroll = 0
        self.tiles = math.ceil(self.width/self.bg_width) + 1
        self.seconde = time.time()

        #Background
        pygame.display.set_caption("Shoot'em up")
        self.background = pygame.image.load('PygameAssets/space/bgspace.jpg')
        self.background = pygame.transform.scale(self.background, (self.bg_width, self.bg_height))
        self.banner = pygame.image.load('PygameAssets/space/banner.png')
        self.banner = pygame.transform.scale(self.banner, (600, 500))
        self.banner_rect = self.banner.get_rect()
        self.banner_rect.x = math.ceil((self.screen.get_width()-600)/2)
        self.banner_rect.y = math.ceil(self.screen.get_height()/70)
        self.gameover = pygame.image.load('PygameAssets/gameover.png')
        self.gameover = pygame.transform.scale(self.gameover, (700, 500))
        self.gameover_rect = self.gameover.get_rect()
        self.gameover_rect.x = math.ceil((self.screen.get_width()-700)/2)
        self.gameover_rect.y = -700 


    def show_screen(self):

        
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.banner, self.banner_rect)
        
    def end_screen(self):    
        self.gameover_rect.y += 10
        
        
            
    def change_bg(self, path):
        self.background = pygame.image.load(path)
        self.background = pygame.transform.scale(self.background, (self.bg_width, self.bg_height))
    
    def scrolling(self, t):
        if abs(self.scroll) > self.bg_width:
            self.scroll = 0
        for i in range(0, self.tiles):
            self.screen.blit(self.background, (i * self.bg_width + self.scroll, 0))
        self.scroll -= t