import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu
from code.Level import Level
from code.Score import Score
from code.DBProxy import DBProxy  # <--- ADICIONE ESTA LINHA (Resolve o erro do DBProxy)
from datetime import datetime
import sys

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
                
                # O level.run() agora retorna a pontuação real acumulada
                pontos_finais = level.run() 
                
                # Salvamento no Banco de Dados
                nome_piloto = "PILOTO_01" 
                db = DBProxy("MeuJogoScore")
                data = {
                    'name': nome_piloto,
                    'score': pontos_finais, # <--- USANDO A VARIÁVEL REAL AQUI
                    'date': datetime.now().strftime("%d/%m/%Y %H:%M")
                }
                db.save(data)
                db.close()

                # Mostra o placar atualizado
                score_screen = Score(self.window)
                score_screen.show()
            
            # No método run do Game.py
            elif menu_return == MENU_OPTION[1]: # 'VER RECORDES'
                score_screen = Score(self.window)
                score_screen.show()
                            
            elif menu_return == MENU_OPTION[2]: # 'SAIR'
                pygame.quit()
                pygame.quit() # Encerra o Pygame com segurança
                sys.exit()    # Encerra o processo do Windows