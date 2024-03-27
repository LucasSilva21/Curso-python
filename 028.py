import random
pc = random.randint(1,5)
eu = int(input('Em que numero eu pensei?  '))
if eu == pc:
    print('Parabéns voce acertou')
else:
    print('Voce errou eu pensei no numero {}'.format(pc))


