#Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
# calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.


''''# Solicita o salário a
salario = float(input('Digite o salário do funcionário: R$'))

# Calcula o aumento com base no salário
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

# Exibe o valor do aumento e o novo salário
novo_salario = salario + aumento

percentual_pensao = 0.30

pensao = novo_salario * percentual_pensao
print(f'O aumento será de R${aumento:.2f}. O novo salário será de R${novo_salario:.2f},\ne a pensão será de R${pensao:.2f}')'''

#Forma alternativa

salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print(f'Quem ganhava R${salário:.2f} passa a ganhar R${novo:.2f} agora')