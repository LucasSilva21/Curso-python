print('Tabuada 2.0')
n = int(input('Escolha a tabuada desejada: '))
s = 0
print('A tabuda de {} é: '.format(n))
for c in range(0, 10):
    s = c + 1
    r = n * s
    print('{} x {} = {}'.format(n, s, r))
print('fim')