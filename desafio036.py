valor = float(input('Qual é o valor do imóvel?'))
salario = float(input('Qual é o seu salário?'))
tempo = int(input('Em quantos anos será parcelado?'))

prestacao = valor / (tempo*12)

if prestacao > salario * 0.3:
    print('Emprestimo NEGADO!')
else:
    print('Emprestimo APROVADO!')