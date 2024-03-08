# Mostrar o codigo dos serviços
print("Impressão PB: 1")
print("Copia PB: 2")
print("Impressão Colorida: 3")
print("Copia colorida: 4")
print("Impressão impressão foto 10x15: 5")
print("Impressão impressão polaroid: 6")
print("Serviços digitais: 7")
print("******************************************************")
      
# Função para atribuiur o codigo do serviço e a quantidade, calculando o preço conforme inserção
def codigoPreco():
    total = 0
    while True:  
        # Tratamento para caso o valor digitado nâo seja um numero
        try:
            x = int(input("\nCódigo do serviço (0 para sair): "))
        except ValueError:
            print("Valor inserido invalido")
            continue
            
            preco = 0
        
        match x:
            case 1:
                preco = 1.00
            case 2:
                preco = 0.50
            case 3:
                preco = 1.50
            case 4:
                preco = 1.00
            case 5:
                preco = 3.50
            case 6:
                preco = 2.00
            case 7:
                preco = 5.00
            case 0:
                break
            case _:
                print("Código invalido.")
                continue
                
        if preco != 0:
            qtd = int(input("\nQual a quantidade? "))
            total += preco * qtd 
            
    return total
    
valorPagar = codigoPreco() 

# Selecionando formas de pagamentos
def pagamento():
    while True:
        # Tratamento para caso o valor digitado nâo seja um numero
        try:
            pagamento = int(input("\nEscolha uma forma de pagamento: \n\n1 - Pix\n2 - Dinheiro\n3 - Cartão de crédito ou debito\n\n"))
        except ValueError:
            print("Valor inserido invalido")
            continue
        match pagamento:
            case 2:
                valorDinheiro = float(input("\nValor pago em dinheiro: R$"))
                troco = valorDinheiro - valorPagar 
                print(f"\nValor total R${valorPagar :5.2f}")
                print(f"Troco: R${troco:5.2f}")
                break
            case 1:
                print("Pagamento em pix")
                print(f"Valor total R${valorPagar :5.2f}")
                break
            case 3:
                print("Pagamento em cartão de crédito ou debito")
                print(f"Valor total R${valorPagar :5.2f}")
                break
            case _:
                print("Forma de pagamento invalida, insira um codigo válido.")
                continue

pagamento()
