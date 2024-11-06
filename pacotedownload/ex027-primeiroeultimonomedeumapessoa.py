#Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.


# Solicita nome ao usuário
'''nome = (str(input(('Digite seu nome: '))))
nome = nome.strip()
print(f'Olá {nome}, seja muito bem vindo!')

#Encontrando a posição do primeiro e último espaços, para a partir daí encontrar
#o primeiro e último nome
espaco_inicial = nome.find(' ')
espaco_final = nome.rfind(' ')


#O primeiro nome é a parte antes do primeiro espaço
primeiro_nome = nome[:espaco_inicial]

#O último nome é a parte após o último espaço
ultimo_nome = nome[espaco_final + 1:]

#Resultado
print(f'Vejo que seu primeiro nome é {primeiro_nome}')
print(f'E seu último nome é {ultimo_nome}')'''

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')


