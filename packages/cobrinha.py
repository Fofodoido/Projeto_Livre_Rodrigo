import random
import pygame

class Cobra():
    def __init__(self, cobrinha, dificuldade):
        self.cobrinha = cobrinha
        self.dificuldade = dificuldade
        self.tamanho = 20
        self.velocidade = {"Facil": 8, "Médio": 12, "Difícil": 18}[dificuldade]
        self.largura = 600
        self.altura = 400
        self.clock = pygame.time.Clock()
        self.direcao = pygame.K_RIGHT
        self.serpente = [(100, 100), (80, 100), (60, 100)]
        self.comida = self._gerar_comida()
        self.pontos = 0

    def _gerar_comida(self):
        return (
            random.randrange(0, self.largura, self.tamanho),
            random.randrange(0, self.altura, self.tamanho)
        )

    def jogar(self):
        print("Iniciando jogo...")
        pygame.init()
        print("Pygame iniciado")
        tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption(f"Snake - {self.cobrinha}")
        fonte = pygame.font.SysFont(None, 36)
        pygame.time.delay(5000) 
        rodando = True
        try:
            while rodando:
                self.clock.tick(self.velocidade)
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        print("Fechando o jogo...")
                        rodando = False
                    elif evento.type == pygame.KEYDOWN:
                        print(f"Tecla pressionada: {pygame.key.name(evento.key)}")
                        if evento.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                            if (evento.key == pygame.K_UP and self.direcao != pygame.K_DOWN or
                                evento.key == pygame.K_DOWN and self.direcao != pygame.K_UP or
                                evento.key == pygame.K_LEFT and self.direcao != pygame.K_RIGHT or
                                evento.key == pygame.K_RIGHT and self.direcao != pygame.K_LEFT):
                                self.direcao = evento.key

                x, y = self.serpente[0]
                if self.direcao == pygame.K_UP:
                    y -= self.tamanho
                elif self.direcao == pygame.K_DOWN:
                    y += self.tamanho
                elif self.direcao == pygame.K_LEFT:
                    x -= self.tamanho
                elif self.direcao == pygame.K_RIGHT:
                    x += self.tamanho

                nova_cabeca = (x, y)

                if x < 0 or x >= self.largura or y < 0 or y >= self.altura or nova_cabeca in self.serpente:
                    print("Colisão! Game Over!")
                    rodando = False
                    break

                self.serpente.insert(0, nova_cabeca)

                if nova_cabeca == self.comida:
                    self.pontos += 10
                    self.comida = self._gerar_comida()
                else:
                    self.serpente.pop()

                tela.fill((0, 0, 0))
                for bloco in self.serpente:
                    pygame.draw.rect(tela, (0, 255, 0), (*bloco, self.tamanho, self.tamanho))
                pygame.draw.rect(tela, (255, 0, 0), (*self.comida, self.tamanho, self.tamanho))

                texto_pontos = fonte.render(f"Pontos: {self.pontos}", True, (255, 255, 255))
                tela.blit(texto_pontos, (10, 10))

                pygame.display.flip()  

        except Exception as e:
            print(f"Erro durante o jogo: {e}")
        finally:
            pygame.quit()  
        return self.pontos
