senha = input("Cadastre uma senha: ")

while len(senha) < 8:
    print("A senha deve possuir pelo menos 8 caracteres.")
    senha = input("Digite outra senha: ")

print("Cadastro realizado com sucesso!")