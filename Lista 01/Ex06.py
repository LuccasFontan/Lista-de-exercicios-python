# Exercicio 05 - Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite ou "Valor inválido!" conforme o caso.

turno_de_estudos = input("Digite o turno em que voce estuda (M-matutino ou V-Vespertino ou N-Noturno): ") 

if turno_de_estudos == "M":
    print("Bom dia")
elif turno_de_estudos == "V":
    print("Boa tarde")
elif turno_de_estudos == "N":
    print("Boa noite")
else:
    print("Digite uma das opçoes validas")