# produtos/almoxarifado.py — a classe Almoxarifado guarda os produtos de uma unidade

class Almoxarifado:
    # Construtor: o almoxarifado nasce com o nome da unidade e sem produtos
    def __init__(self, unidade):
        self.unidade = unidade
        self.prod


# Guarda um objeto Produto no fim da lista
    def adicionar(self, produto):
        self.produtos.append(produto)

    def buscar(self,produto):
        for a in self.produto:
            if a.codigo == self.codigo:
              return a
        return None

    def entrada(self,codigo,qtd):
        p = self.buscar(codigo)
        if p is None:
            return False

        p.entrada(qtd)
        return True

    def saida(self,codigo,qtd):

        p= self.buscar

        if p is None:
             return False
        return p.saida(qtd)



    def listar(self):
        lista = []
        for p in self.produtos:
            lista.append(p.listar_produtos())
            return lista


    def solicitacao_compra(self):
        pedido = []

        for p in self.produtos:
            if p.solicitacao() !="OK":
                pedido.append({
                    "codigo": p.codigo,
                    "nome" : p.listar_produtos()["nome"],
                    "situacao":p.solicitacao()

                })
        return pedido

    def valor_estoque(self):
        total = 0
        for p in self.produtos:
            total = total + p.quantidade * p.preco
        return total

    def para_dicionario(self):
        return {
            "quantidade": self.quantidade,
            "total_produtos": len(self.produtos),
            "produtos": self.listar()
        }
