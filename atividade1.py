class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome=nome
        self.preco=preco
        self.estoque=estoque

    def exibir_detalhes(self):
        print(f"Produto:{self.nome} | Preço: R${self.preco} | Estoque:{self.estoque} unidades")
    
    def preco_final(self):
        print(f"Preço Final: R${self.preco}")
    
    def emitir_nota(self):
        print(f"Nota gerada para {self.nome}.")

p=Produto("Teclado",100.0,20)
p.exibir_detalhes()

class ProdutoNacional(Produto):
    def __init__(self, nome, preco, estoque):
        super().__init__(nome, preco, estoque)
    def preco_final(self):
        print(f"Preço Final do Produto Nacional: R${self.preco}")
    def emitir_nota(self):
        print(f"Nota fiscal nacional para {self.nome}.")

class ProdutoImportado(Produto):
    def __init__(self, nome, preco, estoque, taxa_importacao):
        super().__init__(nome, preco, estoque)
        self.taxa_importacao=taxa_importacao
    def exibir_detalhes(self):
        print(f"Produto Importado: {self.nome} | Preço: R${self.preco} | Estoque: {self.estoque} unidades | Taxa de importação: {self.taxa_importacao}")
    def preco_final(self):
        print(f"Preço Final do Produto Importado: R${self.preco +(self.preco * self.taxa_importacao)}")
    def emitir_nota(self):
        print(f"Nota de importação para {self.nome} com taxa aplicada.")

#pedido do exercício 2
c = ProdutoImportado("Celular",200.0,5,0.15)
c.exibir_detalhes()

#pedido do exercício 3
c.preco_final()
n = ProdutoNacional("Cadeira", 150.0, 10)
n.preco_final()

#teste do exercício 4
c.emitir_nota()
n.emitir_nota()


