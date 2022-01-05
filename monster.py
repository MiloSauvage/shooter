import pygame
import random
import animation


class Monster(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("mummy")
        self.game = game

        self.health = 100
        self.health_max = 100

        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.speed = random.randint(1, 2)
        self.attack = 0.3

    def update_animation(self):
        self.animate()

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 300)
            self.speed = random.randint(1, 3)
            self.health = self.health_max

            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)
                self.game.comet_event.attempt_fall()

    def update_health_bar(self, surface):

        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 10, self.health_max, 5])
        pygame.draw.rect(surface, (111, 206, 46), [self.rect.x + 10, self.rect.y - 10, self.health, 5])


    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.speed

        else:
            self.game.player.damage(self.attack)



