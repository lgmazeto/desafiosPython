first = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
c = 8
termo = 1
print(first)
while c >= 0:
    print(first + termo*razao)
    termo += 1
    if c == 0:
        c = int(input('Deseja ver mais quantos termos?'))
    c -= 1
