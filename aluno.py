class Aluno:
    
    # __init__ é uma função construtora de objetos da classe
    # defini como padrão o valor 0 para nota e freq caso não sejam informados
    def __init__(self, nome, idade, nota = 0, freq = 0):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        self.freq = freq

    def aprovado(self):
        if self.nota >= 6.0 and self.freq >= 0.75:
            return True
        else:
            return False