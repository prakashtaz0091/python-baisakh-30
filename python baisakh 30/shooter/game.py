import pygame
from Game_objects.spaceship import Spaceship
from Game_objects.bullet import Bullet
from Game_objects.enemy import Enemy, create_new_enemy
import pygame.mixer

from helpers import (
    clean_screen,
    check_if_bullet_hits_enemy,
    check_if_space_ship_hits_enemy,
    show_bullet_count,
)


pygame.init()
pygame.mixer.init()
pygame.font.init()

bullet_count_font = pygame.font.SysFont("Monospace", 20)


WIDTH, HEIGHT = 800, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter Game")


# load sounds
fire_sound = pygame.mixer.Sound("./assets/sounds/fire.mp3")
explosion = pygame.mixer.Sound("./assets/sounds/explosion.wav")


# load images
spaceship_img = pygame.image.load("./assets/images/ship.png").convert_alpha()
space_ship = Spaceship(spaceship_img, x=WIDTH // 2, y=HEIGHT - 100, scale=0.2)

bullet_img = pygame.image.load("./assets/images/bullet.png").convert_alpha()

enemy_img = pygame.image.load("./assets/images/enemy.png").convert_alpha()


clock = pygame.time.Clock()
last_shot = 0
last_enemy_spawn = 0
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

    if pygame.time.get_ticks() - last_enemy_spawn > 500:
        last_enemy_spawn = pygame.time.get_ticks()
        create_new_enemy(enemy_img, screen_width=WIDTH)

    # collision between spaceship and enemies
    check_if_bullet_hits_enemy(Bullet, Enemy, explosion)
    hit = check_if_space_ship_hits_enemy(space_ship, Enemy)
    if hit:
        run = False

    # drawings
    Enemy.show(SCREEN)

    Bullet.show_bullets(SCREEN)

    space_ship.show(SCREEN)

    # bullet count
    show_bullet_count(SCREEN, bullet_count_font, Bullet)

    # update
    pygame.display.flip()


pygame.quit()
