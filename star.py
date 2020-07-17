import pygame
from pygame.sprite import Sprite

import random


class Star(Sprite):
    """一个对背景星空进行管理的类"""
    
    def __init__(self, screen, ai_settings):
        super(Star, self).__init__()
        self.screen = screen

        # 加载星星图像并获得其外接矩形
        self.image = pygame.image.load(ai_settings.bullet_image_file).convert_alpha()
        self.rect = self.image.get_rect()

        # 初始位置
        self.rect.bottom = 0
        self.rect.centerx = random.randint(1, 800)

        # 储存用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.speed = ai_settings.star_speed_factor

    def update(self):
        """向下移动星星"""
        self.y += self.speed
        self.rect.y = self.y

    def blitme(self):
        """在指定位置绘制星星"""
        self.screen.blit(self.image, self.rect)
