import pygame

class Ship:
    '''A class to manage ship'''

    def __init__(self,ai_game):
        """Initialize the ship and srt its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        '''we access the screen’s rect attribute using the get_rect()
        method and assign it to self.screen_rect. Doing so allows us to place the
        ship in the correct location on the screen.'''
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image,(50,100)) 
        self.rect = self.image.get_rect()
        
        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        
        # Movement flags

        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Updates the ships possition based on the movement flags
            updating the ship's X value not the rect'''
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Updating rect value
        self.rect.x = self.x

    def blitme(self):
        '''Draw the ship at its current location'''
        self.screen.blit(self.image,self.rect)
