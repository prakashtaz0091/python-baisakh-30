import pygame


class Bullet(pygame.sprite.Sprite):
    speed = 10
    bullets_list = []

    def __init__(self, image, x=0, y=0, scale=1):
        super().__init__()

        self.image = pygame.transform.scale(image, (image.get_width() * scale, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.height = self.rect.height
        self.width = self.rect.width

    def show(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.y -= Bullet.speed

    @staticmethod
    def show_bullets(screen):
        # move bullets
        for bullet in Bullet.bullets_list:
            if bullet.rect.y <= 0:
                Bullet.remove_bullet(bullet)
            else:
                bullet.move()

        # show bullets
        for bullet in Bullet.bullets_list:
            bullet.show(screen)

    @classmethod
    def remove_bullet(cls, bullet):
        cls.bullets_list.remove(bullet)


def create_new_bullet(bullet_img, x, y):
    new_bullet = Bullet(bullet_img, x, y, scale=0.1)

    Bullet.bullets_list.append(new_bullet)
