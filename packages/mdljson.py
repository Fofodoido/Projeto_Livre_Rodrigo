import json
from packages.jogo import Jogo
from packages.cobrinha import Cobra
class Jason():
    def __init__(self,filename):
        self.__filename = "packages/db/" + filename
        self.__models=[]
        self.read()

    def read(self):
        try:
            with open(self.__filename, "r", encoding="utf-8") as fjson:
                self.__models=json.load(fjson)
        except FileNotFoundError:
            print(f"O arquivo {self.__filename} não existe.")
            self.__models=[]
        
    def save(self):
        try:
            with open(self.__filename, "w", encoding="utf-8") as fjson:
                json.dump(self.__models,fjson, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar os dados: {e}")
            
    def get_models(self):
        return self.__models
    

class Placar(Jason):
    def __init__(self, filename):
        super().__init__(filename)
        
    def adicionar_placar(self,nome,pontuacao,dificuldade):
        novo_recorde= {"nome": nome, "pontuacao":pontuacao, "dificuldade": dificuldade}
        self.__models.append(novo_recorde)
        self.__models = sorted(self.__models, key=lambda x: x["pontuacao"], reverse=True)
        self.save()
    
    def exibir_placar(self):
        if not self.__models:
            print("Não há placares registrados ainda.")
        else:
            print("Placar completo:")
            for i, recorde in enumerate(self.__models, start=1):
                print(f"{i}. {recorde['nome']} - {recorde['pontuacao']} pontos - Dificuldade: {recorde['dificuldade']}")        
    
class Jogador(Jason):
    def __init__(self, filename):
        super().__init__(filename)