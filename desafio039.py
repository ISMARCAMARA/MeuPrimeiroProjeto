'''
DESAFIO 039 - Alistamento militar
Crie um programa que leia a data de nascimento de uma pessoa e informe:
# Se ele ainda vai se alistar ao serviço militar; ou
# Se está na hora de se alistar; ou
# Se já passou do tempo.
O programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
ano_atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = ano_atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, ano_atual))
if idade == 18:
    print(f'Você tem de se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda falta {saldo} anos para o alistamento.')
    ano = ano_atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    ano = ano_atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
