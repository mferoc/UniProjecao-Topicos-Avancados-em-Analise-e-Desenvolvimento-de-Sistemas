numeros = []
for i in range(5):
    numeros.append(int(input("Informe  um número: ")))
soma = sum(numeros)
qtd_numeros = len(numeros)
media = soma / qtd_numeros
print("A soma dos números digitados é: %.1f" % soma)
print("A media dos números digitados é: %.1f" % media)
