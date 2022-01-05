import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 60
        self.rect.y = player.rect.y + 80
        self.speed = 5
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove_left(self):
        self.player.all_projectiles_left.remove(self)

    def remove_right(self):
        self.player.all_projectiles_right.remove(self)

    def move_right(self):
        self.rect.x += self.speed
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            monster.damage(self.player.attack)
            self.remove_right()
        if self.rect.x > 1050:
            self.remove_right()
        self.rotate()

    def move_left(self):
        self.rect.x -= self.speed
        if self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
        if self.rect.x < 1:
            self.remove_left()

        self.rotate()





