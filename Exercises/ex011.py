#Leia a largura e a altura de uma parede em metros, calcule a sua area  e a quantidade de tinta necessaria
#Cada litro de tinta pinta uma area de 2 metros.
# Area calcular a área em metros quadrados, multiplique o comprimento pela largura que você mediu.
#A fórmula é: Área (m²) = Comprimento (m) x Largura (m)
print('Em uma loja de contrução...')
print('Bom dia, poderia me dar +/- 2 latas de tinta?')
print('Então, vou precisar das medidas do cômodo.')
large =float(input('Qual é a largura dessa parede da sala? '))
high = float(input('Qual é a altura da parede da sala? '))
area = high * large
#print('Sua parede tem uma dimensão de {} X {} e uma area de {}'.format(large, high, area)) = faltou colocar
#litro = area * 2 = confundi os sinais 
litro = area / 2
print('Você irá precisar de {} litros para pintar a sala'.format(litro))

 

