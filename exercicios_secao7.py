"""
Seção 7 - Exercícios
"""

"""1"""
# A = [1, 0, 5, -2, -5, 7]
# print(A)
#
#
# soma = A[0] + A[1] + A[5]
# print(soma)
#
#
# A[4] = 100
# print(A)
#
#
# for i in A:
#     print(i)

"""2"""
# valores = 5, 13, 7, 9, 12, 57
#
# print(valores)
# print(type(valores))

"""3"""
# reais = [5, 8, 6, 75, 954, 2.87, 65.02, 957, 48, 95.75]
# print(reais)
#
# quadrados = []
#
# for i in reais:
#     indice = i**2
#     quadrados.append(indice)
#
# print(quadrados)

"""4"""
# v = ['debra', 23, False, False, True, 'não quero', 542.86, 0]
# print(v)
#
# X = v[5]
# Y = v[0]
#
# print(X)
# print(Y)
#
# soma = X + Y
# print(soma)

"""5"""
# v = [5, 6, 245, 5498, 5156.88, 2.8, 60, 8, 51, 658.2]
# print(v)
#
# pares = 0
#
# for i in v:
#     if i % 2 == 0:
#         pares += 1
#
# print(pares)

"""6"""
# vetor = []
#
# print('Digite 10 valores de posições de um vetor:')
# for i in range(10):
#     x = float(input(f'{i}: '))
#     vetor.append(x)
#
# print(vetor)
#
# print(max(vetor))
# print(min(vetor))

"""7"""
# numeros = 1, 4, 25, 36.874, 2.6, 2, 8, 65, 754, 454865145
#
# vetor = list(numeros)
# print(vetor)
#
# maximo = max(vetor)
#
# print(maximo)
# print(vetor.index(maximo))

"""10"""
# notas = [10, 5, 10, 10, 2, 10, 5, 10, 8, 9, 9, 8, 10, 2, 10]
#
# soma = sum(notas)
#
# media = soma / len(notas)
# print(media)

"""13"""
# valores = [25, 60, 24, 26.5, 24]
#
# print(valores)
#
# maior = max(valores)
# menor = min(valores)
#
# print(f'O maior valor é {maior}, no índice {valores.index(maior)}')
# print(f'O menor valor é {menor}, no índice {valores.index(menor)}')

"""14"""
# v = [25, 656, 54, 54.6, 25, 6589, 54, 2, 3, 97]
# print(v)
#
# iguais = set()  # conjunto para não repetir os números quando imprimir
#
# for valor in v:
#     ocorrencia = v.count(valor)
#     if ocorrencia > 1:
#         iguais.add(valor)
#
# print(iguais)


