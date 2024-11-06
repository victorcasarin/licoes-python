#Escreva um programa que faça o computador “pensar”
# em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import time
#importar o modulo random
from random import randint

# cores
cor_verde = '\033[92m'
cor_vermelho = '\033[91m'
cor_reset = '\033[0m'

# Fazer o pgr escolher um numero de 0 a 5 e guardar na variável
computador = randint(0, 5)

# O usuario tenta adivinhar o número
print('-=-' * 20)
print(f'{cor_verde}Vou pensar em um número entre 0 e 5. Tente adivinhar o número... {cor_reset}')
print('-=-' * 20)
usuario = int(input('Qual foi o número que eu pensei? '))

print(f'PROCESSANDO...{cor_verde}')
#time.sleep(0,5)

while usuario != computador:
    print('Voce errou, tente novamente')
    usuario = int(input('Qual foi o número que eu pensei? '))
else:
    print('Parabens')


# Verifica se o usuário acertou ou errou
'''if usuario == computador:
    print(f'{cor_verde}Parabéns! Você acertou!!!')
else:
    print(f'{cor_vermelho}Que pena, vc errou! O número escolhido foi {computador}.')'''