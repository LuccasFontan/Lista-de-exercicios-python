# Exercício 04 - Faça um Programa para leitura de duas notas parciais de um aluno. 
# O programa deve calcular a media e aprensentar:

# A - a mensagem "Aprovado", se a media alcançada for maior ou igual a sete;
# B - a mensagem "Reprovado", se a media for menor do que sete;
# C - a mensagem "Aprovado com Distinção", se a media for igual a dez;


nota01 = float(input("Digite a primeira nota: "))
nota02 = float(input("Digite a segunda nota: "))

media = (nota01 + nota02) / 2

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")