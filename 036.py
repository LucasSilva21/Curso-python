casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Quato é o seu salário?R$'))
anos = int(input('Em quantos anos você pretende pagar essa casa? '))
prestacao = casa / (12 * anos)
minimo = salario * 0.30
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end = '')
print(' Sua prestacao sera de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser concedido')
else:
    print('Emprestimo negado')
