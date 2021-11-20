import datetime
currentYear = datetime.datetime.now().year

for c in range(0,3):
    birth = int(input('Ano de nascimento:'))
    if currentYear - birth >= 18:
        print('Essa pessoa é maior de idade.')
    else:
        print('Essa pessoa é menor de idade.')