name = input('Digite o nome completo:')
fistName = name[:name.find(' ')]
lastName = name[name.rfind(' ')+1:]
print('Nome completo: {}\n'
      'Primeiro nome: {}\n'
      'Ultimo nome: {}'
      .format(name, fistName, lastName))