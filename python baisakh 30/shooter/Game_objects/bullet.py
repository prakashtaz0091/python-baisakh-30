import pygame


class Bullet(pygame.sprite.Sprite):
    speed = 10
    bullets_list = []
    magaze = 50

    def __init__(self, image, x=0, y=0, scale=1):
        super().__init__()

        self.image = pygame.transform.scale(image, (image.get_width() * scale, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.height = self.rect.height
        self.width = self.rect.width
        self.mask = pygame.mask.from_surface(self.image)

    def show(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.y -= Bullet.speed

    def destroy(self):
        Bullet.bullets_list.remove(self)

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

    @classmethod
    def decrease_magaze(cls):
        cls.magaze -= 1


def create_new_bullet(bullet_img, x, y):
    new_bullet = Bullet(bullet_img, x, y, scale=0.1)
    Bullet.decrease_magaze()

    Bullet.bullets_list.append(new_bullet)
