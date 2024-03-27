n = float(input('Qual o valor desse produto? R$'))
d = n - (n * 0.05)
print('O produto custa R${:.2f} com o desconto aplicado ele vai custar R${:.2f}'.format(n,d))