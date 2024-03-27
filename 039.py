from datetime import date
ano = int(input('Ano de nascimento: '))
print('Quem nasceu em {} tem {} anos em {}'.format(ano, date.today().year - ano, date.today().year ))
falta = 18 - (date.today().year - ano)
quando = falta + date.today().year
falta2 = (date.today().year - ano) - 18
if date.today().year - ano == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif date.today().year - ano >= 18:
    print('Você já deveria ter se alistado há {} anos. Seu alistamento foi em {}.'.format(falta2, quando))
elif date.today().year - ano < 18:
    print('Ainda faltam {} anos para o alistamento. Seu alistamento será em {}'.format(falta, quando))
