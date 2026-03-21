# Fast Lane - Jogo de Corrida Top-Down
**Disciplina:** Linguagem de Programação Aplicada  
**Instituição:** Centro Universitário Internacional UNINTER

Este projeto é um simulador de corrida desenvolvido em **Python** utilizando a biblioteca **Pygame**. O objetivo é desviar dos obstáculos e inimigos o maior tempo possível, acumulando pontuação que é salva de forma persistente.
<img width="572" height="351" alt="fastlane1" src="https://github.com/user-attachments/assets/e27bec6e-1d07-40e5-ae60-1e8b3f198e45" />

<img width="569" height="345" alt="fastlanerecord1" src="https://github.com/user-attachments/assets/9a492b54-0797-4c4d-a25e-a8b083db6985" />

<img width="574" height="348" alt="image" src="https://github.com/user-attachments/assets/79ced743-b89c-4103-9046-c458ffea65e5" />

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
