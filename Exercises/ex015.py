#Escrever um programa que pergunte a quantidade de kilometros percorridos por um carro e a quantidade de dias que ele foi alugado . Calcule o preço  a pagar , sabendo  que o carro custa 60 reais por dia  e 0.15c por km rodados.
#km / l
print('At a car rental...')
print ('I want to return this car, how much is the total price?')
print(' I need to know to calculate!')
d = int(input ('So,it was rented for how many days?'))
km = float(input('And many km were travelled?'))
print('It was {} days, and km {} '.format( d, km ))
print ('So, you will need to pays {:.2f} dolars'.format(( d * 60 ) + ( km * 0.15 )))