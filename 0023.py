#Digite um numero entre 0 a 9999
num = input('Digite um número: ')
print('Unidade: {}'.format(num[3:4]))
print('Dezena: {}'.format(num[2:3]))
print('Centena: {}'.format(num[1:2]))
print('Milhar: {}'.format(num[:1]))
