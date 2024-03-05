#!/usr/bin/env python
# coding: utf-8

# Mostrar o codigo dos serviços

print("Impressão PB: 1")
print("Copia PB: 2")
print("Impressão Colorida: 3")
print("Copia colorida: 4")
print("Impressão impressão foto 10x15: 5")
print("Impressão impressão polaroid: 6")
print("Serviços digitais: 7")

# Looping para atribuiur o codigo e a quantidade, calculando o preço conforme inserção

total = 0
while True:
    codigo = int(input("\nCodigo do serviço (0 para sair): "))
    preco = 0
    
    if codigo == 0:
        break
    elif codigo == 1:
        preco = 1.00
    elif codigo == 2:
        preco = 0.50
    elif codigo == 3:
        preco = 1.50
    elif codigo == 4:
        preco = 1.00
    elif codigo == 5:
        preco = 3.50
    elif codigo == 6:
        preco = 2.00
    elif codigo == 7:
        preco = 5.00
    else:
        print("\nCodigo inserido inválido")
        continue
        
    if preco != 0:
        qtd = int(input("\nQual a quantidade? "))
        
    total += preco * qtd 
    
# Selecionando formas de pagamentos

pagamento = int(input("\nEscolha uma forma de pagamento: \n\n1 - Pix\n2 - Dinheiro\n3 - Cartão de crédito ou debito\n\n"))

if pagamento == 2:
    valorDinheiro = float(input("\nValor pago em dinheiro: "))
    troco = valorDinheiro - total
    print(f"\nValor total R${total:5.2f}")
    print(f"Troco: R${troco:.2f}")
elif pagamento == 1:
    print("Pagamento em pix")
    print(f"Valor total R${total:5.2f}")
elif pagamento == 3:
    print("Pagamento em cartão de crédito ou debito")
    print(f"Valor total R${total:5.2f}")
else:
    print("Forma de pagamento invalido")

