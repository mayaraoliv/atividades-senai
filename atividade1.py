class Produto:
    def __init__(self,nome,preco,estoque):
        self.nome=nome
        self.preco=preco
        self.estoque=estoque
    def exibir_detalhes(self):
        print(f"Produto:{self.nome} | Preço: R${self.preco} | Estoque:{self.estoque} unidades")
        pass
p=Produto("Teclado",100.0,20)
p.exibir_detalhes()
