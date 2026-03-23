#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        if entity_name == 'Estrada':
            # Retornamos duas partes da estrada para o efeito infinito
            return [Background('Estrada', (0, 0)), 
                    Background('Estrada', (0, -324))] # -324 é o WIN_HEIGHT
        
        if entity_name == 'Player1':
            return Player('Player1', (288, 260)) # Posição inicial no centro/baixo
        
        if entity_name in ['Inimigo1', 'Inimigo2']:
            return Enemy(entity_name, (0, -50)) # Nasce um pouco acima da tela
        
        return None