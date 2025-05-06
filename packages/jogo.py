import os
import json
from packages.cobrinha import Cobra
from click import clear

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

class Jogo():
    
    def __init__(self):
        self.rodando= True
        self.dificuldade=None
        self.cont="0"
        self.nome=""
        #self.placar = json
        
    def iniciar_jogo(self):
        while True:
            print("Escolha a dificuldade:\n  1 - Fácil\n  2 - Médio\n  3 - Difícil\n  0 - Voltar")
            dificuldade=input()
            limpar_tela()
            if dificuldade == '1':
                self.dificuldade = "Facil"
            elif dificuldade == '2':
                self.dificuldade = "Médio"
            elif dificuldade == '3':
                self.dificuldade = "Difícil"
            elif dificuldade == '0':
                limpar_tela()
                self.cont='0'
                break
            else:
                limpar_tela()
                print("Opção inválida. Tente novamente.")
                continue  
            print("Insira o seu nome:")
            self.nome=input()
            self.cobrinha= Cobra(self.nome,self.dificuldade)
  
    def exibir_menu(self):
        while self.cont=="0":
            print("Bem vindo ao menu. Escolha uma das opções abaixo:\n   1 - Iniciar Jogo \n   2 - Ver placar \n   3 - Sair")
            opcao=input()
            if opcao=="1":
                limpar_tela()
                self.iniciar_jogo()
            elif opcao=='2':
                pass
            elif opcao=='3':
                limpar_tela()
                self.cont = "1"
                self.rodando=False
                print("Saindo do Jogo...")
            else:
                limpar_tela()
                print("Opção Inválida, tente novamente.")
                continue