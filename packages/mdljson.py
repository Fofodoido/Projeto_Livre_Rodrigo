import json

class Jason():
    def __init__(self,filename):
        self.__filename = "packages/db/" + filename
        self._models=[]
        self.read()

    def read(self):
        try:
            with open(self.__filename, "r", encoding="utf-8") as fjson:
                self._models=json.load(fjson)
        except FileNotFoundError:
            print(f"O arquivo {self.__filename} não existe.")
            self._models=[]
        
    def save(self):
        try:
            with open(self.__filename, "w", encoding="utf-8") as fjson:
                json.dump(self._models,fjson, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar os dados: {e}")
            
    def get_models(self):
        return self._models
    

class Placar(Jason):
    def __init__(self, filename):
        super().__init__(filename)
        
    def adicionar_placar(self,nome,pontuacao,dificuldade):
        novo_recorde= {"nome": nome, "pontuacao":pontuacao, "dificuldade": dificuldade}
        self._models.append(novo_recorde)
        self._models = sorted(self._models, key=lambda x: x["pontuacao"], reverse=True)
        self.save()
    
    def exibir_placar(self):
        if not self._models:
            print("Não há placares registrados ainda.")
        else:
            print("Placar completo:")
            for i, recorde in enumerate(self._models, start=1):
                print(f"{i}. {recorde['nome']} - {recorde['pontuacao']} pontos - Dificuldade: {recorde['dificuldade']}")        
    
class Jogador(Jason):
    def __init__(self, filename):
        super().__init__(filename)