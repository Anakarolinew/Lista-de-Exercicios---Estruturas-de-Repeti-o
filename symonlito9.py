soma = 0
quantidade = 0

while True:
    numero = float(input("Digite um número (-1 para encerrar): "))

    if numero == -1:
        break

    soma += numero
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
else:
    media = 0

print("Quantidade de números:", quantidade)
print("Soma:", soma)
print("Média:", media)