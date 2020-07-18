import pygame.font


class Button:

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # 设置按钮的大小及文字的属性
        self.width = 200
        self.height = 50
        self.button_color = (255, 250, 240)
        self.text_color = (255, 99, 71)
        self.msg = "PLAY"
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect((0, 0), (self.width, self.height))
        self.rect.center = self.screen_rect.center

        # 创建按钮标签
        self.prep_msg(self.msg)

    def prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
