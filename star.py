import pygame
from pygame.sprite import Sprite

import random


class Star(Sprite):
    """一个对背景星空进行管理的类"""
    
    def __init__(self, screen, ai_settings):
        super(Star, self).__init__()
        self.screen = screen

        # 加载星星图像并获得其外接矩形
        self.image = pygame.image.load('images/star.png').convert_alpha()
        self.rect = self.image.get_rect()

        # 初始位置
        self.rect.centerx = random.randint(1, ai_settings.screen_width)
        self.rect.centery = random.randint(0, 500)
        self.speed = random.randint(2, 8)

    def star_move(self):
        self.rect.centery += self.speed

    def check_star_bottom(self, ai_settings):
        if self.rect.centery > 600:
            self.rect.centerx = random.randint(1, ai_settings.screen_width)
            self.rect.centery = random.randint(0, 100)
            self.speed = random.randint(2, 8)

    def blitme(self):
        """在指定位置绘制星星"""
        self.screen.blit(self.image, self.rect)
