print("Responda as perguntas com S para 'SIM' e N para 'NAO'\n")
p1 = input("Telefonou para a vítima? ")
p2 = input("Esteve no local do crime? ")
p3 = input("Mora perto da vítima? ")
p4 = input("Devia para a vítima? ")
p5 = input("Já trabalhou para a vítima? ")
respostasPositivas = 0
if (p1 != "S" or p1 != "N") and (p2 != "S" or p2 != "N") and (p3 != "S" or p3 != "N") and (p4 != "S" or p4 != "N") and (p5 != "S" or p5 != "N"):
    print("Resposta inválida")
    exit()

#for i in range (5):
if p1 == "S":
    respostasPositivas = respostasPositivas + 1
if p2 == "S":
    respostasPositivas = respostasPositivas + 1
if p3 == "S":
    respostasPositivas = respostasPositivas + 1
if p4 == "S":
    respostasPositivas = respostasPositivas + 1
if p5 == "S":
    respostasPositivas = respostasPositivas + 1

#print(str(respostasPositivas))

if respostasPositivas == 2:
    print("Suspeito(a)")
elif respostasPositivas >= 3 and respostasPositivas <= 4:
    print("Cúmplice")
elif respostasPositivas == 5:
    print("Assassino(a)")
else:
    print("Inocente")