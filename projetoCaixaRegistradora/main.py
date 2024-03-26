from selecionarCodigoServico import calculadora
from selecionarFormaPagamento import pagamento

#Apresentar os codigo e serviços
print("Impressão PB: 1")
print("Copia PB: 2")
print("Impressão Colorida: 3")
print("Copia colorida: 4")
print("Impressão impressão foto 10x15: 5")
print("Impressão impressão polaroid: 6")
print("Serviços digitais: 7")
print("******************************************************")


total_calculado = calculadora.calcularPreco()

pagamento.realizar_pagamento(total_calculado)