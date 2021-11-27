expressao = str(input('Digite uma expressão: ')).strip()
expList = expressao.strip()
if expList.count('(') == expList.count(')'):
    print('A expressão é VALIDA')
else:
    print('Expressão é INvalida!')
