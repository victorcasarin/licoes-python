n = s = 0
while True:
    n = int(input('Digite um número: '))

    #condição de parada:
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')