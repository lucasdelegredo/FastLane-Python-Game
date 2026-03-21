import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu
from code.Level import Level
from code.Score import Score

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Fast Lane: Desafio de Sobrevivência")

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]: # 'INICIAR CORRIDA'
                level = Level(self.window, 'Level1', menu_return)
                level.run()
                from datetime import datetime
                from code.DBProxy import DBProxy

                # Exemplo de salvamento após o jogo
                pontos_finais = 150 # Esse valor viria do level.run()
                nome_piloto = "PILOT" # Você pode criar um input simples no pygame para isso

                db = DBProxy("MeuJogoScore")
                data = {
                    'name': nome_piloto,
                    'score': pontos_finais,
                    'date': datetime.now().strftime("%d/%m/%Y %H:%M")
                }
                db.save(data)
                db.close()
            
            # No método run do Game.py
            elif menu_return == MENU_OPTION[1]: # 'VER RECORDES'
                score_screen = Score(self.window)
                score_screen.show()
                            
            elif menu_return == MENU_OPTION[2]: # 'SAIR'
                pygame.quit()
                quit()