print("Operação - Adição!")

while True:
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")

    resposta = input("Deseja realizar mais uma soma? [S ou N]: ").lower()
    if resposta != "s":
        print("Operação finalizada.")
        break