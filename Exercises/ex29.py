# Escreva um prg que leia a velocidade de um carro.
# Se ultrapasssar 80km/hr, mostre uma msg dnzd que ele foi multado.
# A multa vai custar 7,00 por cada km acima do limite.
print('  On a Federal road...')
s = float(input('How fast was the car you were driving?'))
if s > 80:
  t = (s - 80) * 7
  print('You have been fined and will have to pay {} '.format(t))
else:
  print('Have a good day! good travel! ')
