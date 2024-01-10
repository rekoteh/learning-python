#Leia o salario de um funcionario e mostre  seu novo salario, com 15% de aumento.

salary = float(input('How much you earn at the company you work for? '))
print('There will be a 15% increase in the salary of this company´s employees due to changes in company regulations!')
increase  = salary + (salary * 15 / 100)
print ('This is the new salary {}!'.format(increase))