n1 = input("Digite a primeira nota: ")
n2 = input("Digite a segunda nota: ")
media = (float(n1) + float(n2)) / 2

if 9 <= media <= 10:
    print("Aprovado!!! Conceito A")
elif 7.5 <= media < 9:
    print("Aprovado!!! Conceito B")
elif 6 <= media < 7.5:
    print("Aprovado!!! Conceito C")
elif 4 <= media < 6:
    print("Reprovado!!! Conceito D")
else:
    print("Reprovado!!! Conceito E")