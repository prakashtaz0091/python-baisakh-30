import pygame
import random


class Enemy(pygame.sprite.Sprite):
    enemies_list = []
    MAX_ENEMY_ON_SCREEN = 10

    def __init__(self, image, x=0, y=0, scale=1):
        super().__init__()

        self.image = pygame.transform.scale(
            image, (image.get_width() * scale, image.get_height() * scale)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.height = self.rect.height
        self.width = self.rect.width
        self.speed = random.randint(1, 4)
        # self.rect.center = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def destroy(self):
        Enemy.enemies_list.remove(self)

    @staticmethod
    def check_if_enemy_out_of_screen(screen_height=0):
        for enemy in Enemy.enemies_list:
            if enemy.rect.y >= screen_height:
                Enemy.enemies_list.remove(enemy)

    @staticmethod
    def move(screen_height):
        Enemy.check_if_enemy_out_of_screen(screen_height)
        for enemy in Enemy.enemies_list:
            enemy.rect.y += enemy.speed

    @staticmethod
    def show(screen):
        Enemy.move(screen_height=screen.get_height())
        for enemy in Enemy.enemies_list:
            screen.blit(enemy.image, enemy.rect)


def create_new_enemy(enemy_img, screen_width=0):
    # check if there is enough enemies
    if len(Enemy.enemies_list) >= Enemy.MAX_ENEMY_ON_SCREEN:
        return

    x = random.randint(100, screen_width - 100)
    y = random.randint(-500, -100)
    random_scale = random.uniform(0.05, 0.11)
    new_enemy = Enemy(enemy_img, x, y, scale=random_scale)

    Enemy.enemies_list.append(new_enemy)
