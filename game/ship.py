import pygame

#Manages most of the ship's behavior
class Ship():
    def __init__(self,ai_settings,screen):
        #Initialize the ship and set its initial position
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the ship image and get its bounding rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Place each new ship in the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store a decimal value in the center property of the ship
        self.center = float(self.rect.centerx)

        #moving sign
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #Adjust the position of the ship according to the moving mark
        #Update the center value of the ship instead of the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #Update the rect object according to self.center
        self.rect.centerx = self.center

    def blitme(self):
        #Draw the ship at the specified location
        self.screen.blit(self.image,self.rect)