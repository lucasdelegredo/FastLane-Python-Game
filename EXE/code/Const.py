import pygame

# Cores
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_YELLOW = (255, 255, 0)

# Dimensões da Janela
WIN_WIDTH = 576
WIN_HEIGHT = 324

# Opções do Menu (Exigência do Trabalho)
MENU_OPTION = ('INICIAR CORRIDA',
               'VER RECORDES',
               'SAIR')

# Velocidades Iniciais
ENTITY_SPEED = {
    'Estrada': 3,
    'Player1': 5,
    'Inimigo1': 4,
    'Inimigo2': 6,
}

# Eventos Customizados
EVENT_ENEMY = pygame.USEREVENT + 1
SPAWN_TIME = 2000  # Surgir um inimigo a cada 2 segundos

# Teclas de Controle (Exigência do Trabalho)
PLAYER_KEY_UP = pygame.K_w
PLAYER_KEY_DOWN = pygame.K_s
PLAYER_KEY_LEFT = pygame.K_a
PLAYER_KEY_RIGHT = pygame.K_d