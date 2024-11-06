#Crie um programa que leia o nome completo de uma pessoa x
#o nome com todas as letras maiúsculas x
#o nome com todas as letras minúsculas x
#Quantas letras tem ao todo, sem contar os espaços x
#Quantas letras tem o primeiro nome x


#nome = str(input('Digite seu nome: ')).strip()
#print('Analisando seu nome...')
nome = 'Victor Casarin Antunes'
print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))

#forma alternativa de contar as letras do primeiro nome
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))


#======================================================================================
# Explicação chatgpt

# Solicita o nome completo do usuário
'''nome = input("Digite seu nome completo: ")

# Converte o nome para maiúsculas e minúsculas
nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()

# Remove os espaços e calcula o total de letras
nome_sem_espacos = nome.replace(" ", "")
total_letras = len(nome_sem_espacos)

# Calcula o tamanho do primeiro nome
primeiro_nome = nome.split()[0]
tamanho_primeiro_nome = len(primeiro_nome)

# Exibe os resultados usando .format
print("Nome em maiúsculas: {}".format(nome_maiusculo))
print("Nome em minúsculas: {}".format(nome_minusculo))
print("Total de letras (sem contar espaços): {}".format(total_letras))
print("Tamanho do primeiro nome: {}".format(tamanho_primeiro_nome))'''








