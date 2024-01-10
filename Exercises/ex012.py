#Leia um preço de um produto e  mostre seu novo preço,com 5% de desconto.
price = float(input('Qual é o preço deste livro? '))
discont = (price * 95 / 100)
print(' O novo preço do livro é {} devido ao Black Friday!'.format(discont))

