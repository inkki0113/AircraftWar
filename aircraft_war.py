import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from fighter import Fighter


def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.caption)

    # 创建屏幕上的各元素
    fighter = Fighter(screen, ai_settings.fighter_image_file, ai_settings)
    bullets = Group()

    stars = Group()
    gf.create_stars(screen, ai_settings, stars)

    enemies = Group()
    gf.create_enemies(screen, ai_settings, enemies)

    # 开始游戏的主循环
    while True:
        gf.check_events(fighter, screen, ai_settings, bullets)
        gf.update_stars(stars, ai_settings)
        fighter.update()
        gf.update_enemies(enemies)
        gf.update_bullets(bullets)
        gf.update_screen(screen, ai_settings, fighter, bullets, stars, enemies)


run_game()
