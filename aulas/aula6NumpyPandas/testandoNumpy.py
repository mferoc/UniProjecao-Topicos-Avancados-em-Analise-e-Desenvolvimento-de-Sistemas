import numpy as np

dados = [3, 5, 7, 9]
array = np.array(dados)
print("dados")
print(dados)
print("array")
print(array)
arranjo = np.arange(10)
print("arranjo")
print(arranjo)
uns = np.ones((2, 2))
print("uns")
print(uns)
zeros = np.zeros(10)
print("zeros")
print(zeros)
zeros2 = np.zeros((2, 3))
print("zeros2")
print(zeros2)
vazios = np.empty((2, 3))
print("vazios")
print(vazios)

a1 = np.array([[1, 2, 3], [4, 5, 6]])
print("array1")
print(a1)
a2 = np.ones((2, 3))
print("a2")
print(a2)
print("a1+a2")
print(a1 + a2)
print("a1 * 2")
print(a1 * 2)
print("a1 ^ 2")
print(a1 ** 2)
print("a1 - a1")
print(a1 - a1)

# outras operacoes com array

minhaLista = [3, 4, 5, 7]
meuArray = np.array(minhaLista)
print(meuArray)
pedacoArray = meuArray[1:3]
print("parte do array")
print(pedacoArray)
print("modificando parte do array")
pedacoArray[1] = 23
print(pedacoArray)
print("voltando ao array original")
print(minhaLista)

# arrays de 3 dimensoes

array3d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]])

print(array3d)
print("primeiro array")
print(array3d[0])
print("copiando os dados do primeiro array")
old_values = array3d[0].copy()
print(old_values)
print("mudando o valor do primeiro array")
array3d[0] = 25
print(array3d[0])
print("voltando o valor do primeiro array")
array3d[0] = old_values
print(array3d[0])
