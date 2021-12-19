def cadastrar():
        nome = str(input('Nome: ')).strip()
        idade = str(input('Idade: ')).strip()
        arquivo = open('desafio_115\cadastro.txt', 'a')
        arquivo.writelines(nome+', '+idade+'\n')
        arquivo.close()
