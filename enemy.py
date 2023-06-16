import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):  # враги
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        """загрузка изображения"""
        self.image = pygame.image.load('images/ghost.bmp')
        self.rect = self.image.get_rect() # высвечиваем врага на экран