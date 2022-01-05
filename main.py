import pygame
import math
from game import Game

pygame.init()

screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("shooter")

background = pygame.image.load("assets/bg.jpg")

banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)
banner_rect.y = 0

play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = banner_rect.x + 63
play_button_rect.y = banner_rect.y + 360

sound = pygame.mixer.Sound("assets/sounds/click.ogg")

game = Game()

running = True

while running:

    screen.blit(background, (0, -200))

    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_UP:
                game.player.lunch_projectile_right()

            elif event.key == pygame.K_DOWN:
                game.player.lunch_projectile_left()

            elif event.key == pygame.K_z:
                game.player.auto_spawn()

            elif event.key == pygame.K_e:
                game.player.max_health()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
                sound.play()


pygame.quit()
