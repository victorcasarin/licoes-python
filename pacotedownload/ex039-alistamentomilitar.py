#Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date
atual = date.today().year
print('*' * 30)
print('\033[32mSERVIÇO MILITAR OBRIGATÓRIO\033[m')
print('*' * 30)

nome = input('Nome do candidato: ')
sexo = input('Informe seu sexo (M para masculino e F para feminino):').strip().upper()

if sexo == 'M':
    print('\033[31mVocê se fudeu! Vai se alistar!\033[m')
elif sexo == 'F':
    print('O serviço militar não é obrigatório para pessoas do sexo feminino.')


nasc = int(input('Informe seu ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos pra você se alistar.')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}.')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}.')
