import random
from code.Const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        # O random.randint garante que o carro apareça em uma posição X aleatória
        # Ajuste sdos limites (50 a WIN_WIDTH-50) para ele não nascer fora da pista
        random_x = random.randint(50, WIN_WIDTH - 50)
        super().__init__(name, (random_x, position[1]))

    def move(self):
        # Inimigos vão pra baixo (sentido positivo de Y)
        self.rect.centery += ENTITY_SPEED[self.name]