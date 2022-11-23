"""
Seção 6 - Exercícios
"""

"""1"""
# for i in (range(0, 13, 3)):
#     print(i)

"""2"""
# for i in range(1, 101):
#    print(i)


# i = 1
# while i <= 100:
#     print(i)
#     i += 1

"""3"""
# i = 10
# while i >= 0:
#     print(i)
#     i -= 1
# print('FIM!')

"""4"""
# inteiro = 0
# print(f'inteiro = {inteiro}')

# for i in range(0, 100000, 1000):
#     inteiro += 1000
#     print(f'inteiro = {inteiro}')

"""6"""
from random import randrange

soma = 0
for n in randrange(10):
    inteiro = n + 1
    soma = soma + inteiro
    media = soma / n
    print(media)
