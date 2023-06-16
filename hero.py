import pygame
import time


class Hero:
    def __init__(self, ai_game):
        self.screen = ai_game # получаем размер экрана
        self.screen_rect = ai_game.get_rect()
        # пакмен и начальная позиция
        self.walk_r = pygame.image.load('images/pac_r2.bmp')
        self.walk_l = pygame.image.load('images/pac_l2.bmp')
        self.walk_d = pygame.image.load('images/pac_d2.bmp')
        self.walk_u = pygame.image.load('images/pac_u2.bmp')
        self.rect = self.walk_r.get_rect()  # рисуем пакмена
        self.rect.center = self.screen_rect.center # распологаем пакмена по середине
        self.mov = 0 # переменная для направления движения
        
        """Флаги для непрерывного движения"""
        self.mov_right = False
        self.mov_left = False
        self.mov_up = False
        self.mov_down = False

    def update(self):  # движение
        if self.mov_right and self.rect.right < self.screen_rect.right - 5:
            self.rect.x += 10
        if self.mov_left and self.rect.left > 5 and not self.mov_up:
            self.rect.x -= 10
        if self.mov_up and self.rect.y > 5:
            self.rect.y -= 10
        if self.mov_down and self.rect.bottom < self.screen_rect.bottom - 5:
            self.rect.y += 10

    def blitme(self): # картинка
        if self.mov == 0:
            self.screen.blit(self.walk_r, self.rect)
        elif self.mov == 1:
            self.screen.blit(self.walk_l, self.rect)
        elif self.mov == 2:
            self.screen.blit(self.walk_u, self.rect)
        elif self.mov == 3:
            self.screen.blit(self.walk_d, self.rect)



