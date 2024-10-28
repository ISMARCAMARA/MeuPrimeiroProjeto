'''
Desafio 041 - Crie um programa que leia o ano do nascimento do atleta e forneça
a sua classificação em MIRIM, JÚNIOR, SÊNIOR ou MASTER de acordo.
''' 
from datetime import date
nasc = int(input('Ano de Nascimento: ')) 
atual = date.today().year
idade = atual - nasc
print (f'O atleta tem {idade} anos') 
if idade <=9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19 :
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else
    print('Classificação: MASTER')