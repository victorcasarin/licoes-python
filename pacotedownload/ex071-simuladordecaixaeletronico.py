#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 30)
print('{:^30}'.format('BANCO VIC'))
print('=' * 30)

valor = int(input("Que valor você quer sacar? R$"))
total = valor
cédula = 50
totced = 0
while True:
    if total >= cédula:
        total -= cédula
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        totced = 0
        if total == 0:
            break
