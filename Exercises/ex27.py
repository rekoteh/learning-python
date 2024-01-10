#Ler um nome completo, mostrando em seguida o primeiro e último nome separadamete.
name = input('Whats your name?').split()
print('First Name: {}'.format(name[0]))
print('Last Name: {}'.format(name[-1]))
#print('Last Name: {}'.format(name[len(name)-1])