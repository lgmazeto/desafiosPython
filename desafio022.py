nome = input('Digite o nome completo:\n')
primeiroNome = nome[:nome.find(' ')]
print('maiusculas: {}'.format(nome.upper()))
print('minusculas: {}'.format(nome.lower()))
print('numero de letras sem espaço: {}'.format(len(nome.replace(' ',''))))
print('primeiro nome é: {}'.format(primeiroNome))
print('primeiro nome tem: {} letras'. format(len(primeiroNome)))
