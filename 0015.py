d = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km percorridos? '))
c = (d * 60) + (km * 0.15)
print('O total a ser pago pelo veiculo alugado é de R${:.2f}'.format(c))