'''n = input('Digite algo: ')
print(n.isnumeric())
print(n.isalnum())
print(n.isprintable())
print(n.isalpha())
print(n.isascii())
print(n.isdigit())
print(n.isdecimal())
print(n.isidentifier())
print(n.islower())
print(n.isspace())
print(n.istitle())'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
div = n1 / n2
print(f'A divisão entre {n1} e {n2} é igual a {div:.2f}')