metros = float(input("Digite a quantidade de metros quadrados a serem pintados: "))
litros = metros/3

precoL = 80.0
capacidadeL = 18

latas = litros / capacidadeL
total = latas * precoL

print('Você usara ' + str(latas) + 'latas de tinta')
print('O preco total é de: R$' + str(total))
