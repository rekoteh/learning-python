#Ler uma frase e mostrar qntas vzs aparece a letra A,em que posição ela aparece pela primeira e última vez.
ph = input('Write a sentence:').strip().upper()
print('The letter A appears so {} times!'.format(ph.count('A')))
print('The letter A appears for the first time in {}!'.format(ph.index('A')))
print('The letter A appears for the last time in {}!'.format(ph.rindex('A')))