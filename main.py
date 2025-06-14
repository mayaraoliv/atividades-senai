from produtos_classes import Produto, ProdutoImportado, ProdutoNacional
from funcionarios import Funcionario, FuncionarioCLT, FuncionariosPJ

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

#teste do exercicio 6
print()
p_clt=FuncionarioCLT("Marianina", 5000)
p_clt.calcular_pagamento()

p_pj= FuncionariosPJ("Juana",120,20)
p_pj.calcular_pagamento()