#Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”,
# que é uma estrutura versátil e simples de entender. Por exemplo:
#for c in range(0, 4):
#print(c)
#print(‘Acabou’)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)

