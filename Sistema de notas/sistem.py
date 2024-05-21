#Nome do professor
def professor():
    while True:
        nome_professor = str(input('Digite o do professor(a): ')).strip()
        if len(nome_professor) >=6:
            print('Olá {}, fico contente em vê-lo por aqui!'.format(nome_professor))
            break
        else:
            print('Você precisa atingir o mínimo de 8 letras, tente novamente!')
professor()

#Nome do aluno
def aluno():
    while True:
        nome_aluno = str(input('Digite o nome do aluno: ')).strip()
        if len(nome_aluno) >=6:
            print('\033[1;36mTudo certo!')
            break
        else:
            print('Você precisa atingir o mínimo de 8 letras, tente novamente!')
aluno()

#idade do aluno
def idade():
    while True:
        idade_aluno = int(input('\033[0;0mDigite a idade do aluno: '))
        try:
            idade_aluno = int(idade_aluno)
            if idade_aluno >= 10:
                print('\033[1;1mTUDO PRONTO PARA VOCÊ DIGITAR AS NOTAS!')
                break
            else:
                print('A idade mínima é de 10 anos. Tente novamente!')
        except ValueError:
            print('Por favor, digite um número inteiro para a idade.')
idade()

#Entrada das notas
nota_caderno = float(input('Digite a nota de caderno do aluno: '))
nota_prova = float(input('Agora digite a nota da prova: '))
nota_participacao = float(input('Por utimo, digite a nota de participação: '))

#Resultados
soma_notas = nota_caderno + nota_prova + nota_participacao

media = soma_notas/3

print('A média do aluno será de {:.2f}'.format(media))
if media >= 5:
    print('\033[1;32mAprovado!')
else:
    print('\033[1;31mReprovado!')
