#Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

print(f'Tirando {n1:.1f} e {n2:.1f} a sua média é {media:.1f}')
if 7 > media >= 5:
    print('Você está em RECUPERAÇÃO')
elif media < 5:
    print('Você está REPROVADO!')
elif media >= 7:
    print('PARABÉNS, VOCÊ FOI APROVADO!')