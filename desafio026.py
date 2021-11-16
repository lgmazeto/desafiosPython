ondeA = input('Digite uma frase:').upper()
numA = ondeA.count('A')
primeiroA = ondeA.find('A') + 1
ultimoA = ondeA.rfind('A') + 1
print('Numero de letras A: {}\n'
      'Primeira posição de A: {}\n'
      'Ultima posição de A: {}\n'
      .format(numA, primeiroA, ultimoA))