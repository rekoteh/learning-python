#Ler o nome de uma cidade e  dizer se ela começa com santo ou não.
#city = input('What is the name of this city?')
#print('Santo' in city)
city = input('What is the name of this city?').strip()
print('I live in {}!'.format(city))
print('SANTO' in city.upper())

