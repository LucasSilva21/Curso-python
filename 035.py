r1 = float(input('Digite o comprimento: '))
r2 = float(input('Digite o comprimento: '))
r3 = float(input('Digite o comprimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode se formar um triangulo')
else:
    print('Não pode se formar um triangulo')