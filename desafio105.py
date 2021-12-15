def notas(*nota, sit=False):
    """
    -> Função calcula a média a partir de várias notas.
    :param nota: Notas do aluno.
    :param sit: (opcional) Mostra a situação a partir da média.
    :return: Dicionario com informações maior e menor nota, média e situação do aluno.
    """
    from statistics import mean
    notasDic = dict()
    notasDic['notas'] = len(nota)
    notasDic['maior'] = max(nota)
    notasDic['menor'] = min(nota)
    notasDic['media'] = mean(nota)
    if sit:
        if notasDic['media'] > 7:
            notasDic['situacao'] = 'BOA!'
        elif notasDic['media'] >= 6:
            notasDic['situacao'] = 'REGULAR!'
        else:
            notasDic['situacao'] = 'RUIM!'
    return notasDic


print(notas(3, 7, 4, sit=True))
print(notas(3, 5, 10, 4))
help(notas)
