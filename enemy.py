import pygame
from pygame.sprite import Sprite

import random


class Enemy(Sprite):
    """一个对背景敌人进行管理的类"""

    def __init__(self, screen, ai_settings):
        super(Enemy, self).__init__()
        self.screen = screen

        # 加载敌人图像并获得其外接矩形
        self.image = pygame.image.load(ai_settings.enemy_image_file).convert_alpha()
        self.rect = self.image.get_rect()

        # 初始位置
        self.rect.centerx = random.randint(50, 750)
        self.rect.bottom = 0
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)
