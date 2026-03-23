import random
import sys
import pygame
from pygame import Surface, Rect
from code.Const import C_WHITE, WIN_HEIGHT, WIN_WIDTH, EVENT_ENEMY, SPAWN_TIME
from code.EntityFactory import EntityFactory
from code.Player import Player
from code.Enemy import Enemy

class Level:
    def __init__(self, window: Surface, name: str, game_mode: str):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list = []

        
        # Inicializa a estrada (o Factory retorna as duas partes)
        self.entity_list.extend(EntityFactory.get_entity('Estrada'))
        
        # Inicializa o Player
        self.player = EntityFactory.get_entity('Player1')
        self.entity_list.append(self.player)
        
        # Configura o Timer para surgimento de inimigos
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        
        self.score = 0
        self.speed_multiplier = 1.0  # Para a aceleração progressiva

        pygame.mixer.music.load('./asset/MusicaTema.mp3')
        pygame.mixer.music.set_volume(0.5) # Volume em 50%
        pygame.mixer.music.play(-1) # O -1 faz a música tocar em loop infinito

    def run(self):
        
        clock = pygame.time.Clock()
        
        while True:
            clock.tick(60) # Mantém 60 FPS
            
            # 1. Desenhar e Mover entidades
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                
                # Se um inimigo sair da tela por baixo, ganha ponto
                if isinstance(ent, Enemy) and ent.rect.top > WIN_HEIGHT:
                    self.score += 10
                    self.entity_list.remove(ent)
                    # Aceleração progressiva: a cada ponto, o jogo fica levemente mais rápido
                    self.speed_multiplier += 0.05 

            # 2. Verificar Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == EVENT_ENEMY:
                    # Cria novos inimigos aleatoriamente
                    choice = random.choice(('Inimigo1', 'Inimigo2'))
                    new_enemy = EntityFactory.get_entity(choice)
                    self.entity_list.append(new_enemy)

            # 3. Verificar Colisões (Game Over)
            for ent in self.entity_list:
                if isinstance(ent, Enemy):
                    # Calcula a distância entre os dois objetos para a máscara
                    offset_x = ent.rect.x - self.player.rect.x
                    offset_y = ent.rect.y - self.player.rect.y
                    
                    # Verifica se os pixels REAIS se sobrepõem
                    if self.player.mask.overlap(ent.mask, (offset_x, offset_y)):
                        # Toca o som da batida
                        try:
                            crash_sound = pygame.mixer.Sound('./asset/crash.mp3') # Use o nome exato do seu arquivo
                            crash_sound.play()
                        except:
                            print("Aviso: Arquivo de som não encontrado ou formato incompatível.")

                        # Para a música de fundo para dar destaque à batida
                        pygame.mixer.music.stop()
                        
                        # Pequena pausa de meio segundo para o jogador ver onde bateu
                        pygame.time.delay(500) 
                        
                        print("BOOM! Game Over")
                        return self.score # Sai do level e volta para o Game/Score

            # 4. Mostrar Texto (Pontos e Velocidade)
            self.draw_text(20, f"Pontos: {self.score}", C_WHITE, (10, 10))
            
            pygame.display.flip()

    def draw_text(self, size: int, text: str, color: tuple, pos: tuple):
        font = pygame.font.SysFont("Arial", size)
        text_surf = font.render(text, True, color)
        self.window.blit(text_surf, pos)