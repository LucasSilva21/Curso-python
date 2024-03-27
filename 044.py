print('{:=^40}'.format('MERCADINHO'))
preco = float(input('Preço das compras: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão ''')
opcao = int(input('Qual é a opção? '))
desc_dc = preco - (preco * 0.1) 
desc_cartao = preco - (preco * 0.05)
cartao = preco / 2
if opcao == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, desc_dc))
elif opcao == 2:
    print('Sua compra a vista será de R${:.2f}'.format(desc_cartao))
elif opcao == 3:
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(cartao))
elif opcao == 4:
    parcela = int(input('Quantas parcelas? '))
    produto = (preco / parcela)
    juros = produto + (produto * 0.20)
    final  = preco + (preco * 0.20)
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcela, juros))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, final))
else:
    preco = 0
    print('Opcao invalida. tente novamente!')
print('Obrigado por comprar conosco!')