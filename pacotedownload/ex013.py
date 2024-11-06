salario = float(input('Salário atual:R$'))
aumento = float(input('O aumento em porcentagem é de:'))
sn = salario * aumento / 100
au = salario + sn

print('O aumento é de R${:.2f}, então o salário do funcionário vai para R${:.2f}'.format(sn, au))
