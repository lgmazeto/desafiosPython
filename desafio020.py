import random
print('Digite o nome dos alunos:\n')
aluno1 = input('aluno1\n')
aluno2 = input('aluno2\n')
aluno3 = input('aluno3\n')
aluno4 = input('aluno4\n')
sorteado = [aluno4,aluno3,aluno2,aluno1]
random.shuffle(sorteado)
print('sorteado = {}'.format(sorteado))