"""
Seção 5 - Exercícios
"""

"""1"""
# numero1 = int(input('número 1 = '))
# numero2 = int(input('número 2 = '))

# if numero1 > numero2:
#     print(f'O número {numero1} é maior')
# else:
#     print(f'O número {numero2} é maior')

"""2"""
# numero = float(input('Digite um número: '))

# if numero >= 0:
#     raiz_quadrada = numero ** 0.5
#     print(f'A raiz quadrada de {numero} é {raiz_quadrada}')
# else:
#     print('Número inválido')

"""3"""
# numero = float(input('Digite um número: '))

# if numero >= 0:
#     raiz_quadrada = numero ** 0.5
#     print(f'A raiz quadrada de {numero} é {raiz_quadrada}')
# else:
#     quadrado = numero ** 2
#     print(f'O quadrado de {numero} é {quadrado}')

"""5"""
# numero = int(input('Digite um número inteiro: '))

# if numero % 2 == 0:
#     print(f'O número {numero} é par')
# else:
#     print(f'O número {numero} é ímpar')

"""8"""
# nota1 = float(input('Nota 1 = '))
# nota2 = float(input('Nota 2 = '))

# if (0, 0) <= (nota1, nota2) <= (10, 10):
#     media = (nota1 + nota2) / 2
#     print(f'A média das notas é {media}')
# else:
#     print('Notas inválidas')

"""9"""
# salario = float(input('Salário = '))
# prestacao_emprestimo = float(input('Prestação do empréstimo = '))

# if prestacao_emprestimo > ((salario * 20) / 100):
#     print('Empréstimo não concedido')
# else:
#     print('Empréstimo concedido')

"""10"""
# altura = float(input('Altura = '))
# sexo = input('Sexo = ')

# if sexo == 'masculino':
#     peso_ideal = (72.7 * altura) - 58
#     print(f'Seu peso ideal é {peso_ideal}')
# elif sexo == 'feminino':
#     peso_ideal = (62.1 * altura) - 44.7
#     print(f'Seu peso ideal é {peso_ideal}')

"""11"""
# numero = int(input('Digite um número inteiro positivo: '))
# numero_lido = str(numero)

# soma = 0
# if numero >= 0:
#     for algarismo in numero_lido:
#         soma += int(algarismo)
#     print(f'A soma dos algarismos do número {numero} é {soma}')
# else:
#     print('Número inválido')

"""12"""
# from math import log10

# numero = int(input('Digite um número inteiro: '))

# if numero > 0:
#     logaritmo = log10(numero)
#     print(f'O logaritmo do número {numero} é {logaritmo}')
# else:
#     print('Número inválido')

"""15"""
# dias_semana = ['', 'domingo', 'segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira',
#                'sábado']
# string = str(dias_semana)

# numero = int(input('Digite um número inteiro entre 1 e 7: '))

# if 1 <= numero <= 7:
#     dia_semana = string.split()[numero].replace('[', ' ').replace(']', ' ').replace(',', ' ')
#     print(f'O {numero}º dia da semana é {dia_semana}')
# else:
#     print('Número inválido')

"""18"""
# print('Operações matemáticas disponíveis: \nsoma \nsubtração \nmultiplicação \ndivisão')
# operacao = input('Escolha uma operação: ')
# numero1 = float(input('Número 1 = '))
# numero2 = float(input('Número 2 = '))

# if operacao == 'soma':
#     operacao = '+'
#     resultado = numero1 + numero2
# elif operacao == 'subtração':
#     operacao = '-'
#     resultado = numero1 - numero2
# elif operacao == 'multiplicação':
#     operacao = '*'
#     resultado = numero1 * numero2
# elif operacao == 'divisão':
#     operacao = '/'
#     resultado = numero1 / numero2
# else:
#     print('Operação inválida')

# print(f'{numero1} {operacao} {numero2} = {resultado}')

"""19"""
# numero = int(input('Digite um número inteiro: '))

# if numero % 3 == 0 or numero % 5 == 0:
#     if numero % 3 == 0 and not numero % 5 == 0:
#         print(f'{numero} é divisível por 3, mas não por 5')
#     elif numero % 5 == 0 and not numero % 3 == 0:
#         print(f'{numero} é divisível por 5, mas não por 3')
#     elif numero % 3 == 0 and numero % 5 == 0:
#         print(f'{numero} é divisível por 3 e por 5 simultaneamente')
# else:
#     print(f'{numero} não é divísivel por 3 e nem por 5')

"""20"""
# A = float(input('A = '))
# B = float(input('B = '))
# C = float(input('C = '))

