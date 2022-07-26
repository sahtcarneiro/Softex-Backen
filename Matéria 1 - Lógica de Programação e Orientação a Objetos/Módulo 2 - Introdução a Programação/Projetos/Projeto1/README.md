# Projeto 1 / Módulo 2 / Matéria 1

Autor: Jonathas Carneiro

## Instrução do Projeto

Desenvolva um programa que utiliza o nome de um aluno, duas notas e a quantidade de faltas que ele teve. Conclua se o aluno está aprovado ou reprovado de acordo com as especificações:

- Se a média do aluno for menor que sete, o sistema deve informar o nome do aluno e que ele está reprovado;
- Se o aluno possuir mais de três faltas, o sistema deve informar o nome do aluno e que ele está reprovado;
- Se a média do aluno for maior ou igual a sete, o sistema deve informar o nome do aluno e que ele está aprovado.

No sistema, todos os valores devem estar armazenados em variáveis.

## Resolução do Projeto

name = input("Qual o nome do aluno? ") <br>
nota1 = float(input("Qual sua primeira nota? ")) <br>
nota2 = float(input("Qual a segunda nota? ")) <br>
media = float((nota1 + nota2) / 2) <br>
faltas = int(input("Quantas faltas o aluno teve? ")) <br> <br>

if media < 7 or faltas > 3: <br>
print(name + " foi reprovado!") <br>
else: <br>
print(name + " foi aprovado!") <br>
