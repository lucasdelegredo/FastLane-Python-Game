from code.Const import WIN_HEIGHT, ENTITY_SPEED
from code.Entity import Entity

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        # A estrada move-se para baixo
        self.rect.centery += ENTITY_SPEED[self.name]
        
        # Se a imagem passar totalmente do limite inferior da janela
        if self.rect.top >= WIN_HEIGHT:
            # Ela volta para o topo, exatamente acima da outra imagem de fundo
            self.rect.bottom = 0