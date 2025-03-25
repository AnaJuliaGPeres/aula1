import sys
import pygame
import random

pygame.init()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('pygame')

clock = pygame.time.Clock()

VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE= (0, 255, 0)
ROSA =  (255, 29, 141)
AZUL = (0, 0, 255)

tamanho_fonte = 50
fonte = pygame.font.SysFont(None, tamanho_fonte)


texto = fonte.render("ana Julia", True, ROSA)
texto_rect = texto.get_rect(center=(largura/2, altura/2))
cor_texto= random.randint(10,255),random.randint(10,255),random.randint(10,255)
velocidade_x = random.randint(-1,1)
velocidade_y = random.randint(-1,1)


while velocidade_x ==0:
    velocidade_x = random.randint(-1,1)

while velocidade_y ==0:
    velocidade_y = random.randint(-1,1)
    
    
pygame.mixer.init()
  
pygame.mixer.music.load("believer.mp3")  
pygame.mixer.music.play(-1)

musica_fundo = pygame.mixer.Sound("audiocerto.mp3")  



rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill(PRETO)
    texto_rect.x += velocidade_x
    texto_rect.y += velocidade_y
    
    tela.blit(texto, texto_rect)
    
    if texto_rect.left <= 0:
        velocidade_x = random.randint(0,1)
        velocidade_Y = random.randint(-1,1)
        texto = fonte.render("ana Julia", True,  (random.randint(10,255),random.randint(10,255),random.randint(10,255)))
        musica_fundo.play()
        
    if texto_rect.right >= largura:
        velocidade_x = random.randint(-1,0)
        velocidade_y = random.randint(-1,1)
        texto = fonte.render("ana Julia", True, (random.randint(10,255),random.randint(10,255),random.randint(10,255)))
        musica_fundo.play()
        
    if texto_rect.top <= 0:
        velocidade_x = random.randint(-1,1)
        velocidade_y = random.randint(0,1)
        texto = fonte.render("ana Julia", True, (random.randint(10,255),random.randint(10,255),random.randint(10,255)))
        musica_fundo.play()
        
    if texto_rect.bottom >= altura:
        velocidade_x = random.randint(-1,1)
        velocidade_y = random.randint(-1,0)
        texto = fonte.render("ana Julia", True, (random.randint(10,255),random.randint(10,255),random.randint(10,255)))
        musica_fundo.play()
    
    clock.tick(300)
    pygame.display.flip()

pygame.quit()
sys.exit