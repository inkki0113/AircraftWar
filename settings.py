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
        self.enemy_image_file = 'images/enemy.png'
        self.star_image_file = 'images/star.png'

        # 战斗机的设置
        self.fighter_limit = 3

        # 子弹的设置
        self.bullet_speed_factor = 10

        # 杀死每个敌人的得分
        self.enemy_point = 10

        self.speedup_scale = 2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.fighter_speed_factor = 8

    def increase_speed(self):
        """提高速度设置"""
        self.fighter_speed_factor *= self.speedup_scale
