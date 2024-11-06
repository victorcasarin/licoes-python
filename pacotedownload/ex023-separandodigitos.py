'''#Faça um programa que leia um número de 0 a 9999
e te mostre na tela cada um dos dígitos separados
ex:
Digite um número: 1834
unidade: 4 dezena: 3 centena: 8 milhar: 1'''

'''num = int(input('Informe um número: '))
n = str(num)
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))'''


#Em operações matemáticas

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}...')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')




#Forma alternativa
'''num = int(input('Digite um numero: '))
n = num + 10000
nn = str(n)
print(f'A unidade é: {nn[-1]}')
print(f'A dezena é: {nn[-2]}')
print(f'A centena é: {nn[-3]}')
print(f'O milhar é: {nn[1]}')'''











