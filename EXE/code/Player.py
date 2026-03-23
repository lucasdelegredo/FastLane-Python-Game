#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, \
    PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT
from code.Entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        # Guardamos a imagem original (reta) para usar como base na rotação
        self.original_surf = self.surf 

    def move(self):
        # Captura as teclas pressionadas
        pressed_key = pygame.key.get_pressed()
        
        # Variável para controlar a inclinação visual
        rotation = 0 

        # Movimento para Cima
        if pressed_key[PLAYER_KEY_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        
        # Movimento para Baixo
        if pressed_key[PLAYER_KEY_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        
        # Movimento para Esquerda (limite da pista)
        if pressed_key[PLAYER_KEY_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
            rotation = 15  # Inclina 15 graus para a esquerda
        
        # Movimento para Direita (limite da pista)
        if pressed_key[PLAYER_KEY_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
            rotation = -15 # Inclina 15 graus para a direita

        # Aplica a rotação baseada na imagem original
        # pygame.transform.rotate cria uma nova superfície rotacionada
        self.surf = pygame.transform.rotate(self.original_surf, rotation)
        
        # Ajustamos o rect para o novo tamanho da imagem rotacionada 
        # (isso evita que o carro "vibre" ou saia do lugar ao girar)
        old_center = self.rect.center
        self.rect = self.surf.get_rect(center=old_center)

        self.rect = self.surf.get_rect(center=old_center)
        self.mask = pygame.mask.from_surface(self.surf)

        self.surf = pygame.transform.rotate(self.original_surf, rotation)
        self.rect = self.surf.get_rect(center=old_center)
        self.mask = pygame.mask.from_surface(self.surf) # Atualiza a máscara com a nova rotação