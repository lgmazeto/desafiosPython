import datetime
anoAtual = datetime.date.today().year
nascimento = int(input('Digite o ano de nascimento'))
idade = anoAtual - nascimento
if idade > 18:
    print('Já se alistou')
elif idade == 18:
    print('Vá se alistar')
else:
    print('Ainda não precisa se alistar')