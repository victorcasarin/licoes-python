
#Estruturas condicionais
'''tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro Novo!')
else:
    print('Carro Velho!')
    print('--FIM--')'''

#Condição simplificada
'''tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo <= 3 else 'Carro velho')
print('--FIM--')'''

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m:.3}!')
if m >= 6:
    print('Parabéns!!!')
else:
    print('Voce levou bomba!')