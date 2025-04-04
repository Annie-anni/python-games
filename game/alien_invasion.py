import sys    #Exit game
import pygame #Contains the functions needed to develop games
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Initialize pygame settings and screen objects
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Create a ship
    ship = Ship(ai_settings,screen)
    bg_color = (230, 230, 230)

    #Start the main game loop
    while True:
        #Monitor keyboard and mouse events
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)

run_game()