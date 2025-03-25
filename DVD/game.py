import sys
import pygame
from dvd import BouncingText, VerticalText, HorizontalText

from config import SCREEN_HEIGHT, SCREEN_WIDTH, FPS, PRETO, VERMELHO, BRANCO, VERDE, AZUL

"""
Módulo principal do jogo, gerencia a lógica do jogo e os eventos.
"""

class Game:
    """
    Classe principal que gerencia o jogo.

    Atributos:
        screen (pygame.Surface): Tela do jogo.
        clock (pygame.time.Clock): Relógio para controle de FPS.
        running (bool): Estado do jogo (rodando ou não).
        musics (list): Lista de arquivos de música.
        current_music_index (int): Índice da música atual.
        is_paused (bool): Indica se a música está pausada.
        texts (list): Lista de textos animados na tela.
    """

    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("DVD")
        self.clock = pygame.time.Clock()
        self.running = True

        # Configuração de música
        self.musics = [
            "musicas/believer.mp3",  
            "musicas/Kiss.mp3",
            "musicas/LoveGeneration.mp3"
        ]
        self.current_music_index = 0
        self.is_paused = False
        pygame.mixer.music.load(self.musics[self.current_music_index])
        pygame.mixer.music.play()

        # Instância de textos móveis
        self.texts = [
            BouncingText("Texto que Quica", 50, VERMELHO, SCREEN_WIDTH, SCREEN_HEIGHT),
            VerticalText("Texto Vertical", 50, VERDE, SCREEN_WIDTH, SCREEN_HEIGHT),
            HorizontalText("Texto Horizontal", 50, AZUL, SCREEN_WIDTH, SCREEN_HEIGHT),
        ]

    def play_next_music(self):
        """Troca para a próxima música da lista e reinicia a reprodução."""
        self.current_music_index = (self.current_music_index + 1) % len(self.musics)
        pygame.mixer.music.load(self.musics[self.current_music_index])
        pygame.mixer.music.play()
        self.is_paused = False

    def toggle_pause(self):
        """Alterna entre pausar e retomar a música."""
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
        else:
            pygame.mixer.music.pause()
            self.is_paused = True

    def events(self):
        """Captura eventos do teclado e do jogo."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            # Controles de música
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:  # Tecla S
                    self.play_next_music()
                if event.key == pygame.K_SPACE:  # Tecla Espaço
                    self.toggle_pause()

    def run(self):
        """Loop principal do jogo."""
        try:
            while self.running:
                self.events()
                self.screen.fill(PRETO)

                for text in self.texts:
                    text.update()
                    text.draw(self.screen)

                pygame.display.flip()
                self.clock.tick(FPS)
        finally:
            pygame.quit()
            sys.exit()
