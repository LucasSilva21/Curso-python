n = int(input('Digite um numero inteiro: '))
print('Escolha uma base para a conversão:')
print('[ 1 ] PARA CONVERTER EM BINÁRIO')
print('[ 2 ] PARA CONVERTER EM OCTAL')
print('[ 3 ] PARA CONVERTER EM HEX')
escolha = int(input('Sua opção: '))
if escolha == 1:
    print('{} convertido em binário é {}'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('{} convertido em octal é {}'.format(n, oct(n)[2:]))
elif escolha == 3:
    print('{} convertido em hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Opção invalida, tente novamente!')