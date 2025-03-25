import random

"""
Módulo de configuração contendo constantes globais para o jogo.
"""

SCREEN_WIDTH = 800  # Largura da tela
SCREEN_HEIGHT = 600  # Altura da tela

# Cores RGB
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

FPS = 100  # Taxa de quadros por segundo

SPEED = random.choice([-1, 1])  # Velocidade inicial aleatória

COLOR_MAX = 255
COLOR_MIN = 0
