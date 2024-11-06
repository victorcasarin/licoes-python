from random import shuffle

#Variáveis
n1 = str(input('Primeiro nome:' ))
n2 = str(input('Segundo aluno:' ))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

#Lista
lista = [n1, n2, n3, n4]

#execução do módulo
shuffle(lista)

print('A ordem de apresentação será ')
# print da variável
print(lista)




