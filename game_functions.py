import sys

import pygame
import random
from time import sleep

from bullet import Bullet
from star import Star
from enemy import Enemy


def check_keydown_event(event, fighter, screen, ai_settings, bullets):
    """响应按下按键"""
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_RIGHT:
        fighter.moving_right = True
    if event.key == pygame.K_LEFT:
        fighter.moving_left = True
    if event.key == pygame.K_UP:
        fighter.moving_up = True
    if event.key == pygame.K_DOWN:
        fighter.moving_down = True
    if event.key == pygame.K_SPACE:
        fire_bullets(screen, ai_settings, fighter, bullets)


def check_keyup_event(event, fighter):
    """响应松开按键"""
    if event.key == pygame.K_RIGHT:
        fighter.moving_right = False
    if event.key == pygame.K_LEFT:
        fighter.moving_left = False
    if event.key == pygame.K_UP:
        fighter.moving_up = False
    if event.key == pygame.K_DOWN:
        fighter.moving_down = False


def check_events(fighter, screen, ai_settings, bullets, play_button, stats, enemies, scoreboard):
    """监视键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, fighter, screen, ai_settings, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, fighter)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(play_button, mouse_x, mouse_y, stats, enemies, bullets, screen,
                              ai_settings, fighter, scoreboard)


def check_play_button(play_button, mouse_x, mouse_y, stats, enemies, bullets, screen, ai_settings, fighter, scoreboard):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.reset_stats()
        stats.game_active = True

        scoreboard.prep_msg()

        enemies.empty()
        bullets.empty()

        create_enemies(screen, ai_settings, enemies)
        fighter.center_fighter()

        pygame.mouse.set_visible(False)


def create_stars(screen, ai_settings, stars):
    for _ in range(30):
        star = Star(screen, ai_settings)
        stars.add(star)


def update_stars(stars, ai_settings):
    """更新星星位置，并重置到达底部的星星"""
    # 更新星星位置
    stars.update()
    # 重置到达底部的星星的位置和速度
    for star in stars.copy():
        if star.rect.y > 600:
            star.rect.x = random.randint(1, ai_settings.screen_width)
            star.rect.y = random.randint(0, 100)
            star.speed = random.randint(2, 8)


def create_enemies(screen, ai_settings, enemies):
    for _ in range(3):
        enemy = Enemy(screen, ai_settings)
        enemies.add(enemy)


def update_enemies(enemies, bullets, stats, fighter, screen, ai_settings):
    enemies.update()
    check_enemy_bottom(enemies, bullets, stats, fighter, screen, ai_settings)
    check_enemy_fighter(fighter, enemies, bullets, stats, ai_settings, screen)


def check_enemy_bottom(enemies, bullets, stats, fighter, screen, ai_settings):
    for enemy in enemies.sprites():
        if enemy.rect.bottom == 600:
            enemy_hit(enemies, bullets, fighter, stats, ai_settings, screen)
            break


def enemy_hit(enemies, bullets, fighter, stats, ai_settings, screen):
    if stats.fighter_left > 0:
        enemies.empty()
        bullets.empty()
        create_enemies(screen, ai_settings, enemies)

        stats.fighter_left -= 1

        fighter.center_fighter()

        sleep(0.5)
    else:
        stats.game_active = False
        stats.reset_stats()


def check_enemy_fighter(fighter, enemies, bullets, stats, ai_settings, screen):
    if pygame.sprite.spritecollideany(fighter, enemies):
        enemy_hit(enemies, bullets, fighter, stats, ai_settings, screen)


def fire_bullets(screen, ai_settings, fighter, bullets):
    # 创建一个子弹，并加入到编组bullets中
    new_bullet = Bullet(screen, ai_settings, fighter)
    bullets.add(new_bullet)


def check_bullets_enemies(bullets, enemies, stats, ai_settings, scoreboard):
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, False)
    if collisions:
        for enemies in collisions.values():
            for enemy in enemies:
                enemy.rect.centerx = random.randint(50, 750)
                enemy.rect.bottom = 0
                enemy.speed = random.randint(1, 3)

            stats.score += ai_settings.enemy_point * len(enemies)
            scoreboard.prep_msg()


def update_bullets(bullets, enemies, stats, ai_settings, scoreboard):
    """更新子弹位置，并删除已消失的子弹"""
    # 更新子弹位置
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

    check_bullets_enemies(bullets, enemies, stats, ai_settings, scoreboard)


def update_screen(screen, ai_settings, fighter, bullets, stars, enemies, stats, play_button, scoreboard):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    stars.draw(screen)
    bullets.draw(screen)
    fighter.blitme()
    enemies.draw(screen)
    scoreboard.draw_scoreboard()

    if not stats.game_active:
        play_button.draw_button()
        pygame.mouse.set_visible(True)

    pygame.display.update()
