import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """一个对战斗机发射的子弹进行管理的类"""

    def __init__(self, screen, ai_settings, fighter):
        """在战斗机顶端处创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 加载子弹图像并获得其外接矩形
        self.image = pygame.image.load(ai_settings.bullet_image_file).convert_alpha()
        self.rect = self.image.get_rect()

        # 初始位置
        self.rect.bottom = fighter.rect.top
        self.rect.centerx = fighter.rect.centerx

        # 储存用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.speed = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        self.y -= self.speed
        self.rect.y = self.y

    def blitme(self):
        """在指定位置绘制子弹"""
        self.screen.blit(self.image, self.rect)
