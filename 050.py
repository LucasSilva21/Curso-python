s = 0
for c in range(0, 6):
    n = int(input('Digite um número:'))
    s += n
if s%n == 0:
    print('A soma dos número foi {}'.format(s))
else:
    print('Desconsidere')

