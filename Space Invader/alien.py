import pygame, random

class Alien(pygame.sprite.Sprite):
    def __init__(alien_self, type, x, y):
        super().__init__() 
        alien_self.type = type
        path = f"Graphic/alien_{type}.png"
        alien_self.image = pygame.image.load(path).convert_alpha()
        alien_self.rect = alien_self.image.get_rect(topleft = (x, y))

    def update(alien_self, aliens_direction):
        alien_self.rect.x += aliens_direction

class MysteryShip(pygame.sprite.Sprite):
    def __init__(ms_self, screen_width):
        super().__init__() 
        ms_self.screen_width = screen_width
        original_image = pygame.image.load("Graphic/mystery.png").convert_alpha()
        new_size = (90, 90)  #Adjust the size
        ms_self.image = pygame.transform.scale(original_image, new_size)
        x = random.choice([0, ms_self.screen_width - ms_self.image.get_width()]) #random in list coint 0 or the position of the picture nearest to the right border
        if x == 0:
            ms_self.speed = 3
        else:
            ms_self.speed = -3
        ms_self.rect = ms_self.image.get_rect(topleft = (x, 40))

    def update(ms_self):
        ms_self.rect.x += ms_self.speed
        if ms_self.rect.right > ms_self.screen_width:
            ms_self.kill()
        elif ms_self.rect.left < 0:
            ms_self.kill()