# if A + B > C and B + C > A and A + C > B:
#     if A == B == C:
#         print('Esses podem ser lados de um triângulo e o triângulo será equilátero')
#     elif A == B or A == C or B == C:
#         print('Esses podem ser lados de um triângulo e o triângulo será isósceles')
#     else:
#         print('Esses podem ser lados de um triângulo e o triângulo será escaleno')
# else:
#     print('Esses não podem ser lados de um triângulo')

"""24"""
# valor = float(input('Valor do produto: '))
# estado = input('Estado destino do produto (MG, SP, RJ, MS): ')

# if estado == 'MG':
#     valor = valor + ((valor * 7) / 100)
#     print(f'O valor do produto acrescido do imposto é {valor}')
# elif estado == 'SP':
#     valor = valor + ((valor * 12) / 100)
#     print(f'O valor do produto acrescido do imposto é {valor}')
# elif estado == 'RJ':
#     valor = valor + ((valor * 15) / 100)
#     print(f'O valor do produto acrescido do imposto é {valor}')
# elif estado == 'MS':
#     valor = valor + ((valor * 8) / 100)
#     print(f'O valor do produto acrescido do imposto é {valor}')
# else:
#     print('Estado inválido')

"""29"""
# from random import randint

# repeticoes = 0
# acertos = 0
# erros = 0

# while repeticoes < 5:
#     a = randint(1, 100)
#     b = randint(1, 100)
#     print(f'\nOs números são {a} e {b}')
#     soma = int(input(f'{a} + {b} = '))
#     if soma == a + b:
#         acertos += 1
#         print('Resposta correta')
#     else:
#         erros += 1
#         print(f'A resposta correta é {a + b}')
#     repeticoes += 1

# print(f'\nVocê acertou {acertos} vezes')

"""30"""
# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))

# lista = [a, b, c]
# lista.sort()
# print(lista)

"""35"""
# dia = int(input('dia = '))
# while dia > 31 or dia < 1:
#     print('Dia inválido')
#     dia = int(input('dia = '))

# mes = int(input('mês = '))
# while mes < 1 or mes > 12:
#     print('Mês inválido')
#     mes = int(input('mês = '))

# ano = int(input('ano = '))
# while ano < 1:
#     print('Ano inválido')
#     ano = int(input('ano = '))


# if mes == 2 and (ano % 400 == 0 or (ano % 4 == 0 and not ano % 100 == 0)) and dia <= 29:
#     print(f'Data: {dia}/{mes}/{ano}')
# elif mes == 2 and not (ano % 400 == 0 or (ano % 4 == 0 and not ano % 100 == 0)) and dia <= 28:
#     print(f'Data: {dia}/{mes}/{ano}')
# elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia <= 31:
#     print(f'Data: {dia}/{mes}/{ano}')
# elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia < 31:
#     print(f'Data: {dia}/{mes}/{ano}')
# else:
#     print('Data inválida')

"""37"""
print('Digite seu horário de chegada ao estacionamento:')

horas_chegada = int(input('Hora: '))
while horas_chegada < 00 or horas_chegada > 23:
    print('Hora inválida')
    horas_chegada = int(input('Hora: '))

minutos_chegada = int(input('Minutos: '))
while minutos_chegada < 00 or minutos_chegada >= 60:
    print('Minutos inválidos')
    minutos_chegada = int(input('Minutos: '))


print('\nDigite seu horário de partida do estacionamento:')

horas_partida = int(input('Hora: '))
while horas_partida < 00 or horas_partida > 23:
    print('Hora inválida')
    horas_partida = int(input('Hora: '))

minutos_partida = int(input('Minutos: '))
while minutos_partida < 00 or minutos_partida >= 60:
    print('Minutos inválidos')
    minutos_partida = int(input('Minutos: '))


horas_estadia = horas_partida - horas_chegada
minutos_estadia = minutos_partida - minutos_chegada

while minutos_estadia >= 60:
    horas_estadia += 1
    minutos_estadia = minutos_estadia - 60
if horas_chegada > horas_partida:
    horas_estadia = (24 - horas_chegada) + horas_partida

print(f'\nO tempo que o seu veículo permaneceu no estacionamento foi de {horas_estadia}:{minutos_estadia} horas.')


preco = 0.0
for n in range(0, horas_estadia):
    while n < 1:
        preco += 1.00
    while 1 <= n <= 2:
        preco += 1.00*n
    while 3 <= n <= 4:
        preco += 1.40*n
    while 5 <= n <= 24:
        preco += 2.00*n

print(f'O valor do estacionamento fica em R${preco}.')
