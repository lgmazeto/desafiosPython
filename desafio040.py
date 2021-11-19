import statistics

n1 = float(input('nota 1'))
n2 = float(input('nota 2'))
media = statistics.mean([n1,n2])
if media >= 7:
    print('Aprovado')
elif media >= 5 or media < 7:
    print('Recuperação')
else:
    print('Reprovado')