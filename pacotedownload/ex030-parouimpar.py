# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''import time

n = int(input('Digite um número qualquer: '))
print('PROCESSANDO...')
time.sleep(1.5)

if n % 2 == 0:
    print(f'O número {n} é um número par!')
else:
    print(f'O número {n} é um número ímpar!')'''

número = int(input('Me diga um número qualquer: '))
resultado = número % 2

if resultado == 0:
    print(f'O número {número} é PAR!')
else:
    print(f'O número {número} é ÍMPAR!')



