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

        if enemy.mask.overlap(spaceship.mask, offset):
            spaceship.destroy()
            enemy.destroy()
            hit = True
            break

    return hit


def show_bullet_count(screen, font, Bullet):
    bullet_count_text = f"Bullet: {Bullet.magaze}"
    screen.blit(font.render(bullet_count_text, False, (255, 255, 255)), (10, 10))
