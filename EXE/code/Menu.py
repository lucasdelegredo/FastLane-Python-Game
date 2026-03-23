#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame
from pygame import Surface, Rect
from code.Const import WIN_WIDTH, WIN_HEIGHT, C_YELLOW, C_WHITE, MENU_OPTION

class Menu:
    def __init__(self, window: Surface):
        self.window = window
        # Se tiver uma imagem de fundo para o menu, mude o nome aqui
        try:
            self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        except:
            # Caso não tenha a imagem ainda, cria um fundo preto
            self.surf = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
            self.surf.fill((0, 0, 0))
            
        self.rect = self.surf.get_rect(left=0, top=0)
        self.menu_index = 0  # Indica qual opção está selecionada

    def run(self):
        # Opcional: tocar música do menu
        # pygame.mixer_music.load('./asset/Menu.mp3')
        # pygame.mixer_music.play(-1)

        while True:
            # 1. Desenha o fundo
            self.window.blit(source=self.surf, dest=self.rect)

            # 2. Desenha o Título e os Comandos (EXIGÊNCIA DO TRABALHO)
            self.draw_text(40, "FAST LANE: CORRIDA", C_YELLOW, (WIN_WIDTH / 2, 50))
            self.draw_text(18, "CONTROLOS: W, A, S, D para Dirigir", C_WHITE, (WIN_WIDTH / 2, 100))

            # 3. Desenha as Opções do Menu
            for i in range(len(MENU_OPTION)):
                color = C_YELLOW if i == self.menu_index else C_WHITE
                self.draw_text(25, MENU_OPTION[i], color, (WIN_WIDTH / 2, 180 + (i * 35)))

            pygame.display.flip()

            # 4. Verifica Eventos de Teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.menu_index > 0:
                            self.menu_index -= 1
                        else:
                            self.menu_index = len(MENU_OPTION) - 1
                    
                    if event.key == pygame.K_DOWN:
                        if self.menu_index < len(MENU_OPTION) - 1:
                            self.menu_index += 1
                        else:
                            self.menu_index = 0
                    
                    if event.key == pygame.K_RETURN:  # Tecla Enter
                        return MENU_OPTION[self.menu_index]

    def draw_text(self, size: int, text: str, color: tuple, center_pos: tuple):
        font = pygame.font.SysFont("Arial", size, bold=True)
        text_surf = font.render(text, True, color).convert_alpha()
        text_rect = text_surf.get_rect(center=center_pos)
        self.window.blit(source=text_surf, dest=text_rect)