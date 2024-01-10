# Ler um número inteiro e mostre na tela se é par ou ímpar.
n = int(input('Enter a number: '))
r = n % 2
if r == 0:
  print('This number is even!')
else:
  print('This number is odd!')