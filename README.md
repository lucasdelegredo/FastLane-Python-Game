# Fast Lane - Jogo de Corrida Top-Down
**Disciplina:** Linguagem de Programação Aplicada  
**Instituição:** Centro Universitário Internacional UNINTER

Este projeto é um simulador de corrida desenvolvido em **Python** utilizando a biblioteca **Pygame**. O objetivo é desviar dos obstáculos e inimigos o maior tempo possível, acumulando pontuação que é salva de forma persistente.

---

## 🛠️ Arquitetura e Padrões de Projeto
O jogo foi estruturado seguindo os conceitos avançados de Orientação a Objetos exigidos na disciplina:

* **Fábrica de Entidades (Factory Pattern):** Centralização da criação de jogadores, inimigos e cenários no arquivo `EntityFactory.py`.
* **Persistência de Dados (Proxy Pattern):** Uso da classe `DBProxy.py` para intermediar a comunicação com o banco de dados **SQLite**, garantindo que as pontuações não sejam perdidas ao fechar o jogo.
* **Herança e Polimorfismo:** Todas as entidades do jogo derivam de uma classe abstrata `Entity.py`.
* **Colisão Pixel-Perfect:** Implementação de máscaras (`pygame.mask`) para garantir que as colisões ocorram apenas nos pixels visíveis das imagens.

---

## 🚀 Como Executar

1. **Requisitos:** Certifique-se de ter o Python 3.10+ instalado.
2. **Instalação:**
   ```bash
   pip install -r requirements.txt
