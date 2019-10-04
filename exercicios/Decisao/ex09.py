pMorangoKg = 2.50
pMacasKg = 1.80
kgMorangos = float(input("Quantos kg(s) de Morango quer comprar? "))
kgMacas = float(input("Quantos kg(s) de Maçã quer comprar? "))
if kgMorangos > 5:
    pMorangoKg = 2.20
if kgMacas > 5:
    pMacasKg = 1.50
valorTotal = (pMorangoKg * kgMorangos) + (pMacasKg * kgMacas)
if (kgMorangos + kgMacas) > 8 or valorTotal > 25.00:
    desconto = (valorTotal * 10) / 100
    ValorTotal = valorTotal - desconto
    print("O total da sua compra foi: %.2f R$" % valorTotal)
else:
    print("O total da sua compra foi: %.2f R$" % valorTotal)