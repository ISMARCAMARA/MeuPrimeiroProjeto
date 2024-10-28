#Exercício053 - Detector de PALÍNDROMO sem laço for
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
'''for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))'''
if inverso == junto:
    print('Temos um PALÍNDROMO!!!')
else:
    print('a  frase digitada NÃO É UM PALÍNDROMO!!!')