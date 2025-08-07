# Exercicio 07 - Faça um Programa que faça 5 perguntas para pessoa sobre um crime. 
# As perguntas são: 
# A - "Telefonou para a vitima?"
# B - "Esteve no local do crime?"
# C - "Mora perto da vitima?"
# D - "Devia para a vitima?"
# E - "Já trabalhou para a vitima?"
# O programa deve no final emitir uma classificaçao sobre a participaçao da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questoes ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cumplice" e 5 como "Assasino". Caso contrario, ele será classificado como "Inocente".

respostas = [
    input("Telefonou para a vitima (S / N )? ").strip().lower(),
    input("Esteve no local do crime (S / N )? ").strip().lower(),
    input("Mora perto da vitima (S / N )? ").strip().lower(),
    input("Devia para a vitima (S / N )? ").strip().lower(),
    input("Ja trabalhou para a vitima (S / N )? ").strip().lower(),
    ]

     
positivas = respostas.count("s")
    
if positivas == 2:
    print("Suspeita")
elif positivas > 2 and positivas < 5:
    print("Cumplice")
elif positivas == 5:
    print("Assasino")
else:
    print("Inocente")

    









