import random

class Settings:
    """储存《飞机大战》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        self.caption = "Aircraft War"
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

        # 图片的路径及文件名
        self.fighter_image_file = 'images/fighter.png'
        self.bullet_image_file = 'images/bullet.png'
        self.star_image_file = 'images/star.png'
        self.enemy_image_file = 'images/enemy.png'

        # 战斗机的设置
        self.fighter_speed_factor = 0.8

        # 子弹的设置
        self.bullet_speed_factor = 1

        # 星空的设置
        self.star_speed_factor = random.uniform(0.2, 1)

        # 敌人的设置
        self.enemy_speed_factor = 0.1
