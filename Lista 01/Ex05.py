# Exercicio 05 - Faça um Programa que leia 3 numeros e mostre o maior deles

# Neste caso utilizei a funçao max() para simplificar a logica de encontrar o maior nomero.

try:
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    num3 = int(input("Digite o terceiro numero: "))
    
    print(max(num1, num2, num3))
    
except ValueError:
    print("Valor inválido, Por favor digite um número!")