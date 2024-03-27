n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print(nome[0])
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
