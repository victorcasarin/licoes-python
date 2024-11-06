#Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
'''soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} números PARES e a soma foi {soma}')'''

soma = 0
for i in range(2):
    n = int(input(f'Digite o {i+1}° número: '))
    if n % 2 == 0:
        soma += n
print(f'A soma dos números pares é: {soma}')