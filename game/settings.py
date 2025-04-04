class Settings():
    #A "class" that stores all settings
    def __init__(self):
        #Initialize game settings
        #Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #ship settings
        self.ship_speed_factor = 1.5
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
