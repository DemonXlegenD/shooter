import pygame
import math


class Button:
    def __init__(self, screen, x, y, w, h, path):
        self.screen = screen
        self.button = pygame.image.load(path)
        self.button = pygame.transform.scale(self.button, (w, h))
        self.button_rect = self.button.get_rect()
        self.button_rect.x = math.ceil(self.screen.width/x)
        self.button_rect.y = math.ceil(self.screen.height/y)
        self.is_pressed = False
        self.is_shown = False

    def show_button(self):
        if(self.is_shown):
            self.screen.screen.blit(self.button, self.button_rect)
        
    def is_button_shown(self):
        self.is_pressed = True

    def is_button_pressed(self, event):
        if(self.button_rect.collidepoint(event.pos)):
            self.is_pressed = True
        return self.is_pressed
        
