import pygame
from Game_objects.bullet import create_new_bullet, Bullet


class Spaceship(pygame.sprite.Sprite):
    speed = 5

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
        self.mask = pygame.mask.from_surface(self.image)

    def show(self, screen):
        screen.blit(self.image, (self.rect.x - self.width / 2, self.rect.y))

    def move_left(self):
        if self.rect.x >= self.width // 2:
            self.rect.x -= Spaceship.speed

    def move_right(self, limit=None):
        if limit is not None:  # if there is a limit
            if self.rect.x >= limit:
                return

        self.rect.x += Spaceship.speed

    def move_forward(self):
        if self.rect.y <= 0:
            return
        self.rect.y -= Spaceship.speed

    def move_backward(self, limit=None):
        if limit is not None:
            if self.rect.y >= limit:
                return
        self.rect.y += Spaceship.speed

    def fire(self, bullet_img, fire_sound):
        if Bullet.magaze <= 0:  # magaze empty
            return
        fire_sound.play()
        create_new_bullet(bullet_img, self.rect.x, self.rect.y)

    def destroy(self):
        print("game over")
