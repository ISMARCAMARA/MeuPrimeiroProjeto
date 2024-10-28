'''
Desafio 038 - comparando números 
Faça um programa que leia 2 números inteiros e diga qual deles é o maior, senão
informe que são iguais.
'''

numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))
if numero1>numero2:
    print(f'O PRIMEIRO valor é maior')
elif numero2>numero1:
    print(f'O SEGUNDO valor é maior')
elif numero1 == numero2:
    print(f'os dois valores são IGUAIS')
    