import pygame


def fill_background_with(image, screen, scale=1, screen_height=0):
    image = pygame.transform.scale(image, (image.get_width() * scale, screen_height))
    screen.blit(image, (0, 0))


def clean_screen(screen):
    screen.fill((0, 0, 0))  # black


def check_if_bullet_hits_enemy(Bullet, Enemy, explosion):
    for bullet in Bullet.bullets_list:
        for enemy in Enemy.enemies_list:
            offset = (
                enemy.rect.left - bullet.rect.left,
                enemy.rect.top - bullet.rect.top,
            )

            if bullet.mask.overlap(enemy.mask, offset):
                explosion.play()
                bullet.destroy()
                enemy.destroy()
                break


def check_if_space_ship_hits_enemy(spaceship, Enemy):
    hit = False
    for enemy in Enemy.enemies_list:
        offset = (
            enemy.rect.left - spaceship.rect.left,
            enemy.rect.top - spaceship.rect.top,
        )

        if spaceship.mask.overlap(enemy.mask, offset):
            spaceship.destroy()
            enemy.destroy()
            hit = True
            break

    return hit


def show_bullet_count(screen, font, Bullet):
    bullet_count_text = f"Bullet: {Bullet.magaze}"
    screen.blit(font.render(bullet_count_text, False, (255, 255, 255)), (10, 10))


def check_if_spaceship_hits_consumable(spaceship, Consumable, Bullet):
    for consumable in Consumable.consumables_list:
        offset = (
            consumable.rect.left - spaceship.rect.left,
            consumable.rect.top - spaceship.rect.top,
        )

        if spaceship.mask.overlap(consumable.mask, offset):
            Bullet.refill_magaze()
            consumable.destroy()
            break
