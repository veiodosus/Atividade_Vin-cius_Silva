class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo, estado = 'vivo', estado_civil = 'solteiro', conjuge = None):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo
        self.__estado = estado
        self.__estado_civil = estado_civil
        self.__conjuge =  conjuge

    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @property
    def estado(self):
        return self.__estado
    @property
    def estado_civil(self):
        return self.__estado_civil
    @property
    def conjuge(self):
        return self.__conjuge
    
    @estado_civil.setter
    def estado_civil(self, estado_civil):
        self.__estado_civil = estado_civil
    @conjuge.setter
    def conjuge(self, conjuge):
        self.__conjuge = conjuge

    def __str__(self):
        if self.__conjuge == None:
            return f'\n| Nome: {self.__nome} | Idade: {self.__idade} anos | Peso: {self.__peso}kg |\n| Altura: {self.__altura} | Sexo: {self.__sexo} | Estado civil: {self.__estado_civil} |'
        else:
            return f'\n| Nome: {self.__nome} | Idade: {self.__idade} anos | Peso: {self.__peso}kg |\n| Altura: {self.__altura} | Sexo: {self.__sexo} | Estado civil: {self.__estado_civil}. Conjuge: {self.__conjuge.nome} |'
    
    def envelhecer(self):
        if self.__estado != 'morto':
            if self.__idade < 21:
                self.__altura += 1
            self.__idade += 0.5

    def engordar(self, peso):
        if self.__estado != 'morto':
            self.__peso += peso

    def emagrecer(self, peso):
        if self.__estado != 'morto':
            self.__peso -= peso

    def crescer(self, altura):
        if self.__idade < 21 and self.__estado != 'morto':
            self.__altura += altura
        else:
            print('Pessoas maiores de 21 anos não podem mais crescer!')

    def casar(self, conjuge_p):
        if self.__idade > 18 and self.__estado != 'morto' and self.__estado_civil == 'solteiro' and conjuge_p.idade > 18 and conjuge_p.estado != 'morto' and conjuge_p.estado_civil == 'solteiro':
            self.__estado_civil = 'casado(a)'
            self.__conjuge = conjuge_p
            conjuge_p.estado_civil = 'casado(a)'
            conjuge_p.conjuge = self
           

jonas = Pessoa('Jonas', 34, 70, 180, 'M')
maria = Pessoa('Maria', 34, 70, 180, 'F')

print(jonas)
print(maria)

jonas.casar(maria)
jonas.engordar(10)

print(jonas)
print(maria)

    