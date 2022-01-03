import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):

    def __init__(self, game):

        super().__init__()
        self.game = game
        self.all_projectiles_right = pygame.sprite.Group()
        self.all_projectiles_left = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        self.speedPlayer = 3
        self.attack = 35
        self.health = 100
        self.health_max = 100

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def update_health_bar(self, surface):

        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.health_max, 8])
        pygame.draw.rect(surface, (111, 206, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 8])


    def lunch_projectile_right(self):

        self.all_projectiles_right.add(Projectile(self))

    def lunch_projectile_left(self):
        self.all_projectiles_left.add(Projectile(self))


    def move_right(self):

        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x = self.rect.x + self.speedPlayer

    def move_high(self):
        #cheat
        self.rect.y = self.rect.y - self.speedPlayer

    def move_down(self):
        #cheat
        self.rect.y = self.rect.y + self.speedPlayer


    def move_left(self):
        self.rect.x = self.rect.x - self.speedPlayer

    def auto_spawn(self):
        #cheat
        self.rect.x = 400
        self.rect.y = 500

    def max_health(self):
        self.health = self.health_max

