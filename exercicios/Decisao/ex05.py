p1 = float(input("Digite o preço do produto A: "))
p2 = float(input("Digite o preço do produto B: "))
p3 = float(input("Digite o preço do produto C: "))
maisBarato = p1

if p2 < maisBarato:
    maisBarato = p2
if p3 < maisBarato:
    maisBarato = p3
print("O produto mais barato tem o preço: %.2f" %maisBarato)