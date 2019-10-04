usuario = input("Informe o nome de usuario: ")
senha = input("Informe a senha: ")

while usuario == senha:
    print("Usuario deve ser diferente da senha!\n")
    senha = input("Informe uma nova senha: ")
else:
    print("Dados confirmados")