c = str()
while c != 'M' and c != 'F':
    c = str(input('Digite o sexo da pessoa')).upper().strip()
print('Masculino' if c == 'M' else 'Feminino')