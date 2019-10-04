base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
x = 0
potencia = 1
while x < expoente:
    potencia = potencia * base
    x = x + 1
print("%d" % potencia)
