#Ler um programa que sorteie a ordem de apresentação dos alunos.
from random import shuffle 
s1 = input('First student: ')
s2 = input('Second student: ')
s3 = input('Third student: ')
s4 = input('Four student: ')
l = [s1, s2, s3, s4]
shuffle(l)
print('So, the order of presentation of students is {}'.format(l))
