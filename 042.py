r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triangulo')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('ISOSCELES')
    else:
        print('ESCALENO')
else:
    print('Os segmentos não podem formar um triangulo')