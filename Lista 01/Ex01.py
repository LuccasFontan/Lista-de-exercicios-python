try:
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        print("O número é PAR")
    else:
        print("O número é IMPAR")
except ValueError:
    print("Valor inválido, por favor digite um número inteiro")
