import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #Class that manages the firing of bullets from a spacecraft
    def __init__(self,ai_settings,screen,ship):
        super().__init__()
        self.screen = screen
        #Create a bullet rectangle at (0,0) and set the correct position
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #Stores bullet positions as decimals
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        #move bullet up
        #Update the decimal value representing the bullet position
        self.y -= self.speed_factor
        #Update the rect position representing the bullet
        self.rect.y = self.y

    def draw_bullet(self):
        #Draw bullets on screen
        pygame.draw.rect(self.screen,self.color,self.rect)


