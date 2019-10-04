n = int(input("Digite o numero que terá o fatorial calculado: "))
fatorial = 1

while n > 1:
    fatorial = fatorial * n
    n = n - 1
print("%d" % fatorial)
