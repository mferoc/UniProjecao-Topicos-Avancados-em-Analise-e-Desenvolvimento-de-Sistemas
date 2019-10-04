x = int(input("Digite o número x: "))
y = int(input("Digite o número y: "))
z = int(input("Digite o número z: "))
maiorNum = x

if y > maiorNum:
    maiorNum = y
if z > maiorNum:
    maiorNum = z
print("O maior número é: %d" %maiorNum)