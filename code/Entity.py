from abc import ABC, abstractmethod
import pygame
from pygame import Surface, Rect

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        # 1. Carrega a imagem original
        self.surf: Surface = pygame.image.load(f'./asset/{name}.png').convert_alpha()

        # 2. Redimensionar de acordo com o tipo de objeto
        if 'Estrada' in self.name:
            # Força a estrada a ocupar a tela inteira
            self.surf = pygame.transform.scale(self.surf, (576, 324))
        elif 'Player' in self.name or 'Inimigo' in self.name:
            # Força os carros a terem um tamanho padrão de jogo top-down
            # (40 pixels de largura por 80 de altura)
            self.surf = pygame.transform.scale(self.surf, (40, 80))

        # 3. Definirr o retângulo de colisão BASEADO NO NOVO TAMANHO
        self.rect: Rect = self.surf.get_rect(left=position[0], top=position[1])

        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.mask = pygame.mask.from_surface(self.surf)
        
        # Atributos básicos
        self.health = 100 
        self.score = 0

        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.mask = pygame.mask.from_surface(self.surf) # CRUCIAL

    @abstractmethod
    def move(self):
        """Este método deve ser implementado obrigatoriamente em cada subclasse"""
        pass