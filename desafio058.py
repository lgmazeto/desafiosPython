import random
computer = random.randint(0, 10)
numero  = 99
count = 0
while computer != numero:
    numero = int(input('Digite um número ente 0 e 10:'))
    print('Você VENCEU!' if numero == computer else 'Tente novamente')
    count += 1
print('Foram {} tentativas'.format(count))
