# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

#Solicita a velocidade do carro ao usuário
import time
v = float(input('A velocidade do carro foi de: '))

print('PROCESSANDO...')
time.sleep(2)

if v > 80:
    multa = (v - 80) * 7.00
    print('=' * 40)
    print(f'Você foi multado! A multa é de R${multa:.2f}')
    print('=' * 40)
else:
    print("=" * 50)
    print('Velocidade dentro do limite. Dirija com segurança!')
    print('=' * 50)