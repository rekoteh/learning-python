#Ler o nome dos alunos e mostrar o nome escolhido.
from random import choice
s1 = input('First student: ')
s2 = input('Second student: ')
s3 = input('Third student: ')
s4 = input('Four student: ')
l = [s1, s2, s3, s4]
print('So, the chosen was {}'.format(choice(l)))

