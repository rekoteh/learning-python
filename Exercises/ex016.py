#Ler um numero qualquer no teclado e mostre na tela a proporção inteira.ex:6.7688888454 prop int 6
import math
n = float(input('Enter a number:'))
e = math.trunc(n)
print('So, the number is {} and the entire proportion is {} '. format(n, e))
