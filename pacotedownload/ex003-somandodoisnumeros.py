#Crie um programa que leia dois números e mostre a soma entre eles.

#definindo as varáiveis
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))

#somando
s = n1 + n2

#Resultado
print(f'A soma entre \033[31m{n1}\033[m e \033[31m{n2}\033[m é igual a \033[34m{s:.1f}') #imprime o valor de s formatado com duas casas decimais.

