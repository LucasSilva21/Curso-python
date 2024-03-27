vel = int(input('Qual a velocidade do carro? '))
calc = (vel - 80) * 7
if vel <= 80:
    print('Velocidade permitida')
else:
    print('excedeu o limite! Sua multa é de R${}'.format(calc))