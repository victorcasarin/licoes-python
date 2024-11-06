p = float(input('Preço do produto:R$'))
d = float(input('O percentual de desconto é:'))
j = float(input('O juros para compra parcelada é de:'))

pn = p - (p * d / 100)
pp = p + (p * j / 100)

print('O produto que custava R${:.2f}, à vista com desconto vai custar R${:.2f},\nE à prazo vai custar R${:.2f}'.format(p, pn, pp))



