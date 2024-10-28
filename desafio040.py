'''
Desafio 040 - Crie um programa que calcule a mC)dia de um aluno e informe
se o aluno foi APROVADO, REPROVADO ou ficou em RECUPERAçÃO.
''' 
nota1 = float (input ('Primeira nota: ')) 
nota2 = float (input ('Segunda nota: ')) 
media = (nota1 + nota2) / 2
print ('Tirando {:.1f} e {:.1f}, a média do aluno é: {:.1f}'.format(nota1, nota2, media)) 
if media >= 7:
    print(f 'O aluno estC! APROVADO.')
elif 7 > media >= 5:
    print(f 'O aluno estC! em RECUPERAÇÃO.')
elif media < 5:
    print(f 'O aluno estC! REPROVADO.')
