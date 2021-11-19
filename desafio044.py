valor = float(input('Valor do produto: '))
print('Condições de pagamento\n'
      '1 - A vista dinheiro 10% de desconto.\n'
      '2 - A vista cartão 5% de desconto.\n'
      '3 - 2x cartão sem juros.\n'
      '4 - 3x cartão 20% de juros.')
opcao = int(input('Forma de pagamento?'))
if opcao == 1:
      print('valor a pagar {}'.format(valor*0.9))
elif opcao == 2:
      print('valor a pagar {}'.format(valor*0.95))
elif opcao == 3:
      print('valor a pagar {}, em 2x de {}'.format(valor, valor/2))
elif opcao == 4:
      print('valor a pagar {}, em 3x no cartao {}'.format(valor*1.2,valor*1.2/3))
else:
      print('forma de pagamento invalida.')