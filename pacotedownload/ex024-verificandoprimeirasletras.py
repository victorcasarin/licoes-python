#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO
'''cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')'''


# Resolução alternativa I
'''c = input('Digite o nome da cidade: ').strip().split()
print(c[0].upper() == 'SANTO')'''


#Resolução alternativa II
nome=input('Qual é o nome da sua cidade? ')
nome.strip()
print('Essa cidade começa com "Santo"? ')
print(nome[0:6].lower()=='santo ')