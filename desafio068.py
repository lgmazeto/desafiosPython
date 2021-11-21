from random import randint
vitorias = 0
while True:
    opcao = int(input('Digite sua opção: \n[0 - PAR]  \n[1 - IMPAR]'))
    num = int(input('Digite o numero escolhido de 0 a 10:'))
    numAI = randint(0, 10)
    soma = num + numAI
    opcaoSoma = soma % 2 == 0

    if opcao == 0:
        if opcaoSoma:
            print(f'Você VENCEU!\n {numAI} sorteado pela AI\nTente novamente!')
            vitorias += 1
        else:
            print(f'Você PERDEU!\n {numAI} sorteado pela AI\nO jogo será encerrado!')
            print(f'Seu numero de vitórias foi {vitorias}')
            break
    else:
        if opcaoSoma:
            print(f'Você PERDEU!\n {numAI} sorteado pela AI\nO jogo será encerrado!')
            print(f'Seu numero de vitórias foi {vitorias}')
            break
        else:
            print(f'Você VENCEU!\n {numAI} sorteado pela AI\nTente novamente!')
            vitorias += 1
