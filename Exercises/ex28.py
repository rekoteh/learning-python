#Escreva um programa que faça o pc "pensar" em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir  qual foi  o numero escolhido pelo pc.
#O programa deverá escrever na tela se o usuario venceu ou perdeu.
import random

print('Tente pensar no mesmo numero que eu, sendo ele de 0 a 5')
print('Se acertar você ganha o jogo! ')

c = random.randint (0,5)
n = int(input('Write a number:' ))

if n <= c:
  print('you win! Congratilations')
else:
  print('Im sorry, you lose!')
       
       
       