from pyasn1.compat.octets import null

nota = float(input("Digite uma nota de 0 a 10: "))

while nota > 10 or nota < 0:
    nota = float(input("Digite uma nota de 0 a 10: "))
else:
    print("A nota é %.2f" % nota)
