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

    def repor(self, quantidade):
        self.estoque+= quantidade
        print(f"Após reposição. O estoque atual é de: {self.estoque} unidades.")
    
    def vender(self, quantidade):
        if quantidade <= self.estoque and quantidade>0:
            self.estoque -= quantidade
            print(f"Após venda. O estoque atual é de: {self.estoque} unidades.")
        else:
            return "Quantidade insuficiente a ser vendida"

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

#pedido do exercício 1
p = Produto("Teclado",100.0,20)
p.exibir_detalhes()

#pedido do exercício 2
print()
c = ProdutoImportado("Celular",200.0,5,0.15)
c.exibir_detalhes()

#pedido do exercício 3
print()
c.preco_final()
n = ProdutoNacional("Cadeira", 150.0, 10)
n.preco_final()

#teste do exercício 4
print()
c.emitir_nota()
n.emitir_nota()

#teste do exercício 5
print()
a=Produto("Chinelo",150,5)
a.repor(5)
a.vender(5)
