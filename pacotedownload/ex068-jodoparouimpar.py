#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print(f'DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente!')
print(f'Game Over! Você venceu {v} vezes.')
