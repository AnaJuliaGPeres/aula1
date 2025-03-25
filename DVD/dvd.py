import pygame
import random
from abc import ABC, abstractmethod
from config import SCREEN_WIDTH, SCREEN_HEIGHT, SPEED, COLOR_MAX, COLOR_MIN

"""
Módulo que define classes para movimentação de texto na tela.
"""

pygame.mixer.init()
collision_sound = pygame.mixer.Sound('audiocerto.mp3')

class MoveText(ABC):
    """
    Classe abstrata que representa um texto móvel na tela.

    Atributos:
        text (str): O texto a ser exibido.
        font_size (int): Tamanho da fonte do texto.
        initial_color (tuple): Cor inicial do texto (RGB).
        screen_width (int): Largura da tela.
        screen_height (int): Altura da tela.
    """

    def __init__(self, text, font_size, initial_color, screen_width, screen_height):
        pygame.font.init()
        self.font = pygame.font.SysFont(None, font_size)
        self.color = initial_color
        self.text = text
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.text_surf = self.font.render(self.text, True, self.color)
        self.rect = self.text_surf.get_rect(center=(screen_width // 2, screen_height // 2))
        self.speed_x = SPEED if random.choice([True, False]) else -SPEED
        self.speed_y = SPEED if random.choice([True, False]) else -SPEED

    def _change_color(self):
        """Muda a cor do texto ao mudar de direção."""
        self.color = (
            random.randint(COLOR_MIN, COLOR_MAX),
            random.randint(COLOR_MIN, COLOR_MAX),
            random.randint(COLOR_MIN, COLOR_MAX),
        )
        self.text_surf = self.font.render(self.text, True, self.color)

    def draw(self, screen):
        """Desenha o texto na tela."""
        screen.blit(self.text_surf, self.rect)

    @abstractmethod
    def update(self):
        """Método abstrato: deve ser implementado pelas subclasses."""
        pass

class BouncingText(MoveText):
    """
    Classe que representa um texto que se move e quica nas bordas da tela.
    """

    def update(self):
        """Move o texto e muda de direção aleatoriamente, mas muda de cor somente ao bater nas bordas."""
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        color_changed = False  # Flag para controlar mudança de cor

        if self.rect.left <= 0 or self.rect.right >= self.screen_width:
            self.speed_x *= -1
            self._change_color()
            color_changed = True
            collision_sound.play()

        if self.rect.top <= 0 or self.rect.bottom >= self.screen_height:
            self.speed_y *= -1
            if not color_changed:
                self._change_color()
            collision_sound.play()

        # Muda de direção aleatoriamente (5% de chance a cada frame) sem mudar a cor
        if random.random() < 0.05:
            self.speed_x = random.choice([SPEED, -SPEED])
            self.speed_y = random.choice([SPEED, -SPEED])

class VerticalText(MoveText):
    """Classe que representa um texto que se move apenas na vertical."""

    def update(self):
        """Move o texto apenas na vertical e muda de cor ao bater nas bordas."""
        self.rect.y += self.speed_y
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_height:
            self.speed_y *= -1
            self._change_color()
            collision_sound.play()

class HorizontalText(MoveText):
    """Classe que representa um texto que se move apenas na horizontal."""

    def update(self):
        """Move o texto apenas na horizontal e muda de cor ao bater nas bordas."""
        self.rect.x += self.speed_x
        if self.rect.left <= 0 or self.rect.right >= self.screen_width:
            self.speed_x *= -1
            self._change_color()
            collision_sound.play()
