# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.

distancia = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia:.0f}Km.')

preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print(f'E o preço da sua passagem será de R${preço:.2f}')