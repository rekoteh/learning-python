 #Criar um programa que leia o comprimento de 3 retas 
#Se for True diga ao usuário que elas podem formar um triângulo.
#senão diga que não podem formar um triângulo.
lado1 = input(float('Digite a primeira medida:'))
lado2 = input(float('Digite a segunda medida:'))    
lado3 = input(float('Digite a terceira medida:'))

if lado1 > lado2 + lado3 and lado2 > lado1 + lado3 and lado2 > lado1 + lado3:
  
  print('Então não é possível')

else:
  print('Senão é possível montar um triângulo')
