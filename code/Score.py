import sys
import pygame
from pygame import Surface, Rect
from code.Const import WIN_WIDTH, WIN_HEIGHT, C_YELLOW, C_WHITE
from code.DBProxy import DBProxy

class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        self.surf.fill((0, 0, 0))  # Fundo preto para o placar
        self.rect = self.surf.get_rect(left=0, top=0)

    def show(self):
        # 1. Busca os dados do Banco usando o Proxy
        db_proxy = DBProxy('MeuJogoScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        while True:
            # 2. Desenha o fundo e o título
            self.window.blit(source=self.surf, dest=self.rect)
            self.draw_text(40, 'TOP 10 PILOTOS', C_YELLOW, (WIN_WIDTH / 2, 40))
            self.draw_text(20, 'NOME      PONTOS      DATA', C_YELLOW, (WIN_WIDTH / 2, 90))

            # 3. Lista os resultados
            for index, player_score in enumerate(list_score):
                name, score, date = player_score
                # Exibe cada linha do banco de dados
                text = f"{name}      {score:05d}      {date}"
                self.draw_text(18, text, C_WHITE, (WIN_WIDTH / 2, 130 + (index * 20)))

            self.draw_text(15, 'Pressione ESC para voltar', C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT - 30))
            pygame.display.flip()

            # 4. Eventos para sair do Placar
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return  # Volta para o menu principal

    def draw_text(self, size: int, text: str, color: tuple, center_pos: tuple):
        font = pygame.font.SysFont("Lucida Sans Typewriter", size)
        text_surf = font.render(text, True, color).convert_alpha()
        text_rect = text_surf.get_rect(center=center_pos)
        self.window.blit(source=text_surf, dest=text_rect)