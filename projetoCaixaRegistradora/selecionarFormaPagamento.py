class Pagamento:
    @staticmethod
    def realizar_pagamento(valor_pagar):
        if valor_pagar > 0:
            while True:
                try:
                    forma_pagamento = int(input("\nEscolha uma forma de pagamento: \n\n1 - Pix\n2 - Dinheiro\n3 - Cartão de crédito ou débito\n\n"))
                except ValueError:
                    print("Valor inserido inválido!")
                    continue

                if forma_pagamento == 2:
                    valor_dinheiro = float(input("\nValor pago em dinheiro: R$"))
                    troco = valor_dinheiro - valor_pagar 
                    print(f"\nValor total: R$ {valor_pagar:5.2f}")
                    print(f"Troco: R$ {troco:5.2f}")
                    break
                elif forma_pagamento == 1:
                    print("\nPagamento em Pix.")
                    print(f"\nValor total: R$ {valor_pagar:5.2f}")
                    break
                elif forma_pagamento == 3:
                    print("\nPagamento em cartão de crédito ou débito.")
                    print(f"\nValor total: R$ {valor_pagar:5.2f}")
                    break
                else:
                    print("Forma de pagamento inválida, insira um código válido.")
                    continue
        else:
            print("\nNenhum serviço ou venda foi realizado(a), encerrando programa.")

pagamento = Pagamento()