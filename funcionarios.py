from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self,nome):
        self.nome=nome

    @abstractmethod
    def calcular_pagamento(self):
        pass
class FuncionarioCLT(Funcionario):
    def __init__(self,nome,salario):
        super().__init__(nome)
        self.salario=salario
    
    def calcular_pagamento(self):
        print(f"Salário de {self.nome}: R${self.salario}")
    
class FuncionariosPJ(Funcionario):
    def __init__(self, nome,horas_trabalhadas,valor_hora):
        super().__init__(nome)
        self.horas_trabalhadas=horas_trabalhadas
        self.valor_hora=valor_hora
    
    def calcular_pagamento(self):
        print(f"Sálario de {self.nome}: R${self.horas_trabalhadas*self.valor_hora}\n")