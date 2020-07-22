soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º valor:'))
    cont += 1
    if num%2 == 0:
        soma += num
print(f'Você digitou {cont} valores e a soma dos números pares é {soma}.')
