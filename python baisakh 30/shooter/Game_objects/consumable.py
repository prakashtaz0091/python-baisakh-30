import pygame
import random


class Consumable(pygame.sprite.Sprite):
    consumables_list = []
    MAX_CONSUMABLE_ON_SCREEN = 2

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
        self.mask = pygame.mask.from_surface(self.image)

    def destroy(self):
        Consumable.consumables_list.remove(self)

    @staticmethod
    def check_if_consumable_out_of_screen(screen_height=0):
        for consumable in Consumable.consumables_list:
            if consumable.rect.y >= screen_height:
                Consumable.consumables_list.remove(consumable)

    @staticmethod
    def move(screen_height):
        Consumable.check_if_consumable_out_of_screen(screen_height)
        for consumable in Consumable.consumables_list:
            consumable.rect.y += consumable.speed

    @staticmethod
    def show(screen):
        Consumable.move(screen_height=screen.get_height())
        for consumable in Consumable.consumables_list:
            screen.blit(consumable.image, consumable.rect)

    @staticmethod
    def create_new_consumable(consumable_img, screen_width=0):
        # check if there is enough enemies
        if len(Consumable.consumables_list) >= Consumable.MAX_CONSUMABLE_ON_SCREEN:
            return

        x = random.randint(100, screen_width - 100)
        y = random.randint(-500, -100)
        new_consumable = Consumable(consumable_img, x, y, scale=0.1)

        Consumable.consumables_list.append(new_consumable)
