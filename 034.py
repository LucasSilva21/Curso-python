s = float(input('Qual o seu salário? R$'))
a = s +(s * 0.10)
b = s +(s * 0.15)
if s > 1250:
    print('Você recebeu um aumento de {:.2f}'.format(a))
if s <= 1250:
    print('Você recebeu um aumento de {:.2f}'.format(b))