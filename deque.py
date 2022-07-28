"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance.
"""

# Import
from collections import deque

# Criando deques

deq = deque('geek')

print(deq)

# Adicionando elementos no deque

deq.append('y')  # Adiciona no final da lista também
print(deq)

deq.appendleft('k')
print(deq)  # * Dessa forma, adiciona no começa da lista

# Remover elementos no deque

print(deq.pop())  # Remove e retorna o último elemento
print(deq)

print(deq.popleft())  # * Dessa forma, remove e retorna o primeiro elemento
print(deq)
