# Exercício 01 - Faça um Programa que peça um número inteiro e determine se ele é PAR ou ÍMPAR. 
# Dica: utilize o operador módulo (resto da divisão [%])

try:
    numero = int(input("Digite um número inteiro: "))
    
    if numero % 2 == 0:
        print("O número é PAR")
    else:
        print("O número é IMPAR")
except ValueError:
    print("Valor inválido, Por favor digite um número inteiro")
    

    
