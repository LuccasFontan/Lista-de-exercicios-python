# Exercicio 03 - Faça um Programa que verifica se uma letra digitada é vogal ou consoante.

letra = str(input("Digite uma Letra: ")).lower()

if letra.isalpha() and len(letra) == 1:
    if letra in "aeiou":
        print("É uma vogal")
    else:
        print("É uma consoante")
else:
    print("Entrada invalida, Digite apenas uma letra!!")
 

