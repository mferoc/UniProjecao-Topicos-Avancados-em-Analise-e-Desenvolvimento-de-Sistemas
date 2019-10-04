n1 = input("Digite a primeira nota: ")
n2 = input("Digite a segunda nota: ")
media = (float(n1) + float(n2)) / 2

if media == 10.0:
    print("Aprovado com distinção")
elif media >= 7.0:
    print("Aprovado")
else:
    print("Reprovado")