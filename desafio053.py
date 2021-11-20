text = str(input('Digite uma palavra ou frase:')).strip().upper()
words = text.split()
joinWords = ''.join(words)
rtext = joinWords[::-1]
if joinWords == rtext:
    print('PALÍNDROMO!')
else:
    print('não é palíndromo')

