#Nessa aula, vamos aprender como utilizar os códigos de escape
# sequence ANSI para configurar cores para os seus programas em  Python.
# Veja como utilizar o código \033[m com todas as suas principais possibilidades
'''estilos:
0 = none
1 = bold
4 = underline
7 = negative

cores Texto:     cores fundo(back)
30              40          BRANCO
31              41          VERMELHO
32              42          VERDE
33              43          AMARELO
34              44          AZUL
35              45          ROXO
36              46          TURQUESA
37              47          CINZA'''

'''a = 3
b = 5

print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m!!!')'''

nome = 'Victor'
print('Olá, Muito prazer em te conhecer, {}{}{}!!!'.format('\033[7;97m', nome,'\033[m'))
