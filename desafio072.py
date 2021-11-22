numeros = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',\
          'quatorze', 'quize', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
numBox = int(input('Digite um número entre zero e 20:'))
while numBox < 0 or numBox > 20:
    print('Tente novamente!')
    numBox = int(input('Digite um número entre zero e 20:'))
print(f'Voce digitou o numero {numeros[numBox]}')
