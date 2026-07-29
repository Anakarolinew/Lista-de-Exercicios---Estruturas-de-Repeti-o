quantidade = int(input("Quantidade de alunos: "))

soma = 0

for i in range(quantidade):
    nota = float(input(f"Nota do aluno {i + 1}: "))

    if i == 0:
        maior = nota
        menor = nota
    else:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota

    soma += nota

media = soma / quantidade

print("Maior nota:", maior)
print("Menor nota:", menor)
print("Média da turma:", media)