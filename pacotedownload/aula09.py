frase = 'Curso em Vídeo Python'


'''print("""Nessa aula, vamos aprender operações com String no  Python. 
As principais operações que vamos aprender são o Fatiamento de String,
Análise com len(), count(), find(), transformações com replace(), 
upper(), lower(), capitalize(), title(), strip(), junção com join().""")'''

#frase = '   Aprenda Python  '

#Fatiamento
'''print(frase[9]) #Só pega a letre 9 que é V
print(frase[9:13]) # pega da letra 9 até a 12, retorna Víde
print(frase[9:21:2]) #pulando de 2 em 2
print(frase[:5])#sem nada antes dos dois pontos, começa do zero
print(frase[15:])#sem nada depois dos dois pontos, vai até o fim
print(frase[9::3]) #do 9 em diante, pulando de 3 em 3'''

#Análise
'''print('==================')
print(len(frase)) # Conta qnts caracteres
print(frase.count('o')) #Conta quantos 'o' tem na string
print(frase.count('o', 0, 13)) #Conta qnts 'o' tem de zero até doze
print(frase.find('deo')) #Mostra em que posição esse trecho se inicia
print(frase.find('Android')) #Quando colocado dentro do find uma string que não existe, ela rtrn -1
print('Curso' in frase) # Retorna TRUE se encontrar a string na frase'''

#Transformação
'''print(frase.replace('Python', 'Android')) #Substitui Python por Android
print(frase.upper()) #Escreve tudo em maiúsculas
print(frase.lower()) #Escreve tudo em minúsculas
print(frase.capitalize()) #Escreve só a primeira em maiúscula
print(frase.title()) #Escreve em maiúscula a primeira letra de cada palavra
print(frase.strip()) #Remove espaços "inuteis" no início e no final da String
print(frase.rstrip())#Remove somente os útlimos espaços
print(frase.lstrip())#Remove somente os primeiros espaços'''

#Divisão

'''print(frase.split())'''

#Junção

print('-'.join(frase.upper().lower()))





#print(frase.find('Android'))
#print('Curso' in frase)





