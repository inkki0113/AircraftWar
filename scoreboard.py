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
        self.prep_score()
        self.prep_level()

    def prep_score(self):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.score = str(self.stats.score)
        self.score_image = self.font.render(self.score, True, self.text_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.top = 10
        self.score_image_rect.right = 790

    def prep_level(self):
        self.level = "LV:" + str(self.stats.level)
        self.level_image = self.font.render(self.level, True, self.text_color)
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.top = self.score_image_rect.bottom + 10
        self.level_image_rect.right = 790

    def draw_scoreboard(self):
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
