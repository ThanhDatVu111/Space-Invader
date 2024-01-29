import pygame, random
from spaceship import Spaceship
from obstacle import Obstacle
from obstacle import grid
from alien import Alien
from lazer2 import Lazer2
from alien import MysteryShip
from explosion import Explosion

class Game:
    def __init__(game_self, screen_width, screen_height): #automatically executed when an instance of that class is created
        game_self.screen_width = screen_width
        game_self.screen_height = screen_height
        game_self.spaceship_group = pygame.sprite.GroupSingle()
        game_self.spaceship_group.add(Spaceship(game_self.screen_width, game_self.screen_height))
        game_self.obstacles = game_self.create_obstacles()
        game_self.aliens_group = pygame.sprite.Group()
        game_self.create_alien()
        game_self.aliens_direction = 1
        game_self.alien_lazers_group = pygame.sprite.Group()
        game_self.mystery_ship_group = pygame.sprite.GroupSingle()
        game_self.explosion_group = pygame.sprite.Group()


    def create_obstacles(game_self):
        obstacle_width = len(grid[0]) * 3 #23 * 3 = 69 , length of one obstacle
        gap = (game_self.screen_width - (4 * obstacle_width))/5
        obstacles_list = []
        for i in range(4):
            offset_x = (i + 1) * gap + i * obstacle_width
            obstacle = Obstacle(offset_x, game_self.screen_height - 175)
            obstacles_list.append(obstacle)
        return obstacles_list #this list will hold 5 obstacles with calculated position

    def create_alien(game_self):
        for row in range(5):
            for column in range(11):
                x = 75 + column * 55
                y = 110 + row * 55
                if row == 0:
                    alien_type = 1
                elif row == 1:
                    alien_type = 2
                elif row == 2:
                    alien_type = 3
                elif row == 3:
                    alien_type = 4
                else:
                    alien_type = 5
                alien = Alien(alien_type, x, y)
                game_self.aliens_group.add(alien)

    def move_aliens(game_self):
        game_self.aliens_group.update(game_self.aliens_direction)
        aliens_sprite_list = game_self.aliens_group.sprites()
        for alien in aliens_sprite_list: #if the alien at the end or start of the list hit the left or right barrier, 
                                         #it change the direction for all the alien
            if alien.rect.right >= game_self.screen_width:
                game_self.aliens_direction = -1
                game_self.move_aliens_down(2)
            elif alien.rect.left <= 0:
                game_self.aliens_direction = 1
                game_self.move_aliens_down(2)

    def move_aliens_down(game_self, distance):
        aliens_sprite_list = game_self.aliens_group.sprites()
        if aliens_sprite_list:
            for alien in aliens_sprite_list:
                alien.rect.y += distance

    def alien_shoot_lazer(game_self):
        if game_self.aliens_group.sprites():
            random_alien = random.choice(game_self.aliens_group.sprites())
            laser_sprite = Lazer2(random_alien.rect.center, -6, game_self.screen_height)
            game_self.alien_lazers_group.add(laser_sprite)

    def create_mystery_ship(game_self):
         game_self.mystery_ship_group.add(MysteryShip(game_self.screen_width))

    def check_for_collision(game_self):
        if game_self.spaceship_group.sprite.lazer_group: #if spaceship shoot lazer, lazer exist in the lazer group
            for ship_lazer_sprite in game_self.spaceship_group.sprite.lazer_group:
                if pygame.sprite.spritecollide(ship_lazer_sprite, game_self.aliens_group, True):
                    ship_lazer_sprite.kill()
                    explosion = Explosion(ship_lazer_sprite.rect.centerx, ship_lazer_sprite.rect.centery, 2)
                    game_self.explosion_group.add(explosion)