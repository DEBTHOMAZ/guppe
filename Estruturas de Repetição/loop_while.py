"""
Loop while

Forma geral

while expressão_booleana:
    //execução do loop


O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão booleana é toda expressão onde o resultado é True ou False.

Exemplo:

num = 5

num < 5


# Exemplo 1

numero = 1

while numero < 10:
    print(numero)
    numero += 1

# OBS: Em um loop while, é importante que cuidemos do critério de parada para não causar loop infinito.

# C ou Java

while(expressão){
  //execução
}

# do while (C ou Java)

do {
    //execução
}while(expressão);


* Em alguns softwares é necessário o loop infinito. Como em um jogo, um loop infinito que atualiza
a tela a todo momento

"""

# Exemplo 2

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou, Jéssica? ')
