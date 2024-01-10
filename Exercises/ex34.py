#Ler um programa que pergunte o salário de um funcionário;
#calcule o valor do seu aumento.
#Se os salários forem superiores a R$1,250,00,calcule um aumento de 10%.
#Senão os valores inferiores ou iguais terão um aumento será de 15%.

print('In a bookstore...')
s=float(input('What is your salary here at the company?' ))

if s <= 1.250:
  
  new = s +(s * 10/ 100)

print('You will receive a 10% increase and will receive {}!'.format(new))
else:
  new = s + ( s * 15/ 100)
  
  print('You will receive a 15% increase and will receive {}!'.format(new))
