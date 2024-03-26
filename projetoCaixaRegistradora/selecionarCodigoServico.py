class codigoPreco:
    def __init__(self):
        self.total = 0
        self.precoServico = {
            1: 1.00,
            2: 0.50,
            3: 1.50,
            4: 1.00,
            5: 3.50,
            6: 2.00,
            7: 5.00
        }

    def calcularPreco(self):
        while True:
            try:
                codigoServico = int(input("\nCódigo do serviço (0 para sair): "))
            except ValueError:
                print("Valor inserido inválido!")
                continue

            if codigoServico == 0:
                break
            elif codigoServico not in self.precoServico:
                print("Código inválido!")
                continue

            preco = self.precoServico[codigoServico]
            qtd = int(input("\nQual a quantidade? "))
            self.total += preco * qtd

        return self.total
    
calculadora = codigoPreco()
