import pygame
from Game_objects.spaceship import Spaceship
from Game_objects.bullet import Bullet
import pygame.mixer

from helpers import clean_screen


pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter Game")


# load sounds
fire_sound = pygame.mixer.Sound("./assets/sounds/fire.mp3")


# load images
spaceship_img = pygame.image.load("./assets/images/ship.png")
space_ship = Spaceship(spaceship_img, x=WIDTH // 2, y=HEIGHT - 100, scale=0.2)

bullet_img = pygame.image.load("./assets/images/bullet.png")


clock = pygame.time.Clock()
last_shot = 0
run = True
while run:
    # set fps
    clock.tick(60)

    # clean screen
    clean_screen(SCREEN)

    # look for quit event (x button)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # inputs
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        space_ship.move_left()
    elif keys[pygame.K_RIGHT]:
        space_ship.move_right(limit=WIDTH - space_ship.width + 20)

    if keys[pygame.K_UP]:
        space_ship.move_forward()
    elif keys[pygame.K_DOWN]:
        space_ship.move_backward(limit=HEIGHT - space_ship.height)

    space_key_pressed = keys[pygame.K_SPACE]
    if space_key_pressed and pygame.time.get_ticks() - last_shot > 100:
        # limit
        last_shot = pygame.time.get_ticks()
        space_ship.fire(bullet_img, fire_sound)

    # drawings

    Bullet.show_bullets(SCREEN)

    space_ship.show(SCREEN)

    pygame.display.flip()


pygame.quit()
