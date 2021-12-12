from time import sleep



def contador(inicio, final, passo):
    if passo == 0:
        passo = 1
    if inicio > final:
        while inicio >= final:
            print(inicio, end=' ')
            inicio -= abs(passo)
            sleep(0.6)
        print('Fim!')
    else:
        while inicio <= final:
            print(inicio, end=' ')
            inicio += abs(passo)
            sleep(0.6)
        print('Fim!')



contador(1, 10, 1)
contador(10, 0, 2)
contador(10, 100, 8)
contador(20, 10, -1)
contador(5, -5, 0)