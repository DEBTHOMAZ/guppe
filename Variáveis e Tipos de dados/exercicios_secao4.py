"""
Seção 4 - Exercícios
"""


"1"
# x = 6
# print(x)


"2"
# x = 6.7980
# print(x)


"3"
# x = int(input("Digite um número inteiro: "))
# y = int(input("Digite um número inteiro: "))
# z = int(input("Digite um número inteiro: "))
# print(x + y + z)


"4"
# x = 6.8966
# print(x ** 2)


"5"
# x = 3.656
# print(x / 5)


"6"
# C = 37.7
# F = C * (9.0 / 5.0) + 32.0
# print(F)


"7"
# F = 99.8
# C = 5.0 * ((F - 32.0) / 9.0)
# print(C)


"8"
# K = 0
# C = K - 273.15
# print(C)


"9"
# C = 100
# K = C + 273.15
# print(K)


"10"
# K = 300000000
# M = K / 3.6
# print(M)


"11"
# M = 300000000
# K = M * 3.6
# print(K)


"28"
# x = 4575
# y = 25465.543
# z = 0.864
# print(x ** 2 + y ** 2 + z ** 2)


"29"
# nota1 = 10
# nota2 = 8
# nota3 = 9
# nota4 = 9

# media = (nota1 + nota2 + nota3 + nota4) / 4
# print(media)


"30"
# valor_reais = 10000.00
# cotacao_dolar = 5.44

# print("valor em dólares: " + str(valor_reais / cotacao_dolar))


"31"
# inteiro = 57476768686
# antecessor = inteiro - 1
# sucessor = inteiro + 1
# print(inteiro)
# print(antecessor)
# print(sucessor)


"43"
# valor_total = 4_000.00
# valor_desconto = valor_total - valor_total * 0.10
# valor_parcelas = valor_total / 3.00
# comissao_avista = valor_desconto * 0.05
# comissao_parcelada = valor_total * 0.05

# print(f'O valor total da venda foi de R${valor_total}, o total a ser pago é de R${valor_desconto}. Caso \n'
#       f'parcelada a compra em 3x sem juros, o valor das parcelas ficam em R${valor_parcelas}. A \n'
#       f'comissão do vendedor caso o pagamento seja à vista é de R${comissao_avista}. Caso seja parcelado, \n'
#       f'é de R${comissao_parcelada}.')


"45"
# maiuscula = 'B'
# maiuscula_ASCII = ord(maiuscula)
# minuscula_ASCII = maiuscula_ASCII + 32
# minuscula = chr(minuscula_ASCII)

# print(minuscula)


"46"
# numero = 345
# numero_lido = str(numero)

# numero_invertido = numero_lido[::-1]
# numero_invertido = int(numero_invertido)

# print(numero_invertido)


"47"
# numero = 1923
# numero_lido = str(numero)

# print(f'{numero_lido[:1]} \n{numero_lido[1:2]} \n{numero_lido[2:3]} \n{numero_lido[3:4]} '
#       f'\n{numero_lido[4:5]}')


"48"
# segundos = 1000000
# print(f'{segundos} segundos correspondem a {segundos / 60} minutos e {segundos / 360} horas.')


"49"
# horario_inicio = input("Início do experimento: \nHoras = ") + ":" + input("Minutos = ") + ":" + \
#                  input("Segundos = ")
# print("Início do experimento: " + horario_inicio)


# duracao = input("Duração do experimento: \nHoras = ") + ":" + input("Minutos = ") + ":" + \
#           input("Segundos = ")
# print("Duração do experimento: " + duracao)


# horario_inicio_lido = str(horario_inicio)

# hora_inicio_lido = horario_inicio_lido[:2]
# hora_inicio = int(hora_inicio_lido)

# minutos_inicio_lido = horario_inicio_lido[3:5]
# minutos_inicio = int(minutos_inicio_lido)

# segundos_inicio_lido = horario_inicio_lido[6:8]
# segundos_inicio = int(segundos_inicio_lido)

# duracao_lido = str(duracao)

# hora_duracao_lido = duracao_lido[:2]
# hora_duracao = int(hora_duracao_lido)

# minutos_duracao_lido = duracao_lido[3:5]
# minutos_duracao = int(minutos_duracao_lido)

# segundos_duracao_lido = duracao_lido[6:8]
# segundos_duracao = int(segundos_duracao_lido)

# dia_termino = 0
# hora_termino = hora_inicio + hora_duracao
# while hora_termino > 24:
#     dia_termino = dia_termino + 1
#     hora_termino = hora_termino - 24

# minutos_termino = minutos_inicio + minutos_duracao
# if minutos_termino > 60:
#     hora_termino = hora_termino + 1
#     minutos_termino = minutos_termino - 60

# segundos_termino = segundos_inicio + segundos_duracao
# if segundos_termino > 60:
#     minutos_termino = minutos_termino + 1
#     segundos_termino = segundos_termino - 60

# termino = str(hora_termino) + ":" + str(minutos_termino) + ":" + str(segundos_termino)
# if dia_termino == 0:
#     print("O experimento termina às " + termino)
# else:
#     print(f'O experimento termina em {dia_termino} dias e {termino} horas')


"50"
# idade = int(input("Quantos anos você faz nesse ano? "))
# ano_atual = 2020

# ano_nascimento = ano_atual - idade
# print(f'Você nasceu em {ano_nascimento}')


"51"
# x = int(input("x = "))
# y = int(input("y = "))
# coordenadas = (x,y)
# print(coordenadas)

# origem = (0,0)
# distancia_origem = ((0 - x) ** 2 + (0 - y) ** 2) ** 0.5
# print(distancia_origem)


"53"
# c = float(input("Comprimento do terreno (metros) = "))
# l = float(input("Largura do terreno (metros) = "))
# terreno_area = c * l

# p = float(input("Valor do metro quadrado da tela= "))
# valor_terreno_coberto = terreno_area * p

# print(f'O custo para cerca esse terreno com tela é de R${valor_terreno_coberto}')
