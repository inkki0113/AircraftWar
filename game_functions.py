import sys

import pygame
import random

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


def check_events(fighter, screen, ai_settings, bullets):
    """监视键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, fighter, screen, ai_settings, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, fighter)


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


def update_enemies(enemies):
    enemies.update()
    for enemy in enemies.copy():
        if enemy.rect.top > 600:
            enemy.rect.centerx = random.randint(50, 750)
            enemy.rect.bottom = 0
            enemy.speed = random.randint(1, 3)


def fire_bullets(screen, ai_settings, fighter, bullets):
    # 创建一个子弹，并加入到编组bullets中
    new_bullet = Bullet(screen, ai_settings, fighter)
    bullets.add(new_bullet)


def update_bullets(bullets):
    """更新子弹位置，并删除已消失的子弹"""
    # 更新子弹位置
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)


def update_screen(screen, ai_settings, fighter, bullets, stars, enemies):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    stars.draw(screen)
    bullets.draw(screen)
    fighter.blitme()
    enemies.draw(screen)

    pygame.display.update()
