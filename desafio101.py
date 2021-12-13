from datetime import date

def voto(nascimento):
    """
    -> Função que avalia obrigatóriedade do voto.
    :param nascimento: data de nascimento a ser avaliada.
    :return: sem retorno.
    """
    idade = date.today().year - nascimento
    print(f'Com {idade} anos:', end=' ')
    if idade >= 18 and idade < 65:
        return 'VOTO OBRIGATÓRIO!'
    elif idade >= 65 or idade >= 16 and idade < 18 :
        return 'VOTO FACULTATIVO!'
    else:
        return 'NÃO PODE VOTAR!'


nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))
