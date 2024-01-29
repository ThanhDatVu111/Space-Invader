import pygame 
from lazer import Lazer

class Spaceship(pygame.sprite.Sprite):
    def __init__(ship_self, screen_width, screen_height):
        super().__init__() #invoke the constructor of the parent class.
        ship_self.screen_width = screen_width
        ship_self.screen_height = screen_height
        original_image = pygame.image.load("Graphic/ship_trans.png").convert_alpha()
        new_size = (90, 90)  #Adjust the size
        ship_self.image = pygame.transform.scale(original_image, new_size) # Scale the original image to the new size
        ship_self.rect = ship_self.image.get_rect() #create a rectangle for on the ship image (for collision)
        ship_self.rect.midbottom = (ship_self.screen_width/2, ship_self.screen_height - 20) #set position
        ship_self.speed = 5.0

        ship_self.lazer_group = pygame.sprite.Group()
        ship_self.lazer_ready = True
        ship_self.lazer_time = 0
        ship_self.lazer_delay = 300

    def get_user_input(ship_self):
        key_pressed = pygame.key.get_pressed()     
        if key_pressed[pygame.K_RIGHT]:
            ship_self.rect.x += ship_self.speed
        if key_pressed[pygame.K_LEFT]:
            ship_self.rect.x -= ship_self.speed
        if key_pressed[pygame.K_SPACE] and ship_self.lazer_ready == True:
            lazer = Lazer((ship_self.rect.center[0], ship_self.rect.centery - 40), 5, ship_self.screen_height)
            ship_self.lazer_group.add(lazer)
            ship_self.lazer_time = pygame.time.get_ticks()
            ship_self.lazer_ready = False

    def constrain_movement(ship_self):
        if ship_self.rect.right > ship_self.screen_width:
            ship_self.rect.right = ship_self.screen_width
        if ship_self.rect.left < 0:
            ship_self.rect.left = 0

    def recharge_lazer(ship_self):
        if ship_self.lazer_ready == False:
            current_time = pygame.time.get_ticks()
            if current_time - ship_self.lazer_time >= ship_self.lazer_delay:
                ship_self.lazer_ready = True

    def update(ship_self):
        ship_self.get_user_input()
        ship_self.constrain_movement()
        ship_self.lazer_group.update()
        ship_self.recharge_lazer()