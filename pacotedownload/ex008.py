#Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.

# Solicita ao usuário para inserir um valor em metros
metros = float(input('Digite um valor em metros: '))

# Converte metros para centímetros e milímetros
cm = metros * 100
mm = metros * 1000
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10

# Exibe os resultados
print(f'A medida de {metros:.2f}m corresponde a:')
print(f'{cm:.2f} centímetros (cm)')
print(f'{mm:.2f} milímetros (mm)')
print(f'{km:.6f} quilômetros (km)')
print(f'{hm:.2f} hectômetros (hm)')
print(f'{dam:.2f} decâmetros (dam)')
print(f'{dm:.2f} decímetros (dm)')