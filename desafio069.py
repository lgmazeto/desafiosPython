homens = 0
homens_maiores_dezoito = 0
mulheres_menores_vinte = 0
while True:
    idade = int(input('Digite a idade:'))
    sexo = str(input('Sexo: [F/M]:')).strip().upper()

    if sexo == 'M':
        homens += 1
        if idade > 18:
            homens_maiores_dezoito += 1
    elif sexo == 'F':
           if idade <= 20:
               mulheres_menores_vinte += 1
    else:
        sexo = str(input('Sexo: [F/M]:')).strip().upper()

    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()

    if continuar == 'N':
        break

print(f'O total de homens cadastrados foi {homens}.\n'
      f'O total de homens com mais de 18 anos foi {homens_maiores_dezoito}.\n'
      f'O total de mulheres com menos de 20 anos foi {mulheres_menores_vinte}.')