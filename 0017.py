import math
c1 = float(input('Qual a medida: '))
c2 = float(input('Qual a medida: '))
h = math.sqrt(c1 ** 2 + c2 ** 2)
print('As medidas dos catetos são {} e {} e o comprimento da hipotenusa é {:.2f}'.format(c1, c2, h))