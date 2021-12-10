from datetime import date

cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
anoNascimento = int(input('Ano de nascimento: '))
cadastro['idade'] = date.today().year - anoNascimento
cpts = int(input('Digite o número da carteira CTPS, (0 = não tem!)'))
if cpts == 0:
    cadastro['ctps'] = cpts
    for k, v in cadastro.items():
        print(f'O {k} tem valor: {v}')
else:
    cadastro['ctps'] = cpts
    cadastro['ano_contratacao'] = int(input('Digite o ano de contração: '))
    cadastro['salario'] = int(input('Digite o seu salário: '))
    cadastro['aposentar'] = date.today().year - cadastro['ano_contratacao']


print(cadastro)