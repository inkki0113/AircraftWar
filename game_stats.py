class GameStats:
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        # 因为每次重新开始都要初始化，所以写一个方法专门存放需要初始化的数据
        self.fighter_left = self.ai_settings.fighter_limit
        self.score = 0
        self.level = 1
