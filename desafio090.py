aluno = dict()
aluno['nome'] = str(input('Digite o nome:'))
aluno['media'] = float(input('Digite a média:'))
if aluno['media'] < 7:
    aluno['situacao'] = 'Reprovado'
else:
    aluno['situacao'] = 'Aprovado'
for k, v in aluno.items():
    print(f'{k}: {v}')
