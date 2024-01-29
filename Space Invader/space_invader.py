import pygame, sys, random
from game import Game

pygame.init()
screen_width = 750
screen_height = 700
game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("🚀🛸 SPACE INVADER 🛸🚀")

FPS = 60
game_clock = pygame.time.Clock()
game = Game(screen_width, screen_height)
bg = pygame.image.load("Graphic/space_bg.png")

SHOOT_LAZER = pygame.USEREVENT #USEREVENT help me to create my own event in this game
pygame.time.set_timer(SHOOT_LAZER, 300) # trigger this SHOOT_LAZER every 300 milliseconds. 

MYSTERY_SHIP_SPAWN = pygame.USEREVENT + 1 #create a new event ID that is distinct from the one represented by pygame.USEREVENT
pygame.time.set_timer(MYSTERY_SHIP_SPAWN, random.randint(4000,8000)) #trigger ms spawn every 4 to 8 seconds. 

#game loop
while True:
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() #close window
        if event.type == SHOOT_LAZER:
            game.alien_shoot_lazer()
        if event.type == MYSTERY_SHIP_SPAWN:
            game.create_mystery_ship()

    #updating
    game.spaceship_group.update()
    game.move_aliens()
    game.alien_lazers_group.update()
    game.mystery_ship_group.update()
    game.check_for_collision()
    game.explosion_group.update()

    #drawing 
    game_screen.blit(bg, (0, 0)) #update background
    game.spaceship_group.draw(game_screen)
    game.spaceship_group.sprite.lazer_group.draw(game_screen)
    game.aliens_group.draw(game_screen)
    game.alien_lazers_group.draw(game_screen)
    game.mystery_ship_group.draw(game_screen)
    game.explosion_group.draw(game_screen)
    for obs in game.obstacles: #drawing obstacle by looping through the list that create_obstacle() return
        obs.blocks_group.draw(game_screen)
    
    pygame.display.update()
    game_clock.tick(FPS)