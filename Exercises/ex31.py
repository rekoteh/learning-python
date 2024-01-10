# Perguntar a distância de uma viajem em km.
# Calcule o preço da passagem
# Se a viajem for maior que 200km, cobre R$0,45 por km
# Senão, cobre R$0,50 por km
distance = float(input('Você viajou por quantos kilômetros? '))

if distance > 200.0:
  price = distance * 0.45
else:
 price = distance * 0.50

print('O preço da sua viajem será R${}! Boa viagem!'.format(price))
   