numeros = []
print("Insira uma nota: / Para parar de inserir, quando perguntado digite 0: ")
sair = 1
while sair != 0:
    numeros.append(int(input("Informe  um número: ")))
    sair = int(input("Deseja sair: "))
soma = sum(numeros)
qtd_numeros = len(numeros)
media = soma / qtd_numeros
print("A media dos números digitados é: %.1f" % media)