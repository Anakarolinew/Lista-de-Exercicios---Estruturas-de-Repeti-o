texto = input("Digite uma palavra ou frase: ")

contador = 0
vogais = "aeiouAEIOU"

for letra in texto:
    if letra in vogais:
        contador += 1

print("Quantidade de vogais:", contador)