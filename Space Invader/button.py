import pygame

class Button():
    def __init__(button_self, x, y): 
        button_self.image = pygame.image.load("Graphic/restart1.png")
        new_size = (120, 60)  #Adjust the size
        button_self.image = pygame.transform.scale(button_self.image, new_size) # Scale the original image to the new size
        button_self.rect = button_self.image.get_rect(topleft = (x, y)) #get rect for collision and set position
        button_self.press_sound = pygame.mixer.Sound("Sound/restart.wav")

    def button_pressed(button_self):
        action = False
        pos = pygame.mouse.get_pos() #get mouse position
        if button_self.rect.collidepoint(pos): #if the mouse coordinates fall within button rectangle
            if pygame.mouse.get_pressed()[0] == 1: #if clicked
                action = True
                button_self.press_sound.play()
        return action