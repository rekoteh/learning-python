#Ler o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
co = float(input('Enter the length of opposite leg: '))
ca = float(input('Enter the length of adjacent leg: '))
h = (co ** 2 + ca ** 2) ** (1/2)
print ('the length of the hypotenuse is {}'.format(h))