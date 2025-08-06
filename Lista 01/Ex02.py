# Exercício 02 - Faça um Programa que peça dois números e imprima o maior deles.

try:
    num1 = int(input("Digite um o primeiro número: "))
    num2 = int(input("Digite um o segundo número: "))
    
    if num1 == num2:
        print("Os números são iguais")
    elif num1 > num2:
        print(num1) 
    else:
        print(num2)
except ValueError:
    print("Valor inválido, Por favor digite um número!")

