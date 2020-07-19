import pygame.font


class ScoreBoard:

    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.stats = stats

        # 设置记分牌的大小及文字的属性
        self.text_color = (255, 99, 71)
        self.font = pygame.font.SysFont(None, 40)

        # 创建记分牌标签
        self.prep_msg()

    def prep_msg(self):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.score = str(self.stats.score)
        self.msg_image = self.font.render(self.score, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.top = 10
        self.msg_image_rect.right = 790

    def draw_scoreboard(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)
