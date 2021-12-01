alunos = list()
aluno = list()
notas = list()
count = 0
verNotas = 0
while True:
    nome = str(input('Digite o NOME do aluno: ')).strip().upper()
    n1 = float(input('Digite a NOTA 1 do aluno: '))
    n2 = float(input('Digite a NOTA 2 do aluno: '))
    aluno.append(nome)
    notas.append(n1)
    notas.append(n2)
    aluno.append(notas[:])
    aluno.append(((n1+n2)/2))
    alunos.append(aluno[:])
    nome = ''
    aluno.clear()
    notas.clear()
    count += 1
    cont = str(input('Continuar? [S/N]')).strip()
    if cont in 'Nn':
        break

for c in range(0, count):
    print(f'pos:{c} nome:{alunos[c][0]} media:{alunos[c][2]}')

while True:
    verNotas = int(input('Deseja ver notas de algum aluno? (999 PARA SAIR!)'))
    if verNotas == 999:
        break
    for c in range(verNotas, verNotas+1):
        print(f'As notas de {alunos[c][0]} são: {alunos[c][1]}')
