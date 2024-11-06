#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

#Variáveis
larg = float(input("Insira a largura da parede: "))
alt = float(input("Insira a altura da parede: "))

# Cálculo das variáveis
ar = larg * alt

# Resultado
print(f'A dimensão da parede é de {larg}x{alt} e sua área é de {ar:.0f}m²')
tinta = ar / 2
print(f'Para pintar essa parede, vc precisará de {tinta}l de tinta.')