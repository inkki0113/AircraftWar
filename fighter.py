import pygame


class Fighter:

    def __init__(self, screen, fighter_image_file, ai_settings):
        """初始化战斗机并设置其初始位置"""
        self.screen = screen

        # 加载战斗机图像并获取其外接矩形
        self.image = pygame.image.load(fighter_image_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 每艘战斗机初始位置在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom + 10

        # 在战斗机的属性center中储存小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.speed = ai_settings.fighter_speed_factor

    def update(self):
        """根据移动标志调整战斗机的位置"""
        # 更新战斗机的centerx与centery值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.speed

        # 根据self.centerx与self.centery更新rect
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """在指定位置绘制战斗机"""
        self.screen.blit(self.image, self.rect)
