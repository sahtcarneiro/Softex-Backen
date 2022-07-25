name = input("Qual o nome do aluno? ")
nota1 = float(input("Qual sua primeira nota? "))
nota2 = float(input("Qual a segunda nota? "))
media = float((nota1 + nota2) / 2)
faltas = int(input("Quantas faltas o aluno teve? "))

if media < 7 or faltas > 3:
    print(name + " foi reprovado!")
else:
    print(name + " foi aprovado!")
