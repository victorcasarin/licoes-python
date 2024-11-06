#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO!')




'''n = int(input('Digite um número inteiro: '))
if  % 2 == 0:
    print(f'O número {n} é par.')
else:
    print(f'O número {n} é ímpar.')

n = int(input('Digite um número para ver sua tabuada: '))
print(f'Tabuada do número {n}:')
for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')

soma = 0
while True:
    numero = int(input('Digite um número (ou 0 para sair): '))
    if numero == 0:
        break
    soma += numero
print(f'A soma dos números digitados é: {soma}')'''