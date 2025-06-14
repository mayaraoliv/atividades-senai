class Produto:
    def __init__(self,nome,preco,estoque):
        self.nome=nome
        self.preco=preco
        self.estoque=estoque
    def exibir_detalhes(self):
        print(f"Produto:{self.nome} | Preço: R${self.preco} | Estoque:{self.estoque} unidades")

p=Produto("Teclado",100.0,20)
p.exibir_detalhes()

class ProdutoNacional(Produto):
    def __init__(self,nome,preco,estoque):
        super().__init__(nome,preco,estoque)

class ProdutoImportado(Produto):
    def __init__(self,nome,preco,estoque,taxa_importacao):
        super().__init__(nome,preco,estoque)
        self.taxa_importacao=taxa_importacao
    def exibir_detalhes(self):
        print(f"Produto Importado: {self.nome} | Preço: R${self.preco} | Estoque: {self.estoque} unidades | Taxa de importação: {self.taxa_importacao}")


c=ProdutoImportado("Celular",200.0,5,0.15)
c.exibir_detalhes()
